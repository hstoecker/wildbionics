#!/usr/bin/env python3
"""Render the OG preview images of an article from its front matter (rules: wildbionics-figures).

    python3 plugins/wildbionics/skills/wildbionics-figures/scripts/og.py <ref>

Every language version of the article (_articles/<ref>.<lang>.md) carries its card text:

    image: /assets/og/<ref>-en.jpg
    og: { eyebrow: "Biology · Fluid dynamics", title: "Swimming in <em>honey</em>", sub: "One line.",
          title_px: 58 }          # optional: figure (default: hero_figure), bg1, bg2, title_px

The script writes temporary pages that include _includes/og-card.html, builds the site, serves
_site on a free local port, renders each card with shots.sh at 2× and saves a 1200×630 JPEG
(quality 85) at the path in `image:`. So a card can always be re-rendered exactly – after a
figure, the logo or the text changed. Needs bundle (Jekyll, Ruby), Pillow (.venv) and shots.sh.
"""
import functools
import http.server
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
SHOTS = Path(__file__).with_name("shots.sh")


def front_matter(path):
    """Parsed by Ruby's YAML (always there with Jekyll) – no PyYAML needed."""
    rb = ('require "yaml"; require "json"; require "date"; '
          'puts YAML.safe_load(File.read(ARGV[0]).split(/^---\\s*$/, 3)[1], permitted_classes: [Date]).to_json')
    return json.loads(subprocess.run(["ruby", "-e", rb, str(path)], check=True, capture_output=True,
                                     text=True, env={**os.environ, "LANG": "en_US.UTF-8", "LC_ALL": "en_US.UTF-8"}).stdout)


def main(ref):
    from PIL import Image
    pages = sorted((ROOT / "_articles").glob(f"{ref}.*.md"))
    if not pages:
        sys.exit(f"no _articles/{ref}.<lang>.md")
    tmp_dir = ROOT / "og-tmp"
    tmp_dir.mkdir(exist_ok=True)
    cards = []
    try:
        for page in pages:
            fm = front_matter(page)
            og = fm.get("og") or sys.exit(f"{page.name}: add og: {{eyebrow, title, sub}} to the front matter")
            params = {"eyebrow": og["eyebrow"], "title": og["title"], "sub": og["sub"],
                      "figure": og.get("figure", fm.get("hero_figure", "")),
                      "bg1": og.get("bg1", "#0d1a16"), "bg2": og.get("bg2", "#0a1512"),
                      "title_px": og.get("title_px", 64)}
            bad = [k for k, v in params.items() if '"' in str(v)]
            if bad:
                sys.exit(f"{page.name}: og.{bad[0]} contains a straight double quote – use typographic quotes")
            args = " ".join(f'{k}="{v}"' for k, v in params.items())
            lang = fm["lang"]
            (tmp_dir / f"{lang}.html").write_text(
                f"---\nlayout: null\npermalink: /og-tmp/{lang}.html\nlang: {lang}\nsitemap: false\n---\n"
                f"{{% include og-card.html {args} %}}\n", encoding="utf-8")
            cards.append((lang, ROOT / fm["image"].lstrip("/")))
        subprocess.run(["bundle", "exec", "jekyll", "build", "-q"], cwd=ROOT, check=True)
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT / "_site"))
        handler.log_message = lambda *a: None
        with socket.socket() as s:
            s.bind(("127.0.0.1", 0))
            port = s.getsockname()[1]
        server = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        with tempfile.TemporaryDirectory() as td:
            for lang, out in cards:
                png = Path(td) / f"{lang}.png"
                subprocess.run([str(SHOTS), "page", f"http://127.0.0.1:{port}/og-tmp/{lang}.html", str(png),
                                "1200", "0", "630"], check=True)
                Image.open(png).convert("RGB").resize((1200, 630), Image.LANCZOS).save(out, quality=85, optimize=True)
                print(f"wrote {out.relative_to(ROOT)}")
        server.shutdown()
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
