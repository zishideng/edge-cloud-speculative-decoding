#!/usr/bin/env bash
# Download Llama-3.2-1B-Instruct in GGUF Q4_K_M format.
#
# Why this exact model+quant:
#   - Same family as our H200 target (Llama-3.1-8B) → tokenizer matches
#   - 1B fits comfortably in Orin Nano 8GB unified RAM
#   - Q4_K_M = ~770 MB, sweet spot between size and accuracy
#
# Source: bartowski (the de-facto community quantizer, weights match upstream)
set -e

WORK_ROOT="${WORK_ROOT:-/home/jetson/specdecode}"
MODELS_DIR="$WORK_ROOT/models"
mkdir -p "$MODELS_DIR"
cd "$MODELS_DIR"

# Overridable for the other draft GGUFs. Examples:
#   0.6B draft (qwen3 pair):
#     REPO=Qwen/Qwen3-0.6B-GGUF MODEL_FILE=Qwen3-0.6B-Q4_K_M.gguf MINSIZE=300000000 bash download_model.sh
#   1.5B draft (deepseek pair):
#     REPO=bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF \
#     MODEL_FILE=DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf MINSIZE=900000000 bash download_model.sh
REPO="${REPO:-bartowski/Llama-3.2-1B-Instruct-GGUF}"
MODEL_FILE="${MODEL_FILE:-Llama-3.2-1B-Instruct-Q4_K_M.gguf}"
MINSIZE="${MINSIZE:-700000000}"
URL="https://huggingface.co/$REPO/resolve/main/$MODEL_FILE"

if [[ -f "$MODEL_FILE" && $(stat -c%s "$MODEL_FILE") -gt "$MINSIZE" ]]; then
    echo "==> $MODEL_FILE already present ($(du -h "$MODEL_FILE" | cut -f1)). Skipping."
else
    echo "==> Downloading $MODEL_FILE from $REPO"
    # If you have HF_TOKEN set (gated models), curl uses it; for bartowski
    # repos no auth is needed.
    AUTH_HEADER=""
    if [[ -n "${HF_TOKEN:-}" ]]; then
        AUTH_HEADER="Authorization: Bearer $HF_TOKEN"
    fi
    curl -L -H "$AUTH_HEADER" -o "$MODEL_FILE" "$URL"
fi

echo
echo "==> Model ready:"
ls -lh "$MODELS_DIR/$MODEL_FILE"
