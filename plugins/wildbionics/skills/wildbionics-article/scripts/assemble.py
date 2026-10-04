#!/usr/bin/env python3
"""Turn article drafts with citation keys into the published Markdown (rules: wildbionics-article).

Drafts live in drafts/ (git-ignored, kept locally between sessions) and cite by key:

    The claw closes in under a millisecond {{c:versluis}}.          # body, key facts, FAQ
    sources:
      - key: versluis                                               # first line of each source
        authors: ["Versluis, M.", ...]

    python3 plugins/wildbionics/skills/wildbionics-article/scripts/assemble.py drafts/<slug>.en.md drafts/<slug>.de.md

writes _articles/<slug>.en.md and _articles/<slug>.de.md. Sources are numbered in the order of
their first citation in the EN body (the DE file reuses that order, so [3] is the same paper in
both languages); {{c:key}} becomes [n](#ref-n){:.cite}, the key: lines are dropped, and a
non-breaking space is put between numbers and units outside code blocks. Unknown keys and
sources that are never cited are errors. Standard library only.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
CITE = re.compile(r"\{\{c:(\w+)\}\}")
UNITS = (r"(?:µm²/s|µm/s|µm<sup>2</sup>/s|µm|nm|Å|mPa·s|Pa·s|kPa|MPa|kHz|Hz|ms|µs|m/s|km/h|mm|cm|km|"
         r"m|dB|s|°C|°|%|K|kg|g|W|J|N|mN|µN|nN|L)")


def split(text):
    _, fm, body = text.split("---\n", 2)
    head, rest = fm.split("sources:\n", 1)
    srcs, tail = rest.split("status:", 1)
    blocks = [b for b in re.split(r"(?m)^(?=  - key: )", srcs) if b.strip()]
    by_key = {}
    for b in blocks:
        m = re.match(r"  - key: (\w+)\n", b)
        if not m:
            sys.exit(f"every source needs '  - key: <name>' as its first line:\n{b[:200]}")
        by_key[m.group(1)] = b
    return head, by_key, tail, body


def nbsp(text):
    return re.sub(r"(\d) (" + UNITS + r")(?=[\s.,;:)\]*–/-]|$)", "\\1\u00a0\\2", text)


def assemble(path, order=None):
    head, by_key, tail, body = split(path.read_text(encoding="utf-8"))
    cited = list(dict.fromkeys(CITE.findall(body)))
    if order is None:
        order = cited + [k for k in by_key if k not in cited]          # front-matter-only citations last
    unknown = sorted(set(CITE.findall(head + body)) - set(by_key))
    unused = sorted(set(by_key) - set(CITE.findall(head + body)))
    if unknown or unused or set(order) != set(by_key):
        sys.exit(f"{path}: unknown keys {unknown}, never cited {unused}, "
                 f"differs from EN order {sorted(set(order) ^ set(by_key))}")
    num = {k: i + 1 for i, k in enumerate(order)}
    cite = lambda m: f"[{num[m.group(1)]}](#ref-{num[m.group(1)]}){{:.cite}}"
    sources = "".join(re.sub(r"(?m)^  - key: \w+\n    ", "  - ", by_key[k]) for k in order)
    fm = CITE.sub(cite, head) + "sources:\n" + sources + "status:" + tail
    parts = re.split(r"(```python.*?```)", CITE.sub(cite, body), flags=re.S)
    body = "".join(p if p.startswith("```") else nbsp(p) for p in parts)
    out = ROOT / "_articles" / path.name
    out.write_text("---\n" + nbsp(fm) + "---\n" + body, encoding="utf-8")
    print(f"{out.relative_to(ROOT)}: " + ", ".join(f"[{num[k]}] {k}" for k in order))
    return order


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    order = assemble(Path(sys.argv[1]))
    for other in sys.argv[2:]:
        assemble(Path(other), order)
