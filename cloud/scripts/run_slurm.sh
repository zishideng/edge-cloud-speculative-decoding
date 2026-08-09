#!/bin/bash
#SBATCH --job-name=specdec_day1
#SBATCH --output=/data/zliu604/specdecode-day1/logs/slurm-%j.out
#SBATCH --error=/data/zliu604/specdecode-day1/logs/slurm-%j.err
#SBATCH --time=12:00:00
#SBATCH --gres=gpu:1
# NOTE: you may need to add --partition=... or --account=... for your cluster.
#       Ask the admin or check `sinfo` / `sacctmgr show user`.

set -e

# ---- Bring in our env ------------------------------------------------------
# Resolve the script dir so this works regardless of where you sbatch from.
SCRIPT_DIR="/data/zliu604/cloud"
# shellcheck disable=SC1091
source "$SCRIPT_DIR/env.sh"

cd "$PROJECT_ROOT"

# ---- Diagnostics -----------------------------------------------------------
echo "============================================================"
echo "Job ID:      $SLURM_JOB_ID"
echo "Node:        $SLURM_NODELIST"
echo "GPU:         $CUDA_VISIBLE_DEVICES"
echo "Started:     $(date)"
echo "============================================================"

DATA="$PROJECT_ROOT/data/gsm8k_test_200.jsonl"
if [[ ! -f "$DATA" ]]; then
    echo "ERROR: $DATA not found. Run 'python download_gsm8k.py' on a login node first."
    exit 1
fi

# ---- B1: Autoregressive ----------------------------------------------------
echo
echo "##### B1 — Autoregressive #####"
python "$SCRIPT_DIR/bench_one.py" \
    --mode ar \
    --target "meta-llama/Llama-3.1-8B-Instruct" \
    --data "$DATA" \
    --out "$PROJECT_ROOT/results/B1_AR.json" \
    --tag B1_AR

# ---- B2: Speculative Decoding ----------------------------------------------
# Note: each `python` invocation starts a fresh process → GPU is fully freed
# between the two baselines. Important on H200 where leftover CUDA graphs
# from B1 would otherwise sit in VRAM during B2 startup.
echo
echo "##### B2 — Speculative Decoding (γ=5) #####"
for gamma in 3 5 7 10; do
    python "$SCRIPT_DIR/bench_one.py" \
        --mode sd \
        --target "meta-llama/Llama-3.1-8B-Instruct" \
        --draft  "meta-llama/Llama-3.2-1B-Instruct" \
        --gamma $gamma \
        --data "$DATA" \
        --out "$PROJECT_ROOT/results/B2_SD_g${gamma}.json" \
        --tag B2_SD_g${gamma}
done
# ---- Compare ---------------------------------------------------------------
echo
echo "##### Building comparison.md #####"
python "$SCRIPT_DIR/summarize.py"

echo
echo "Done at $(date). Open $PROJECT_ROOT/results/comparison.md"
