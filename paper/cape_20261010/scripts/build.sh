#!/usr/bin/env bash
# Compile the manuscript into build/ and copy the PDF next to main.tex.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
mkdir -p build
if command -v latexmk >/dev/null 2>&1; then
  latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex
elif command -v tectonic >/dev/null 2>&1; then
  tectonic --keep-logs --keep-intermediates --outdir build main.tex
else
  echo 'Install latexmk with XeLaTeX or Tectonic, or compile in Overleaf.' >&2
  exit 1
fi
cp build/main.pdf main.pdf
