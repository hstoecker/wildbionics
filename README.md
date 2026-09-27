# WildBionics

**Nature's physics, explained.** – [wildbionics.com](https://wildbionics.com) · [Deutsch](https://wildbionics.com/de/)

WildBionics is a bilingual (English/German) open compendium that connects **biology** with
**physics, mathematics, chemistry, computer science and Physical AI** – through animals, plants,
geology, bionics and robots. Every article looks at one phenomenon through several *lenses*,
cites peer-reviewed sources and becomes a node in an open [knowledge graph](https://wildbionics.com/graph/).

## Contribute – with or without Claude

Everyone can contribute: articles, corrections, translations, figures, code. The full guide is on
the website: **[wildbionics.com/contribute](https://wildbionics.com/contribute/)** (German:
[wildbionics.com/de/mitmachen](https://wildbionics.com/de/mitmachen/)), details in
[CONTRIBUTING.md](CONTRIBUTING.md).

Step-by-step guides for the three ways to work:
[1 · Ask Claude on GitHub](https://wildbionics.com/contribute/#way-1) ·
[2 · Work with Claude Code](https://wildbionics.com/contribute/#way-2) ·
[3 · Work by hand](https://wildbionics.com/contribute/#way-3)

**With Claude Code**, the project's rules come as skills. Open this repository in Claude Code and
they load automatically – or install them anywhere from this repository's plugin marketplace:

```text
/plugin marketplace add hstoecker/wildbionics
/plugin install wildbionics@wildbionics
```

| Skill | For |
|---|---|
| `wildbionics-contribute` | orientation, workflow, setup – start here |
| `wildbionics-article` | research, sources, structure, lenses, SEO/AEO/GEO |
| `wildbionics-translate` | EN⇄DE with the project glossary |
| `wildbionics-figures` | conceptual figures that pass the quality bar |
| `wildbionics-graph` | ontology and knowledge graph |
| `wildbionics-design` | UI/UX, accessibility, front-end rules |
| `wildbionics-review` | reviewing pull requests (+ agent `wildbionics-fact-checker`) |

## How a change goes live

1. Branch → work with the skills → local gates → pull request
2. CI: terminology, content, plugin and site gates · preview with screenshots · Claude review
3. The maintainer reviews and merges → GitHub Pages deploy → search engines notified (IndexNow)

## Tech

Static [Jekyll](https://jekyllrb.com) site on GitHub Pages, no dependencies beyond the
`github-pages` gem, self-hosted fonts, vanilla JS. Local preview:

```bash
bundle install && bundle exec jekyll serve --livereload
```

## Licences

Code: [MIT](LICENSE) · Content (texts, figures, data): [CC BY-SA 4.0](LICENSE-CONTENT.txt) ·
Fonts: SIL OFL 1.1 (`assets/fonts/`).
