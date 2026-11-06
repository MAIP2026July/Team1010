#!/bin/bash
# usage: render.sh input.md output.pdf
set -e
html="/tmp/$(basename "$1" .md).html"
pandoc "$1" -s --embed-resources --css "$(dirname "$0")/style.css" -o "$html" --metadata pagetitle="ReconPilot"
google-chrome --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf="$2" "file://$html" 2>/dev/null
