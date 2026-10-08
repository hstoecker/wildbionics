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
`role="status"` announcement), plain text pages (`_layouts/page.html`, e.g. `run-code/index.md`, `about/index.md` with
`schema_type: AboutPage`),
`key-facts`, `faq__item`, `references`, `graph-tags`, `article-card`, `dimension` cards, graph page,
header `menu` (mobile navigation, below).
New UI strings go into `_data/i18n.yml` for **every** language; templates never contain hard-coded
text.

## Layout and responsiveness

- Container `min(1200px, 100% − 2 × gutter)`, gutter 16–40 px; article text column 760 px.
- Breakpoints: 1080 px (2-column cards), 1120 px (the main nav moves into the menu – German needs
  about 1110 px; re-measure in EN and DE when adding a nav item or resizing the header brand), 920 px (single column),
  640 px (graph page), 600 px (phone), 460 px (tighter header gaps), 389 px (menu button shows only
  its icon).
- **Navigation on phones:** `_includes/header.html` writes the nav items once and renders them
  twice – inline `site-nav` (desktop) and the `menu` disclosure (≤ 1120 px, a `<details>` element,
  so it works without JavaScript; `assets/js/nav.js` closes it on link click, Escape and outside
  tap). The GitHub link moves into the menu on phones. Never hide navigation without a
  replacement; new top-level pages are added to `nav_items` only. A nav item that leaves the site (Discussions
  on GitHub) shows `↗` (`.nav-external`, `aria-hidden`) plus the visually hidden `nav.external`
  ("(on GitHub)"), so sighted and screen-reader users both know before they click.
- No horizontal scrolling from 320 px (WCAG reflow) – check 320, 390, 920 and 1121 px; tap targets ≥ 44 px
  on phones (language switch, copy buttons, pills, chips, footer and breadcrumb links – see the
  600 px block);
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
- **One landmark per purpose:** the footer's language list is a plain list labelled by its visible
  heading (`lang-switch.html context="footer"`), not a second "Language" navigation.
- **Foreign words:** English UI labels, error messages and paper titles on German pages carry
  `lang="en"` (sources: `lang` field, default `en`); formula `aria-label`s come from i18n.
- **Decorative glyphs** are not read aloud (`content: "+" / ""`, `aria-hidden` on "01"-style indices).
- **Copy buttons** sit next to the `<pre>`, never inside it, announce "Copied" in a `role="status"`
  region and fall back to selecting the text; code that scrolls sideways gets `tabindex="0"`.
- **Graph:** node names from the i18n templates `graph.node_name`/`node_name_dim` (no plural
  trouble: "connections: 3"), `aria-pressed` on pinnable nodes, an invisible tap circle of ≥ 44 px
  on screen (`.node-hit`, excluded from the label-collision boxes), the info panel floats beside
  the active node (towards the middle, never over the node or its label) and lets the pointer
  through while hovering (`pointer-events: none`, `auto` once pinned) – otherwise it covers the
  pointer, ends the hover and flickers; on phones it sits below the drawing and scrolls into view;
  the no-JS list renders open.
- SVG figures: `role="img"`, `aria-labelledby` → `<title>` and `aria-describedby` → `<desc>`, both in
  the page language.

## Metadata (layouts handle it – keep it that way)

`_layouts/default.html` + `_includes/jsonld.html`: title, description, canonical, hreflang incl.
`x-default`, Open Graph/Twitter image, JSON-LD @graph. New page types need a `ref` (translations),
`lang`, `title`, `description` (50–160 chars), a `short_title` if the title is long (breadcrumb
name) and, if special, `schema_type` (`CollectionPage` lists its articles as an `ItemList`).
- **Image sitemap:** `sitemap.xml` lists every image of a page for image search – its preview card
  (`image`, the default card only on `home`), its figures (`/figures/<name>.<lang>.svg`, from the `page` in
  `_data/figures.yml`) and its code-example charts. `check_site.py` fails on a listed image without a
  file and on a figure or chart that no page lists. Figures and charts are found by image search only
  through this list and their `ImageObject`s: inline SVGs are not indexed as images.

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
- **No Markdown in data:** key facts go through `_includes/plain-text.html` before they reach
  JSON-LD (`abstract`) or `llms.txt` (citation links, `**`, `{:.cite}` removed; `refs="keep"`
  keeps "[3]" where a source list follows). The gate fails on `**`, `{:` or `](#` in either.
- **Collection and data pages:** a `CollectionPage` has `mainEntity` → `ItemList` of its articles;
  a page with `dataset: true` has `mainEntity` → its own `#dataset` node (one per language) with
  two distributions, `/graph.jsonld` (application/ld+json) and `/graph.json`. The `Dataset` has a
  `name` and a 50–5000-character `description` and **no `isPartOf` → `#website`**: Google accepts only a
  larger `Dataset` there (Search Console: "Invalid object type for field isPartOf"); the page links
  it to the site through `WebPage.mainEntity` and `WebPage.isPartOf`. `check_site.py` enforces this.
- **Articles link into the graph:** `keywords` = the free keywords plus every ontology term as a
  `DefinedTerm` with the stable IRI `<site>/graph/#term-<slug>` and `inDefinedTermSet`; lenses are
  `educationalAlignment` (educationalSubject → the lens's discipline IRI). See `wildbionics-graph`.
- **Dates:** only real dates – `updated | default: date`; pages without a date get no `lastmod`.
- **`noindex` pages** (404) carry no canonical and no hreflang. Titles never repeat the brand:
  the layout skips " · WildBionics" when the title already contains it. Descriptions 50–160
  characters (the gate warns outside). `og:locale` is `en_GB` (British spelling) / `de_DE`.
- **Charts of code examples** (`/examples/<ref>/<name>.<lang>.svg`) are one `ImageObject` each
  (`#chart-<name>`): `contentUrl`, `encodingFormat`, size, `name` = the include's `label`,
  `caption` = its `caption`, `description` = its `alt`, and the same licence fields as the preview
  image; the article lists them in `associatedMedia`. `code_examples.py` copies label, caption and
  alt into `_data/code_examples.yml`; the gate fails on a chart without its ImageObject.
- **Figures** stay inline SVG on the page (`role="img"`, `<title>`, `<desc>`) and are also published
  as standalone files `/figures/<name>.<lang>.svg` (`.github/scripts/figures.py`, registry
  `_data/figures.yml`, fonts embedded as subsets). Every page lists the figures it shows as one
  `ImageObject` each (`#figure-<name>`: `contentUrl`, `encodingFormat`, `name` = title, `description`
  = desc, licence fields) – from the article's `associatedMedia` or, on other pages, the WebPage's.
  The gate fails on a figure without its ImageObject or file, and on a file whose fonts are not embedded.

## Logo and icons

- **Mark:** a bee flying to the right inside a honeycomb cell – nature (bee) and bionics (the
  hexagon). Three colours only: night `#0d1a16`, cream `#eef2ea`, amber `#e3a93a`. The geometry
  lives once in `_includes/sprite.svg` (`#logo-mark`: hexagon and wings in `currentColor`,
  `--accent`, `--night`; stripes are arc paths, no `clipPath`, so it renders inside `<use>`), used
  by header, footer, `og-card.html` and – large, on the right of the page header – pages with
  `hero_mark: true` (`_layouts/page.html`, e.g. `/about/`; hidden ≤ 760 px). Sizes: header 44 px
  with a 1.9 rem wordmark (phones ≤ 600 px: 38 px, wordmark 1.35 rem; ≤ 389 px 36 px, 1.1 rem),
  footer 30 px, OG card 40 px. Header gaps tighten at ≤ 460 px so brand, language switch and menu
  fit down to 320 px. `assets/favicon.svg` is the same mark on a night tile (rx 7).
- **Raster files** (render `favicon.svg` at 512 px with `shots.sh`, downscale with PIL – no new tools):
  `/favicon.ico` (16/32/48 px, rounded tile), `assets/favicon-192.png` and
  `assets/apple-touch-icon.png` (180 px) full-bleed square (Google crops favicons round, iOS rounds
  the corners itself), `assets/logo-512.png` (rounded tile, transparent corners; JSON-LD publisher logo).
- **Google Search favicon:** the home pages link an icon that is square and a multiple of 48 px
  (`favicon.ico` 48 px, `favicon-192.png`), crawlable (robots.txt allows `/`), at a stable URL.
  `check_site.py` fails otherwise. Google picks up a change when it recrawls the home page
  (Search Console → URL inspection → request indexing speeds it up).
- **When the mark changes:** update the symbol, `favicon.svg`, all raster files and the OG images in
  `assets/og/` (their logo; recipe in `wildbionics-figures`, step 6), and show the user the renders.
  The bee logo was swapped into the existing OG images in place (same 40 px size and position);
  a card re-rendered from `og-card.html` uses `#logo-mark` and matches them – compare the logo
  crop when you regenerate one.

## Policy

- No new dependencies, frameworks, CDNs or tracking; fonts and scripts are self-hosted and small.
  `_config.yml` sets `theme: null` – the github-pages default theme would ship an unused 136 KB
  stylesheet. Icons: see "Logo and icons" above.
- Plain CSS in `main.css`, vanilla JS in `assets/js/` loaded with `defer`, only on pages that need it.
- Link CSS and JS from `_layouts/default.html` with `?v={{ asset_version }}` (the build time): GitHub Pages
  lets browsers cache assets for 10 minutes, and a page with a new figure but an old `main.css` shows
  unstyled SVG (black fills). New asset links get the same suffix.
- Visual changes are checked with screenshots on desktop (1440 px) and phone (390 px) in EN and
  DE – renderer: `plugins/wildbionics/skills/wildbionics-figures/scripts/shots.sh`.
