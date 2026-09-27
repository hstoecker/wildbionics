---
name: wildbionics-figures
description: "Create, redesign or review conceptual figures for WildBionics – SVG illustrations and diagrams in _includes/svg/ (organisms, mechanisms, physics plots, lens figures), hero figures of articles and OG preview images. Use whenever a figure is added or changed, or the user criticises how a figure looks. Enforces the quality bar (recognisable, conceptually clear, scientifically correct, attractive) and an iterate-until-it-passes review loop with rendered screenshots."
---

# WildBionics figures – quality bar and review loop

A WildBionics figure must let a reader **recognise what they see at a glance, understand what
happens conceptually, and find it attractive** – before reading a single label. A figure that
merely "works" is not done. Keep iterating until every item of the acceptance checklist passes.

**Reference standard:** `_includes/svg/claw.svg` (Fig. 1 of the pistol shrimp article). It was
accepted only after the first version – an abstract claw fragment – failed: readers could not
tell it was a shrimp. The accepted version shows the whole animal with its diagnostic features
*and* the mechanism in context. Match that level for every new figure.
Other good examples: `hero-echolocation.svg` (scene + measured quantities + inset),
`bernoulli.svg` (plot computed from the formula), `lens-biology.svg` (interaction of two organisms).

## Quality criteria

1. **Recognisable subject.** Show the organism, object or setting as a whole, in a typical pose,
   with its *diagnostic features* – the traits a biologist or engineer would use to identify it
   (pistol shrimp: oversized snapping claw, small pincer claw, carapace with eye hood, segmented
   abdomen with pleura, tail fan, antennae). Never show only an isolated fragment; zoom-ins go
   into an inset or a second figure, next to the whole.
2. **The concept is readable.** One main idea per figure. Make the causal chain visible:
   sequence left → right (or top → bottom), cause → effect, with direction cues (arrows, jets,
   wave fronts, speed lines). The key element of the concept gets the strongest visual weight.
3. **Scientifically correct.** Anatomy and technical terms right; quantities consistent with the
   article text and its sources; plots are *computed* (generate the path from the formula in a
   script), not drawn by eye; mark schematic figures "Schematic · not to scale"; never invent data.
4. **Attractive and on-brand.** Use the design tokens (`--signal`, `--accent`, `--ink`, dimension
   colours, fonts: Fraunces for titles, JetBrains Mono for labels), subtle gradients and
   highlights for volume, a faded grid for the "lab journal" feel, calm composition with air
   around the subject. No clip-art look, no clutter.
5. **Labels that help.** Short, from `_data/i18n.yml` (EN + DE, German terms per the glossary),
   callouts with a leader line and a dot that sits *on* the element meant. No overlaps with
   each other, with shapes or with other leader lines; nothing clipped at the edge; readable on
   a phone (roughly ≥ 9 px effective size – enlarge labels in the ≤ 600 px media query).
6. **Accessible.** `role="img"` with bilingual `<title>` and `<desc>` that describe the concept,
   not just the objects; enough contrast on dark and light surfaces; never encode meaning by
   colour alone (add shape, dash pattern or label).

### Pitfalls seen before – check for them explicitly
- Dots or dark shapes that read as eyes or faces (a hinge dot made the claw look like a head).
- Abstract fragments without context (the first claw figure).
- Proportions that hide the story (the snapping claw was too small to be the obvious "weapon").
- Hard, angular artefacts on organic shapes (a step in the claw outline).
- Labels colliding (jet vs. shock wave), labels on top of curves, callout dots floating in space.
- Two nodes/labels saying the same thing (duplicate "Biology" in the graph).
- Grids or panels with hard edges – fade them with a radial mask.

## Workflow – iterate until it passes

1. **Brief (before drawing).** Write down in 3 lines: what must the reader understand? Which
   diagnostic features make the subject recognisable? What is the sequence of the concept?
   Check facts and numbers against the article's sources.
2. **Build** the SVG in `_includes/svg/<name>.svg`: start with `{%- include i18n.html -%}`,
   labels from `t.figures.<name>.*`, styles in `assets/css/main.css` (scoped by the figure's
   class). Compose from anatomical/technical parts, back to front.
3. **Render** – always all of these views:
   ```bash
   plugins/wildbionics/skills/wildbionics-figures/scripts/shots.sh figure <article-url> <out.png>        # large
   plugins/wildbionics/skills/wildbionics-figures/scripts/shots.sh page <url> <out.png> 1440 <y> <h>    # in context
   plugins/wildbionics/skills/wildbionics-figures/scripts/shots.sh page <url> <out.png> 390 <y> <h>     # phone
   ```
   Render EN **and** DE (labels differ in length). On macOS `SHOT_JS="…"` can click tabs or focus
   nodes first; on Linux (cloud sessions) the script uses headless Chrome (on `PATH` or the
   preinstalled Playwright Chromium) and captures the top of the page. Headless Chrome has a minimum
   window width of about 500 px, so its 390 px renders look cut off on the right – for true phone
   views use Playwright (preinstalled in cloud sessions) with a 390 px viewport, or the CI screenshots. Without any renderer, open the PR and review the CI screenshots (`preview-pr-<n>`). Alternative: the Browser pane (`preview_start` + screenshot). Local server:
   `bundle exec jekyll serve --livereload` → http://localhost:4000.
4. **Critique** each render against the checklist below and write the findings down as a list
   (what is wrong, why, the fix). Look at the large render for detail and the phone render for
   legibility. Ask: *Would someone who has never heard of this animal/mechanism recognise it
   and understand what happens?*
5. **Fix and repeat** steps 3–4 until the checklist passes completely. Several rounds are normal
   (the pistol shrimp needed four).
6. **Finish:** regenerate OG images that contain the figure (`_includes/og-card.html`, see
   CLAUDE.md), update captions and alt texts in both languages, run the gates:
   ```bash
   ruby .github/scripts/check_terms.rb && bundle exec jekyll build && python3 .github/scripts/check_site.py _site
   ```
   Then **show the user the final render** (send the large PNG) before committing, and say
   honestly if something is still schematic or simplified.

## Acceptance checklist (all must be ✔)

- [ ] Subject recognisable without labels; diagnostic features present; shown as a whole.
- [ ] The concept (cause → effect, sequence) is visible at a glance; the key element dominates.
- [ ] Facts, numbers, anatomy and terms correct and consistent with the article and sources.
- [ ] Attractive: on-brand colours and fonts, volume/highlights, balanced composition, no clutter.
- [ ] No unintended readings (faces, eyes, odd symbols); organic shapes without angular artefacts.
- [ ] Labels: EN + DE from i18n, glossary terms, no overlaps, nothing clipped, dots on target.
- [ ] Legible and uncluttered at phone width (390 px) and in the article layout (desktop).
- [ ] `<title>`/`<desc>` describe the concept in both languages; contrast OK; not colour-only.
- [ ] OG images regenerated if they contain the figure; captions and `image_alt` (describes the
      OG image; also its JSON-LD caption) updated; gates pass.
- [ ] Final large render shown to the user.
