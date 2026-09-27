# Contributing to WildBionics

Thank you for helping to explain nature's physics! This guide is for people; AI agents find the
same rules in [AGENTS.md](AGENTS.md) and in the skills under `plugins/wildbionics/skills/`.
*Deutsch: siehe unten.*

## Ways to contribute

- **Report** a mistake or propose a phenomenon – open an issue (templates provided).
- **Write** an article or a new lens for an existing one.
- **Translate** (German today, more languages welcome).
- **Draw** figures, **improve** the site (accessibility, knowledge graph, code).

## Three ways to work

1. **Just ask Claude on GitHub** (collaborators): write an issue or a comment that contains
   `@claude`, e.g. *"@claude draft an article about how geckos stick to walls"*. Claude works with
   the project skills and opens a pull request for review.
2. **Claude Code** (desktop app, terminal or [claude.ai/code](https://claude.ai/code)): open this
   repository – the WildBionics skills load automatically – and describe your task.
3. **By hand**: fork, branch, edit Markdown/YAML, run the gates, open a pull request.

## Claude Code on the web – one-time setup

1. Accept the collaborator invitation (maintainer adds you) and sign in at [claude.ai/code](https://claude.ai/code) (Claude Pro, Max, Team or Enterprise).
2. Connect GitHub when asked.
3. Create a cloud environment `WildBionics`: network access **Custom**, tick *Also include default list of common package managers*, allow:
   ```text
   api.crossref.org
   doi.org
   eutils.ncbi.nlm.nih.gov
   pubmed.ncbi.nlm.nih.gov
   www.ncbi.nlm.nih.gov
   api.semanticscholar.org
   www.wikidata.org
   *.wikipedia.org
   ```
4. Start a session on `hstoecker/wildbionics` with this environment and describe your task, e.g. *"Write a new article about how geckos stick to walls, following the WildBionics skills."* Review the diff and create the pull request from the session.

## The workflow

1. Issue → branch (`article/<slug>`, `fix/<topic>`)
2. Work with the matching skill (see the table in [README.md](README.md)); English first, then German
3. Run the gates locally:
   ```bash
   ruby .github/scripts/check_terms.rb
   ruby .github/scripts/check_content.rb
   ruby .github/scripts/check_plugin.rb
   bundle exec jekyll build && python3 .github/scripts/check_site.py _site
   ```
4. Pull request (fill in the template)
5. Automatic checks, a downloadable **preview** (built site + screenshots) and – for branches in
   this repository – a **Claude review** comment
6. **The maintainer reviews and merges.** Only merged changes deploy to wildbionics.com.

## Quality rules in short

- Every fact needs a verifiable source (DOI); derived numbers are recomputed; code is run.
- Hypotheses (e.g. superintelligence) are presented as scenarios, never as facts.
- German uses the glossary terms (`_data/glossary.yml`); the CI rejects forbidden variants.
- Figures must be recognisable, conceptually clear, correct and attractive (figures skill).
- WCAG 2.2 AA, works without JavaScript, no new dependencies.
- Changed a convention? Update the skill in the same PR and bump the plugin version.

By contributing you agree that code is licensed MIT and content CC BY-SA 4.0.

---

## Deutsch – Kurzfassung

Fehler melden oder Themen vorschlagen: Issue öffnen. Mit Claude arbeiten: im Issue oder Kommentar
`@claude` erwähnen (für Mitwirkende mit Schreibrechten) oder das Repository in Claude Code bzw. auf
[claude.ai/code](https://claude.ai/code) öffnen – die WildBionics-Skills laden automatisch.
Jede Änderung kommt als Pull Request, durchläuft alle Prüfungen samt Vorschau und Claude-Review und
geht erst nach Freigabe durch den Maintainer live. Ausführlich: [wildbionics.com/de/mitmachen](https://wildbionics.com/de/mitmachen/).
