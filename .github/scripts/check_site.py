#!/usr/bin/env python3
"""Quality gate for the built site (_site): SEO metadata, JSON-LD, links, sitemap.

Runs in CI before every deploy and locally with:  python3 .github/scripts/check_site.py _site
Uses only the Python standard library. Exits non-zero if any error is found.
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

SITE_URL = "https://wildbionics.com"
root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
errors, warnings = [], []


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.title = ""
        self.meta = {}
        self.links = []          # (rel, href, hreflang)
        self.hrefs = []
        self.ids = set()
        self.h1 = 0
        self.imgs_without_alt = 0
        self.jsonld = []
        self._in_title = self._in_jsonld = False
        self._svg = 0           # <title> inside inline SVG is not the page title
        self._buf = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "svg":
            self._svg += 1
        elif tag == "title" and not self._svg and not self.title:
            self._in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key] = a.get("content", "")
        elif tag == "link":
            self.links.append((a.get("rel", ""), a.get("href", ""), a.get("hreflang")))
        elif tag == "a" and "href" in a:
            self.hrefs.append(a["href"])
        elif tag == "h1":
            self.h1 += 1
        elif tag == "img" and "alt" not in a:
            self.imgs_without_alt += 1
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in_jsonld, self._buf = True, ""

    def handle_endtag(self, tag):
        if tag == "svg":
            self._svg -= 1
        elif tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_jsonld:
            self._in_jsonld = False
            self.jsonld.append(self._buf)

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_jsonld:
            self._buf += data


def url_to_file(url):
    """Map an absolute or root-relative site URL to a file in _site (or None if external)."""
    u = urlparse(url)
    if u.scheme and not url.startswith(SITE_URL):
        return None
    path = unquote(u.path) or "/"
    target = root / path.lstrip("/")
    if path.endswith("/"):
        target = target / "index.html"
    elif not target.suffix:
        target = target.with_suffix(".html") if target.with_suffix(".html").exists() else target / "index.html"
    return target


pages = {}
for f in sorted(root.rglob("*.html")):
    if "assets" in f.parts:
        continue
    p = Page()
    p.feed(f.read_text(encoding="utf-8"))
    pages[f] = p

for f, p in pages.items():
    rel = f.relative_to(root)
    where = f"/{rel}"
    noindex = "noindex" in p.meta.get("robots", "")
    if not p.lang:
        errors.append(f"{where}: <html> has no lang attribute")
    if not p.title.strip():
        errors.append(f"{where}: missing <title>")
    elif len(p.title) > 70:
        warnings.append(f"{where}: title is {len(p.title)} chars (> 70)")
    desc = p.meta.get("description", "")
    if not desc:
        errors.append(f"{where}: missing meta description")
    elif not 50 <= len(desc) <= 180:
        warnings.append(f"{where}: meta description is {len(desc)} chars (aim for 50–180)")
    if p.h1 != 1:
        errors.append(f"{where}: expected exactly one <h1>, found {p.h1}")
    if p.imgs_without_alt:
        errors.append(f"{where}: {p.imgs_without_alt} <img> without alt")
    canon = [h for r, h, _ in p.links if r == "canonical"]
    if not noindex and (len(canon) != 1 or not canon[0].startswith(SITE_URL)):
        errors.append(f"{where}: needs exactly one absolute canonical URL")
    for key in ("og:title", "og:description", "og:image", "og:url"):
        if key not in p.meta:
            errors.append(f"{where}: missing {key}")
    img = p.meta.get("og:image")
    if img and (url_to_file(img) is None or not url_to_file(img).exists()):
        errors.append(f"{where}: og:image not found in build: {img}")
    for block in p.jsonld:
        try:
            data = json.loads(block)
        except json.JSONDecodeError as e:
            errors.append(f"{where}: invalid JSON-LD ({e})")
            continue
        types = {t for node in data.get("@graph", [data]) for t in ([node.get("@type")] if isinstance(node.get("@type"), str) else node.get("@type", []))}
        if "Article" in types:
            art = next(n for n in data["@graph"] if "Article" in (n["@type"] if isinstance(n["@type"], list) else [n["@type"]]))
            for k in ("headline", "datePublished", "author", "image", "inLanguage"):
                if not art.get(k):
                    errors.append(f"{where}: Article JSON-LD lacks {k}")
    # hreflang: every alternate must exist and point back
    for r, href, hl in p.links:
        if r == "alternate" and hl and hl != "x-default":
            target = url_to_file(href)
            if not target or not target.exists():
                errors.append(f"{where}: hreflang {hl} target missing: {href}")
            elif target in pages:
                back = [h for rr, h, l in pages[target].links if rr == "alternate" and l]
                if canon and canon[0] not in back:
                    errors.append(f"{where}: hreflang {hl} page {href} does not link back")
    # internal links and anchors
    for href in p.hrefs:
        if href.startswith(("mailto:", "tel:", "javascript:")):
            continue
        u = urlparse(href)
        if u.scheme and not href.startswith(SITE_URL):
            continue
        if not u.path and u.fragment:            # same-page anchor
            if u.fragment not in p.ids:
                errors.append(f"{where}: broken anchor #{u.fragment}")
            continue
        target = url_to_file(href)
        if target and not target.exists():
            errors.append(f"{where}: broken link {href}")
        elif target and u.fragment and target in pages and u.fragment not in pages[target].ids:
            errors.append(f"{where}: broken anchor {href}")

# sitemap
sitemap = root / "sitemap.xml"
if not sitemap.exists():
    errors.append("sitemap.xml missing")
else:
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [e.text for e in ET.parse(sitemap).getroot().findall("s:url/s:loc", ns)]
    for loc in locs:
        t = url_to_file(loc)
        if not t or not t.exists():
            errors.append(f"sitemap.xml: URL without page: {loc}")
    indexable = {f for f, p in pages.items() if "noindex" not in p.meta.get("robots", "")}
    listed = {url_to_file(l) for l in locs}
    for f in indexable - listed:
        warnings.append(f"sitemap.xml: indexable page not listed: /{f.relative_to(root)}")

# knowledge graph data
graph_file = root / "graph.json"
if not graph_file.exists():
    errors.append("graph.json missing")
else:
    try:
        graph = json.loads(graph_file.read_text(encoding="utf-8"))
        ids = [n["id"] for n in graph["nodes"]]
        if len(ids) != len(set(ids)):
            errors.append("graph.json: duplicate node ids")
        for e in graph["edges"]:
            if e["source"] not in ids or e["target"] not in ids:
                errors.append(f"graph.json: edge points to unknown node {e}")
        for n in graph["nodes"]:
            for lang in graph["languages"]:
                if not (n.get("label") or {}).get(lang):
                    errors.append(f"graph.json: {n['id']} has no {lang} label")
            for lang, url in (n.get("url") or {}).items():
                t = url_to_file(url)
                if not t or not t.exists():
                    errors.append(f"graph.json: {n['id']} links to missing page {url}")
    except (json.JSONDecodeError, KeyError) as e:
        errors.append(f"graph.json invalid: {e}")

# robots.txt, llms.txt, IndexNow key
for name in ("robots.txt", "llms.txt"):
    if not (root / name).exists():
        errors.append(f"{name} missing")
cfg = Path("_config.yml").read_text(encoding="utf-8") if Path("_config.yml").exists() else ""
m = re.search(r'^indexnow_key:\s*"?([0-9a-fA-F-]{8,128})"?', cfg, re.M)
if m:
    keyfile = root / f"{m.group(1)}.txt"
    if not keyfile.exists() or keyfile.read_text().strip() != m.group(1):
        errors.append(f"IndexNow key file /{m.group(1)}.txt missing or wrong content")

for w in warnings:
    print(f"warning: {w}")
for e in errors:
    print(f"ERROR:   {e}")
print(f"\nChecked {len(pages)} pages: {len(errors)} errors, {len(warnings)} warnings.")
sys.exit(1 if errors else 0)
