#!/usr/bin/env bash
# Run the two key B3 experiments + summarize + backup
set -e

cd ~/Downloads/day4b_jetson
source /home/jetson/specdecode/venv/bin/activate

URL="http://localhost:9090"
DATA="$HOME/Downloads/day3_jetson/gsm8k_test_50.jsonl"
OUT_DIR="$HOME/b3_results"
mkdir -p "$OUT_DIR"

# Pre-flight check
curl -sf "$URL/health" >/dev/null || { echo "H200 verify server not reachable; check SSH tunnel"; exit 1; }
echo "==> H200 verify server OK"

# Pre-flight: check llama-server too
curl -sf http://localhost:8080/health >/dev/null || { echo "Jetson llama-server not running"; exit 1; }
echo "==> Jetson llama-server OK"

# Run γ=5
echo
echo "==> Running B3 γ=5 (50 samples)"
python bench_edge_cloud.py \
    --verifier remote --remote-url "$URL" \
    --gamma 5 --n 50 \
    --data "$DATA" \
    --out "$OUT_DIR/B3_remote_g5.json" \
    --tag B3_remote_g5

# Run γ=3
echo
echo "==> Running B3 γ=3 (50 samples)"
python bench_edge_cloud.py \
    --verifier remote --remote-url "$URL" \
    --gamma 3 --n 50 \
    --data "$DATA" \
    --out "$OUT_DIR/B3_remote_g3.json" \
    --tag B3_remote_g3

# Quick summary
echo
echo "==> Done. Results in $OUT_DIR"
echo
for f in "$OUT_DIR"/B3_*.json; do
    echo "--- $f ---"
    python3 -c "
import json
d = json.load(open('$f'))
s = d['summary']
print(f\"  tag: {s['tag']}\")
print(f\"  accuracy: {s['accuracy']:.1%}\")
print(f\"  agg tok/s: {s['aggregate_tokens_per_second']:.1f}\")
print(f\"  avg latency: {s['avg_latency_s']:.2f}s\")
print(f\"  acceptance: {s['acceptance_rate']:.1%}\")
print(f\"  output_tokens dist: avg={s['avg_output_tokens']:.0f}\")
print(f\"  draft/verify/network ms: {s['avg_draft_ms_per_req']:.0f}/{s['avg_verify_ms_per_req']:.0f}/{s['avg_network_ms_per_req']:.0f}\")
"
done
