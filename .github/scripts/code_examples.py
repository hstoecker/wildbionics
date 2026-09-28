#!/usr/bin/env python3
"""Code-example gate and generator (rules: wildbionics-article, section "Code examples").

Every Python example on the site is a complete program. A code block is marked as an example
by the include that follows it:

    ```python                                  {% highlight python %}
    …                                          …
    ```                                        {% endhighlight %}
    {% include code-result.html file="x.py" %} {% include code-result.html file="x.py" ref="home" lang="en" %}

"Try it yourself" changes are tested, too. Each one is an include anywhere in the same file:

    {% include code-variant.html file="x.py" id="bigger" replace="R_MAX = 3.0e-3" with="R_MAX = 6.0e-3" expect="551 557" %}

The script replaces the `replace` text (it must occur exactly once), runs the changed program and
checks that every number in `expect` – the numbers the text quotes – appears in its output.

This script finds every example, runs it (Matplotlib without a window) and writes

    examples/<ref>/<name>.<lang>.py      download (code + header with source and how to run)
    examples/<ref>/<name>.<lang>.ipynb   notebook for "Open in Colab"
    examples/<ref>/<name>.<lang>.svg     the chart, if the program draws one
    _data/code_examples.yml              printed output + file paths for code-result.html

A Python block without the include, a crash, a warning, a run over TIMEOUT seconds, more than
one chart or a program that prints nothing fails the gate.

    python3 -m pip install -r examples/requirements.txt
    python3 .github/scripts/code_examples.py           # run all, (re)write generated files
    python3 .github/scripts/code_examples.py --check   # CI: also fail if committed files are stale

Charts are always rewritten and never compared (fonts and library versions change the SVG
bytes); CI regenerates them before the Jekyll build, so the site always shows the current run.
"""

import difflib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "examples"
DATA = ROOT / "_data" / "code_examples.yml"
SITE_URL = "https://wildbionics.com"
TIMEOUT = 60
SKIP_DIRS = {"_site", "vendor", "plugins", "examples", ".git", ".jekyll-cache", "node_modules", ".bundle"}
SKIP_FILES = {"CLAUDE.md", "AGENTS.md", "CONTRIBUTING.md", "README.md", "code-result.html", "code-variant.html"}

FENCE = re.compile(r"^```python[ \t]*\n(.*?)^```[ \t]*$", re.S | re.M)
HIGHLIGHT = re.compile(r"\{%-?\s*highlight python\s*-?%\}\n(.*?)\{%-?\s*endhighlight\s*-?%\}", re.S)
INCLUDE = re.compile(r"\s*\{%-?\s*include code-result\.html\b(.*?)-?%\}", re.S)
VARIANT = re.compile(r"\{%-?\s*include code-variant\.html\b(.*?)-?%\}", re.S)
PARAM = re.compile(r'(\w+)="([^"]*)"')
PACKAGES = {"numpy": "numpy", "scipy": "scipy", "matplotlib": "matplotlib"}

# Text for the generated files (not site UI – that lives in _data/i18n.yml).
TEXT = {
    "en": {
        "from": "From",
        "quote": "“{}”",
        "home": "the WildBionics home page",
        "needs": "Needs",
        "run": "Run",
        "licence": "Code: MIT licence",
        "nb_run": "Run the cell below: **Runtime → Run all** (or click into it and press Shift+Enter).",
        "nb_result": "The result appears under the cell.",
        "nb_chart": "The result and the chart appear under the cell.",
        "nb_try": "Change a value and run it again.",
        "nb_help": "How to run it on your own computer",
    },
    "de": {
        "from": "Aus",
        "quote": "„{}“",
        "home": "der WildBionics-Startseite",
        "needs": "Braucht",
        "run": "Starten",
        "licence": "Code: MIT-Lizenz",
        "nb_run": "Führe die Zelle unten aus: **Laufzeit → Alle ausführen** (oder in die Zelle klicken und "
                  "Umschalt+Enter drücken).",
        "nb_result": "Das Ergebnis erscheint unter der Zelle.",
        "nb_chart": "Ergebnis und Diagramm erscheinen unter der Zelle.",
        "nb_try": "Ändere einen Wert und führe sie erneut aus.",
        "nb_help": "So führst du den Code auf deinem eigenen Rechner aus",
    },
}
HELP_URL = {"en": "/run-code/", "de": "/de/code-ausfuehren/"}

# Runs inside the example's interpreter: no window, catch the chart, deterministic SVG.
RUNNER = r"""
import runpy, sys, warnings
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "wildbionics"
plt.show = lambda *args, **kwargs: None
warnings.simplefilter("default")
runpy.run_path(sys.argv[1], run_name="__main__")
figures = plt.get_fignums()
if len(figures) > 1:
    sys.exit(f"draws {len(figures)} charts – one example, one chart")
if figures:
    plt.figure(figures[0]).savefig(sys.argv[2], format="svg", metadata={"Date": None})
"""


def front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fm = {}
    for line in (m.group(1) if m else "").splitlines():
        kv = re.match(r'(\w+):\s*"?(.*?)"?\s*$', line)
        if kv:
            fm[kv.group(1)] = kv.group(2)
    return fm


def sources():
    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT)
        if path.suffix not in {".md", ".html"} or rel.name in SKIP_FILES:
            continue
        if SKIP_DIRS & set(rel.parts[:-1]):
            continue
        yield path, rel


def find_examples(errors):
    examples = []
    for path, rel in sources():
        text = path.read_text(encoding="utf-8")
        fm = front_matter(text)
        for pattern in (FENCE, HIGHLIGHT):
            for m in pattern.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                inc = INCLUDE.match(text, m.end())
                if not inc:
                    errors.append(f"{rel}:{line}: Python block without "
                                  '{% include code-result.html file="<name>.py" %} right after it')
                    continue
                if '\\"' in inc.group(1):
                    errors.append(f"{rel}:{line}: code-result parameters contain \\\" – Liquid has no escapes, "
                                  "the value would be cut off; use typographic quotes “…” instead")
                params = dict(PARAM.findall(inc.group(1)))
                ex = {
                    "where": f"{rel}:{line}",
                    "code": m.group(1).rstrip() + "\n",
                    "file": params.get("file", ""),
                    "ref": params.get("ref") or fm.get("ref", ""),
                    "lang": params.get("lang") or fm.get("lang", ""),
                    "title": fm.get("title", ""),
                    "url": fm.get("permalink", "/" if params.get("ref") == "home" else ""),
                    "params": params,
                }
                ex["variants"] = []
                if not re.fullmatch(r"[a-z0-9_]+\.py", ex["file"]):
                    errors.append(f"{ex['where']}: file=\"{ex['file']}\" must be a snake_case .py name")
                elif ex["lang"] not in TEXT or not ex["ref"]:
                    errors.append(f"{ex['where']}: needs ref and lang (front matter or include parameters)")
                else:
                    examples.append(ex)
        for m in VARIANT.finditer(text):
            if '\\"' in m.group(1):
                errors.append(f"{rel}:{text.count(chr(10), 0, m.start()) + 1}: code-variant parameters contain \\\" – "
                              "use typographic quotes “…” instead")
            v = dict(PARAM.findall(m.group(1)))
            v["where"] = f"{rel}:{text.count(chr(10), 0, m.start()) + 1}"
            owner = [ex for ex in examples if ex["where"].startswith(f"{rel}:") and ex["file"] == v.get("file")]
            missing = [k for k in ("file", "id", "replace", "with", "expect") if not v.get(k)]
            if missing:
                errors.append(f"{v['where']}: code-variant needs {', '.join(missing)}")
            elif not owner:
                errors.append(f"{v['where']}: code-variant for {v['file']}, but that example is not in this file")
            else:
                owner[0]["variants"].append(v)
    seen = {}
    for ex in examples:
        key = (ex["ref"], ex["lang"], ex["file"])
        if key in seen and seen[key]["code"] != ex["code"]:
            errors.append(f"{ex['where']}: {ex['file']} differs from the example at {seen[key]['where']}")
        seen.setdefault(key, ex)
    return list(seen.values())


def download(ex, stem):
    t = TEXT[ex["lang"]]
    needs = [p for mod, p in PACKAGES.items() if re.search(rf"^\s*(from|import) {mod}\b", ex["code"], re.M)]
    source = t["quote"].format(ex["title"]) if ex["title"] else t["home"]
    head = [f"# {ex['file']} – {t['from']} {source}",
            f"# {SITE_URL}{ex['url']} · {t['licence']}"]
    if needs:
        head.append(f"# {t['needs']}: python3 -m pip install {' '.join(needs)}")
    head.append(f"# {t['run']}: python3 {ex['file']}   ({SITE_URL}{HELP_URL[ex['lang']]})")
    return "\n".join(head) + "\n\n" + ex["code"]


def notebook(ex, chart):
    t = TEXT[ex["lang"]]
    title = t["quote"].format(ex["title"]) if ex["title"] else t["home"]
    how = f"{t['nb_run']} {t['nb_chart'] if chart else t['nb_result']} {t['nb_try']}"
    intro = (f"# {ex['file']}\n\n{t['from']} [{title}]({SITE_URL}{ex['url']}) · {t['licence']}\n\n"
             f"{how}\n\n[{t['nb_help']}]({SITE_URL}{HELP_URL[ex['lang']]})")

    def lines(s):
        parts = s.split("\n")
        return [p + "\n" for p in parts[:-1]] + ([parts[-1]] if parts[-1] else [])

    nb = {
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": lines(intro)},
            {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
             "source": lines(ex["code"].rstrip("\n"))},
        ],
        "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                     "language_info": {"name": "python"}},
        "nbformat": 4,
        "nbformat_minor": 4,
    }
    return json.dumps(nb, indent=1, ensure_ascii=False) + "\n"


def run(ex, svg_path, errors):
    with tempfile.TemporaryDirectory() as tmp:
        script = Path(tmp) / ex["file"]
        script.write_text(ex["code"], encoding="utf-8")
        chart = Path(tmp) / "chart.svg"
        env = dict(os.environ, MPLBACKEND="Agg", PYTHONHASHSEED="0", PYTHONIOENCODING="utf-8")
        try:
            p = subprocess.run([sys.executable, "-c", RUNNER, str(script), str(chart)], cwd=tmp, env=env,
                               capture_output=True, text=True, encoding="utf-8", timeout=TIMEOUT)
        except subprocess.TimeoutExpired:
            errors.append(f"{ex['where']}: {ex['file']} ran longer than {TIMEOUT} s")
            return None, None
        noise = [line for line in p.stderr.splitlines() if "font cache" not in line]
        if p.returncode != 0:
            errors.append(f"{ex['where']}: {ex['file']} failed:\n    " + "\n    ".join(noise[-12:]))
            return None, None
        if any("Warning" in line for line in noise):
            errors.append(f"{ex['where']}: {ex['file']} prints warnings:\n    " + "\n    ".join(noise[-6:]))
        output = "\n".join(line.rstrip() for line in p.stdout.rstrip().splitlines())
        if not output:
            errors.append(f"{ex['where']}: {ex['file']} prints nothing – an example must print its result")
        size = None
        if svg_path is None:
            return output, None
        if chart.exists():
            svg = chart.read_text(encoding="utf-8")
            svg_path.write_text(svg, encoding="utf-8")
            w, h = (float(re.search(rf'{k}="([\d.]+)pt"', svg).group(1)) for k in ("width", "height"))
            size = (round(w * 4 / 3), round(h * 4 / 3))
        elif svg_path.exists():
            svg_path.unlink()
        return output, size


def yaml_data(entries):
    out = ["# Generated by .github/scripts/code_examples.py – do not edit by hand.",
           "# Printed output and file paths of every code example, read by _includes/code-result.html."]
    for ref in sorted(entries):
        out.append(f"{ref}:")
        for lang in sorted(entries[ref]):
            out.append(f"  {lang}:")
            for file in sorted(entries[ref][lang]):
                out.append(f"    {json.dumps(file)}:")
                for k, v in entries[ref][lang][file].items():
                    out.append(f"      {k}: {json.dumps(v, ensure_ascii=False)}")
    return "\n".join(out) + "\n"


def main():
    check = "--check" in sys.argv
    errors, stale = [], []
    examples = find_examples(errors)
    expected, entries = {}, {}
    for ex in examples:
        stem = ex["file"].removesuffix(".py")
        folder, name = OUT / ex["ref"], f"{stem}.{ex['lang']}"
        folder.mkdir(parents=True, exist_ok=True)
        py_path, nb_path, svg_path = (folder / f"{name}{ext}" for ext in (".py", ".ipynb", ".svg"))
        output, size = run(ex, svg_path, errors)
        if output is None:
            continue
        rel = (folder / name).relative_to(ROOT).as_posix()
        expected[py_path] = download(ex, stem)
        expected[nb_path] = notebook(ex, size is not None)
        entry = {"output": output, "py": f"/{rel}.py", "notebook": f"{rel}.ipynb"}
        if size:
            entry.update(chart=f"/{rel}.svg", chart_width=size[0], chart_height=size[1])
            for key in ("label", "caption", "alt"):     # for the chart's ImageObject in the page's JSON-LD
                if ex["params"].get(key):
                    entry[f"chart_{key}"] = " ".join(re.sub(r"<[^>]+>", "", ex["params"][key]).split())
        if size and ex["params"].get("variant") != "card" and not ex["params"].get("alt"):
            errors.append(f"{ex['where']}: {ex['file']} draws a chart – describe it with alt=\"…\" in the include")
        for v in ex["variants"]:
            if ex["code"].count(v["replace"]) != 1:
                errors.append(f"{v['where']}: replace=\"{v['replace']}\" must occur exactly once in {ex['file']}")
                continue
            changed = dict(ex, code=ex["code"].replace(v["replace"], v["with"]), where=v["where"])
            out, _ = run(changed, None, errors)
            if out is None:
                continue
            for number in v["expect"].split():
                if not re.search(rf"(?<![\w.]){re.escape(number)}(?![\w]|\.\d)", out):
                    errors.append(f"{v['where']}: variant \"{v['id']}\" does not print {number} – "
                                  f"the text quotes it. Output:\n    " + out.replace("\n", "\n    "))
            entry.setdefault("variants", {})[v["id"]] = {"with": v["with"], "output": out}
        entries.setdefault(ex["ref"], {}).setdefault(ex["lang"], {})[ex["file"]] = entry
        extras = ("  + chart" if size else "") + (f"  + {len(ex['variants'])} variants" if ex["variants"] else "")
        print(f"ok   {ex['where']}  {ex['file']} ({ex['lang']}){extras}")
    if errors:                              # keep the committed files when something failed
        for e in errors:
            print(f"ERROR: {e}")
        print(f"\nCode examples: {len(examples)} found, {len(errors)} errors.")
        return 1
    expected[DATA] = yaml_data(entries)

    keep = set(expected) | {p.with_suffix(".svg") for p in expected if p.suffix == ".py"} | {OUT / "requirements.txt"}
    for path in sorted(OUT.rglob("*")):
        if path.is_file() and path not in keep:
            stale.append(f"{path.relative_to(ROOT)} belongs to no example")
            path.unlink()
    for path, content in expected.items():
        old = path.read_text(encoding="utf-8") if path.exists() else None
        if old != content:
            stale.append(f"{path.relative_to(ROOT)} was out of date")
            if check and old is not None:          # show what changed, so CI logs explain it
                diff = difflib.unified_diff(old.splitlines(), content.splitlines(), "committed", "this run", lineterm="", n=0)
                print("\n".join(list(diff)[:40]))
            path.write_text(content, encoding="utf-8")
    for d in sorted(OUT.glob("*/"), reverse=True):
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()

    for s in stale:
        print(f"{'ERROR' if check else 'wrote'}: {s}")
    if check and stale:
        print("\nRun `python3 .github/scripts/code_examples.py` and commit the result.")
    print(f"\nCode examples: {len(examples)} run, {len(stale)} files {'stale' if check else 'updated'}.")
    return 1 if check and stale else 0


if __name__ == "__main__":
    sys.exit(main())
