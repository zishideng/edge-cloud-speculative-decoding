# Step 1 (Bootstrap) + Step 2 (Fallback) — Runbook

## Part A: patch H200 verify_server (one-time)

```bash
# On H200 login node
cd /data/zliu604/day1_slurm
# copy patch_verify_server.py here, then:
python patch_verify_server.py
# Restart server so /generate is live
scancel -u $USER            # or scancel the serve job id
sbatch slurm_serve.sh
# wait for "Server ready"
tail -f /data/zliu604/specdecode-day1/logs/serve-*.out
```

Verify /generate works (from H200 login node):
```bash
curl -s -X POST http://foscsmlprd03:9090/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt_ids":[128000,9906],"max_tokens":3,"temperature":0.0}' | python3 -m json.tool
# Should return token_ids list of length 3
```

## Part B: deploy client files (Jetson)
Copy to `~/Downloads/day4b_jetson/`:
- `verifier_ext.py`
- `edge_client_smart.py`
- `bench_smart.py`

(make sure SSH tunnel localhost:9090 → H200 is up)

## Part C: ablation matrix (GSM8K first, ~40 min)

Each run 30 samples. 15W mode (`sudo nvpmodel -m 0 && sudo jetson_clocks`).

```bash
cd ~/Downloads/day4b_jetson
D=~/Downloads/day3_jetson/gsm8k_test_50.jsonl
O=~/b3_results

# base: plain edge-cloud SD γ=2 (no bootstrap, no fallback)
python bench_smart.py --bootstrap 0 --fallback-k 0 --gamma 2 --task gsm8k \
    --data $D --n 30 --profile-energy --out $O/S_base_gsm8k.json

# +bootstrap (skip round 0, H200 generates first 2 tokens)
python bench_smart.py --bootstrap 2 --fallback-k 0 --gamma 2 --task gsm8k \
    --data $D --n 30 --profile-energy --out $O/S_boot_gsm8k.json

# +fallback (switch to cloud if acceptance<0.65 after 3 rounds)
python bench_smart.py --bootstrap 0 --fallback-k 3 --fallback-thresh 0.65 --gamma 2 --task gsm8k \
    --data $D --n 30 --profile-energy --out $O/S_fb_gsm8k.json

# full system
python bench_smart.py --bootstrap 2 --fallback-k 3 --fallback-thresh 0.65 --gamma 2 --task gsm8k \
    --data $D --n 30 --profile-energy --out $O/S_full_gsm8k.json
```

## Part D: MT-Bench (where fallback should shine — acceptance 72.7%)

```bash
D=~/Downloads/day3_jetson/mtbench_30.jsonl
# base vs full — fallback should help a lot here
python bench_smart.py --bootstrap 0 --fallback-k 0 --gamma 2 --task mtbench \
    --data $D --n 30 --profile-energy --out $O/S_base_mtbench.json
python bench_smart.py --bootstrap 2 --fallback-k 3 --fallback-thresh 0.70 --gamma 2 --task mtbench \
    --data $D --n 30 --profile-energy --out $O/S_full_mtbench.json
```

## Compare
```bash
python3 << 'PY'
import json, glob
for f in sorted(glob.glob("/home/jetson/b3_results/S_*.json")):
    s=json.load(open(f))["summary"]
    acc=f"{s['accuracy']:.2f}" if s['accuracy'] is not None else "  -"
    print(f"{s['tag']:<22} tok/s={s['agg_tok_s']:6.2f} lat={s['avg_latency_s']:6.1f} "
          f"acc={acc} fb_rate={s['fallback_rate']:.0%} J/tok={s['joules_per_token']:.3f}")
PY
```

## Expected
- **+bootstrap**: small latency win (skip worst round). GSM8K maybe +2-4%.
- **+fallback on GSM8K**: minimal (acceptance already high 80%, few fall back).
- **+fallback on MT-Bench**: BIG win — ~25% of requests fall back to 162 tok/s
  cloud AR instead of 10 tok/s edge. Expect avg tok/s to jump significantly.
- **full system**: best latency, especially on mixed/low-acceptance workloads.

The headline result should be MT-Bench: full system >> base.

## Tuning notes
- If fallback_rate=0 on MT-Bench, lower --fallback-thresh won't help; raise it
  (more requests fall back). Try 0.75.
- If fallback_rate=100%, threshold too high — you're sending everything to cloud.
  The sweet spot routes the genuinely-bad requests only.
- bootstrap M=1 or 2; M>2 wastes cloud compute on tokens edge could handle.
