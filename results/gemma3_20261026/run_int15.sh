#!/usr/bin/env bash
# CAPE with interrupt vs plain CAPE at 100 ms and dynamic delay (180 requests), Gemma-3 pair.
cd "$(dirname "$0")/../.."
bash results/gemma3_20261026/run_full.sh gemma3_int15 gemma-3-4b-it
