---
name: wildbionics-contribute
description: "Start here for any work on WildBionics (wildbionics.com) – orientation, repository map, which WildBionics skill to use for which task, the contribution and approval workflow (branch → checks → pull request → review → maintainer approval → deploy), local setup and the rule that skills are updated together with every convention change. Use when someone asks how to contribute, starts a new task in this repository, or is unsure which rules apply."
---

# Contributing to WildBionics

WildBionics is a bilingual (English first, then German) open compendium that connects biology
with physics, mathematics, chemistry, computer science and Physical AI – through animals, plants,
geology, bionics and robots. It is a static Jekyll site on GitHub Pages; everything is in this
repository, and every change reaches the live site only through a reviewed pull request.

## Which skill for which task

| Task | Skill |
|---|---|
| Orientation, workflow, setup, keeping skills up to date | `wildbionics-contribute` (this one) |
| Write or extend an article (structure, research, sources, lenses, SEO/AEO/GEO) | `wildbionics-article` |
| Translate or check German/English wording and technical terms | `wildbionics-translate` |
| Create or change a figure, diagram or preview image | `wildbionics-figures` |
| Add ontology terms, organisms, lenses; anything about the knowledge graph | `wildbionics-graph` |
| Pages, components, layout, accessibility, UI strings | `wildbionics-design` |
| Review a pull request or your own work before submitting | `wildbionics-review` (+ agent `wildbionics-fact-checker`) |

Project facts and architecture decisions live in `CLAUDE.md` (read it first); `AGENTS.md` is the
short version for other AI agents; `CONTRIBUTING.md` is the human guide.

## Repository map

- `_articles/<slug>.<lang>.md` – articles (one file per language, linked by `ref`)
- `_data/i18n.yml` – all UI strings (EN/DE keys must match) · `_data/glossary.yml` – EN→DE terms
- `_data/taxonomy.yml`, `_data/beings.yml`, `_data/lenses.yml` – ontology and graph data
- `_includes/` – page parts; `_includes/svg/` – figures; `_layouts/` – page layouts
- `assets/css/main.css`, `assets/js/` – design system and the only scripts (no dependencies)
- `graph.json`, `sitemap.xml`, `robots.txt`, `llms.txt` – generated machine-readable files
- `.github/scripts/` – quality gates · `.github/workflows/` – CI, deploy, review
- `plugins/wildbionics/` – this plugin (skills, agent) · `.claude-plugin/marketplace.json` – marketplace

## Workflow (humans and agents)

1. **Pick or open an issue** (article idea, correction, translation, feature) so work is visible.
2. **Create a branch** (`article/<slug>`, `fix/<topic>`, …) – never commit to `main` directly.
3. **Work with the matching skill.** Content changes follow the order research → English text →
   figures → German translation → knowledge-graph data.
4. **Run the gates locally** before pushing:
   ```bash
   ruby .github/scripts/check_terms.rb
   ruby .github/scripts/check_content.rb
   ruby .github/scripts/check_plugin.rb
   bundle exec jekyll build && python3 .github/scripts/check_site.py _site
   ```
5. **Self-review** with `wildbionics-review` and fix every must-fix finding.
6. **Open a pull request** using the template. CI runs all gates, builds a preview (downloadable
   artifact with screenshots) and – for branches in this repository – posts a Claude review.
7. **Maintainer approval:** Hendrik Stöcker reviews and merges. Only merged changes deploy
   (GitHub Actions → GitHub Pages → IndexNow).

## CI, review and deploy (what runs where)

| Workflow / script | When | What |
|---|---|---|
| `.github/workflows/deploy.yml` | every push to `main` and every PR | gates `check_terms.rb`, `check_content.rb`, `check_plugin.rb` (PR: `--base` → version bump), Jekyll build, `check_site.py`; PR: `preview_shots.sh` + preview artifact; `main`: deploy to Pages, then `indexnow.py` notifies search engines |
| `.github/workflows/claude-review.yml` | PR opened/updated (branches of this repo) | Claude runs `wildbionics-review` from the marketplace on `main` and posts one review comment |
| `.github/workflows/claude.yml` | `@claude` in an issue, PR comment or review | Claude works on the request with these skills and opens a pull request |
| `.github/scripts/check_terms.rb` | CI + local | glossary terms, EN/DE consistency, typography, taxonomy/beings/lenses |
| `.github/scripts/check_content.rb` | CI + local | article front matter, lens panels, citations ↔ sources, DOIs, figures |
| `.github/scripts/check_plugin.rb` | CI + local | manifests, skill links, referenced paths exist, coverage, version bump |
| `.github/scripts/check_site.py` | CI + local | titles, descriptions, canonical/hreflang, JSON-LD, links, sitemap, graph.json |
| `.github/scripts/preview_shots.sh` | CI (PR) | screenshots of key pages and changed articles (1440 px, 390 px) |
| `.github/scripts/indexnow.py` | CI (after deploy) | submits the sitemap URLs to IndexNow (key in `_config.yml`) |
| `.github/CODEOWNERS` | every PR | the maintainer is the required reviewer |

**Branch protection on `main`:** changes only via pull requests; required checks `build` and
`plugin` must pass; one approving review from the code owner; new commits dismiss earlier
approvals; no force-push or deletion. Admins may merge their own PRs (GitHub forbids self-approval).

Claude in CI needs the repository secret `CLAUDE_CODE_OAUTH_TOKEN` (or `ANTHROPIC_API_KEY`) and the
Claude GitHub App; without them the review job only prints a notice. Fork PRs receive no secrets –
the maintainer reviews them by hand (or runs `wildbionics-review` locally).

## Keeping the skills up to date – mandatory

The skills are the project's rulebook for humans *and* agents. **Whenever a convention, file
structure, check or workflow changes, update the affected skill in the same pull request**, and
bump `version` in `plugins/wildbionics/.claude-plugin/plugin.json` (semver: patch = wording,
minor = new rule or skill, major = changed workflow). `check_plugin.rb` enforces that skills only
reference existing files and that every check script, data file and workflow is covered by a
skill; CI fails a PR that changes the plugin without a version bump.

## Local setup (macOS)

```bash
brew install ruby@3.3 gh          # GitHub Pages builds with Ruby 3.3
bundle install                    # github-pages gem (no Gemfile.lock in the repo, on purpose)
bundle exec jekyll serve --livereload   # http://localhost:4000
```
Opening the repository in Claude Code loads these skills automatically (`.claude/skills/` links
to the plugin). Outside the repository, install the plugin from the marketplace:
`/plugin marketplace add hstoecker/wildbionics` and `/plugin install wildbionics@wildbionics`.

## Ground rules

- English is the source language; German must use the glossary terms.
- Every factual statement needs a verifiable source (peer-reviewed, with DOI where possible);
  hypothetical topics (e.g. superintelligence) are presented as scenarios, never as facts.
- No new dependencies, plugins or external scripts without the maintainer's approval.
- Accessibility target WCAG 2.2 AA; pages must work without JavaScript.
- Content licence CC BY-SA 4.0, code MIT – contributions are accepted under these licences.
- Never commit secrets; never weaken a check to make it pass.
