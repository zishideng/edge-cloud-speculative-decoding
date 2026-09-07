#!/usr/bin/env bash
#SBATCH --job-name=spec_verify
#SBATCH --output=/data/zliu604/specdecode-day1/logs/serve-%j.out
#SBATCH --error=/data/zliu604/specdecode-day1/logs/serve-%j.err
#SBATCH --gres=gpu:1
#SBATCH --time=12:00:00

# If the cluster rejects 8h jobs, drop to 04:00:00 or 02:00:00 and re-sbatch
# at the start of each session. We aim for one long server per session.
#
# GPU count: 1 GPU is enough for every current pair (8B, Qwen3-32B, and the
# DeepSeek-R1-Distill-Qwen-32B target all fit one 80 GB H200 in bf16). If you
# ever add a 70B+ bf16 target, request 2 GPUs (sbatch --gres=gpu:2) and set
# tp: 2 in models.yaml, or set quantization: fp8 to keep it on one card.

set -e
SCRIPT_DIR="/data/zliu604/cloud"
source "$SCRIPT_DIR/env.sh"
cd "$PROJECT_ROOT"

PORT=9090
READY="$PROJECT_ROOT/logs/serve-${SLURM_JOB_ID}.ready"
rm -f "$READY"

echo "============================================================"
echo "Verify server (Day 4A)"
echo "Job ID:   $SLURM_JOB_ID"
echo "Node:     $SLURM_NODELIST"
echo "Port:     $PORT"
echo "Started:  $(date)"
echo "============================================================"
nvidia-smi || true
echo

# Make sure deps are installed (idempotent; pip is fast when cached)
pip install --quiet fastapi 'uvicorn[standard]' pydantic pyyaml

# Resolve the target model + serving knobs.
# Priority: TARGET env var  >  MODEL_CONFIG looked up in models.yaml.
# There is NO silent default model: if neither is given (or the config is
# wrong) we abort, so a misconfigured run can never quietly serve the wrong
# model. Optional per-pair yaml fields: tp, dtype, quantization, gpu_memory_utilization.
TARGET="${TARGET:-}"
TP="${TP:-}"; DTYPE="${DTYPE:-}"; QUANT="${QUANT:-}"; GPUUTIL="${GPUUTIL:-}"
SRC="TARGET env"

if [[ -z "$TARGET" ]]; then
    if [[ -z "${MODEL_CONFIG:-}" ]]; then
        echo "ERROR: nothing to serve. Set MODEL_CONFIG=<pair> (llama3|qwen3|deepseek|...)" >&2
        echo "       or TARGET=<hf-model-id>. Refusing to default to a model." >&2
        exit 2
    fi
    YAML="${MODELS_YAML:-$SCRIPT_DIR/../models.yaml}"
    [[ -f "$YAML" ]] || { echo "ERROR: models.yaml not found: $YAML" >&2; exit 2; }
    SRC="MODEL_CONFIG=$MODEL_CONFIG ($YAML)"
    # Parameterized python (no shell interpolation into the source): prints one
    # line on success, or a clear message + non-zero exit if the key is missing.
    ROW="$(python3 - "$YAML" "$MODEL_CONFIG" <<'PY' 2>&1
import sys, yaml
path, name = sys.argv[1], sys.argv[2]
reg = yaml.safe_load(open(path)) or {}
cfg = reg.get(name)
if cfg is None:
    sys.exit("model-config '%s' not in %s; available: %s"
             % (name, path, ', '.join(sorted(reg))))
print(cfg['target'], cfg.get('max_model_len', 4096), cfg.get('tp', 1),
      cfg.get('dtype', 'bfloat16'), cfg.get('quantization', 'none'),
      cfg.get('gpu_memory_utilization', 0.85))
PY
)" || { echo "ERROR resolving $SRC: $ROW" >&2; exit 3; }
    read -r TARGET MAXLEN CFG_TP CFG_DTYPE CFG_QUANT CFG_UTIL <<< "$ROW"
    TP="${TP:-$CFG_TP}"; DTYPE="${DTYPE:-$CFG_DTYPE}"
    QUANT="${QUANT:-$CFG_QUANT}"; GPUUTIL="${GPUUTIL:-$CFG_UTIL}"
fi

# Knob defaults: fill in only what neither env nor yaml provided.
MAXLEN="${MAXLEN:-4096}"
TP="${TP:-1}"; DTYPE="${DTYPE:-bfloat16}"; QUANT="${QUANT:-none}"; GPUUTIL="${GPUUTIL:-0.85}"

echo "============================================================"
echo "Target to serve : $TARGET"
echo "  source        : $SRC"
echo "  max_model_len=$MAXLEN  tp=$TP  dtype=$DTYPE  quant=$QUANT  gpu_util=$GPUUTIL"
echo "============================================================"

# Start server. The --ready-file lets us announce when the model is loaded.
python -m cloud.verify_server \
    --target "$TARGET" \
    --host 0.0.0.0 \
    --port "$PORT" \
    --max-model-len "$MAXLEN" \
    --tensor-parallel-size "$TP" \
    --dtype "$DTYPE" \
    --quantization "$QUANT" \
    --gpu-memory-utilization "$GPUUTIL" \
    --ready-file "$READY" &

SERVER_PID=$!

# Poll the ready file for up to 5 minutes
echo "Waiting for model to load..."
for i in $(seq 1 300); do
    if [[ -f "$READY" ]]; then
        IFS=$'\t' read -r NODE PRT < "$READY"
        echo "============================================================"
        echo "Server ready at $NODE:$PRT"
        echo "From login node, smoke-test with:"
        echo "  python $SCRIPT_DIR/test_verify_local.py --host $NODE --port $PRT"
        echo "From Jetson via VPN, smoke-test with:"
        echo "  bash test_from_jetson.sh ${NODE}.its.auckland.ac.nz $PRT"
        echo "============================================================"
        break
    fi
    sleep 1
done

if [[ ! -f "$READY" ]]; then
    echo "ERROR: server did not become ready in 5 minutes."
    kill $SERVER_PID 2>/dev/null
    exit 1
fi

# Wait for the server process. The Slurm job will be killed by --time limit
# (8h), at which point uvicorn shuts down cleanly.
wait $SERVER_PID
