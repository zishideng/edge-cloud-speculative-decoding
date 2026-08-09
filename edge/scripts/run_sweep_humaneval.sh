#!/usr/bin/env bash
# run_sweep_humaneval.sh — fallback threshold sweep (GSM8K) + HumanEval base/fallback.
# Jetson, 15W. ~70 min. Pre: sudo nvpmodel -m 0 && sudo jetson_clocks
set -e
cd ~/Downloads/day4b_jetson
source /home/jetson/specdecode/venv/bin/activate

curl -sf http://localhost:8080/health >/dev/null || { echo "llama-server down"; exit 1; }
curl -sf http://localhost:9090/health >/dev/null || { echo "verify server down"; exit 1; }
echo "==> servers OK"; sudo nvpmodel -q | head -2

O=~/b3_results; mkdir -p "$O"
GSM=~/Downloads/day3_jetson/gsm8k_test_50.jsonl
HE=~/Downloads/day3_jetson/humaneval_30.jsonl
N=30

run() {  # out_tag bootstrap fk thresh task data
    local out="$O/$1.json"
    [[ -f "$out" ]] && { echo "[skip] $out"; return; }
    echo; echo "==> $1"
    python bench_smart.py --bootstrap $2 --fallback-k $3 --fallback-thresh $4 \
        --gamma 2 --task $5 --data $6 --n $N --profile-energy --out "$out"
}

# --- GSM8K fallback threshold sweep ---
run S_fb_t055_gsm8k 0 3 0.55 gsm8k "$GSM"
run S_fb_t065_gsm8k 0 3 0.65 gsm8k "$GSM"
run S_fb_t070_gsm8k 0 3 0.70 gsm8k "$GSM"
run S_fb_t075_gsm8k 0 3 0.75 gsm8k "$GSM"

# --- HumanEval base vs fallback ---
run S_base_humaneval 0 0 0.0  humaneval "$HE"
run S_fb_humaneval   0 3 0.65 humaneval "$HE"

echo; echo "================ RESULTS ================"
python3 << 'PY'
import json, glob
rows=[]
for f in sorted(glob.glob("/home/jetson/b3_results/S_*.json")):
    s=json.load(open(f))["summary"]
    acc=f"{s['accuracy']:.2f}" if s['accuracy'] is not None else "  - "
    rows.append((s['tag'], s['agg_tok_s'], s['avg_latency_s'], acc,
                 s['fallback_rate'], s['joules_per_token'],
                 s.get('fallback_thresh')))
print(f"{'tag':<24}{'tok/s':>7}{'lat':>7}{'acc':>6}{'fb%':>6}{'J/tok':>8}{'thr':>6}")
print("-"*65)
for t,tps,lat,acc,fb,jpt,thr in rows:
    print(f"{t:<24}{tps:>7.2f}{lat:>7.1f}{acc:>6}{fb*100:>5.0f}%{jpt:>8.3f}{str(thr):>6}")

# Highlight best GSM8K threshold
gsm=[(t,tps,jpt) for t,tps,lat,acc,fb,jpt,thr in rows if "t0" in t and "gsm8k" in t]
if gsm:
    best=max(gsm, key=lambda x:x[1])
    print(f"\nBest GSM8K fallback threshold: {best[0]} @ {best[1]:.2f} tok/s, {best[2]:.3f} J/tok")
PY
echo; echo "Done."
