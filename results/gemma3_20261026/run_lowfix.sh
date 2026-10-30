#!/usr/bin/env bash
# Low-delay CAPE variants (270 requests) on the Gemma-3 pair.
cd "$(dirname "$0")/../.."
bash results/gemma3_20261026/run_full.sh gemma3_lowfix15 gemma-3-4b-it
