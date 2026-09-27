#!/bin/zsh
# Render WildBionics pages for figure review (WebKit, same engine as Safari).
#
#   shots.sh build                                   # compile the renderer once
#   shots.sh page  <url> <out.png> <width> [y h]     # full page, or a clip (CSS px)
#   shots.sh figure <url> <out.png>                  # article hero figure, rendered large
#
# Env: SHOT_JS="…"  JavaScript to run before the snapshot (e.g. click a tab, focus a node).
# Animations are disabled for the snapshot. Output is 2× (Retina) resolution.
set -e
DIR=${0:A:h}
BIN="${TMPDIR:-/tmp}/wildbionics-figures/shot"
case "$1" in
  build)
    # On this Mac the default SDK does not match the Command Line Tools; pin 26.5 if present.
    SDK=/Library/Developer/CommandLineTools/SDKs/MacOSX26.5.sdk
    [ -d "$SDK" ] && export SDKROOT=$SDK
    mkdir -p "${BIN:h}" && swiftc -O "$DIR/shot.swift" -o "$BIN" && echo "built $BIN" ;;
  page)
    [ -x "$BIN" ] || "$0" build
    shift; "$BIN" "$@" ;;
  figure)
    [ -x "$BIN" ] || "$0" build
    SHOT_JS="document.querySelector('.article-header__grid').style.gridTemplateColumns='1fr';document.querySelector('.article-header__copy').style.display='none';${SHOT_JS:-}" \
      "$BIN" "$2" "$3" 1440 120 820 ;;
  *) sed -n '2,9p' "$0"; exit 1 ;;
esac
