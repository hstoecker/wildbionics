#!/usr/bin/env python3
"""Publish every WildBionics figure as a standalone SVG file with embedded fonts.

    python3 .github/scripts/figures.py _site      # after `jekyll build`, before check_site.py

The figures are inline SVG on the pages (accessible, styled by assets/css/main.css). For search
engines, answer engines and readers who want to open, zoom or reuse a figure, this script writes
/figures/<name>.<lang>.svg next to the built site – nothing is committed:

1. It reads /figures/manifest.json (built by Jekyll from _data/figures.yml): which figure, which
   page it is cut from, which HTML surrounds it and which background it sits on.
2. It cuts the rendered <svg> (labels already translated) out of the built EN and DE page.
3. It copies the CSS rules of main.css that apply to the figure and its surroundings (design tokens
   from :root, the figure's classes, the context classes) – so main.css stays the only source.
4. It subsets the self-hosted fonts (SIL OFL 1.1) to the characters the figure uses and embeds them
   as WOFF2 data URIs, so the file looks right everywhere – also as an <img> or a search preview.

Needs fontTools with brotli (.github/scripts/requirements.txt). Rules: wildbionics-figures skill.
"""
import base64
import html
import io
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

PAD = 28                        # margin around the figure in the standalone file (SVG units)
SVG_TAGS = {"svg", "g", "path", "circle", "ellipse", "rect", "line", "polyline", "polygon", "text",
            "tspan", "textPath", "use", "defs", "symbol", "marker", "pattern", "clipPath", "mask",
            "linearGradient", "radialGradient", "stop", "filter", "image", "title", "desc", "*"}
DYNAMIC = re.compile(r"::|:(hover|focus|focus-visible|focus-within|active|visited|link|target|has|checked)\b")
XML_ENTITIES = {"amp", "lt", "gt", "quot", "apos"}
FONT_LICENCE = ("Fonts embedded as subsets: Fraunces (The Fraunces Project Authors), Inter (The Inter Project "
                "Authors), JetBrains Mono (The JetBrains Mono Project Authors) – SIL Open Font License 1.1, "
                "https://openfontlicense.org")


def css_blocks(css):
    """Split a stylesheet into top-level (prelude, body) pairs; nested at-rule bodies stay raw."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j < 0:
            break
        prelude, depth, k = css[i:j].strip(), 1, j + 1
        while k < n and depth:
            depth += {"{": 1, "}": -1}.get(css[k], 0)
            k += 1
        out.append((prelude, css[j + 1:k - 1].strip()))
        i = k
    return out


def split_selectors(prelude):
    parts, depth, cur = [], 0, ""
    for ch in prelude:
        depth += {"(": 1, ")": -1}.get(ch, 0)
        if ch == "," and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    return parts + [cur.strip()] if cur.strip() else parts


def applies(selector, classes, attrs, ids):
    """Could this selector match inside the standalone file? Conservative, no cascade engine needed."""
    if selector == ":root":
        return True
    if DYNAMIC.search(selector):
        return False
    for neg in re.findall(r":not\(([^)]*)\)", selector):   # .figure:not(.figure--dark): drop if the
        neg_classes = re.findall(r"\.([\w-]+)", neg)          # negated classes are all present
        if neg_classes and all(c in classes for c in neg_classes):
            return False
    plain = re.sub(r":not\([^)]*\)", "", selector)
    plain = re.sub(r"\[[^\]]*\]", lambda m: " " if m.group(0)[1:].split("=")[0].strip("]") in attrs else " \x00 ", plain)
    if "\x00" in plain:
        return False
    for token in re.split(r"[\s>+~]+", plain.strip()):
        if not token:
            continue
        tag = re.match(r"^[a-zA-Z*][\w-]*", token)
        if tag and tag.group(0) not in SVG_TAGS:
            return False
        if any(c not in classes for c in re.findall(r"\.([\w-]+)", token)):
            return False
        if any(i not in ids for i in re.findall(r"#([\w-]+)", token)):
            return False
        if re.search(r":(?!not)[\w-]+", token):              # other pseudo-classes (:first-child …)
            return False
    return True


def fonts_of(css, site):
    """@font-face rules of main.css → {(family, style): woff2 path}."""
    faces = {}
    for prelude, body in css_blocks(css):
        if prelude == "@font-face":
            family = re.search(r'font-family:\s*"([^"]+)"', body).group(1)
            style = (re.search(r"font-style:\s*(\w+)", body) or [None, "normal"])[1]
            src = re.search(r'url\("\.\./fonts/([^"]+)"\)', body).group(1)
            faces[(family, style)] = (site / "assets" / "fonts" / src, body)
    return faces


def subset_font(path, text):
    font = TTFont(path)
    opts = subset.Options()
    opts.flavor, opts.layout_features, opts.name_IDs, opts.notdef_outline = "woff2", ["*"], ["*"], True
    sub = subset.Subsetter(opts)
    sub.populate(text=text + " ")
    sub.subset(font)
    buf = io.BytesIO()
    font.flavor = "woff2"
    font.save(buf)
    return base64.b64encode(buf.getvalue()).decode()


def cut_svg(page_html, fig_id):
    m = re.search(rf'<svg\b[^>]*aria-labelledby="{re.escape(fig_id)}-title"[^>]*>', page_html)
    if not m:
        return None
    depth, pos = 1, m.end()
    for t in re.finditer(r"<(/?)svg\b[^>]*>", page_html[pos:]):
        depth += -1 if t.group(1) else 1
        if depth == 0:
            return page_html[m.start():pos + t.end()]
    return None


def xml_safe(markup):
    """HTML → XML: named entities other than the five XML ones become characters."""
    markup = re.sub(r"&([a-zA-Z][a-zA-Z0-9]*);",
                    lambda m: m.group(0) if m.group(1) in XML_ENTITIES else html.unescape(m.group(0)), markup)
    return re.sub(r"&(?!#?\w+;)", "&amp;", markup)     # a bare & (fine in HTML) is invalid XML


def element_by_id(page_html, ref):
    """The complete element (<symbol>, <g>, <path> …) with id="ref" in the page, nesting-aware."""
    m = re.search(rf'<([a-zA-Z]+)\b[^>]*\sid="{re.escape(ref)}"[^>]*?(/?)>', page_html)
    if not m:
        return None
    if m.group(2):                                    # self-closing
        return m.group(0)
    tag, depth, pos = m.group(1), 1, m.end()
    for t in re.finditer(rf"<(/?){tag}\b[^>]*?(/?)>", page_html[pos:]):
        if t.group(2):
            continue
        depth += -1 if t.group(1) else 1
        if depth == 0:
            return page_html[m.start():pos + t.end()]
    return None


def referenced_symbols(page_html, markup):
    """<use href="#x"> pointing outside the figure (the page's sprite): copy those elements along,
    including what they reference themselves (the bat symbol uses #bat-wing)."""
    have = set(re.findall(r'\sid="([\w-]+)"', markup))
    defs, todo = [], list(dict.fromkeys(re.findall(r'href="#([\w-]+)"', markup)))
    while todo:
        ref = todo.pop(0)
        if ref in have:
            continue
        el = element_by_id(page_html, ref)
        if el:
            defs.append(el)
            have.update(re.findall(r'\sid="([\w-]+)"', el))
            todo += re.findall(r'href="#([\w-]+)"', el)
    return "".join(defs)


def standalone(fig, lang, svg, css_rules, faces, page_html=""):
    root = re.match(r"<svg\b([^>]*)>", svg)
    attrs_root = dict(re.findall(r'([\w:-]+)="([^"]*)"', root.group(1)))
    minx, miny, w, h = (float(v) for v in attrs_root["viewBox"].split())
    inner = svg[root.end():svg.rfind("</svg>")]
    title = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", inner, re.S).group(1)).strip()
    desc = html.unescape(re.search(r"<desc[^>]*>(.*?)</desc>", inner, re.S).group(1)).strip()
    inner = re.sub(r"<title[^>]*>.*?</title>|<desc[^>]*>.*?</desc>", "", inner, flags=re.S)
    symbols = referenced_symbols(page_html, inner)
    if symbols:
        inner = f"<defs>{symbols}</defs>" + inner
    doc = svg + symbols + f' class="{fig["context"]}"'
    classes = {c for group in re.findall(r'class="([^"]*)"', doc) for c in group.split()}
    attrs = set(re.findall(r'\s([\w-]+)="', doc))
    ids = set(re.findall(r'\sid="([\w-]+)"', doc))

    kept = []
    for prelude, body in css_rules:
        if prelude.startswith("@"):
            continue                                   # media queries, font faces, keyframes
        sels = [s for s in split_selectors(prelude) if applies(s, classes, attrs, ids)]
        if sels:
            kept.append(f"{', '.join(sels)} {{ {body} }}")
    rules = "\n".join(kept)

    text = html.unescape(" ".join(re.findall(r">([^<>]+)<", inner)))
    families = {"Inter"}                               # body text font, inherited by SVG text
    if "var(--font-display)" in rules:
        families.add("Fraunces")
    if "var(--font-mono)" in rules:
        families.add("JetBrains Mono")
    font_css = []
    for (family, style), (path, body) in sorted(faces.items()):
        if family in families and (style == "normal" or "italic" in rules):
            data = subset_font(path, text)
            body = re.sub(r'src:[^;]+;', f'src: url("data:font/woff2;base64,{data}") format("woff2");', body)
            font_css.append(f"@font-face {{ {body} }}")

    ow, oh = w + 2 * PAD, h + 2 * PAD
    fmt = lambda v: f"{v:g}"
    root_attrs = " ".join(f'{k}="{v}"' for k, v in attrs_root.items()
                          if k not in ("role", "aria-labelledby", "aria-describedby", "xmlns", "viewBox"))
    out = (f'<?xml version="1.0" encoding="UTF-8"?>\n'
           f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{fmt(minx - PAD)} {fmt(miny - PAD)} {fmt(ow)} {fmt(oh)}" '
           f'width="{fmt(ow)}" height="{fmt(oh)}" role="img" lang="{lang}" aria-labelledby="t" aria-describedby="d">\n'
           f'<title id="t">{html.escape(title)}</title>\n<desc id="d">{html.escape(desc)}</desc>\n'
           f'<!-- WildBionics · {html.escape(fig["url"])} · CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/). '
           f'{FONT_LICENCE} -->\n'
           f'<style>\n{chr(10).join(font_css)}\nsvg {{ font-family: var(--font-sans); }}\n{rules}\n</style>\n'
           f'<rect x="{fmt(minx - PAD)}" y="{fmt(miny - PAD)}" width="{fmt(ow)}" height="{fmt(oh)}" style="fill: {fig["bg"]}"/>\n'
           f'<g class="{fig["context"]}"><svg {root_attrs} x="{fmt(minx)}" y="{fmt(miny)}" width="{fmt(w)}" height="{fmt(h)}" '
           f'viewBox="{attrs_root["viewBox"]}" style="overflow: visible; width: {fmt(w)}px; height: {fmt(h)}px; max-width: none">{inner}</svg></g>\n</svg>\n')
    out = xml_safe(out)
    ET.fromstring(out.encode("utf-8"))                 # must be well-formed XML
    return out


def main():
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
    manifest = json.loads((site / "figures" / "manifest.json").read_text(encoding="utf-8"))
    css = (site / "assets" / "css" / "main.css").read_text(encoding="utf-8")
    rules, faces = css_blocks(css), fonts_of(css, site)
    errors, written = [], 0
    for fig in manifest["figures"]:
        for lang in manifest["languages"]:
            url = fig["pages"].get(lang)
            page = site / url.lstrip("/") / "index.html" if url else None
            if not page or not page.exists():
                errors.append(f"{fig['name']} ({lang}): page {url} not built")
                continue
            page_html = page.read_text(encoding="utf-8")
            svg = cut_svg(page_html, fig["id"])
            if not svg:
                errors.append(f"{fig['name']} ({lang}): no <svg aria-labelledby=\"{fig['id']}-title\"> on {url}")
                continue
            try:
                data = standalone(dict(fig, url=url), lang, svg, rules, faces, page_html)
            except (ET.ParseError, AttributeError, KeyError, ValueError) as e:
                errors.append(f"{fig['name']} ({lang}): {e}")
                continue
            out = site / "figures" / f"{fig['name']}.{lang}.svg"
            out.write_text(data, encoding="utf-8")
            written += 1
            print(f"ok   /figures/{out.name}  {len(data.encode()) / 1024:.0f} KB")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"\nFigures: {written} files written, {len(errors)} errors.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
