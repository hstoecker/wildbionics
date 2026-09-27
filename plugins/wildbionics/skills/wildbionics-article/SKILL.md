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
5. Code in an article must be **run**; its printed output is pasted from the actual run.
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
beings: [<slug>]               # from _data/beings.yml
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

## 4. Writing style

Answer-first, concrete, friendly, precise. Short paragraphs, active voice, one idea per
paragraph. Explain every technical term at first use. Put the most important number in bold.
No marketing language, no unverifiable superlatives ("loudest animal" needs a source or goes).

## 5. SEO, AEO, GEO

- `description` is the search snippet; `key_facts` and FAQ make the article answer-ready for
  answer engines; JSON-LD (Article, FAQPage, BreadcrumbList named by `short_title`, citations
  with DOI, Wikidata `about`, licensed preview `ImageObject` with `image_alt` as caption) is
  generated by `_includes/jsonld.html` from front matter – rules in `wildbionics-design`.
- Create the OG image (1200×630) with `_includes/og-card.html` (see `wildbionics-figures`).
- `llms.txt`, `sitemap.xml` and `graph.json` update automatically on build.

## 6. Finish

Add new ontology terms/organisms via `wildbionics-graph`, translate via `wildbionics-translate`,
then run all gates (see `wildbionics-contribute`) and review with `wildbionics-review`.
