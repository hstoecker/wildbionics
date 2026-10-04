#!/usr/bin/env python3
"""Verify DOIs and draft the sources of an article (rules: wildbionics-article, research protocol).

    python3 plugins/wildbionics/skills/wildbionics-article/scripts/sources.py <slug> 10.1126/science.1195421 10.1038/...

For every DOI: resolve it at Crossref (title, authors, journal, volume, pages, year), fetch the
abstract and open-access status from OpenAlex (PubMed as fallback) and write

    drafts/<slug>.sources.yml   the sources: block with a key per source, ready for the draft
    drafts/<slug>.reading.md    title + abstract of each source – read it, then note in
                                _data/source_notes/<slug>.yml which claim comes from where

A DOI that does not resolve is reported and left out: a DOI you have not resolved is not a
source. Metadata is checked, the content is not – reading stays your job. Standard library only.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
UA = {"User-Agent": "WildBionics/1.0 (https://wildbionics.com; contribute (at) wildbionics.com)"}


def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
            return r.read().decode("utf-8")
    except Exception as e:                       # network errors are reported per DOI
        return f"ERROR {e}"


def initials(given):
    return " ".join(p[0] + "." for p in re.split(r"[\s-]+", given or "") if p)


def abstract(doi):
    raw = get(f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi)}?mailto=contribute@wildbionics.com")
    oa, text = False, ""
    if not raw.startswith("ERROR"):
        w = json.loads(raw)
        oa = bool((w.get("open_access") or {}).get("is_oa"))
        inv = w.get("abstract_inverted_index") or {}
        pos = {i: word for word, idx in inv.items() for i in idx}
        text = " ".join(pos[i] for i in sorted(pos))
    if not text:                                 # PubMed fallback
        ids = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&term="
                  + urllib.parse.quote(f"{doi}[doi]"))
        idlist = [] if ids.startswith("ERROR") else json.loads(ids)["esearchresult"]["idlist"]
        if idlist:
            time.sleep(0.4)
            text = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&rettype=abstract"
                       f"&retmode=text&id={idlist[0]}")
    return oa, text.strip() or "(no abstract found – read the paper itself or do not cite it)"


def main(slug, dois):
    yml, reading, keys = ["sources:"], [f"# Reading list for {slug}\n"], set()
    for doi in dois:
        raw = get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
        if raw.startswith("ERROR") or raw.startswith("Resource not found"):
            print(f"NOT RESOLVED  {doi}  ({raw[:60]})")
            continue
        m = json.loads(raw)["message"]
        authors = [f"{a.get('family', a.get('name', ''))}, {initials(a.get('given'))}".rstrip(", ")
                   for a in m.get("author", [])]
        year = (m.get("published-print") or m.get("published-online") or m["issued"])["date-parts"][0][0]
        title = re.sub(r"<[^>]+>", "", m["title"][0])
        pages = m.get("page") or m.get("article-number") or ""
        key = re.sub(r"\W", "", (m.get("author") or [{"family": "anon"}])[0].get("family", "anon").lower()) + str(year)
        while key in keys:
            key += "b"
        keys.add(key)
        oa, text = abstract(m["DOI"])
        yml += [f"  - key: {key}",
                f"    authors: {json.dumps(authors, ensure_ascii=False)}",
                f"    year: {year}",
                f"    title: {json.dumps(title, ensure_ascii=False)}",
                f"    journal: {json.dumps((m.get('container-title') or [''])[0], ensure_ascii=False)}"]
        if m.get("volume"):
            yml.append(f"    volume: {m['volume']}")
        if pages:
            yml.append(f"    pages: \"{pages.replace('-', '–')}\"")
        yml.append(f"    doi: \"{m['DOI']}\"")
        if oa:
            yml.append("    open_access: true")
        reading.append(f"## {key} – {title} ({year})\nhttps://doi.org/{m['DOI']}\n\n{text}\n")
        print(f"ok            {doi}  →  {key}{'  (open access)' if oa else ''}")
        time.sleep(0.2)
    out = ROOT / "drafts"
    out.mkdir(exist_ok=True)
    (out / f"{slug}.sources.yml").write_text("\n".join(yml) + "\n", encoding="utf-8")
    (out / f"{slug}.reading.md").write_text("\n".join(reading), encoding="utf-8")
    print(f"\nwrote drafts/{slug}.sources.yml and drafts/{slug}.reading.md")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2:])
