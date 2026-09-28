---
name: wildbionics-graph
description: "Extend or change the WildBionics knowledge graph and ontology – the four dimensions (time, space, rules of physics, adjacent sciences), taxonomy terms with dim/order, organisms (beings), lens-to-discipline mapping, graph.json generation and the interactive graph page. Use when an article needs a new term, organism or lens, when the ontology or time axis changes, or when graph.json / the graph view is touched."
---

# WildBionics knowledge graph

The graph is **derived at build time from article front matter** – there is no database.
Every published article becomes a node linked to the terms of its four dimensions, to its
organisms (beings) and, through its lenses, to disciplines.

## Data files

| File | Content | Rules |
|---|---|---|
| `_data/taxonomy.yml` | ontology terms: `slug: { dim, order?, en, de }` | `dim` ∈ `time`, `space`, `physics` (= "Rules"), `adjacent_sciences`; time terms need an integer `order` on the axis Big Bang → … → future; names in every language; optional `wikidata: Q…` only when a Wikidata item is *exactly* this concept – verify label and description via the Wikidata API (becomes `sameAs`) |
| `_data/beings.yml` | organisms (later also machines): `slug: { en, de, taxon, wikidata }` | verify the Wikidata ID; `taxon` is the scientific name (rendered in italics) |
| `_data/lenses.yml` | lens key → graph node (`term:<slug>` or `dim:<dimension>`) | every lens in `_data/i18n.yml` `lens.*` needs an entry |
| article front matter | `dimensions`, `beings`, `lenses` | slugs must exist and sit under the matching dimension |

## Ontology rules

- **Time** runs from the Big Bang through evolution and geology into technology: … → `modern-era`
  → `age-of-ai` → `future-scenarios`. Superintelligence and future humanoid robots belong to
  `future-scenarios` and are always framed as hypotheses/scenarios with sources.
- **Space**: habitats and scales (microcosm, deep sea, coral reef, desert, stratosphere, lab, urban).
- **Rules**: fields of physics (mechanics, fluid dynamics, thermodynamics, optics, acoustics,
  electromagnetism, quantum, relativity).
- **Adjacent sciences**: biology, chemistry, mathematics, computer science, artificial
  intelligence, Physical AI, robotics, medical technology, materials science, bionics.
- Prefer existing terms; add a new term only if an article needs it and no existing term fits.
  Slugs are English, lowercase, hyphenated; display names follow the glossary (`wildbionics-translate`).

## Generated output

- `graph.jsonld` (Liquid, same sources) → the graph as schema.org linked data with **stable IRIs**:
  `<site>/graph/#dim-<dimension>` (DefinedTermSet), `#term-<slug>` (DefinedTerm, `sameAs` Wikidata),
  `#being-<slug>` (Taxon), articles as `<url>#article` (the same `@id` as on the article page) with
  `keywords` → terms, `about` → organisms, `educationalAlignment` → lens disciplines. Article pages
  repeat their terms as DefinedTerms with these IRIs. Never rename a slug that is live – the IRI
  would break; add a new term instead.
- `graph.json` (Liquid) → nodes `dimension`, `term` (with `used`), `article`, `being`;
  edges `contains`, `<dimension>`, `about`, `lens`. Labels and URLs per language, CC BY-SA.
- `_includes/graph-page.html` → pages `/graph/` and `/de/wissensgraph/`, including a complete
  no-JS list of all connections and a reader explainer (`graph.explain` in `_data/i18n.yml`: what a
  knowledge graph is, nodes and edges, dimensions, lenses, why links matter, what readers can do –
  its example quotes the gecko article's real edges, so keep it true when that article changes); `assets/js/graph.js` draws the interactive view (own force
  layout with fixed dimension anchors and a label-collision pass – no dependencies).
- `check_terms.rb` validates taxonomy/beings/lenses and article references;
  `check_site.py` validates graph.json (unique ids, no dangling edges, labels, links) and
  graph.jsonld (references resolve, every term in a DefinedTermSet, `sameAs` = Wikidata item URL,
  every graph.json node present, article keywords/about identical to graph.json's edges).

## Checklist for graph changes

- [ ] New slugs added to the right file with names in all languages (and `order` for time).
- [ ] Article front matter uses the slugs under the correct dimension.
- [ ] `ruby .github/scripts/check_terms.rb` and the site gate pass; `graph.json` and `graph.jsonld` rebuilt.
- [ ] New terms: Wikidata ID checked (exact match only) or deliberately left out.
- [ ] Graph page rendered on desktop and phone (see `wildbionics-figures` for the renderer):
      no overlapping labels, new nodes placed near their dimension.
- [ ] If the ontology itself changes (new dimension, new node type): update `CLAUDE.md`, this
      skill, `graph.json`, `graph.jsonld`, `graph.js`, the checks, the i18n legend and the explainer (`graph.explain`) in the same pull request.
