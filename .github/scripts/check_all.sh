#!/usr/bin/env bash
# All quality gates in CI order, one line each – what the build check of a pull request runs.
#
#   .github/scripts/check_all.sh                 # everything (as CI)
#   .github/scripts/check_all.sh --only <ref>    # code examples of one page only (fast while writing)
#
# Uses .venv if present, UTF-8 for Ruby (German umlauts), and stops at the first failing gate
# with its full output. Warns if `jekyll serve` is running: it rewrites _site while the gates read it.
set -uo pipefail
cd "$(dirname "$0")/../.."
export LANG="${LANG:-en_US.UTF-8}" LC_ALL="${LC_ALL:-en_US.UTF-8}"
[ -f .venv/bin/activate ] && source .venv/bin/activate
only=()
[ "${1:-}" = "--only" ] && [ -n "${2:-}" ] && only=(--only "$2")
if pgrep -f "jekyll serve" >/dev/null 2>&1; then
  echo "warning: jekyll serve is running – it rewrites _site during the checks; stop it for reliable results"
fi

gate() {   # name, command… – print the summary line, or the full output on failure
  local name=$1; shift
  local start=$SECONDS out
  if out=$("$@" 2>&1); then
    printf "ok    %-14s %4ss  %s\n" "$name" $((SECONDS - start)) "$(printf '%s\n' "$out" | grep -v -e '^\s*$' -e 'faraday' | tail -1)"
  else
    printf "FAIL  %-14s %4ss\n%s\n" "$name" $((SECONDS - start)) "$out"
    exit 1
  fi
}

gate terms     ruby .github/scripts/check_terms.rb
gate content   ruby .github/scripts/check_content.rb
gate plugin    ruby .github/scripts/check_plugin.rb --base origin/main
if [ ${#only[@]} -gt 0 ]; then
  gate code      python3 .github/scripts/code_examples.py "${only[@]}"
else
  gate code      python3 .github/scripts/code_examples.py --check
fi
gate build     bash -c "bundle exec jekyll build -q && echo 'site built: _site'"
gate figures   python3 .github/scripts/figures.py _site
gate site      python3 .github/scripts/check_site.py _site
echo "all gates passed"
