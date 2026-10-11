#!/usr/bin/env bash
# Usage: tools/autoplay.sh "<ids comma list or empty for all>" "<tiers, default 1>" [real-timeout-seconds]
# Runs dev/autoplay.html in headless Chrome with a large virtual-time budget and prints the AUTOPLAY lines.
OUT="/c/Users/Phil/AppData/Local/Temp/claude/C--1-Astra-Nova---Finn/d87786aa-7853-4953-8446-4bd24828fbf1/scratchpad/shots"
mkdir -p "$OUT"
IDS="$1"; TIERS="${2:-1}"; TO="${3:-900}"
Q="tiers=$TIERS"; [ -n "$IDS" ] && Q="ids=$IDS&$Q"
rm -rf "$OUT/profile-autoplay"
timeout "$TO" "/c/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --enable-unsafe-swiftshader --use-angle=swiftshader \
  --no-first-run --user-data-dir="$OUT/profile-autoplay" --window-size=1720,820 --virtual-time-budget=20000000 \
  --enable-logging=stderr --v=0 --screenshot="$OUT/autoplay.png" "http://127.0.0.1:8100/dev/autoplay.html?$Q" 2>&1 | grep -E "AUTOPLAY" | sed -E 's/^.*AUTOPLAY /AUTOPLAY /; s/", source.*$//'
