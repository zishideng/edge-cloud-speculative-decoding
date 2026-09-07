# RUNBOOK — extra model pairs (`qwen3`, `deepseek`)

Goal: reproduce the paper's core measurements on two more edge–cloud pairs so
the generalization claim (cold-start and task-dependence) holds
beyond the Llama-3.1-8B/1B pair, **and** report metrics that line up with
Venkatesha et al. 2025 (the early-exit FSD paper, `cited_pdfs/5014_...pdf`).

Both pairs fit a **single H200** and keep the **edge draft ≈1B** so the 8 GB
Orin Nano does not OOM. No tensor parallelism, no quantization needed.

| key        | draft (edge / Jetson)              | target (cloud / H200, 1 GPU)              | vocab  | eos    |
|------------|------------------------------------|-------------------------------------------|--------|--------|
| `qwen3`    | Qwen3-0.6B Q8_0 (~639 MB)           | Qwen3-32B bf16 (~64 GB)                    | 151936 | 151645 |
| `deepseek` | DeepSeek-R1-Distill-Qwen-1.5B Q4 (~1.1 GB) | DeepSeek-R1-Distill-Qwen-32B bf16 (~64 GB) | 151936 | 151643 |

Two caveats baked into `models.yaml`:

- **`deepseek` `strict_vocab: false`** — the 1.5B and 32B distills share the
  same tokenizer (token ids match) but their embedding `vocab_size` may differ
  (151936 vs 152064). That is padding, not a tokenizer mismatch, so SD is
  correct; the flag downgrades the vocab check from fatal to a warning.
- **Both are reasoning-ish models.** Qwen3 has a `<think>` thinking mode (turn
  it **off** for SD runs); DeepSeek distills always emit reasoning chains
  (outputs are long — compare throughput *within* a pair, not across pairs).

> Confirm the two GGUF filenames against the live HF repos before downloading;
> community repos occasionally rename files.

---

## 0. What to copy where (scp)

You already have the repo deployed. Only the **changed files** need to go out.
Run these from the repo root on your laptop (adjust the local path if needed).

```bash
# ---- to the CLOUD (H200 login node) ----
CLOUD=zliu604@foscsmlprd03.its.auckland.ac.nz
scp models.yaml              $CLOUD:/data/zliu604/models.yaml
scp cloud/verify_server.py   $CLOUD:/data/zliu604/cloud/verify_server.py
scp cloud/slurm_serve.sh     $CLOUD:/data/zliu604/cloud/slurm_serve.sh
# (cloud/bench_one.py and cloud/env.sh are unchanged — only re-copy if missing)

# ---- to the JETSON (edge) ----
JET=jetson@192.168.50.19
scp models.yaml              $JET:~/specdecode/models.yaml
scp src/bench_edge_cloud.py  $JET:~/specdecode/src/bench_edge_cloud.py
scp src/bench_smart.py       $JET:~/specdecode/src/bench_smart.py
scp edge/start_server.sh     $JET:~/specdecode/edge/start_server.sh
scp edge/download_model.sh   $JET:~/specdecode/edge/download_model.sh
# (src/model_config.py is unchanged; the strict flag is read from models.yaml)
```

Rule of thumb: **the cloud only runs the target (vLLM verify server); the Jetson
runs everything else** (draft server + the bench control loop). `models.yaml`
must exist on **both** sides.

---

## 1. Cloud: launch the target (H200, Slurm) — pick ONE pair at a time

`slurm_serve.sh` reads `tp/dtype/quantization/gpu_memory_utilization` from the
pair's `models.yaml` entry; both pairs are `tp:1`.

```bash
ssh $CLOUD
cd /data/zliu604

MODEL_CONFIG=qwen3    sbatch cloud/slurm_serve.sh     # or:
MODEL_CONFIG=deepseek sbatch cloud/slurm_serve.sh

squeue -u zliu604                                     # find the job
tail -f specdecode-day1/logs/serve-<jobid>.out        # wait for "Server ready at <node>:9090"
```

First load of a 32B checkpoint (download + weights) can take several minutes.

> **Node / driver gotcha:** this conda env's vLLM is built for **CUDA 13**,
> which needs GPU driver **≥ 580**. If Slurm lands you on an older node
> (`nvidia-smi` shows CUDA 12.x / driver 575.x), vLLM fails to import with
> `ImportError: libcudart.so.13: cannot open shared object file`. Fix: request a
> node whose driver supports CUDA 13 (don't fight it on a 575 node), or build a
> separate CUDA-12 vLLM env for that node.

---

## 2. Open the tunnel (from the Jetson)

```bash
ssh $JET
ssh -N -L 9090:<node>.its.auckland.ac.nz:9090 \
    zliu604@foscsmlprd03.its.auckland.ac.nz &
# for me
ssh -N -f -L 9090:localhost:9090 zliu604@foscsmlprd03.its.auckland.ac.nz
```

`<node>` is the compute node printed in the ready line.

---

## 3. Jetson: download + launch the draft (one pair at a time)

**Step 1 — download the draft GGUF.** Verify the filename actually exists in the
repo first (a 404 page saved as `.gguf` is the #1 trap):

```bash
# qwen3 — the OFFICIAL Qwen repo ships only Q8_0 (there is NO Q4_K_M):
REPO=Qwen/Qwen3-0.6B-GGUF MODEL_FILE=Qwen3-0.6B-Q8_0.gguf MINSIZE=600000000 \
  bash edge/download_model.sh
# deepseek (bartowski has Q4_K_M, ~1.12 GB):
REPO=bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF \
MODEL_FILE=DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf MINSIZE=1000000000 \
  bash edge/download_model.sh
# ALWAYS sanity-check the magic bytes — must print GGUF, not 'Entr'/'<htm':
head -c 4 ~/specdecode/models/Qwen3-0.6B-Q8_0.gguf; echo
```

**Step 2 — launch the draft.** `start_server.sh` picks the model by its
ARGUMENT (`llama` | `qwen3` | `deepseek`). Never edit or uncomment lines to
switch models — doing that is what caused the earlier infinite-recursion crash.
Use `nohup` so the server survives an SSH logout:

```bash
pkill -9 -f llama-server ; sleep 4 ; pgrep -af llama-server   # must be EMPTY before relaunch
nohup bash edge/start_server.sh deepseek > ~/draft.log 2>&1 &
#   ... start_server.sh qwen3      # the Qwen pair (needs a newer llama.cpp, see note)
#   ... start_server.sh llama      # the reference pair
sleep 8
tail -8 ~/draft.log               # expect "HTTP server is listening", and NO "error loading model"
pgrep -af llama-server            # confirm the -m path is the pair you wanted
```

The script auto-checks the GGUF magic, sets `LD_LIBRARY_PATH`, and cannot
recurse. To confirm *which* model loaded, read the `-m` path from `pgrep` — do
**not** rely on `curl /props | grep n_vocab`, because this llama.cpp build does
not expose `n_vocab`.

**Gotchas learned the hard way:**

- **Qwen3 needs a newer llama.cpp.** Build b5050 aborts with
  `unknown model architecture: 'qwen3'`. Upgrade and rebuild (Orin = sm_87):
  ```bash
  cd ~/specdecode/llama.cpp && git fetch --all && git checkout master && git pull
  rm -rf build && cmake -B build -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=87
  cmake --build build --config Release -j6 --target llama-server
  ```
  DeepSeek-R1-Distill-Qwen is **qwen2** architecture and runs on b5050 as-is.
- **Crash in `cudaMemGetInfo` / core dump** = a previous llama-server is still
  holding the GPU. `pkill -9 -f llama-server; sleep 4` until `pgrep` is empty,
  then relaunch.
- **`libllama.so: cannot open shared object file`** = `LD_LIBRARY_PATH` missing.
  The script sets it; if you run the binary directly, prefix the command with
  `env LD_LIBRARY_PATH=$HOME/specdecode/llama.cpp/build/bin:$LD_LIBRARY_PATH`.
- **Always `nohup`** (or tmux). A bare `&` dies on SSH logout (SIGHUP).

Set the power mode first so energy numbers match the paper:

```bash
sudo bash edge/power_mode.sh 15W
```

---

## 4. Smoke test (5 samples, with vocab validation) — run from `src/`

```bash
cd ~/specdecode/src
python bench_edge_cloud.py --verifier remote --remote-url http://localhost:9090 \
    --model-config qwen3 --gamma 2 --n 5 \
    --data ../edge/data/gsm8k_test_50.jsonl --out /tmp/qwen3_smoke.json
# PASS = "[model_config] vocab OK" (or a strict_vocab warning for deepseek)
#        AND acceptance_rate > 0
```

If acceptance ≈ 0 with vocab OK → wrong eos / chat format. For `qwen3` that's
almost always **thinking mode still on** (see §7).

---

## 5. The experiment ladder (swap `qwen3` ⇄ `deepseek` and the filenames)

`bench_edge_cloud.py` takes `--model-config`; `bench_smart.py` takes `--config` with `MODEL_PAIR`.

**(a) Baseline + acceptance + cold-start + τ.** `bench_edge_cloud.py` now writes
`tau_tokens_per_verify` (the Venkatesha τ) into the summary, plus per-round
acceptance in each record's `rounds` field (the cold-start curve):

```bash
python bench_edge_cloud.py --verifier remote --remote-url http://localhost:9090 \
    --model-config qwen3 --gamma 2 --n 50 \
    --data ../edge/data/gsm8k_test_50.jsonl --out ../results/B3_qwen3_g2.json
# repeat with --gamma 3 to confirm gamma=2 still wins
```

**(b) Per-task acceptance** (task-dependence spread):

```bash
for T in humaneval_30 mtbench_30; do
  python bench_edge_cloud.py --verifier remote --remote-url http://localhost:9090 \
      --model-config qwen3 --gamma 2 --n 30 \
      --data ../edge/data/${T}.jsonl --out ../results/B3_qwen3_g2_${T}.json
done
```

**(c) Current quality-constrained experiments.**

Use `python -m edge.bench_smart --mode real --config configs/my-experiment.json`
from the repository root. Set `MODEL_PAIR`, `DRAFT_URL`, `CLOUD_URL` and quality/window parameters.
The A/B/C/Proposed comparisons are described in [EXPERIMENT_SYSTEM.md](EXPERIMENT_SYSTEM.md).

---

## 7. Qwen3 thinking-mode (must disable for `qwen3`)

Qwen3 defaults to emitting `<think>…</think>`. Disable it for SD runs:
`apply_chat_template(..., enable_thinking=False)` or append `/no_think` to the
prompt. Draft and target must use the **same** setting or acceptance craters.

---

## 8. Collect results

```bash
cd ~/specdecode/src && python make_results_index.py   # -> results/RESULTS_INDEX.md
```

Headline numbers per pair: round-0 vs steady acceptance (`rounds` in
`B3_<pair>_g2.json`), `tau_tokens_per_verify`, per-task `acceptance_rate`,
and the new A/B/C/Proposed latency, throughput and quality tables.

---

## 9. Troubleshooting

| symptom | fix |
|---|---|
| vLLM OOM on 32B (1 GPU) | lower `max_model_len` to 2048 or raise `gpu_memory_utilization` toward 0.95 in `models.yaml`. |
| `VOCAB MISMATCH` abort on `deepseek` | expected if 32B reports 152064 — `strict_vocab: false` already downgrades it to a warning; make sure the flag is present. |
| acceptance ≈ 0, vocab OK (`qwen3`) | thinking mode still on (§7). |
| acceptance ≈ 0, vocab OK (`deepseek`) | draft/target chat templates differ; both must use the DeepSeek R1 template. |
| `llama-server` slow but not OOM | normal for first request (KV warmup) — that's the cold-start we measure. |
