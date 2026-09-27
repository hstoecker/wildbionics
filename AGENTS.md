# AGENTS.md – instructions for AI agents working on WildBionics

You are contributing to **wildbionics.com**, a bilingual (EN first, then DE) Jekyll site that
explains nature through biology, physics, mathematics, chemistry, computer science and Physical AI.

**Read first:** `CLAUDE.md` (architecture and decisions). The complete rulebook is in the skills
under `plugins/wildbionics/skills/` – read `wildbionics-contribute/SKILL.md` and then the skill for
your task (article, translate, figures, graph, design, review). Claude Code loads them
automatically via `.claude/skills/`.

## Non-negotiables

1. Never push to `main`; work on a branch and open a pull request. A human maintainer approves.
2. Every factual claim needs a verified source (resolve DOIs via Crossref/PubMed); recompute
   derived numbers; run code before quoting its output. Hypotheses are framed as scenarios.
3. English is the source; German must use `_data/glossary.yml` terms.
4. UI text lives only in `_data/i18n.yml` (all languages, identical keys).
5. Ontology slugs come from `_data/taxonomy.yml` (with `dim`, and `order` for time terms).
6. Figures follow the figures skill's acceptance checklist; render and check them.
7. No new dependencies; WCAG 2.2 AA; pages work without JavaScript.
8. Run all gates before opening a PR:
   `ruby .github/scripts/check_terms.rb`, `ruby .github/scripts/check_content.rb`,
   `ruby .github/scripts/check_plugin.rb`, `python3 .github/scripts/code_examples.py --check`, `bundle exec jekyll build && python3 .github/scripts/check_site.py _site`.
9. If you change a convention, update the matching skill in the same PR and bump
   `plugins/wildbionics/.claude-plugin/plugin.json` `version`.
10. Never weaken a check to make it pass; never commit secrets.
