#!/usr/bin/env bash
# Waits for gemma3_lowfix15, then runs the extra energy weights (390 requests) on the Gemma-3 pair.
cd "$(dirname "$0")/../.."
D=results/gemma3_20261026
until grep -qE "complete|gave up" $D/gemma3_lowfix15_maintenance.log 2>/dev/null; do sleep 30; done
grep -q "gave up" $D/gemma3_lowfix15_maintenance.log && exit 1
bash $D/run_full.sh gemma3_lowfix15_w gemma-3-4b-it
