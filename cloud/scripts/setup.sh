#!/usr/bin/env bash
# One-time setup. Safe to re-run; idempotent.
# Runs on either a login node or a GPU node — both fine.
set -e

# Bootstrap our env config FIRST so all caches redirect.
# shellcheck disable=SC1091
source "$(dirname "$0")/env.sh"

cd "$PROJECT_ROOT"

# --- Conda ------------------------------------------------------------------
if ! command -v conda &> /dev/null; then
    echo "ERROR: conda not found. Try 'module load conda' or 'module load anaconda',"
    echo "or ask the cluster admin which module loads miniconda."
    exit 1
fi
eval "$(conda shell.bash hook)"

if conda env list | grep -q "^$ENV_NAME "; then
    echo "[setup] Env '$ENV_NAME' exists, reusing."
else
    echo "[setup] Creating conda env '$ENV_NAME' at $CONDA_ENVS_PATH"
    conda create -p "$CONDA_ENVS_PATH/$ENV_NAME" python=3.11 -y
fi
conda activate "$CONDA_ENVS_PATH/$ENV_NAME"

# --- PyTorch ----------------------------------------------------------------
# CUDA 13.2 driver. PyTorch official wheels target CUDA runtimes. As of
# May 2026 there is no official cu132 wheel; cu128 wheels are forward-
# compatible because NVIDIA drivers are backward-compatible across the
# major version. If pytorch.org adds cu130/cu132 by the time you run this,
# swap the URL.
echo "[setup] Installing PyTorch (cu128 wheels, driver-compatible with 13.x)"
pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128 || {
    echo "[setup] cu128 install failed, falling back to default index..."
    pip install torch
}

# --- vLLM -------------------------------------------------------------------
echo "[setup] Installing vLLM (>=0.7 for --speculative-config string API)"
pip install "vllm>=0.7.0"

# --- Helpers ----------------------------------------------------------------
echo "[setup] Installing helper packages"
pip install \
    "datasets>=2.20.0" \
    "tqdm>=4.66" \
    "tabulate>=0.9.0"

# --- Sanity ----------------------------------------------------------------
echo "[setup] Verifying torch installation"
python -c "import torch; print('Torch:', torch.__version__, '| CUDA built:', torch.version.cuda)"
# Do NOT call torch.cuda.is_available() on a login node — it may print False
# while still working fine on the compute node where the GPU lives.


mkdir -p "$PROJECT_ROOT/results" "$PROJECT_ROOT/logs" "$PROJECT_ROOT/data"

echo
echo "[setup] DONE. Next:"
echo "  1.  source env.sh"
echo "  2.  python download_gsm8k.py"
echo "  3.  sbatch slurm_run.sh"
