#!/usr/bin/env bash
# Energy-weight sweep of CAPE with interrupt at 2 ms (50 requests), Gemma-3 pair.
cd "$(dirname "$0")/../.."
ping -c 30 -i 0.2 172.23.123.195 | tail -1
bash results/gemma3_20261026/run_full.sh gemma3_wsweep10 gemma-3-4b-it
ping -c 30 -i 0.2 172.23.123.195 | tail -1
