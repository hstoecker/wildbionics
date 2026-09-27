#!/usr/bin/env ruby
# frozen_string_literal: true
#
# Plugin gate: keeps the WildBionics skills (the project's rulebook) valid and up to date.
#
#   ruby .github/scripts/check_plugin.rb                 # integrity + coverage
#   ruby .github/scripts/check_plugin.rb --base <ref>    # + version bump if plugins/ changed
#
# Checks: marketplace.json / plugin.json, skill and agent front matter, .claude/ links,
# every repository path mentioned in the rulebook exists, and every check script, data file
# and workflow is described by at least one skill. Standard library only.

require "json"
require "yaml"

Dir.chdir(File.expand_path("../..", __dir__))
errors = []
warnings = []

PLUGIN = "plugins/wildbionics"
market = JSON.parse(File.read(".claude-plugin/marketplace.json"))
manifest = JSON.parse(File.read("#{PLUGIN}/.claude-plugin/plugin.json"))

# --- manifests ---------------------------------------------------------------------
%w[name owner plugins].each { |k| errors << "marketplace.json lacks #{k}" unless market[k] }
entry = Array(market["plugins"]).find { |p| p["name"] == manifest["name"] }
errors << "marketplace.json has no entry for plugin #{manifest['name']}" unless entry
errors << "marketplace entry source must be ./#{PLUGIN}" if entry && entry["source"] != "./#{PLUGIN}"
errors << "plugin.json version must be semver (x.y.z)" unless manifest["version"].to_s.match?(/\A\d+\.\d+\.\d+\z/)
%w[description author license repository].each { |k| errors << "plugin.json lacks #{k}" unless manifest[k] }

def front_matter(path)
  _, fm, body = File.read(path).split(/^---\s*$/, 3)
  [YAML.safe_load(fm.to_s) || {}, body.to_s]
end

# --- skills and agents -------------------------------------------------------------
skills = Dir["#{PLUGIN}/skills/*/"].map { |d| File.basename(d) }.sort
skills.each do |name|
  file = "#{PLUGIN}/skills/#{name}/SKILL.md"
  unless File.exist?(file)
    errors << "#{PLUGIN}/skills/#{name}/ has no SKILL.md"
    next
  end
  fm, body = front_matter(file)
  errors << "#{file}: front matter name must be #{name}" unless fm["name"] == name
  d = fm["description"].to_s
  errors << "#{file}: description missing" if d.empty?
  warnings << "#{file}: description is #{d.size} characters (keep ≤ 1024)" if d.size > 1024
  errors << "#{file}: body is almost empty" if body.strip.size < 200
  link = ".claude/skills/#{name}"
  unless File.symlink?(link) && File.readlink(link) == "../../#{PLUGIN}/skills/#{name}"
    errors << "#{link} must be a symlink to ../../#{PLUGIN}/skills/#{name} (so the repo loads the skill)"
  end
end
Dir[".claude/skills/*"].each do |l|
  errors << "#{l} points to a skill that no longer exists" unless skills.include?(File.basename(l))
end
Dir["#{PLUGIN}/agents/*.md"].each do |file|
  fm, = front_matter(file)
  errors << "#{file}: agent needs name and description" if fm["name"].to_s.empty? || fm["description"].to_s.empty?
  link = ".claude/agents/#{File.basename(file)}"
  errors << "#{link} must link to ../../#{file}" unless File.symlink?(link) && File.readlink(link) == "../../#{file}"
end

# --- every path mentioned in the rulebook exists -------------------------------------
rulebook = Dir["#{PLUGIN}/skills/*/SKILL.md"] + Dir["#{PLUGIN}/agents/*.md"] +
           %w[CLAUDE.md AGENTS.md CONTRIBUTING.md README.md].select { |f| File.exist?(f) }
PATHISH = %r{\A(?:\.github/|\.claude/|\.claude-plugin/|_articles/|_data/|_includes/|_layouts/|assets/|plugins/|de/|articles/|graph/|examples/|run-code/)|
             \A(?:CLAUDE|AGENTS|CONTRIBUTING|README)\.md\z|\A(?:graph\.json|sitemap\.xml|robots\.txt|llms\.txt|Gemfile|_config\.yml)\z}x
rulebook.each do |file|
  File.read(file).scan(/`([^`\s]+)`/).flatten.uniq.each do |token|
    path = token.sub(/[.,:;)]+\z/, "").sub(/:\d+\z/, "")
    next unless path.match?(PATHISH)
    next if path.match?(/[<>*{}]|\.\.\./)            # placeholders like <slug>, globs
    errors << "#{file}: mentions `#{path}`, which does not exist" unless File.exist?(path) || File.symlink?(path)
  end
end

# --- coverage: every mechanism is described by a skill ------------------------------
skill_text = Dir["#{PLUGIN}/skills/*/SKILL.md"].map { |f| File.read(f) }.join("\n")
mechanisms = Dir[".github/scripts/*"] + Dir["_data/*.yml"] + Dir[".github/workflows/*.yml"]
mechanisms.sort.each do |m|
  next if skill_text.include?(m) || skill_text.include?(File.basename(m))
  errors << "#{m} is not described in any skill – document it in the matching skill"
end

# --- version bump when the plugin changes (pull requests) ---------------------------
if (i = ARGV.index("--base")) && (base = ARGV[i + 1])
  changed = `git diff --name-only #{base}...HEAD -- #{PLUGIN} .claude-plugin 2>/dev/null`.split("\n")
  if changed.any?
    old = `git show #{base}:#{PLUGIN}/.claude-plugin/plugin.json 2>/dev/null`
    old_version = old.empty? ? nil : JSON.parse(old)["version"]
    if old_version && old_version == manifest["version"]
      errors << "plugin files changed (#{changed.size}) but version is still #{old_version} – bump it in #{PLUGIN}/.claude-plugin/plugin.json"
    end
  end
end

warnings.each { |w| puts "warning: #{w}" }
errors.each { |e| puts "ERROR:   #{e}" }
puts "\nPlugin check: #{skills.size} skills, #{Dir["#{PLUGIN}/agents/*.md"].size} agents, " \
     "#{mechanisms.size} mechanisms covered, #{errors.size} errors, #{warnings.size} warnings."
exit(errors.empty? ? 0 : 1)
