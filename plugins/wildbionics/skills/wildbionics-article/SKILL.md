---
name: wildbionics-article
description: "Write or extend a WildBionics article – research protocol with verified sources (DOI via Crossref/PubMed), article structure and front matter, lens panels (biology, physics, mathematics, computer science, Physical AI), key facts, FAQ, citations, worked calculations and runnable code, SEO/AEO/GEO fields and OG image. Use for new articles, new sections or lenses, and any change to factual content."
---

# Writing a WildBionics article

An article explains **one natural phenomenon** so that a curious reader understands it and can
check every claim. Reference article: `_articles/pistol-shrimp-cavitation.en.md` (and `.de.md`).

## 1. Research protocol (before writing)

1. Collect **primary sources**: peer-reviewed papers, ideally with DOI; prefer open access.
2. **Verify every source** via Crossref (`https://api.crossref.org/works/<doi>`) or PubMed
   (E-utilities) – title, authors, journal, volume, pages, year must match what you cite.
   A DOI you have not resolved is not a source. In a cloud session these APIs must be allowed
   in the environment (see `wildbionics-contribute`); if a lookup fails, say so – never guess.
3. Read at least the abstract (PubMed `efetch`, Semantic Scholar, open-access full text).
   Note for each number *where exactly* it comes from. If a source says "at least 5,000 K",
   write "at least 5,000 K", not "5,000 K".
4. Derived numbers (e.g. a collapse time from Rayleigh's formula) are **calculated in a script**,
   and the worked calculation is shown in the article with its assumptions labelled.
5. Code in an article is a **complete, tested program** (section 4) – its output and chart on the
   page come from an actual run, never from typing.
6. Anything speculative or hypothetical (e.g. superintelligence, future robots) is written as a
   scenario with sources for the positions described – never as fact.

## 2. File and front matter

`_articles/<slug>.en.md` (source) and `_articles/<slug>.de.md` (translation, see
`wildbionics-translate`). Required front matter (checked by `check_content.rb`):

```yaml
id: <slug>                     # = ref, same in all languages
lang: en
ref: <slug>
title: "…"                     # ≤ 70 characters incl. " · WildBionics" where possible
short_title: "…"               # breadcrumb and graph label
kicker: "Flagship article · Fluid dynamics"
description: "…"               # 50–160 characters, answer-first (search snippet)
dek: "…"                       # longer teaser under the title (optional)
date: 2026-09-26
updated: 2026-09-27           # set on every later change of facts, text or figures: visible date,
                               # JSON-LD dateModified, sitemap lastmod (never fake it with the build time)
permalink: /articles/<slug>/   # DE: /de/artikel/<german-slug>/
image: /assets/og/<slug>-en.jpg
image_alt: "…"                 # describes what the OG image shows: og:image:alt + ImageObject caption
hero_figure: svg/<figure>.svg  # see wildbionics-figures
hero_caption: "<span class=\"caption__label\">Fig. 1</span> …"
educational_level: "Intermediate"
keywords: [...]                # ≥ 3
about: [{ name, wikidata: Q…, wikipedia }]   # main subjects, Wikidata IDs verified
mentions: [{ name, wikidata: Q… }]
dimensions: { time: [...], space: [...], physics: [...], adjacent_sciences: [...] }  # slugs from _data/taxonomy.yml
beings: [<slug>]               # from _data/beings.yml (real organisms)
thought_experiments: [<slug>]  # from _data/thought_experiments.yml – instead of beings when the subject is imagined
lenses: [biology, physics, math, cs]          # keys from _data/lenses.yml
key_facts: [...]               # 3–7 answer-ready facts with citations
faq: [{ q, a }]                # ≥ 3, plain text answers (also FAQPage JSON-LD)
sources: [{ authors: [...], year, title, journal, volume, pages, doi, open_access? }]
status: draft | published
```

## 3. Body structure

1. Intro section (`## …`): the phenomenon, who/where, why it is remarkable – with citations.
2. A short sequence section if there is a process ("The snap in four steps").
3. `{% include lens-tabs.html lenses="biology,physics,math,cs" %}` followed by one panel per lens:
   `{% include lens-start.html lens="physics" %}` · `## Physics lens: …` · content ·
   `{% include lens-end.html %}` – the panels must match `lenses:` exactly and in order.
4. An outlook section: bionics, technology, medicine, open questions.
5. FAQ, sources and graph tags are rendered by the layout from front matter – do not repeat them.

**Citations:** `[1](#ref-1){:.cite}` – numbers follow the order of `sources`. Every source must be
cited at least once and every citation must have a source.
**Formulas:** HTML inside `<div class="formula" role="math" aria-label="…">` with `<var>`,
`.frac`, `.sqrt` (see existing examples); give every formula a spoken `aria-label`.
**Figures:** `<figure class="figure">{% include svg/<name>.svg %}<figcaption class="caption">…`
(`figure--dark` for dark figures). Figures follow `wildbionics-figures`.
**Numbers:** a non-breaking space (U+00A0) between number and unit.

## 4. Code examples

Every code example teaches **one idea** and is a program the reader can run unchanged. The gate
`.github/scripts/code_examples.py` runs every example at every build; readers learn how to run
them on `/run-code/` (`run-code/index.md`, DE `de/code-ausfuehren/index.md`).

**Markup** – the include directly after the block marks it as an example:

````markdown
```python
…complete program…
```
{% include code-result.html file="rayleigh_plesset.py" label="Fig. 4" caption="…" alt="…" %}
````

Include parameters are plain Liquid strings without escapes: never write `\"` inside `caption="…"` or `alt="…"` – use typographic quotes “…” (the gate fails otherwise, because the value would be cut off on the page and in the JSON-LD). The include renders the action bar (Open in Colab, Download .py, How to run), the tested
**Output** box and – if the program draws one – the chart with caption. Output, chart and
downloads come from `_data/code_examples.yml` and `examples/<ref>/<name>.<lang>.{py,ipynb,svg}`,
which the script writes; never edit them by hand. Code inside an include (home page) passes
`ref="home"`, `lang="en"`/`lang="de"` and `variant="card"` – one block per language inside
`{% if lang == "de" %}…{% else %}…{% endif %}`, so every language shows its own comments and output. `assets/js/code.js` adds the copy button.

**Rules for the program** (the gate enforces: runs without error or warning in ≤ 60 s, prints something, at most one chart, output and generated files up to date – the rest is on you and the review):
- Complete and self-contained: imports, constants with units in comments, no files, no network,
  no user input. Only `numpy`, `scipy`, `matplotlib` (versions pinned in `examples/requirements.txt`).
- Runs in under 60 s, prints no warnings, prints its result; random numbers use a fixed seed
  (`np.random.default_rng(1)`) and the result must not hinge on the seed – check a few hundred
  seeds before you publish.
- At most **one** chart (one figure, subplots allowed), ended with `plt.show()`. It must stay
  readable on a 390 px phone, where it is scaled to about 330 px: stack panels vertically
  (`plt.subplots(2, 1, figsize=(6.4, 8.4))`, not side by side) and set `plt.rcParams["font.size"] = 13`. Log axes get plain tick labels
  (`ax.yaxis.set_major_formatter("{x:g}")`): the default 10ⁿ labels go through matplotlib's
  mathtext, which prints pyparsing deprecation warnings in CI and fails the gate. Axis labels with
  units, a title that states the takeaway, a legend; German labels in the DE version, short enough
  not to be clipped. Look at the rendered SVG before you commit. Mark where the model stops being
  valid (e.g. dotted lines where an assumption breaks) instead of plotting unphysical results as if
  they were real; distinguish curves by more than colour (direct labels or line styles). Every chart needs `alt` (what the
  chart shows, with the key numbers) and a numbered `label`/`caption` like any figure – all three
  also become the chart's `ImageObject` in the JSON-LD (search engines index it as an image).
- Print only as many digits as are **stable across platforms** – CI runs Linux, you may run macOS.
  Quantities that depend strongly on solver steps (peaks, minima, anything raised to a high power)
  get 2–3 significant figures, e.g. `{speed / 1e3:.1f}` km/s instead of `{speed:,.0f}` m/s; otherwise
  the gate reports `_data/code_examples.yml` as stale in CI (it prints the diff).
- The printed result is **meaningful**: numbers with units that answer a question, ideally compared
  with a known limit (analytical formula, measurement from a cited source) – "validation".
- Readable over clever: short functions, descriptive names, comments explain *why*.

**Text around the code** (this is what makes the reader learn):
1. Before the code: what question the program answers and what is unknown or assumed.
2. After the code: "What the result teaches" – interpret the printed numbers and the chart in
   2–4 bullets (which result is robust, which is sensitive, where the model breaks down).
3. "Try it yourself": 2–3 one-line changes, each with its outcome. Every change is a **tested
   variant** – after the list, one include per change:
   `{% include code-variant.html file="x.py" id="bigger" replace="R_MAX = 3.0e-3" with="R_MAX = 6.0e-3" expect="551 557" %}`.
   The gate replaces `replace` (must occur exactly once), runs the program and fails unless every
   number in `expect` – list all numbers the text quotes for this change – appears in the output.
   The page shows the variant's output as a collapsible "Tested output with …" (optional
   `label="…"` names the change when `with` alone is unclear).
Numbers quoted in the text must match the Output box; rerun the script after every code change.

**Run the gate** (needs Python ≥ 3.9 with the pinned libraries):
```bash
python3 -m venv .venv && source .venv/bin/activate && python3 -m pip install -r examples/requirements.txt
python3 .github/scripts/code_examples.py          # run all examples, write generated files – commit them
python3 .github/scripts/code_examples.py --check  # what CI runs: fails on errors or stale files (also rewrites them – check git status)
```

## 5. Writing style

Answer-first, concrete, friendly, precise. Short paragraphs, active voice, one idea per
paragraph. Explain every technical term at first use. Put the most important number in bold.
No marketing language, no unverifiable superlatives ("loudest animal" needs a source or goes).

## 6. SEO, AEO, GEO

- `description` is the search snippet; `key_facts` and FAQ make the article answer-ready for
  answer engines; JSON-LD (Article, FAQPage, BreadcrumbList named by `short_title`, citations
  with DOI, Wikidata `about`, licensed preview `ImageObject` with `image_alt` as caption) is
  generated by `_includes/jsonld.html` from front matter – rules in `wildbionics-design`.
- Create the OG images (1200×630, EN and DE) with `_includes/og-card.html` – recipe in
  `wildbionics-figures`, step 6.
- `llms.txt`, `sitemap.xml`, `graph.json` and `graph.jsonld` update automatically on build; the article's
  JSON-LD lists its ontology terms as DefinedTerms with the graph's stable IRIs.

## 7. Finish

Add new ontology terms/organisms via `wildbionics-graph`, translate via `wildbionics-translate`,
then run all gates (see `wildbionics-contribute`) and review with `wildbionics-review`.
