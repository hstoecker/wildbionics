#!/usr/bin/env python3
"""Notify IndexNow (Bing, Yandex, Seznam, Naver, …) about the site's URLs after a deploy.

    indexnow.py changed _site changed-urls.txt   # build job, before deploy: list the pages whose
                                                  # HTML differs from the live site (or are new)
    indexnow.py --urls changed-urls.txt          # after deploy: submit only those
    indexnow.py                                  # after deploy: submit every sitemap URL

Reads the key from _config.yml, waits until the key file is reachable (GitHub Pages' CDN can
lag a little), then submits the URLs in one request. Submitting only changed pages keeps
IndexNow's signal meaningful – CSS, script or docs-only deploys submit nothing.
Docs: https://www.indexnow.org/documentation
"""
import hashlib
import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

SITE = "https://wildbionics.com"
ENDPOINT = "https://api.indexnow.org/indexnow"

key = re.search(r'^indexnow_key:\s*"?([0-9a-fA-F-]{8,128})"?', open("_config.yml", encoding="utf-8").read(), re.M).group(1)
key_url = f"{SITE}/{key}.txt"


def get(url, raw=False):
    req = urllib.request.Request(url, headers={"User-Agent": "wildbionics-deploy", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
    return data if raw else data.decode("utf-8")


NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def changed(site_dir, out_file):
    """Compare every page of the new build with the live page; write new or changed URLs."""
    root = Path(site_dir)
    urls = [e.text for e in ET.parse(root / "sitemap.xml").getroot().findall("s:url/s:loc", NS)]
    result = []
    for url in urls:
        path = url[len(SITE):] or "/"
        local = root / path.lstrip("/")
        if path.endswith("/"):
            local = local / "index.html"
        try:
            live = get(f"{url}?t={int(time.time())}", raw=True)
        except Exception:  # noqa: BLE001 – not live yet (new page) or not reachable: submit it
            live = b""
        if hashlib.sha256(live).digest() != hashlib.sha256(local.read_bytes()).digest():
            result.append(url)
    Path(out_file).write_text("".join(u + "\n" for u in result), encoding="utf-8")
    print(f"IndexNow: {len(result)} of {len(urls)} pages new or changed")
    for u in result:
        print("  ", u)


if len(sys.argv) > 1 and sys.argv[1] == "changed":
    changed(sys.argv[2], sys.argv[3])
    sys.exit(0)

urls_file = sys.argv[sys.argv.index("--urls") + 1] if "--urls" in sys.argv else None
if urls_file:
    urls = [u.strip() for u in Path(urls_file).read_text(encoding="utf-8").splitlines() if u.strip()]
    if not urls:
        print("IndexNow: no page changed in this deploy – nothing to submit")
        sys.exit(0)


for attempt in range(20):
    try:
        if get(f"{key_url}?t={int(time.time())}").strip() == key:
            break
    except Exception as e:  # noqa: BLE001 – retry on any network error
        print(f"key file not reachable yet ({e}); retrying…")
    time.sleep(15)
else:
    sys.exit(f"IndexNow key file {key_url} never became reachable")

if not urls_file:
    urls = [e.text for e in ET.fromstring(get(f"{SITE}/sitemap.xml?t={int(time.time())}")).findall("s:url/s:loc", NS)]
payload = {"host": SITE.split("//")[1], "key": key, "keyLocation": key_url, "urlList": urls}
req = urllib.request.Request(ENDPOINT, data=json.dumps(payload).encode(), method="POST",
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"IndexNow: HTTP {r.status} for {len(urls)} URLs")
except urllib.error.HTTPError as e:
    # 200/202 = accepted; 422 = URLs don't match host/key; 429 = too many requests
    sys.exit(f"IndexNow rejected the submission: HTTP {e.code} {e.read().decode(errors='replace')}")
for u in urls:
    print("  ", u)
