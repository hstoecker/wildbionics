#!/usr/bin/env python3
"""Quality gate for the built site (_site): SEO metadata, JSON-LD (linked graph, breadcrumbs,
licensed preview image), links, sitemap.

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
        self.imgs = []
        self.jsonld = []
        self.crumbs = []         # visible breadcrumb (nav.breadcrumb li texts)
        self._in_title = self._in_jsonld = False
        self._in_crumbs = False
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
        elif tag == "img":
            self.imgs.append(a.get("src", ""))
            if "alt" not in a:
                self.imgs_without_alt += 1
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in_jsonld, self._buf = True, ""
        elif tag == "nav" and "breadcrumb" in a.get("class", "").split():
            self._in_crumbs = True
        elif tag == "li" and self._in_crumbs:
            self.crumbs.append("")

    def handle_endtag(self, tag):
        if tag == "svg":
            self._svg -= 1
        elif tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_jsonld:
            self._in_jsonld = False
            self.jsonld.append(self._buf)
        elif tag == "nav":
            self._in_crumbs = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_jsonld:
            self._buf += data
        if self._in_crumbs and self.crumbs:
            self.crumbs[-1] += data


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


def types_of(node):
    t = node.get("@type", [])
    return {t} if isinstance(t, str) else set(t)


def id_refs(obj):
    """Yield every {"@id": …} reference inside a JSON-LD value."""
    if isinstance(obj, dict):
        if set(obj) == {"@id"}:
            yield obj["@id"]
        else:
            for v in obj.values():
                yield from id_refs(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from id_refs(v)


MARKDOWN_LEAKS = ("**", "{:", "](#")


def strings_in(obj):
    """Yield every string value inside a JSON-LD value."""
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from strings_in(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings_in(v)


def check_graph(where, nodes, page_url, noindex, crumbs, imgs=()):
    """Linked-graph rules: references resolve, breadcrumbs end at the page, the preview image is licensed,
    collection pages list their articles, no Markdown leaks into the data."""
    ids = {n.get("@id") for n in nodes}
    for text in strings_in(nodes):
        leak = next((m for m in MARKDOWN_LEAKS if m in text), None)
        if leak:
            errors.append(f"{where}: JSON-LD text contains Markdown {leak!r}: {text[:80]!r}")
            break
    local = {SITE_URL + "/", page_url}
    for n in nodes:
        for ref in id_refs({k: v for k, v in n.items() if k != "@id"}):
            if ref.split("#")[0] in local and ref not in ids:
                errors.append(f"{where}: JSON-LD reference {ref} points to no node")
    by_id = {n.get("@id"): n for n in nodes}
    webpage = by_id.get(f"{page_url}#webpage")
    if webpage is None:
        errors.append(f"{where}: JSON-LD has no {page_url}#webpage node")
    else:
        img = webpage.get("primaryImageOfPage") or {}
        img = by_id.get(img.get("@id"), img)          # resolve a reference
        for k in ("contentUrl", "caption", "license", "acquireLicensePage", "creditText", "creator", "copyrightNotice"):
            if not img.get(k):
                errors.append(f"{where}: preview image (primaryImageOfPage) lacks {k}")
    article = by_id.get(f"{page_url}#article")
    media = {m.get("@id") for m in (article or {}).get("associatedMedia", [])}
    for src in imgs:                                  # charts of code examples: licensed ImageObjects
        if not (src.startswith("/examples/") and src.endswith(".svg")):
            continue
        url = SITE_URL + src
        img = next((n for n in nodes if "ImageObject" in types_of(n) and n.get("contentUrl") == url), None)
        if img is None:
            errors.append(f"{where}: chart {src} has no ImageObject in the JSON-LD")
            continue
        for k in ("caption", "description", "license", "acquireLicensePage", "creditText", "creator"):
            if not img.get(k):
                errors.append(f"{where}: chart ImageObject {src} lacks {k}")
        if article is not None and img.get("@id") not in media:
            errors.append(f"{where}: chart {src} is not in the article's associatedMedia")
    if webpage is not None and "CollectionPage" in types_of(webpage):
        lst = by_id.get((webpage.get("mainEntity") or {}).get("@id"))
        if not lst or "ItemList" not in types_of(lst):
            errors.append(f"{where}: CollectionPage needs mainEntity → ItemList of its articles")
        else:
            items = lst.get("itemListElement", [])
            if lst.get("numberOfItems") != len(items):
                errors.append(f"{where}: ItemList numberOfItems {lst.get('numberOfItems')} ≠ {len(items)} items")
            for it in items:
                target = url_to_file(it.get("url", ""))
                if not target or not target.exists():
                    errors.append(f"{where}: ItemList links to a missing page {it.get('url')}")
    for bc in (n for n in nodes if "BreadcrumbList" in types_of(n)):
        items = bc.get("itemListElement", [])
        if noindex:
            errors.append(f"{where}: noindex page must not have a BreadcrumbList")
        if [i.get("position") for i in items] != list(range(1, len(items) + 1)):
            errors.append(f"{where}: breadcrumb positions must run 1, 2, 3 …")
        if items and items[-1].get("item") != page_url:
            errors.append(f"{where}: last breadcrumb must be the page itself ({page_url}), not {items[-1].get('item')}")
        names = [i.get("name") for i in items]
        visible = [" ".join(c.split()) for c in crumbs]
        if visible and names != visible:
            errors.append(f"{where}: JSON-LD breadcrumb {names} differs from the visible one {visible}")


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
    if p.title.count("WildBionics") > 1:
        warnings.append(f"{where}: brand name twice in <title>: {p.title!r}")
    desc = p.meta.get("description", "")
    if not desc:
        errors.append(f"{where}: missing meta description")
    elif not 50 <= len(desc) <= 160:
        warnings.append(f"{where}: meta description is {len(desc)} chars (aim for 50–160)")
    if p.h1 != 1:
        errors.append(f"{where}: expected exactly one <h1>, found {p.h1}")
    if p.imgs_without_alt:
        errors.append(f"{where}: {p.imgs_without_alt} <img> without alt")
    canon = [h for r, h, _ in p.links if r == "canonical"]
    if noindex and (canon or any(r == "alternate" and hl for r, _, hl in p.links)):
        errors.append(f"{where}: noindex page must not declare canonical or hreflang")
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
        own_url = canon[0] if canon else SITE_URL + "/" + rel.as_posix().removesuffix("index.html")
        check_graph(where, data.get("@graph", [data]), own_url, noindex, p.crumbs, p.imgs)
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

# llms.txt: plain text for language models – no Markdown link or attribute leftovers from key facts
llms = root / "llms.txt"
if not llms.exists():
    errors.append("llms.txt missing")
else:
    for n, line in enumerate(llms.read_text(encoding="utf-8").splitlines(), 1):
        if "](#" in line or "{:" in line:
            errors.append(f"llms.txt:{n}: Markdown leftover: {line.strip()[:80]}")

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

# graph.jsonld: the same graph as linked data – valid, resolving, and in step with graph.json
ld_file = root / "graph.jsonld"
if not ld_file.exists():
    errors.append("graph.jsonld missing")
else:
    try:
        ld = {n["@id"]: n for n in json.loads(ld_file.read_text(encoding="utf-8"))["@graph"]}
        G = SITE_URL + "/graph/#"
        def ref_ids(v):
            return {x["@id"] for x in (v if isinstance(v, list) else [v]) if isinstance(x, dict) and "@id" in x}
        for i, n in ld.items():
            for k, v in n.items():
                for r in ref_ids(v) if k != "@id" else ():
                    if r.startswith(G) and r not in ld:
                        errors.append(f"graph.jsonld: {i} → {r} points to no node")
            if "DefinedTerm" == n.get("@type") and not str(n.get("inDefinedTermSet", {}).get("@id", "")).startswith(G + "dim-"):
                errors.append(f"graph.jsonld: {i} has no inDefinedTermSet")
            same = n.get("sameAs")
            if same and not re.fullmatch(r"https://www\.wikidata\.org/wiki/Q\d+", same):
                errors.append(f"graph.jsonld: {i} sameAs is not a Wikidata item URL: {same}")
        if graph_file.exists():
            graph = json.loads(graph_file.read_text(encoding="utf-8"))
            prefix = {"term": "term-", "being": "being-", "dimension": "dim-"}
            for n in graph["nodes"]:
                kind, slug = n["id"].split(":", 1)
                if kind in prefix and G + prefix[kind] + slug not in ld:
                    errors.append(f"graph.jsonld: {n['id']} from graph.json is missing")
            for n in (x for x in graph["nodes"] if x["type"] == "article"):
                edges = [e for e in graph["edges"] if e["source"] == n["id"]]
                terms = {G + "term-" + e["target"].split(":", 1)[1] for e in edges if e["type"] not in ("about", "lens")}
                beings = {G + "being-" + e["target"].split(":", 1)[1] for e in edges if e["type"] == "about"}
                for url in n["url"].values():
                    art = ld.get(url + "#article")
                    if art is None:
                        errors.append(f"graph.jsonld: no Article {url}#article")
                        continue
                    if ref_ids(art.get("keywords", [])) != terms:
                        errors.append(f"graph.jsonld: {url} keywords differ from graph.json's term edges")
                    if ref_ids(art.get("about", [])) != beings:
                        errors.append(f"graph.jsonld: {url} about differs from graph.json's organism edges")
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        errors.append(f"graph.jsonld invalid: {e}")

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
