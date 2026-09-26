# WildBionics – Project Context for Claude

## What this is
**wildbionics.com** – a bilingual open-source compendium that explains science (physics, math, computer science, chemistry) through examples from animals, plants, geology and bionics.
- Primary language: **English** (site root `/`), secondary: **German** (`/de/`). More languages later via community (`/fr/`, …).
- Owner: Hendrik Stöcker. Communicates in German; site content EN first, then DE.
- Target audience: nature enthusiasts, students, developers, open-source community.

## Core USP: the "Lens" feature
Each article can be viewed through switchable lenses on the same phenomenon, e.g. bat echolocation:
- Physics lens: acoustics, Doppler effect
- Math lens: trigonometry of distance measurement
- CS lens: code for radar/sonar algorithms of autonomous drones

## Ontology – 4 dimensions (knowledge graph)
1. **Time** – evolution & geology (Big Bang → humanoid robots)
2. **Space** – habitats & scales (microcosm, deep sea, desert, stratosphere, lab, urban)
3. **Rules** – physics (mechanics, thermodynamics, optics, acoustics, EM, quantum, relativity)
4. **Adjacent sciences** – math, CS/AI, medical technology, bionics, materials science

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
- [ ] **Phase 0** – Minimal live site: `_config.yml`, `index.md` (EN), `de/index.md` (DE), `CNAME`; DNS check (A records to GitHub Pages, `www` CNAME), enforce HTTPS, verify domain in GitHub.
- [ ] **Phase 1** – Mac setup: Homebrew, git, gh, Ruby + Bundler + Jekyll; clone repo; `bundle exec jekyll serve`.
- [ ] **Phase 2** – Landing page design: hero + tagline ("Nature's physics, explained."), lens demo (bat, 3 tabs), 4 dimensions, flagship article teaser, "Contribute on GitHub", language switcher, footer with licenses.
- [ ] **Phase 3** – First flagship article with lens feature, JSON-LD, DOI sources; `llms.txt`.
- [ ] **Phase 4** – `graph.json` from front matter + interactive graph view.

## Working style
- Step by step, small verifiable wins. Explain commands before running them (owner is setting up a fresh Mac).
- Don't add dependencies/plugins without asking; prefer what GitHub Pages builds natively.
