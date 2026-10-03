---
name: wildbionics-translate
description: "Translate or review WildBionics content between English and German (articles in _articles/, UI strings in _data/i18n.yml, SVG labels, taxonomy). Use whenever a German (or other) translation is written, updated or reviewed, or when the user asks to check terminology (Fachbegriffe). Enforces the project glossary and runs the terminology gate."
---

# WildBionics translation (EN ⇄ DE)

English is the source language; German lives under `/de/`. Every translation must use the
correct technical terms of the target discipline (zoology, physics, mathematics, chemistry,
computer science, Physical AI/robotics, medicine) – not literal translations.

## Workflow

1. **Load the glossary first:** read `_data/glossary.yml`. For every term in it, use the
   `de` form (or a `de_alt`) and never an `avoid` variant.
2. **Translate** (see rules below). For a new article, copy the EN file to
   `_articles/<slug>.de.md`, keep `id`, `ref`, `dimensions`, `lenses`, `sources` identical,
   set `lang: de` and a German `permalink` under `/de/artikel/`.
3. **New technical terms:** when a term is not in the glossary, look up the established
   German term in the discipline's literature (e.g. Duden, Wikipedia DE of the field,
   German textbooks) – then add it to `_data/glossary.yml` with `why` if a tempting wrong
   variant exists.
4. **Run the gate** and fix everything it reports:
   ```bash
   ruby .github/scripts/check_terms.rb
   bundle exec jekyll build && python3 .github/scripts/figures.py _site && python3 .github/scripts/check_site.py _site
   ```
   Both also run in CI (`.github/workflows/deploy.yml`); errors block the deploy.
5. **Review pass** – read the German text once as a subject expert would:
   are terms, units and statements exactly as precise as in English? Formulas unchanged?

## Rules for German

- **Fachsprache vor Alltagssprache:** Stoßwelle (nicht Schockwelle), Schere (nicht Klaue),
  Häutung (nicht Mauser), Dactylus/Zapfen/Grube, Adiabatenexponent, Optimalfilter,
  interauraler Laufzeitunterschied … – see the glossary. Introduce an English term in
  parentheses only where it is common in German research, e.g. „Optimalfilter (Matched Filter)“.
- **False friends:** *flagship article* = Schwerpunktartikel (nicht Leitartikel = Meinungsbeitrag),
  *eventually* = schließlich, *sensible* = vernünftig, *billion* = Milliarde.
- **AI terms:** *Physical AI* stays English in German (established term); explain it on first
  use as „verkörperte künstliche Intelligenz“ – never „physikalische KI“ (physikalisch =
  die Physik betreffend). *Superintelligenz* is hypothetical: keep modal wording
  („könnte“, „Szenario“) exactly as hedged as the English source.
- **Numbers:** decimal comma (0,915), thousands point (5.000), a *non-breaking* space
  (U+00A0) between number and unit (25 m/s, 20 °C), ranges with en dash (3–5 cm),
  `≈` and `≥` unchanged.
- **Scientific names** of species and genera always in italics (*Alpheus*, *Synalpheus
  parneomeris*), also in UI strings (`<em>Bertholdia trigona</em>`); German common name first,
  scientific name on first mention.
- **Quotation marks:** „…“ (inner: ‚…‘). Dash with spaces: „ – “.
- **Address:** informal *du* (as on the rest of the site), consistent within a text. Exception: a
  text that speaks to a group (teachers, parents, a class) uses plural *ihr/euch*, e.g. the audience
  cards on `/de/mitmachen/` – singular groups (pupils, the curious) keep *du*.
- **Gender-fair German without special characters:** no gender star, colon or Binnen-I
  (*Forschende\*r*, *Schüler:in*). Use neutral forms (*Lehrkräfte*, *Forschende*, *Studierende*)
  or pair forms (*Schülerinnen und Schüler*) – the same wording on the site, in forms and templates.
- **Keep unchanged:** DOIs, English titles of cited papers, author names, formulas and
  variable names, Liquid tags (`{% include … %}`), HTML/ids/anchors (`#ref-3`, `#lens-math`),
  code identifiers. In code examples, translate comments, docstrings, printed strings and chart
  labels (keep chart titles short enough not to be clipped); keep identifiers, numbers and the
  `file=` name identical. The DE program must compute exactly what the EN one does; avoid Python's
  English thousands separator in DE output (`{x:.0f}` instead of `{x:,.0f}`). Then run
  `.github/scripts/code_examples.py` – output, chart and notebook of the DE version are generated,
  and numbers quoted in the DE text must match its Output box (with decimal comma in the text).
- **Same structure:** identical number of key facts, FAQ entries, sources and citations
  `[n](#ref-n)` in both languages – the gate checks this.
- **SVG labels** come from `_data/i18n.yml` (`figures.*`, `hero.svg_*`, `lens.*.svg_*`);
  translate them there, keeping them short enough for the figure. German labels are often
  longer – re-render the figure in DE and check it with the `wildbionics-figures` skill.

## Adding a language

Copy the `en:` block in `_data/i18n.yml`, add the code to `languages` in `_config.yml`, add a
column to `_data/taxonomy.yml` and a name to every entry of `_data/beings.yml` and `_data/thought_experiments.yml` (the terminology
gate requires both), translate the pages under `/<lang>/` (home, article index, graph, contribute, about,
run-code – copy the `de/` folder as a template and give each page the same `ref`), and extend this
skill and the glossary with the new language.
