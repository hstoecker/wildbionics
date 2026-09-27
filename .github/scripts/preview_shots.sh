#!/usr/bin/env bash
# Pull-request preview: serve the built site and take screenshots of the key pages and of
# every article changed in the PR (desktop 1440 px and phone 390 px), with headless Chrome.
#
#   .github/scripts/preview_shots.sh <site-dir> <out-dir> [base-ref]
set -euo pipefail
SITE=${1:-_site}; OUT=${2:-preview}; BASE=${3:-}
mkdir -p "$OUT"
CHROME=$(command -v google-chrome || command -v chromium || command -v chromium-browser || true)
if [ -z "$CHROME" ]; then echo "no Chrome found – skipping screenshots"; exit 0; fi

python3 -m http.server 4173 --directory "$SITE" >/dev/null 2>&1 &
SERVER=$!
trap 'kill $SERVER' EXIT
sleep 1

pages=(/ /de/ /graph/ /de/wissensgraph/)
if [ -n "$BASE" ]; then
  # permalinks of articles changed in this PR
  while read -r f; do
    [ -f "$f" ] || continue
    p=$(grep -m1 '^permalink:' "$f" | sed 's/permalink:[[:space:]]*//')
    [ -n "$p" ] && pages+=("$p")
  done < <(git diff --name-only "$BASE"...HEAD -- '_articles/*.md')
fi

for p in "${pages[@]}"; do
  name=$(echo "$p" | sed 's#^/##; s#/$##; s#/#_#g'); name=${name:-home}
  for w in 1440 390; do
    h=$([ "$w" = 390 ] && echo 5200 || echo 4200)
    "$CHROME" --headless=new --no-sandbox --hide-scrollbars --disable-gpu \
      --window-size="$w,$h" --screenshot="$OUT/${name}_${w}.png" \
      "http://localhost:4173$p" >/dev/null 2>&1 || echo "screenshot failed: $p ($w)"
  done
done
ls -1 "$OUT"
