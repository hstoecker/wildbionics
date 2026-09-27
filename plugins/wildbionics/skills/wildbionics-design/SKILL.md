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
code examples (`_includes/code-result.html`: `code-actions`, `code-output`, `code-chart`,
`code-card__foot`, `code-variant` (`_includes/code-variant.html`); copy buttons from `assets/js/code.js` with a clipboard fallback and a
`role="status"` announcement), plain text pages (`_layouts/page.html`, e.g. `run-code/index.md`),
`key-facts`, `faq__item`, `references`, `graph-tags`, `article-card`, `dimension` cards, graph page,
header `menu` (mobile navigation, below).
New UI strings go into `_data/i18n.yml` for **every** language; templates never contain hard-coded
text.

## Layout and responsiveness

- Container `min(1200px, 100% − 2 × gutter)`, gutter 16–40 px; article text column 760 px.
- Breakpoints: 1080 px (2-column cards), 920 px (single column; the main nav moves into the menu),
  600 px (phone), 420 px (tighter header gaps), 385 px (menu button shows only its icon).
- **Navigation on phones:** `_includes/header.html` writes the nav items once and renders them
  twice – inline `site-nav` (desktop) and the `menu` disclosure (≤ 920 px, a `<details>` element,
  so it works without JavaScript; `assets/js/nav.js` closes it on link click, Escape and outside
  tap). The GitHub link moves into the menu on phones. Never hide navigation without a
  replacement; new top-level pages are added to `nav_items` only.
- No horizontal scrolling from 320 px (WCAG reflow) – check 320, 390 and 920 px; tap targets ≥ 44 px;
  labels in SVGs enlarged on phones; long German compounds need `hyphens: auto` plus
  `overflow-wrap: break-word` (not every browser has a German hyphenation dictionary).
- Long links, commands and code in narrow columns must wrap (`overflow-wrap: anywhere`, grid columns
  `minmax(0, 1fr)`, `white-space: pre-wrap` for command blocks). Measure instead of eyeballing:
  run the renderer with `SHOT_PRINT_TITLE=1 SHOT_JS='…'` (macOS) where the script compares
  `document.documentElement.scrollWidth` with `clientWidth` and lists elements whose right edge
  exceeds the viewport – the result must be 0 on every changed page. Rebuild (`jekyll build`) before
  measuring; a stale local server shows old CSS.

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
`lang`, `title`, `description` (50–160 chars), a `short_title` if the title is long (breadcrumb
name) and, if special, `schema_type` (`CollectionPage` lists its articles as an `ItemList`).

Rules for the JSON-LD graph (enforced by `check_site.py`):
- **Every page:** Organization, Person, WebSite, WebPage (`#webpage`) and one preview
  `ImageObject` (`#primaryimage`) with caption, `license`, `acquireLicensePage`, `creditText`,
  `creator` and `copyrightNotice` – the page and the article reference it by `@id`, never inline.
- **Captions describe the image:** `page.image_alt` for pages with their own `image`; pages that
  use the default card get `og_image_alt` from `_data/i18n.yml` (same text as `og:image:alt`) –
  never the page description.
- **Breadcrumbs:** Home › page, articles Home › Articles › article; names = `short_title | default:
  title`, identical to the visible `nav.breadcrumb`; the last item is the page itself; no
  breadcrumb on the home page and on `noindex` pages.
- Every `@id` reference to a node of the same page or the site must resolve.
- Figures are inline SVG (`role="img"`, `<title>`, `<desc>`) – accessible, but without an own URL
  they are not indexed as images and have no `ImageObject` yet (planned: figure files under
  `/assets/figures/` plus one `ImageObject` per figure).

## Policy

- No new dependencies, frameworks, CDNs or tracking; fonts and scripts are self-hosted and small.
- Plain CSS in `main.css`, vanilla JS in `assets/js/` loaded with `defer`, only on pages that need it.
- Visual changes are checked with screenshots on desktop (1440 px) and phone (390 px) in EN and
  DE – renderer: `plugins/wildbionics/skills/wildbionics-figures/scripts/shots.sh`.
