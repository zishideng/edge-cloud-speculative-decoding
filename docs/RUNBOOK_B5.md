# B5 + Multi-task — Runbook

## Files (copy to Jetson `~/Downloads/day4b_jetson/`)
- `edge_client_b5.py`
- `bench_b5.py`
- `fetch_extra_datasets.py`

## Prereqs
- C3 done. You have `~/b3_results/C3_lookup.json`
- H200 verify server up, SSH tunnel localhost:9090
- llama-server on 8080

## Step 1: fetch extra datasets (5 min)
```bash
cd ~/Downloads/day4b_jetson
python fetch_extra_datasets.py --n 30 \
    --mtbench-out ~/Downloads/day3_jetson/mtbench_30.jsonl \
    --humaneval-out ~/Downloads/day3_jetson/humaneval_30.jsonl
```

## Step 2: inspect lookup table
```bash
cat ~/b3_results/C3_lookup.json
```
Likely picks:
- SLO 5s  → MAXN γ=2 (fastest)
- SLO 15s → 15W γ=2 (best J/tok)
- SLO 30s → 15W γ=2 or 7W γ=2

## Step 3: B5 GSM8K — main experiment

Run twice with two SLOs to show routing works:

```bash
# Fast SLO → router picks MAXN γ=2
sudo nvpmodel -m 2
sudo jetson_clocks
sleep 5
python bench_b5.py \
    --lookup ~/b3_results/C3_lookup.json \
    --slo 13 --power-mode MAXN \
    --task gsm8k \
    --data ~/Downloads/day3_jetson/gsm8k_test_50.jsonl \
    --n 30 \
    --out ~/b3_results/B5_gsm8k_slo13.json

# Energy-tight SLO → router picks 15W γ=2
sudo nvpmodel -m 0
sleep 5
python bench_b5.py \
    --lookup ~/b3_results/C3_lookup.json \
    --slo 15 --power-mode 15W \
    --task gsm8k \
    --data ~/Downloads/day3_jetson/gsm8k_test_50.jsonl \
    --n 30 \
    --out ~/b3_results/B5_gsm8k_slo15.json
```

## Step 4: MT-Bench (generalization)
```bash
# Use 15W (energy mode)
sudo nvpmodel -m 0
sleep 5
python bench_b5.py \
    --lookup ~/b3_results/C3_lookup.json \
    --slo 15 --power-mode 15W \
    --task mtbench \
    --data ~/Downloads/day3_jetson/mtbench_30.jsonl \
    --n 30 \
    --out ~/b3_results/B5_mtbench_slo15.json
```

## Step 5: HumanEval (generalization)
```bash
python bench_b5.py \
    --lookup ~/b3_results/C3_lookup.json \
    --slo 15 --power-mode 15W \
    --task humaneval \
    --data ~/Downloads/day3_jetson/humaneval_30.jsonl \
    --n 30 \
    --out ~/b3_results/B5_humaneval_slo15.json
```

## What to vet
Each run reports `routed_config`. Confirm:
- The `gamma` field matches what router picked
- `power_mode` warning is absent (Jetson actually set to that mode)
- `agg_tok_s`, `joules_per_token` on the order of C3 grid cells

## Expected key paper numbers

| Run | Expected tok/s | J/tok | vs B3 baseline |
|---|---|---|---|
| B5 gsm8k SLO=13s MAXN | ~17 | ~0.47 | +13% tok/s, -5% J/tok |
| B5 gsm8k SLO=15s 15W | ~15 | ~0.45 | -2% tok/s, **-9% J/tok** |
| B5 mtbench 15W | ~12-14 | varies | Genralizes? |
| B5 humaneval 15W | ~14-16 | varies | Long code outputs |

The B5 SLO=15s 15W run is the **headline result** — best J/tok by routing.

## Total time
~50-60 min for all 4 runs (4 × ~12 min each).
