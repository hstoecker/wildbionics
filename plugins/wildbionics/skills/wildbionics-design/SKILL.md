---
name: wildbionics-design
description: "UI/UX and front-end rules for WildBionics – design tokens, typography, surfaces, components (hero, lens tabs, cards, formulas, figures, key facts, FAQ, graph), responsive layout, accessibility (WCAG 2.2 AA, no-JS fallbacks, reduced motion), bilingual UI strings, SEO metadata in layouts and the no-dependency policy. Use when creating or changing pages, layouts, includes, CSS or JavaScript."
---

# WildBionics design system and UX rules

Concept: **field notebook meets lab journal** – editorial serif, precise mono labels, dark
"night/deep-sea" surfaces alternating with paper and sand, amber for nature, teal for science.

## Tokens (`assets/css/main.css`, `:root`)

- Surfaces: `--night` #0d1a16, `--ocean` #08171e/`--ocean-2`, `--paper` #f6f2e9, `--sand` #ece5d5, `--card` #fbf9f4
- Text: `--ink`, `--ink-2` (on light) · `--on-dark`, `--on-dark-2` (on dark)
- Accents: `--accent` #e3a93a / `--accent-ink` #8a5a00 (amber) · `--signal` #5ccbb6 / `--signal-ink` #0e6b5d (teal)
- Dimensions: time #95560f, space #0e6b5d, rules #2d5b88, adjacent #7a3d5c (light); lighter variants on dark (`.graph-page`)
- Context variables `--text`, `--text-2`, `--eyebrow`, `--focus`, `--rule` are set per surface – use them instead of hard-coding colours.
- Fonts (self-hosted, OFL, `assets/fonts/`): Fraunces (display; set `"WONK" 0` for formulas), Inter (text), JetBrains Mono (labels, eyebrows, code).

## Components (reuse, don't reinvent)

`eyebrow`, `section-title`, `section-intro`, `button--primary|ghost|dark|outline`, `link-arrow`,
`chips`, `caption` + `caption__label`, `lens__tabs`/`lens__panel` (+ `assets/js/lens.js`),
`formula` (+ `.frac`, `.sqrt`, `formula--steps`), `figure`/`figure--dark`, `code-card`/`.highlight`,
`key-facts`, `faq__item`, `references`, `graph-tags`, `article-card`, `dimension` cards, graph page.
New UI strings go into `_data/i18n.yml` for **every** language; templates never contain hard-coded
text.

## Layout and responsiveness

- Container `min(1200px, 100% − 2 × gutter)`, gutter 16–40 px; article text column 760 px.
- Breakpoints: 1080 px (2-column cards), 920 px (single column, no main nav), 600 px (phone).
- No horizontal scrolling at 390 px; tap targets ≥ 44 px; labels in SVGs enlarged on phones.

## Accessibility (WCAG 2.2 AA)

- Contrast ≥ 4.5:1 for text (the token pairs above are verified); focus visible (`:focus-visible`).
- Semantic HTML, one `<h1>` per page, landmarks, skip link, `lang` on `<html>` and on foreign-language snippets.
- Everything works without JavaScript: tabs degrade to stacked panels, the graph to a list.
- Respect `prefers-reduced-motion`; animations are decorative only.
- Interactive widgets follow WAI-ARIA patterns (tabs with arrow keys, buttons with `aria-pressed`/labels).
- SVG figures: `role="img"`, `<title>`, `<desc>` in the page language.

## Metadata (layouts handle it – keep it that way)

`_layouts/default.html` + `_includes/jsonld.html`: title, description, canonical, hreflang incl.
`x-default`, Open Graph/Twitter image, JSON-LD @graph. New page types need a `ref` (translations),
`lang`, `title`, `description` (50–160 chars) and, if special, `schema_type`.

## Policy

- No new dependencies, frameworks, CDNs or tracking; fonts and scripts are self-hosted and small.
- Plain CSS in `main.css`, vanilla JS in `assets/js/` loaded with `defer`, only on pages that need it.
- Visual changes are checked with screenshots on desktop (1440 px) and phone (390 px) in EN and
  DE – renderer: `plugins/wildbionics/skills/wildbionics-figures/scripts/shots.sh`.
