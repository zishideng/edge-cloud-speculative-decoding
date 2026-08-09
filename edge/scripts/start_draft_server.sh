#!/usr/bin/env bash
# Launch the edge draft model (llama-server) for a chosen model pair.
#
# Usage:
#   bash start_server.sh <pair>
#     <pair> = llama | qwen3 | deepseek      (or a direct path to a .gguf)
#
# Examples:
#   bash start_server.sh deepseek                         # foreground
#   CTX=2048 bash start_server.sh deepseek                # smaller context
#   nohup bash start_server.sh deepseek >~/draft.log 2>&1 &   # survive ssh logout
#
# Switch models by changing the ARGUMENT, never by editing/uncommenting lines
# below. There is no line in this script that calls the script itself, so it
# can never recurse.
set -euo pipefail

WORK_ROOT="${WORK_ROOT:-/home/jetson/specdecode}"
LLAMA_BIN="$WORK_ROOT/llama.cpp/build/bin/llama-server"
MODELS_DIR="$WORK_ROOT/models"

# --- model registry: pair name -> GGUF filename (edit filenames here only) ---
declare -A GGUF=(
  [llama]="Llama-3.2-1B-Instruct-Q4_K_M.gguf"
  [qwen3]="Qwen3-0.6B-Q8_0.gguf"
  [qwen25]="qwen2.5-0.5b-instruct-q4_k_m.gguf"
  [deepseek]="DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf"
)

PAIR="${1:-}"
if [[ -z "$PAIR" ]]; then
  echo "Usage: bash start_server.sh <pair>"
  echo "  <pair> = one of: ${!GGUF[*]}   (or a path to a .gguf file)"
  exit 2
fi

# Resolve the model path: a known pair name, or a direct .gguf path.
if [[ -n "${GGUF[$PAIR]:-}" ]]; then
  MODEL="$MODELS_DIR/${GGUF[$PAIR]}"
elif [[ -f "$PAIR" ]]; then
  MODEL="$PAIR"
else
  echo "ERROR: unknown pair '$PAIR'."
  echo "       known pairs: ${!GGUF[*]}   (or pass a .gguf path)"
  exit 2
fi

PORT="${PORT:-8080}"
HOST="${HOST:-0.0.0.0}"     # 0.0.0.0 so VPN clients (the cloud) can reach us
NGL="${NGL:-99}"            # GPU layers; 99 = all on GPU
CTX="${CTX:-4096}"          # context window; CTX=2048 if RAM is tight

[[ -x "$LLAMA_BIN" ]] || { echo "ERROR: $LLAMA_BIN not found. Build llama.cpp first."; exit 1; }
[[ -f "$MODEL" ]]     || { echo "ERROR: model not found: $MODEL  (download it first)."; exit 1; }

# Fail loudly on a bad / half-downloaded file (e.g. an HTML 404 saved as .gguf).
MAGIC="$(head -c 4 "$MODEL" 2>/dev/null || true)"
if [[ "$MAGIC" != "GGUF" ]]; then
  echo "ERROR: $MODEL is not a valid GGUF (magic='$MAGIC', expected 'GGUF')."
  echo "       The download is corrupt or a 404 page — re-download it."
  exit 1
fi

echo "==> pair:   $PAIR"
echo "==> model:  $MODEL"
echo "==> serve:  http://$HOST:$PORT   (n-gpu-layers=$NGL, ctx=$CTX)"
echo

# Make llama.cpp's shared libs (libllama.so, libggml*.so) findable.
export LD_LIBRARY_PATH="$WORK_ROOT/llama.cpp/build/bin:${LD_LIBRARY_PATH:-}"

exec "$LLAMA_BIN" \
  -m "$MODEL" \
  --host "$HOST" --port "$PORT" \
  --n-gpu-layers "$NGL" --ctx-size "$CTX" \
  --parallel 1 --cont-batching --metrics
