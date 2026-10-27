#!/usr/bin/env bash
# Delay sweep (600 requests), then CAPE ablation (360 requests), both on the Gemma-3 pair.
cd "$(dirname "$0")/../.."
D=results/gemma3_20261026
bash $D/run_full.sh gemma3_delay_sweep gemma-3-4b-it || exit 1
bash $D/run_full.sh gemma3_ablation gemma-3-4b-it
