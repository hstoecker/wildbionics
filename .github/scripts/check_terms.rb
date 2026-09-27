#!/usr/bin/env ruby
# frozen_string_literal: true
#
# Translation quality gate: German technical terms (Fachbegriffe), consistency between
# EN and DE articles, German typography and i18n completeness.
#
#   ruby .github/scripts/check_terms.rb            # run from the repository root
#
# Rules live in _data/glossary.yml. Uses only the Ruby standard library.
# Exits non-zero if any error is found; warnings never fail the build.

require "date"
require "yaml"

ROOT = File.expand_path("../..", __dir__)
Dir.chdir(ROOT)

errors = []
warnings = []

glossary = YAML.load_file("_data/glossary.yml").fetch("terms")
i18n = YAML.load_file("_data/i18n.yml")
taxonomy = YAML.load_file("_data/taxonomy.yml")
langs = YAML.load_file("_config.yml").fetch("languages")

# "Stoßwelle*" → /(?<![\p{L}\p{N}])Stoßwelle\p{L}*(?![\p{L}\p{N}])/i
# A leading * allows German compounds: "*schere*" matches "Knallschere", "Greifscheren".
def term_regex(term)
  body = term.split("*", -1).map { |part| Regexp.escape(part).gsub("\\ ", "\\s+") }.join("\\p{L}*")
  Regexp.new("(?<![\\p{L}\\p{N}])#{body}(?![\\p{L}\\p{N}])", Regexp::IGNORECASE)
end

# Front matter + body of a Markdown file.
def split_front_matter(text)
  return [{}, text] unless text.start_with?("---")
  _, fm, body = text.split(/^---\s*$/, 3)
  [YAML.safe_load(fm, permitted_classes: [Date]) || {}, body.to_s]
end

# Prose only: drop code blocks, Liquid tags, HTML tags, Markdown link targets and IALs.
def prose(text)
  text.gsub(/^```.*?^```/m, " ")
      .gsub(/\{%.*?%\}/m, " ").gsub(/\{\{.*?\}\}/m, " ")
      .gsub(/<[^>]+>/, " ")
      .gsub(/\]\([^)]*\)/, "]").gsub(/\{:[^}]*\}/, " ")
      .gsub(/`[^`]*`/, " ")
      .gsub(%r{https?://\S+}, " ")
end

# Text of an article that should be translated: body, key facts, FAQ, title, description.
def article_text(fm, body)
  parts = [fm["title"], fm["description"], fm["dek"], fm["hero_caption"], fm["image_alt"]]
  parts += Array(fm["key_facts"])
  parts += Array(fm["faq"]).flat_map { |q| [q["q"], q["a"]] }
  prose(([body] + parts.compact).join("\n"))
end

def leaves(node, path = [], &block)
  case node
  when Hash then node.each { |k, v| leaves(v, path + [k.to_s], &block) }
  when Array then node.each_with_index { |v, i| leaves(v, path + [i.to_s], &block) }
  else yield(path, node.to_s)
  end
end

def line_of(text, index)
  text[0...index].count("\n") + 1
end

# ---------------------------------------------------------------------------------
# 1. Collect German content: [label, text]
# ---------------------------------------------------------------------------------
german = []
leaves(i18n.fetch("de")) { |path, value| german << ["_data/i18n.yml de.#{path.join('.')}", prose(value)] }
taxonomy.each { |slug, names| german << ["_data/taxonomy.yml #{slug}", names["de"].to_s] }

articles = Dir["_articles/*.md"].sort.map do |file|
  fm, body = split_front_matter(File.read(file))
  { file: file, fm: fm, body: body, lang: fm["lang"], ref: fm["ref"] }
end
articles.select { |a| a[:lang] == "de" }.each do |a|
  german << [a[:file], article_text(a[:fm], a[:body])]
end
Dir["de/**/*.{html,md}"].sort.each { |file| german << [file, prose(split_front_matter(File.read(file)).last)] }

# ---------------------------------------------------------------------------------
# 2. Forbidden variants (avoid)
# ---------------------------------------------------------------------------------
glossary.each do |entry|
  Array(entry["avoid"]).each do |bad|
    rx = term_regex(bad)
    german.each do |label, text|
      text.to_enum(:scan, rx).each do
        m = Regexp.last_match
        msg = "#{label}: „#{m[0]}“ → „#{entry['de'].delete('*')}“#{entry['why'] ? " (#{entry['why']})" : ''}"
        (entry["level"] == "warn" ? warnings : errors) << msg
      end
    end
  end
  # Sanity: the preferred term must not be on its own avoid list.
  if Array(entry["avoid"]).any? { |bad| term_regex(bad).match?(entry["de"].delete("*")) }
    errors << "_data/glossary.yml: „#{entry['de']}“ is both preferred and avoided"
  end
end

# ---------------------------------------------------------------------------------
# 3. EN → DE consistency per article pair
# ---------------------------------------------------------------------------------
articles.group_by { |a| a[:ref] }.each do |ref, versions|
  by_lang = versions.to_h { |a| [a[:lang], a] }
  (langs - by_lang.keys).each { |missing| warnings << "article „#{ref}“ has no #{missing} version" }
  en, de = by_lang["en"], by_lang["de"]
  next unless en && de

  en_text = article_text(en[:fm], en[:body])
  de_text = article_text(de[:fm], de[:body])
  glossary.each do |entry|
    next unless entry["en"] && term_regex(entry["en"]).match?(en_text)
    candidates = [entry["de"]] + Array(entry["de_alt"])
    next if candidates.any? { |c| term_regex(c).match?(de_text) }
    warnings << "#{de[:file]}: EN uses „#{entry['en'].delete('*')}“, but the DE text lacks „#{entry['de'].delete('*')}“"
  end
  # Same number of citations and sources in both languages
  %w[sources faq key_facts].each do |key|
    n_en, n_de = Array(en[:fm][key]).size, Array(de[:fm][key]).size
    errors << "#{de[:file]}: #{key} has #{n_de} entries, EN has #{n_en}" if n_en != n_de
  end
  cites_en = en[:body].scan(/#ref-(\d+)/).flatten.sort
  cites_de = de[:body].scan(/#ref-(\d+)/).flatten.sort
  errors << "#{de[:file]}: citations differ from EN (#{cites_de.tally} vs #{cites_en.tally})" if cites_en != cites_de
end

# UI strings: the same key in EN and DE must use the glossary term
en_strings = {}
leaves(i18n.fetch("en")) { |path, value| en_strings[path.join(".")] = prose(value) }
leaves(i18n.fetch("de")) do |path, value|
  en_text = en_strings[path.join(".")] or next
  de_text = prose(value)
  glossary.each do |entry|
    next unless entry["en"] && term_regex(entry["en"]).match?(en_text)
    next if ([entry["de"]] + Array(entry["de_alt"])).any? { |c| term_regex(c).match?(de_text) }
    warnings << "_data/i18n.yml de.#{path.join('.')}: EN uses „#{entry['en'].delete('*')}“, but DE lacks „#{entry['de'].delete('*')}“"
  end
end

# ---------------------------------------------------------------------------------
# 4. German typography in article prose
# ---------------------------------------------------------------------------------
articles.select { |a| a[:lang] == "de" }.each do |a|
  text = prose(a[:body])
  # 2.76 or 0.3 (decimal point) – but not 5.000 (German thousands separator)
  text.to_enum(:scan, /(?<![\d.,\/])\d+\.(?:\d{1,2}|\d{4,})(?!\d|\.\d)/).each do
    m = Regexp.last_match
    warnings << "#{a[:file]}:~#{line_of(text, m.begin(0))}: decimal point in „#{m[0]}“ – im Deutschen Dezimalkomma"
  end
  # 5,000 (English thousands separator) – but not 0,915 (German decimal comma)
  text.to_enum(:scan, /(?<![\d.,])[1-9]\d{0,2},\d{3}(?!\d|,\d)/).each do
    m = Regexp.last_match
    warnings << "#{a[:file]}:~#{line_of(text, m.begin(0))}: „#{m[0]}“ looks like an English thousands separator – im Deutschen „#{m[0].tr(',', '.')}“"
  end
  text.to_enum(:scan, /\d (?:kHz|Hz|m\/s|µs|ms|kPa|dB|mm|cm|°C|K)(?![\p{L}])/).each do
    m = Regexp.last_match
    warnings << "#{a[:file]}:~#{line_of(text, m.begin(0))}: „#{m[0]}“ – zwischen Zahl und Einheit ein geschütztes Leerzeichen (U+00A0)"
  end
  text.to_enum(:scan, /"[^"\n]{1,80}"/).each do
    m = Regexp.last_match
    warnings << "#{a[:file]}:~#{line_of(text, m.begin(0))}: straight quotes #{m[0]} – im Deutschen „…“"
  end
end

# ---------------------------------------------------------------------------------
# 5. Completeness of UI strings and taxonomy
# ---------------------------------------------------------------------------------
keys = langs.to_h { |l| k = []; leaves(i18n.fetch(l)) { |path, _| k << path.join(".") }; [l, k] }
langs.each do |l|
  (keys[langs.first] - keys[l]).each { |k| errors << "_data/i18n.yml: #{l}.#{k} missing" }
  (keys[l] - keys[langs.first]).each { |k| errors << "_data/i18n.yml: #{l}.#{k} has no #{langs.first} counterpart" }
end
DIMS = %w[time space physics adjacent_sciences].freeze
taxonomy.each do |slug, names|
  langs.each { |l| errors << "_data/taxonomy.yml: #{slug} has no #{l} name" if names.to_h[l].to_s.strip.empty? }
  errors << "_data/taxonomy.yml: #{slug} needs dim: one of #{DIMS.join(', ')}" unless DIMS.include?(names.to_h["dim"])
  errors << "_data/taxonomy.yml: time term #{slug} needs a numeric order" if names.to_h["dim"] == "time" && !names["order"].is_a?(Integer)
end
lenses = YAML.load_file("_data/lenses.yml")
lens_keys = i18n.fetch(langs.first).fetch("lens").select { |_, v| v.is_a?(Hash) && v["tab"] }.keys
(lens_keys - lenses.keys).each { |k| errors << "_data/lenses.yml: lens „#{k}“ has no graph target" }
lenses.each do |k, target|
  kind, slug = target.to_s.split(":", 2)
  ok = (kind == "term" && taxonomy.key?(slug)) || (kind == "dim" && DIMS.include?(slug))
  errors << "_data/lenses.yml: #{k} → „#{target}“ is not a taxonomy term or dimension" unless ok
end
beings = YAML.load_file("_data/beings.yml")
beings.each do |slug, names|
  langs.each { |l| errors << "_data/beings.yml: #{slug} has no #{l} name" if names.to_h[l].to_s.strip.empty? }
end
articles.each do |a|
  a[:fm].fetch("dimensions", {}).each do |dim, slugs|
    Array(slugs).each do |slug|
      if !taxonomy.key?(slug)
        errors << "#{a[:file]}: dimension slug „#{slug}“ missing in _data/taxonomy.yml"
      elsif taxonomy[slug]["dim"] != dim
        errors << "#{a[:file]}: „#{slug}“ is listed under #{dim}, but _data/taxonomy.yml puts it in #{taxonomy[slug]['dim']}"
      end
    end
  end
  Array(a[:fm]["lenses"]).each { |l| errors << "#{a[:file]}: lens „#{l}“ missing in _data/lenses.yml" unless lenses.key?(l) }
  Array(a[:fm]["beings"]).each { |b| errors << "#{a[:file]}: being „#{b}“ missing in _data/beings.yml" unless beings.key?(b) }
end

warnings.uniq.each { |w| puts "warning: #{w}" }
errors.uniq.each { |e| puts "ERROR:   #{e}" }
puts "\nTerminology check: #{glossary.size} glossary terms, #{german.size} German texts, " \
     "#{errors.uniq.size} errors, #{warnings.uniq.size} warnings."
exit(errors.empty? ? 0 : 1)
