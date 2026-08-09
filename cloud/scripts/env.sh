#!/usr/bin/env bash
# Source this from every script that needs the env.
# Keeps all paths under /data/zliu604.
# --- Personal scratch root --------------------------------------------------
export PROJECT_ROOT="/data/zliu604/specdecode-day1"

# --- Conda env --------------------------------------------------------------
# Force conda to install envs under our quota, not the default ~/miniconda3.
export CONDA_ENVS_PATH="$PROJECT_ROOT/conda-envs"
export CONDA_PKGS_DIRS="$PROJECT_ROOT/conda-pkgs"
export ENV_NAME="${ENV_NAME:-specdecode}"

# --- HuggingFace caches ------------------------------------------------------
# Critical: default is ~/.cache, which is small / shared / quota-limited.
export HF_HOME="$PROJECT_ROOT/hf-cache"
export TRANSFORMERS_CACHE="$HF_HOME/transformers"
export HF_DATASETS_CACHE="$HF_HOME/datasets"
export HF_HUB_CACHE="$HF_HOME/hub"
# Avoid HF telemetry pings from compute nodes that may block egress.
export HF_HUB_DISABLE_TELEMETRY=1

# --- pip cache --------------------------------------------------------------
export PIP_CACHE_DIR="$PROJECT_ROOT/pip-cache"

# --- vLLM / torch caches -----------------------------------------------------
export TORCH_HOME="$PROJECT_ROOT/torch-cache"
export VLLM_CACHE_ROOT="$PROJECT_ROOT/vllm-cache"
# vLLM compiles cuda graphs / kernels; default goes to /tmp which may be tiny.
export XDG_CACHE_HOME="$PROJECT_ROOT/xdg-cache"
# Prevent vllm from probing the internet on every load.
export HF_HUB_OFFLINE=0   # flip to 1 once everything is cached

# --- Make sure dirs exist ----------------------------------------------------
mkdir -p "$PROJECT_ROOT" "$CONDA_ENVS_PATH" "$CONDA_PKGS_DIRS" \
         "$HF_HOME" "$PIP_CACHE_DIR" "$TORCH_HOME" "$VLLM_CACHE_ROOT" \
         "$XDG_CACHE_HOME"

# --- Activate conda env if it exists -----------------------------------------
# If conda is on the cluster's module system, you may need:
#   module load conda
# before sourcing this file.
if command -v conda &> /dev/null; then
    # shellcheck disable=SC1091
    eval "$(conda shell.bash hook)"
    if conda env list | grep -q "^$ENV_NAME "; then
        conda activate "$ENV_NAME"
    fi
fi

echo "env.sh: PROJECT_ROOT=$PROJECT_ROOT, ENV=$ENV_NAME"
# export your HF_TOKEN
