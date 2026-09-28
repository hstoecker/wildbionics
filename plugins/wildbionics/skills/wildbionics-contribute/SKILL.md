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
- `_data/taxonomy.yml`, `_data/beings.yml`, `_data/thought_experiments.yml`, `_data/lenses.yml` – ontology and graph data
- `_includes/` – page parts; `_includes/svg/` – figures; `_layouts/` – page layouts
- `assets/css/main.css`, `assets/js/` – design system and the only scripts (no dependencies)
- `graph.json`, `graph.jsonld`, `sitemap.xml`, `robots.txt`, `llms.txt` – generated machine-readable files
- `examples/` – generated downloads, Colab notebooks and charts of the code examples, plus
  `examples/requirements.txt`; `_data/code_examples.yml` – their tested output (both written by
  `.github/scripts/code_examples.py`, see `wildbionics-article`)
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
   python3 .github/scripts/code_examples.py --check   # needs examples/requirements.txt installed
   bundle exec jekyll build && python3 .github/scripts/figures.py _site && python3 .github/scripts/check_site.py _site
   ```
5. **Self-review** with `wildbionics-review` and fix every must-fix finding.
6. **Open a pull request** using the template. CI runs all gates, builds a preview (downloadable
   artifact with screenshots) and – for branches in this repository – posts a Claude review.
7. **Maintainer approval:** Hendrik Stöcker reviews and merges. Only merged changes deploy
   (GitHub Actions → GitHub Pages → IndexNow).

## CI, review and deploy (what runs where)

| Workflow / script | When | What |
|---|---|---|
| `.github/workflows/deploy.yml` | every push to `main` and every PR | gates `check_terms.rb`, `check_content.rb`, `check_plugin.rb` (PR: `--base` → version bump), `code_examples.py --check` (Python 3.12), Jekyll build, `check_site.py`; PR: `preview_shots.sh` + preview artifact; `main`: deploy to Pages, then `indexnow.py` notifies search engines of the changed pages |
| `.github/workflows/claude-review.yml` | PR opened/updated (branches of this repo) | Claude runs `wildbionics-review` from the marketplace on `main` and posts one review comment; the transcript is kept as artifact `claude-review-pr-<n>`, blocked tool calls appear as warnings; if Claude did not post its report, the job posts Claude's final message (or a notice). Changes to this workflow are only tested after merging – the action refuses to run on a PR that edits its own workflow |
| `.github/workflows/claude.yml` | `@claude` in an issue, PR comment or review | Claude works on the request with these skills, pushes a branch after every major step and posts a link to create the pull request; for small, focused tasks (turn limit, maintainer's tokens) – whole articles are written with Claude Code |
| `.github/scripts/check_terms.rb` | CI + local | glossary terms, EN/DE consistency, typography, taxonomy/beings/thought experiments/lenses |
| `.github/scripts/check_content.rb` | CI + local | article front matter, lens panels, citations ↔ sources, DOIs, figures |
| `.github/scripts/check_plugin.rb` | CI + local | manifests, skill links, referenced paths exist, coverage, version bump |
| `.github/scripts/code_examples.py` | CI + local | runs every Python example; writes output (`_data/code_examples.yml`), charts, `.py` downloads and Colab notebooks; `--check` fails on errors or stale files – and still rewrites them, so run it on a clean tree and look at `git status` (charts can differ slightly outside CI's Python 3.12; don't commit those) |
| `.github/scripts/figures.py` | CI + local (after `jekyll build`) | writes `/figures/<name>.<lang>.svg` for every figure in `_data/figures.yml`: cut from the built page, CSS from `main.css`, font subsets embedded (needs `.github/scripts/requirements.txt`: fonttools, brotli) |
| `.github/scripts/check_site.py` | CI + local | titles, descriptions, canonical/hreflang, JSON-LD (resolving `@id`s, breadcrumbs, licensed preview image), links, sitemap, graph.json |
| `.github/scripts/preview_shots.sh` | CI (PR) | screenshots of key pages and changed articles (1440 px, 390 px) |
| `.github/scripts/indexnow.py` | CI (`main`) | `changed` (build job, before deploy): lists the pages whose HTML differs from the live site or are new; after deploy submits only those to IndexNow (key in `_config.yml`) – CSS, script or docs-only deploys submit nothing |
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
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install -r examples/requirements.txt -r .github/scripts/requirements.txt   # code examples + figure files
bundle exec jekyll serve --livereload   # http://localhost:4000 (keeps running – last line)
```
If `jekyll build` fails with "Invalid US-ASCII character", set `export LANG=en_US.UTF-8`.
Opening the repository in Claude Code loads these skills automatically (`.claude/skills/` links
to the plugin). Outside the repository, install the plugin from the marketplace:
`/plugin marketplace add hstoecker/wildbionics` and `/plugin install wildbionics@wildbionics`.

## Claude Code on the web (claude.ai/code) – one-time setup

The website guide recommends this way first (1 · Claude Code, recommended; 2 · `@claude` on
GitHub, friends & family only, because it uses the maintainer's Claude tokens; 3 · by hand, only
experts the maintainer knows personally – anchors `#claude-code`, `#github`, `#by-hand`).

Cloud sessions run in an Ubuntu VM (Ruby 3.3, Python, Node, Playwright Chromium preinstalled) whose
default network level **Trusted** blocks the research APIs the fact-checking needs. Create a cloud
environment named `WildBionics` (environment selector → *Add cloud environment*; later: environment
menu in the session's title bar → *Edit*) with network access **Custom**, tick *Also include
default list of common package managers*, and allow these domains:

```text
api.crossref.org
doi.org
eutils.ncbi.nlm.nih.gov
pubmed.ncbi.nlm.nih.gov
www.ncbi.nlm.nih.gov
api.semanticscholar.org
www.wikidata.org
*.wikipedia.org
```

Two more fields are required – both learnt from failing sessions:

- **Environment variables:** `LANG=C.UTF-8`. The VM has no UTF-8 locale (`LC_CTYPE=POSIX`);
  without it Jekyll and all Ruby gates crash with `invalid byte sequence in US-ASCII`.
- **Setup script:**
  ```bash
  #!/bin/bash
  set -e
  gem install github-pages -v 232 --no-document
  ln -sf "$(ruby -e 'print Gem.bindir')/jekyll" /usr/local/bin/jekyll
  python3 -m pip install numpy==2.0.2 scipy==1.13.1 matplotlib==3.9.4 fonttools==4.54.1 brotli==1.1.0   # code examples + figure files, pinned as in examples/ and .github/scripts/requirements.txt
  ```
  `ruby` on the `PATH` installs gems into an rbenv Ruby whose `bin/` is not on the `PATH`, so
  `bundle exec jekyll` fails with `bundler: command not found: jekyll` until `jekyll` is linked.

Then start a **new** session on `hstoecker/wildbionics` with that environment (environment
settings only apply to new sessions) and verify it first: all five local gates report 0 errors and
`api.crossref.org` answers. In a session without these settings, `export LANG=C.UTF-8` and the same
setup-script commands fix it for that session. Figures are rendered with `shots.sh`, which finds the
preinstalled Chromium; CI also attaches screenshots to every pull request (artifact
`preview-pr-<n>`). If the repository is missing from the list or a push is refused, the
contributor has not accepted the collaborator invitation or must reconnect GitHub.
On Windows, prefer claude.ai/code: `.claude/skills` are symlinks, which plain Windows git may
check out as text files.

## Ground rules

- English is the source language; German must use the glossary terms.
- Every factual statement needs a verifiable source (peer-reviewed, with DOI where possible);
  hypothetical topics (e.g. superintelligence) are presented as scenarios, never as facts.
- No new dependencies, plugins or external scripts without the maintainer's approval.
- Accessibility target WCAG 2.2 AA; pages must work without JavaScript.
- Content licence CC BY-SA 4.0, code MIT – contributions are accepted under these licences.
- Never commit secrets; never weaken a check to make it pass.
