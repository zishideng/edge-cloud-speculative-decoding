# Warmup-Aware SD — Runbook

## Files (copy to `~/Downloads/day4b_jetson/`)
- `edge_client_warmup.py`
- `bench_warmup.py`

## Quick smoke (2 min)
```bash
cd ~/Downloads/day4b_jetson
python bench_warmup.py --schedule warmup --gamma 3 --task gsm8k \
    --data ~/Downloads/day3_jetson/gsm8k_test_50.jsonl --n 5 \
    --out /tmp/smoke.json
```
Look at `round_profile`: round 0 γ should be 1, round 1 should be 2, round 2+ = 3.

## Main experiment (Jetson on 15W mode, ~75 min total)

```bash
sudo nvpmodel -m 0 && sudo jetson_clocks && sleep 5

# GSM8K: fixed vs warmup
python bench_warmup.py --schedule fixed --gamma 3 --task gsm8k \
    --data ~/Downloads/day3_jetson/gsm8k_test_50.jsonl --n 30 \
    --profile-energy \
    --out ~/b3_results/W_fixed_g3_gsm8k.json

python bench_warmup.py --schedule warmup --gamma 3 --task gsm8k \
    --data ~/Downloads/day3_jetson/gsm8k_test_50.jsonl --n 30 \
    --profile-energy \
    --out ~/b3_results/W_warmup_g3_gsm8k.json

# HumanEval
python bench_warmup.py --schedule fixed --gamma 3 --task humaneval \
    --data ~/Downloads/day3_jetson/humaneval_30.jsonl --n 30 \
    --profile-energy \
    --out ~/b3_results/W_fixed_g3_humaneval.json

python bench_warmup.py --schedule warmup --gamma 3 --task humaneval \
    --data ~/Downloads/day3_jetson/humaneval_30.jsonl --n 30 \
    --profile-energy \
    --out ~/b3_results/W_warmup_g3_humaneval.json

# MT-Bench
python bench_warmup.py --schedule fixed --gamma 3 --task mtbench \
    --data ~/Downloads/day3_jetson/mtbench_30.jsonl --n 30 \
    --profile-energy \
    --out ~/b3_results/W_fixed_g3_mtbench.json

python bench_warmup.py --schedule warmup --gamma 3 --task mtbench \
    --data ~/Downloads/day3_jetson/mtbench_30.jsonl --n 30 \
    --profile-energy \
    --out ~/b3_results/W_warmup_g3_mtbench.json
```

## Expected wins

| Task | fixed γ=3 tok/s | warmup tok/s | Expected gain |
|---|---|---|---|
| GSM8K (long output ~220 tok) | 15.6 | ~15.9 | +2% |
| HumanEval (~130 tok) | ~14-15 | ~15-16 | +5-8% |
| MT-Bench (long, ~270 tok) | ~10 | ~10.3 | +3% |

Larger gain expected on shorter outputs — warmup fixed overhead amortizes less.

## What to check after each run
```bash
# Round 0 should now be γ=1 (not γ=3)
python3 -c "
import json
d = json.load(open('~/b3_results/W_warmup_g3_gsm8k.json'.replace('~', '/home/jetson')))
print('round_profile:')
for k, v in list(d['round_profile'].items())[:5]:
    print(f'  round {k}: accept={v[\"mean_accept\"]:.3f}, n={v[\"n\"]}')
"
```

## Side-by-side comparison (after both runs)
```bash
python3 << 'PY'
import json
for task in ["gsm8k", "humaneval", "mtbench"]:
    f = json.load(open(f"/home/jetson/b3_results/W_fixed_g3_{task}.json"))
    w = json.load(open(f"/home/jetson/b3_results/W_warmup_g3_{task}.json"))
    print(f"\n=== {task} ===")
    for d, label in [(f, "fixed"), (w, "warmup")]:
        s = d["summary"]
        print(f"  {label}:  tok/s={s['agg_tok_s']:.2f}  "
              f"acc={s['accuracy']}  "
              f"r0_accept={s['round_0_accept']:.3f}  "
              f"r2+_accept={s['round_2plus_accept']:.3f}  "
              f"J/tok={s['joules_per_token']:.3f}")
PY
```
