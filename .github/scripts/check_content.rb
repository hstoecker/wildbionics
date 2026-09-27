#!/usr/bin/env ruby
# frozen_string_literal: true
#
# Structure gate for WildBionics content (rules: plugins/wildbionics/skills/wildbionics-article):
# article front matter, lens panels, citations ↔ sources, DOIs, images and figures.
#
#   ruby .github/scripts/check_content.rb      # from the repository root
#
# Standard library only. Exits non-zero on errors; warnings never fail the build.

require "date"
require "yaml"

Dir.chdir(File.expand_path("../..", __dir__))
errors = []
warnings = []

config = YAML.load_file("_config.yml")
langs = config.fetch("languages")
lenses = YAML.load_file("_data/lenses.yml")
REQUIRED = %w[id lang ref title short_title kicker description date permalink image image_alt
              hero_figure keywords dimensions lenses key_facts faq sources status].freeze
DOI = %r{\A10\.\d{4,9}/\S+\z}
WIKIDATA = /\AQ\d+\z/

def front_matter(path)
  text = File.read(path)
  _, fm, body = text.split(/^---\s*$/, 3)
  [YAML.safe_load(fm, permitted_classes: [Date]) || {}, body.to_s]
end

articles = Dir["_articles/*.md"].sort.map do |f|
  fm, body = front_matter(f)
  { file: f, fm: fm, body: body }
end

articles.each do |a|
  f, fm, body = a[:file], a[:fm], a[:body]
  (REQUIRED - fm.keys).each { |k| errors << "#{f}: front matter lacks `#{k}`" }
  next unless (REQUIRED - fm.keys).empty?

  errors << "#{f}: id (#{fm['id']}) must equal ref (#{fm['ref']})" if fm["id"] != fm["ref"]
  errors << "#{f}: lang #{fm['lang']} not in _config.yml languages" unless langs.include?(fm["lang"])
  expected = fm["lang"] == langs.first ? %r{\A/articles/[a-z0-9-]+/\z} : %r{\A/#{fm['lang']}/[a-z]+/[a-z0-9-]+/\z}
  errors << "#{f}: permalink #{fm['permalink']} does not match #{expected.source}" unless fm["permalink"].to_s.match?(expected)
  unless File.basename(f) == "#{fm['ref']}.#{fm['lang']}.md"
    errors << "#{f}: file name must be <ref>.<lang>.md (#{fm['ref']}.#{fm['lang']}.md)"
  end
  errors << "#{f}: date must be YYYY-MM-DD" unless fm["date"].is_a?(Date)
  errors << "#{f}: status must be draft or published" unless %w[draft published].include?(fm["status"])

  d = fm["description"].to_s
  errors << "#{f}: description has #{d.size} characters (50–160)" unless d.size.between?(50, 160)
  warnings << "#{f}: title has #{fm['title'].size} characters (aim for ≤ 60)" if fm["title"].size > 60
  errors << "#{f}: image #{fm['image']} not found" unless File.exist?(fm["image"].to_s.delete_prefix("/"))
  errors << "#{f}: hero_figure _includes/#{fm['hero_figure']} not found" unless File.exist?("_includes/#{fm['hero_figure']}")
  errors << "#{f}: keywords need at least 3 entries" if Array(fm["keywords"]).size < 3

  (Array(fm["about"]) + Array(fm["mentions"])).each do |t|
    errors << "#{f}: about/mentions entry #{t['name']} needs a Wikidata ID (Q…)" unless t["wikidata"].to_s.match?(WIKIDATA)
  end

  # key facts, FAQ
  kf = Array(fm["key_facts"])
  errors << "#{f}: key_facts needs 3–7 entries (has #{kf.size})" unless kf.size.between?(3, 7)
  faq = Array(fm["faq"])
  errors << "#{f}: faq needs at least 3 entries" if faq.size < 3
  faq.each_with_index { |q, i| errors << "#{f}: faq[#{i}] needs q and a" if q["q"].to_s.empty? || q["a"].to_s.empty? }

  # sources ↔ citations
  sources = Array(fm["sources"])
  errors << "#{f}: at least one source is required" if sources.empty?
  sources.each_with_index do |s, i|
    %w[authors year title journal doi].each { |k| errors << "#{f}: sources[#{i}] lacks #{k}" if s[k].to_s.empty? }
    errors << "#{f}: sources[#{i}] DOI #{s['doi']} is not a valid DOI" unless s["doi"].to_s.match?(DOI)
  end
  text = body + kf.join("\n")
  cited = text.scan(/\(#ref-(\d+)\)/).flatten.map(&:to_i).uniq
  cited.each { |n| errors << "#{f}: citation [#{n}] has no source" if n < 1 || n > sources.size }
  (1..sources.size).each { |n| errors << "#{f}: source #{n} (#{sources[n - 1]['title']}) is never cited" unless cited.include?(n) }

  # lenses: front matter ↔ tab bar ↔ panels
  fl = Array(fm["lenses"])
  fl.each { |l| errors << "#{f}: lens #{l} missing in _data/lenses.yml" unless lenses.key?(l) }
  tabs = body[/lens-tabs\.html lenses="([^"]+)"/, 1].to_s.split(",")
  panels = body.scan(/lens-start\.html lens="([^"]+)"/).flatten
  errors << "#{f}: lens-tabs (#{tabs.join(',')}) must match lenses (#{fl.join(',')})" if tabs != fl
  errors << "#{f}: lens panels (#{panels.join(',')}) must match lenses (#{fl.join(',')})" if panels != fl
  errors << "#{f}: every lens-start needs a lens-end" if body.scan("lens-end.html").size != panels.size

  # figures included in the body
  body.scan(/\{%\s*include\s+(svg\/[\w.-]+)/).flatten.each do |inc|
    errors << "#{f}: figure _includes/#{inc} not found" unless File.exist?("_includes/#{inc}")
  end
end

# translations of published articles
articles.group_by { |a| a[:fm]["ref"] }.each do |ref, versions|
  next unless versions.any? { |v| v[:fm]["status"] == "published" }
  missing = langs - versions.map { |v| v[:fm]["lang"] }
  errors << "article #{ref} is published but has no #{missing.join(', ')} version" unless missing.empty?
  statuses = versions.map { |v| v[:fm]["status"] }.uniq
  warnings << "article #{ref}: languages have different status (#{statuses.join(', ')})" if statuses.size > 1
end

# figures: accessible SVG with i18n labels
Dir["_includes/svg/*.svg"].sort.each do |f|
  s = File.read(f)
  errors << "#{f}: must start with {%- include i18n.html -%}" unless s.start_with?("{%- include i18n.html -%}")
  errors << "#{f}: <svg> needs role=\"img\" and aria-labelledby" unless s.match?(/<svg[^>]*role="img"[^>]*aria-labelledby=/m)
  %w[title desc].each { |tag| errors << "#{f}: missing <#{tag}>" unless s.include?("<#{tag} ") }
  warnings << "#{f}: hard-coded text in <text> (use _data/i18n.yml)" if s.match?(/<text[^>]*>[A-Za-zÄÖÜäöü]{4,}[^{<]*<\/text>/)
end

warnings.each { |w| puts "warning: #{w}" }
errors.each { |e| puts "ERROR:   #{e}" }
puts "\nContent check: #{articles.size} articles, #{Dir['_includes/svg/*.svg'].size} figures, " \
     "#{errors.size} errors, #{warnings.size} warnings."
exit(errors.empty? ? 0 : 1)
