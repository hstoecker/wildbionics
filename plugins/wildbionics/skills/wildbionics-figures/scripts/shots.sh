#!/usr/bin/env bash
# Render WildBionics pages for figure review.
#   macOS: WebKit renderer (shot.swift, compiled on first use) – supports clips and SHOT_JS.
#   Linux (Claude Code on the web, CI): headless Chrome/Chromium – full width, top of page.
#
#   shots.sh page   <url> <out.png> <width> [y h]   # page, or a clip (CSS px)
#   shots.sh figure <url> <out.png>                 # article hero figure, rendered large
#   shots.sh build                                  # macOS: compile the renderer
#
# Env (macOS only): SHOT_JS="…" runs JavaScript before the snapshot (click a tab, focus a node).
# No renderer available? Every pull request gets screenshots from CI: artifact preview-pr-<n>.
set -euo pipefail
DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
BIN="${TMPDIR:-/tmp}/wildbionics-figures/shot"
cmd=${1:-}

chrome() {
  command -v google-chrome || command -v chromium || command -v chromium-browser || command -v google-chrome-stable || true
}

linux_shot() {   # url out width height
  local c; c=$(chrome)
  if [ -z "$c" ]; then
    echo "No Chrome/Chromium found. Install one (e.g. 'sudo apt-get install -y chromium-browser')"
    echo "or open a pull request and use the CI screenshots (artifact preview-pr-<n>)." >&2
    exit 2
  fi
  "$c" --headless=new --no-sandbox --hide-scrollbars --disable-gpu --force-device-scale-factor=2 \
    --window-size="$3,$4" --screenshot="$2" "$1" >/dev/null 2>&1
  echo "wrote $2"
}

if [ "$(uname)" != "Darwin" ]; then
  case "$cmd" in
    page)   h=$(( ${5:-0} + ${6:-2400} )); linux_shot "$2" "$3" "$4" "$h" ;;
    figure) linux_shot "$2" "$3" 1440 1100 ;;
    build)  echo "nothing to build on Linux (uses headless Chrome)" ;;
    *) sed -n '2,11p' "$0"; exit 1 ;;
  esac
  exit 0
fi

case "$cmd" in
  build)
    # Some Macs ship an SDK newer than their Command Line Tools; pin 26.5 if present.
    SDK=/Library/Developer/CommandLineTools/SDKs/MacOSX26.5.sdk
    [ -d "$SDK" ] && export SDKROOT=$SDK
    mkdir -p "$(dirname "$BIN")" && swiftc -O "$DIR/shot.swift" -o "$BIN" && echo "built $BIN" ;;
  page)
    [ -x "$BIN" ] || "$0" build
    shift; "$BIN" "$@" ;;
  figure)
    [ -x "$BIN" ] || "$0" build
    SHOT_JS="document.querySelector('.article-header__grid').style.gridTemplateColumns='1fr';document.querySelector('.article-header__copy').style.display='none';${SHOT_JS:-}" \
      "$BIN" "$2" "$3" 1440 120 820 ;;
  *) sed -n '2,11p' "$0"; exit 1 ;;
esac
