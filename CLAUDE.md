# WildBionics – Project Context for Claude

## What this is
**wildbionics.com** – a bilingual open-source compendium that connects biology with physics, math, chemistry, computer science and Physical AI – through examples from animals, plants, geology and bionics, up to robots and AI.
- Primary language: **English** (site root `/`), secondary: **German** (`/de/`). More languages later via community (`/fr/`, …).
- Owner: Hendrik Stöcker. Communicates in German; site content EN first, then DE.
- Target audience: nature enthusiasts, students, developers, open-source community.

## Core USP: the "Lens" feature
Each article can be viewed through switchable lenses on the same phenomenon, e.g. bat echolocation:
- Biology lens: sensory ecology, bat–moth arms race
- Physics lens: acoustics, Doppler effect
- Math lens: trigonometry of distance measurement
- CS lens: code for radar/sonar algorithms of autonomous drones
- Physical AI lens (key `physical-ai`, first used in the gecko article: gecko-inspired climbing robots and grippers): embodied AI and robots that sense and act in the physical world, e.g. sonar-guided robots

## Ontology – 4 dimensions (knowledge graph)
1. **Time** – evolution & geology, continued into technology (Big Bang → … → age of AI → humanoid robots → superintelligence). Slugs `age-of-ai`, `future-scenarios`. Superintelligence does not exist today: always present it as a hypothesis/scenario with sources, never as fact.
2. **Space** – habitats & scales (microcosm, deep sea, desert, stratosphere, lab, urban)
3. **Rules** – physics (mechanics, thermodynamics, optics, acoustics, EM, quantum, relativity)
4. **Adjacent sciences** – biology, chemistry, math, CS, artificial intelligence, **Physical AI** & robotics, medical technology, bionics, materials science

## Architecture decisions (agreed, 2026-09-26)
- **Static site: Jekyll on GitHub Pages** with custom domain wildbionics.com. No server.
- **No Next.js, no Neo4j, no Docker for now.** The graph is derived from article front matter at build time (→ `graph.json`), rendered client-side (D3/Cytoscape) later. Revisit only if Jekyll becomes limiting.
- **i18n without plugins**: English at root, German under `/de/`, UI strings in `_data/i18n.yml`, `lang` + `ref` in front matter to link translations, `hreflang` tags incl. `x-default`.
- Content authored in Markdown (Obsidian can open the repo as a vault).
- Accessibility target: **WCAG 2.2 AA**.
- Machine readability: JSON-LD (Schema.org) per page, `/llms.txt`, sitemap.
- Licenses: `LICENSE` = MIT (code), `LICENSE-CONTENT.txt` = CC BY-SA 4.0 (content).
- Deferred: Google Trends integration, graph database, complex tooling.

## Article front matter (draft)
```yaml
---
id: "pistol-shrimp-cavitation"
lang: en
ref: pistol-shrimp-cavitation   # same value across translations
title: "The Pistol Shrimp and the Physics of Cavitation"
date: 2026-09-26
dimensions:
  time: ["cenozoic", "modern-era"]
  space: ["deep-sea", "coastal"]
  physics: ["thermodynamics", "fluid-dynamics", "acoustics"]
  adjacent_sciences: ["medical-technology", "materials-science"]
beings: ["pistol-shrimp"]
sources:
  - title: "How snapping shrimp snap: through cavitating bubbles"
    doi: "10.1126/science.289.5487.2114"
status: draft
---
```

## Roadmap (keep it simple, quick wins first)
- [x] **Phase 0** – Minimal live site: `_config.yml`, home pages (EN at `/`, DE at `/de/`), `CNAME`; DNS check (A records to GitHub Pages, `www` CNAME), enforce HTTPS, verify domain in GitHub.
- [x] **Phase 1** – Mac setup: Homebrew, git, gh, Ruby + Bundler + Jekyll; clone repo; `bundle exec jekyll serve`.
- [x] **Phase 2** – Landing page design: hero + tagline ("Nature's physics, explained."), lens demo (bat, 3 tabs), 4 dimensions, flagship article teaser, "Contribute on GitHub", language switcher, footer with licenses.
- [x] **Phase 3** – First flagship article with lens feature, JSON-LD, DOI sources; `llms.txt`.
- [x] **Phase 4** – `graph.json` from front matter + interactive graph view (`/graph/`, `/de/wissensgraph/`).

## Contribution system (plugin, skills, review)
- The repository is a **Claude Code plugin marketplace**: `.claude-plugin/marketplace.json` → plugin `plugins/wildbionics/` (skills `wildbionics-contribute`, `-article`, `-translate`, `-figures`, `-graph`, `-design`, `-review`; agent `wildbionics-fact-checker`). `.claude/skills/*` and `.claude/agents/*` are symlinks to the plugin, so opening the repo loads them. Install elsewhere: `/plugin marketplace add hstoecker/wildbionics`, `/plugin install wildbionics@wildbionics`.
- **The skills are the rulebook.** Any change of a convention updates the matching skill in the same PR and bumps the plugin `version`; `check_plugin.rb` enforces references, coverage and the version bump.
- Every change goes through a PR: gates + preview + Claude review (`claude-review.yml`), `@claude` in issues/PRs (`claude.yml`); the maintainer approves and merges (`CODEOWNERS`). Human guide: `CONTRIBUTING.md`, website `/contribute/`; agents: `AGENTS.md`.

## How things are built (as of Phase 4)
- **Deploy:** GitHub Actions (`.github/workflows/deploy.yml`): gates (terms, content, plugin, code examples) → Jekyll build → `.github/scripts/check_site.py` quality gate → GitHub Pages → IndexNow (`.github/scripts/indexnow.py`, key in `_config.yml` + `/<key>.txt`). PRs only build + check.
- **Articles:** `_articles/<slug>.<lang>.md`, layout `article`; lenses via `{% include lens-tabs.html %}` + `lens-start`/`lens-end`; key facts, FAQ, sources (with DOI) in front matter → rendered + JSON-LD (Article, FAQPage, BreadcrumbList). Ontology slugs need a display name in `_data/taxonomy.yml`.
- **Code examples:** every Python block in the site is a complete program followed by `{% include code-result.html file="…" %}`. `.github/scripts/code_examples.py` runs them all (CI: Python 3.12, `examples/requirements.txt`, `--check`) and writes the tested output (`_data/code_examples.yml`), charts, `.py` downloads and Colab notebooks (`examples/<ref>/`). Copy buttons: `assets/js/code.js`. Reader guide: `/run-code/`, `/de/code-ausfuehren/` (layout `page`). Rules: `wildbionics-article` section 4. No in-browser Python runtime (decided 2026-09-27: static result + Colab instead).
- **UI strings:** `_data/i18n.yml` (EN/DE keys must match). SVG figures in `_includes/svg/` pull labels from i18n.
- **Figures:** follow the project skill `plugins/wildbionics/skills/wildbionics-figures/` – every figure must be recognisable, conceptually clear, correct and attractive; iterate with rendered screenshots (`scripts/shots.sh`) until its acceptance checklist passes, and show the user the final render.
- **Translation:** follow the project skill `plugins/wildbionics/skills/wildbionics-translate/`; German technical terms are fixed in `_data/glossary.yml` and enforced by `.github/scripts/check_terms.rb` (runs first in CI; forbidden variants fail the build).
- **Knowledge graph:** `graph.json` (Liquid, built from `_data/taxonomy.yml` with `dim`/`order`, `_data/beings.yml`, `_data/lenses.yml` and article front matter) → `assets/js/graph.js` (own force layout, no dependencies; dimensions are fixed anchors, label-collision pass via getBBox). The page `_includes/graph-page.html` also renders a full no-JS list. `check_site.py` validates graph.json.
- **Machine readability:** `sitemap.xml` (hreflang), `robots.txt` (AI crawlers allowed), `llms.txt`, OG images in `assets/og/` (1200×630, rendered from `_includes/og-card.html`). JSON-LD graph rules (breadcrumbs = visible breadcrumb, licensed `#primaryimage`, `ItemList` on collection pages) live in the `wildbionics-design` skill and are enforced by `check_site.py`.
- Check locally (cloud sessions first need `LANG=C.UTF-8` and the setup script from the `wildbionics-contribute` skill): `ruby .github/scripts/check_terms.rb && ruby .github/scripts/check_content.rb && ruby .github/scripts/check_plugin.rb && python3 .github/scripts/code_examples.py --check && bundle exec jekyll build && python3 .github/scripts/check_site.py _site`

## Working style
- Step by step, small verifiable wins. Explain commands before running them (owner is setting up a fresh Mac).
- Don't add dependencies/plugins without asking; prefer what GitHub Pages builds natively.
