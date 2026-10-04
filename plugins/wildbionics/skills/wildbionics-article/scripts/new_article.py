#!/usr/bin/env python3
"""Start a new article: EN and DE drafts with the full front matter and lens skeleton.

    python3 plugins/wildbionics/skills/wildbionics-article/scripts/new_article.py <ref> <german-slug> [lenses]

    e.g.  new_article.py robin-magnetic-compass rotkehlchen-magnetkompass biology,physics,math,cs,physical-ai

writes drafts/<ref>.en.md and drafts/<ref>.de.md (git-ignored) and an empty notes file
_data/source_notes/<ref>.yml. Fill in the drafts – cite with {{c:key}}, paste the sources block
from sources.py – then run assemble.py to publish them to _articles/. Existing files are never
overwritten.
"""
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
TEXT = {
    "en": dict(kicker="Article · ", perma="/articles/{ref}/", fig="Fig.", intro="## TODO: the phenomenon",
               steps="## TODO: the process in steps", lens="## {name} lens: TODO", outlook="## TODO: outlook",
               names={"biology": "Biology", "physics": "Physics", "math": "Mathematics", "cs": "Computer science",
                      "physical-ai": "Physical AI"}),
    "de": dict(kicker="Artikel · ", perma="/de/artikel/{slug}/", fig="Abb.", intro="## TODO: das Phänomen",
               steps="## TODO: der Ablauf in Schritten", lens="## {name}-Linse: TODO", outlook="## TODO: Ausblick",
               names={"biology": "Biologie", "physics": "Physik", "math": "Mathematik", "cs": "Informatik",
                      "physical-ai": "Physical-AI"}),
}


def draft(ref, slug, lang, lenses):
    t = TEXT[lang]
    panels = "\n".join(f'{{% include lens-start.html lens="{l}" %}}\n\n{t["lens"].format(name=t["names"].get(l, l))}\n\n'
                       f'{{% include lens-end.html %}}\n' for l in lenses)
    return f"""---
id: {ref}
lang: {lang}
ref: {ref}
title: "TODO"
short_title: "TODO"
kicker: "{t['kicker']}TODO"
description: "TODO – 50 to 160 characters, answer-first"
dek: "TODO"
date: {date.today().isoformat()}
permalink: {t['perma'].format(ref=ref, slug=slug)}
image: /assets/og/{ref}-{lang}.jpg
og: {{ eyebrow: "TODO", title: "TODO with <em>one</em> word in italics", sub: "TODO" }}
image_alt: "TODO – what the OG image shows"
hero_figure: svg/{ref}.svg
hero_caption: "<span class=\\"caption__label\\">{t['fig']} 1</span> TODO"
educational_level: "Intermediate"
keywords: ["TODO", "TODO", "TODO"]
about:
  - {{ name: "TODO", wikidata: Q0, wikipedia: "TODO" }}
mentions: []
dimensions:
  time: []
  space: []
  physics: []
  adjacent_sciences: []
beings: []
lenses: {lenses}
key_facts:
  - "TODO {{{{c:key}}}}"
faq:
  - q: "TODO"
    a: "TODO"
sources:
  - key: key
    authors: ["TODO"]
status: draft
---

{t['intro']}

TODO {{{{c:key}}}}

{t['steps']}

{{% include lens-tabs.html lenses="{','.join(lenses)}" %}}

{panels}
{t['outlook']}
"""


def main(ref, slug, lenses):
    (ROOT / "drafts").mkdir(exist_ok=True)
    targets = {ROOT / "drafts" / f"{ref}.{lang}.md": draft(ref, slug, lang, lenses) for lang in ("en", "de")}
    notes = ROOT / "_data" / "source_notes" / f"{ref}.yml"
    targets[notes] = (f"# Research notes for {ref} – one entry per source, keyed by DOI (wildbionics-article).\n"
                      f"# \"10.xxxx/yyyy\":\n#   read: \"Abstract (PubMed)\"\n#   claims:\n#     - \"claim – where in the source\"\n")
    for path, text in targets.items():
        if path.exists():
            print(f"kept  {path.relative_to(ROOT)} (exists)")
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "biology,physics,math,cs").split(","))
