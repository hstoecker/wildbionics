#!/usr/bin/env python3
"""Notify IndexNow (Bing, Yandex, Seznam, Naver, …) about the site's URLs after a deploy.

Reads the key from _config.yml and the URL list from the live sitemap, waits until the
key file is reachable (GitHub Pages' CDN can lag a little), then submits all URLs in one
request. Docs: https://www.indexnow.org/documentation
"""
import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

SITE = "https://wildbionics.com"
ENDPOINT = "https://api.indexnow.org/indexnow"

key = re.search(r'^indexnow_key:\s*"?([0-9a-fA-F-]{8,128})"?', open("_config.yml", encoding="utf-8").read(), re.M).group(1)
key_url = f"{SITE}/{key}.txt"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "wildbionics-deploy", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8")


for attempt in range(20):
    try:
        if get(f"{key_url}?t={int(time.time())}").strip() == key:
            break
    except Exception as e:  # noqa: BLE001 – retry on any network error
        print(f"key file not reachable yet ({e}); retrying…")
    time.sleep(15)
else:
    sys.exit(f"IndexNow key file {key_url} never became reachable")

ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
urls = [e.text for e in ET.fromstring(get(f"{SITE}/sitemap.xml?t={int(time.time())}")).findall("s:url/s:loc", ns)]
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
