#!/usr/bin/env bash
# run_prefetch_all.sh — sync vs prefetch across 3 tasks (Jetson, 15W).
# ~75 min. Pre-set: sudo nvpmodel -m 0 && sudo jetson_clocks
set -e
cd ~/Downloads/day4b_jetson
source /home/jetson/specdecode/venv/bin/activate

curl -sf http://localhost:8080/health >/dev/null || { echo "llama-server down"; exit 1; }
curl -sf http://localhost:9090/health >/dev/null || { echo "verify server down"; exit 1; }
echo "==> servers OK"; sudo nvpmodel -q | head -2

OUT=~/b3_results; mkdir -p "$OUT"; DATA=~/Downloads/day3_jetson; N=30

run() {
    local mode=$1 task=$2 data=$3
    local out="$OUT/P_${mode}_${task}.json"
    [[ -f "$out" ]] && { echo "[skip] $out"; return; }
    echo; echo "==> $mode × $task"
    python bench_prefetch.py --mode "$mode" --gamma 3 --task "$task" \
        --data "$data" --n "$N" --profile-energy --out "$out"
}

run sync     gsm8k     "$DATA/gsm8k_test_50.jsonl"
run prefetch gsm8k     "$DATA/gsm8k_test_50.jsonl"
run sync     humaneval "$DATA/humaneval_30.jsonl"
run prefetch humaneval "$DATA/humaneval_30.jsonl"
run sync     mtbench   "$DATA/mtbench_30.jsonl"
run prefetch mtbench   "$DATA/mtbench_30.jsonl"

echo; echo "============ RESULTS ============"
python3 << 'PY'
import json
print(f"{'task':<10}{'mode':<9}{'tok/s':>7}{'lat':>7}{'hit%':>6}{'acc':>6}{'J/tok':>7}")
print("-"*52)
g={}
for task in ["gsm8k","humaneval","mtbench"]:
    rows={}
    for mode in ["sync","prefetch"]:
        try:
            s=json.load(open(f"/home/jetson/b3_results/P_{mode}_{task}.json"))["summary"]
            rows[mode]=s
            acc=f"{s['accuracy']:.2f}" if s['accuracy'] is not None else "  -"
            print(f"{task:<10}{mode:<9}{s['agg_tok_s']:>7.2f}{s['avg_latency_s']:>7.1f}"
                  f"{s['prefetch_hit_rate']*100:>5.0f}%{acc:>6}{s['joules_per_token']:>7.3f}")
        except Exception as e: print(f"{task:<10}{mode:<9} ERR {e}")
    if "sync" in rows and "prefetch" in rows:
        gt=(rows["prefetch"]["agg_tok_s"]-rows["sync"]["agg_tok_s"])/rows["sync"]["agg_tok_s"]*100
        gj=(rows["sync"]["joules_per_token"]-rows["prefetch"]["joules_per_token"])/max(1e-9,rows["sync"]["joules_per_token"])*100
        g[task]=(gt,gj)
print("\nGAINS (prefetch vs sync):")
for t,(gt,gj) in g.items(): print(f"  {t:<10} Δtok/s={gt:+.1f}%  ΔJ/tok={gj:+.1f}%")
PY
echo; echo "Done."
