---
name: wildbionics-review
description: "Review a WildBionics pull request or change set (or your own work before submitting) – runs the automated gates, then checks factual correctness against sources (with the wildbionics-fact-checker agent), article structure, translation and terminology, figure quality, knowledge-graph consistency, UI/UX and accessibility, SEO/AEO/GEO and skill upkeep; produces a structured verdict. Use for \"review this PR\", self-review before a PR, and in CI (argument: owner/repo/pull/<n>, optional --comment to post the result)."
---

# Reviewing a WildBionics change

Goal: nothing reaches wildbionics.com that is factually wrong, misleading, badly translated,
hard to understand, inaccessible or against the project's structure. Be strict, specific and
kind; every finding names the file/line, the problem and a concrete fix.

## Inputs

- A pull request (`owner/repo/pull/<n>`): read it with `gh pr view` and `gh pr diff`.
- Or local changes: `git diff main...HEAD`.
- With `--comment`: post the final report as one PR comment (`gh pr comment <n> --body-file …`).

## Step 1 – automated gates

Run (or read the CI results of) all gates; any error is a **must-fix**:
```bash
ruby .github/scripts/check_terms.rb      # terminology, EN/DE consistency, taxonomy
ruby .github/scripts/check_content.rb    # article structure, citations, figures
ruby .github/scripts/check_plugin.rb     # skills/plugin integrity and coverage
python3 .github/scripts/code_examples.py --check   # every code example runs; output/charts up to date
bundle exec jekyll build && python3 .github/scripts/check_site.py _site   # SEO, JSON-LD, links, graph.json
```

## Step 2 – manual review by area

Go through every area the change touches; skip areas it doesn't touch and say so.

1. **Facts** – delegate to the `wildbionics-fact-checker` agent for every changed article or
   factual UI text. Must-fix: unsupported, contradicted or over-precise claims; unresolved or
   mismatching DOIs; calculations that don't reproduce; hypotheses stated as facts.
2. **Structure** (`wildbionics-article`) – front matter complete, lens panels match `lenses`,
   citations ↔ sources, key facts answer-first, FAQ useful, title/description lengths.
2b. **Code examples** (`wildbionics-article`, section 4) – does the program teach one idea? Is the
   printed result meaningful (units, comparison with a known limit)? Does the text interpret the
   output and chart, and do all numbers in the text (incl. "Try it yourself") match the Output box
   or a `code-variant` whose `expect` lists them? Chart readable (labels, units, takeaway title,
   `alt`) and scientifically honest (invalid model regions marked, not colour-only)? Rerun a variant
   yourself if a claim looks off.
3. **Language** (`wildbionics-translate`) – correct technical terms (glossary), same meaning and
   hedging in EN and DE, typography (decimal comma, „…“, non-breaking spaces), consistent *du*.
4. **Figures** (`wildbionics-figures`) – render the changed figures (large, desktop, phone,
   EN/DE) and apply its acceptance checklist: recognisable, conceptually clear, correct,
   attractive, labels without overlaps.
5. **Knowledge graph** (`wildbionics-graph`) – slugs exist under the right dimension, new terms
   justified, graph renders cleanly.
6. **UI/UX & accessibility** (`wildbionics-design`) – components and tokens reused, no hard-coded
   strings, WCAG 2.2 AA, works without JS, no new dependencies, desktop + phone screenshots OK.
7. **SEO/AEO/GEO** – description, OG image with a truthful `image_alt`, JSON-LD validity and
   graph rules (breadcrumb = visible breadcrumb and ends at the page, licensed `#primaryimage`,
   resolving `@id`s – see `wildbionics-design`), hreflang, llms.txt/sitemap entries.
8. **Skill upkeep** (`wildbionics-contribute`) – if conventions changed, the skills were updated
   and the plugin version bumped.
9. **Licence & safety** – content compatible with CC BY-SA 4.0 (images: licence and attribution),
   no secrets, no personal data, no changes that weaken checks.

## Step 3 – report

Use exactly this structure (German if the PR author writes German, otherwise English):

```markdown
## WildBionics review

**Verdict:** ✅ ready to merge | ⚠️ merge after small fixes | ❌ changes required

| Area | Result | Notes |
|---|---|---|
| Gates | ✅/❌ | … |
| Facts | ✅/⚠️/❌ | … |
| Structure | … | … |
| Language | … | … |
| Figures | … | … |
| Knowledge graph | … | … |
| UI/UX & a11y | … | … |
| SEO/AEO/GEO | … | … |
| Skills | … | … |

### Must fix
1. `path:line` – problem → fix

### Suggestions
- …

### Verified facts
- claim → source (DOI) ✔
```

The verdict is a recommendation – **only the maintainer approves and merges**. Never approve or
merge yourself, never push fixes during a review unless asked, and say plainly what you could not
check (e.g. paywalled sources).
