#!/usr/bin/env bash
# run_warmup_all.sh — Run all 6 warmup experiments (Jetson, 15W).
# After: compares fixed vs warmup across 3 tasks.
#
# Pre-reqs:
#   - llama-server running on :8080
#   - SSH tunnel localhost:9090 → H200 verify_server
#   - data files at ~/Downloads/day3_jetson/{gsm8k_test_50,humaneval_30,mtbench_30}.jsonl
#
# Total time ~75 min.
set -e

cd ~/Downloads/day4b_jetson
source /home/jetson/specdecode/venv/bin/activate

# Pre-flight
curl -sf http://localhost:8080/health >/dev/null || { echo "Jetson llama-server down"; exit 1; }
curl -sf http://localhost:9090/health >/dev/null || { echo "H200 verify server down (check SSH tunnel)"; exit 1; }
echo "==> Both servers OK"

# 15W mode (assumes you've already run: sudo nvpmodel -m 0 && sudo jetson_clocks)
echo "==> Current power mode:"
sudo nvpmodel -q | head -3
echo

OUT=~/b3_results
mkdir -p "$OUT"
DATA=~/Downloads/day3_jetson
N=30

run_one() {
    local schedule=$1 task=$2 data=$3
    local out="$OUT/W_${schedule}_g3_${task}.json"
    if [[ -f "$out" ]]; then
        echo "  [skip] $out exists"
        return
    fi
    echo
    echo "==> $schedule × $task"
    python bench_warmup.py \
        --schedule "$schedule" --gamma 3 --task "$task" \
        --data "$data" --n "$N" \
        --profile-energy \
        --out "$out"
}

# 6 cells
run_one fixed  gsm8k     "$DATA/gsm8k_test_50.jsonl"
run_one warmup gsm8k     "$DATA/gsm8k_test_50.jsonl"
run_one fixed  humaneval "$DATA/humaneval_30.jsonl"
run_one warmup humaneval "$DATA/humaneval_30.jsonl"
run_one fixed  mtbench   "$DATA/mtbench_30.jsonl"
run_one warmup mtbench   "$DATA/mtbench_30.jsonl"

# ---- Side-by-side summary ----
echo
echo "============================================================"
echo "RESULTS"
echo "============================================================"
python3 << 'PY'
import json
print(f"{'task':<10} {'sched':<8} {'tok/s':>7} {'acc':>6} {'r0':>6} {'r2+':>6} {'J/tok':>7} {'W':>6}")
print("-" * 60)
gains = {}
for task in ["gsm8k", "humaneval", "mtbench"]:
    rows = {}
    for sched in ["fixed", "warmup"]:
        try:
            s = json.load(open(f"/home/jetson/b3_results/W_{sched}_g3_{task}.json"))["summary"]
            rows[sched] = s
            acc = f"{s['accuracy']:.2f}" if s['accuracy'] is not None else "  -"
            r0 = f"{s['round_0_accept']:.2f}" if s['round_0_accept'] is not None else "  -"
            r2 = f"{s['round_2plus_accept']:.2f}" if s['round_2plus_accept'] is not None else "  -"
            print(f"{task:<10} {sched:<8} {s['agg_tok_s']:>7.2f} {acc:>6} {r0:>6} {r2:>6} "
                  f"{s['joules_per_token']:>7.3f} {s['avg_watts']:>6.2f}")
        except Exception as e:
            print(f"{task:<10} {sched:<8} ERROR: {e}")
    if "fixed" in rows and "warmup" in rows:
        gain_tps = (rows["warmup"]["agg_tok_s"] - rows["fixed"]["agg_tok_s"]) / rows["fixed"]["agg_tok_s"] * 100
        gain_jpt = (rows["fixed"]["joules_per_token"] - rows["warmup"]["joules_per_token"]) / max(1e-9, rows["fixed"]["joules_per_token"]) * 100
        gains[task] = (gain_tps, gain_jpt)
print()
print("GAINS (warmup vs fixed):")
print(f"{'task':<10} {'Δ tok/s':>10} {'Δ J/tok':>10}")
print("-" * 32)
for task, (g_tps, g_jpt) in gains.items():
    print(f"{task:<10} {g_tps:>+9.1f}%  {g_jpt:>+9.1f}%")
PY

echo
echo "Done. Results in $OUT/W_*"

