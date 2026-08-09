#!/usr/bin/env bash
# Day 3 — Jetson Orin Nano environment setup
#
# Builds llama.cpp from source with CUDA support, installs Python deps,
# sets up the workspace under /data/zliu604/jetson.
#
# Tested config: JetPack 6.x, L4T r36.x, CUDA 12.6, Orin Nano 8GB.
#
# Re-runnable: skips already-done steps.
set -e

WORK_ROOT="${WORK_ROOT:-/home/jetson/specdecode}"
LLAMA_DIR="$WORK_ROOT/llama.cpp"
MODELS_DIR="$WORK_ROOT/models"

echo "==> Workspace: $WORK_ROOT"
mkdir -p "$WORK_ROOT" "$MODELS_DIR"

# ---------------------------------------------------------------------------
# 1. Apt prerequisites
# ---------------------------------------------------------------------------
echo "==> Installing apt packages"
sudo apt-get update -qq
sudo apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    pkg-config \
    libcurl4-openssl-dev \
    python3-pip \
    python3-venv

# Check gcc version — JetPack 6 ships gcc 11+, which is fine for new llama.cpp
echo "==> gcc version:"
gcc --version | head -1

# ---------------------------------------------------------------------------
# 2. Verify CUDA toolkit
# ---------------------------------------------------------------------------
echo "==> Checking CUDA"
if [[ ! -d /usr/local/cuda ]]; then
    echo "ERROR: /usr/local/cuda not found. Run 'sudo apt-get install nvidia-jetpack' first."
    exit 1
fi

# Add CUDA to PATH if not already there
if ! command -v nvcc &>/dev/null; then
    export PATH="/usr/local/cuda/bin:$PATH"
    export LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH:-}"
    # Persist for future shells (idempotent grep)
    if ! grep -q "/usr/local/cuda/bin" ~/.bashrc; then
        cat >> ~/.bashrc <<'BRC'

# --- CUDA (added by Day 3 setup) ---
export PATH="/usr/local/cuda/bin:$PATH"
export LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH:-}"
BRC
    fi
fi

echo "==> nvcc version:"
nvcc --version | tail -1

# ---------------------------------------------------------------------------
# 3. Set Jetson to MAXN power mode for setup
# ---------------------------------------------------------------------------
echo "==> Setting MAXN power mode for fast compilation"
# Orin Nano power modes: 0=15W (default), 1=7W, 2=MAXN. JetPack 6 reuses these.
sudo nvpmodel -m 0 2>/dev/null || echo "  (skipping nvpmodel — might already be set)"
sudo jetson_clocks 2>/dev/null || echo "  (skipping jetson_clocks — non-critical)"

# ---------------------------------------------------------------------------
# 4. Clone & build llama.cpp with CUDA
# ---------------------------------------------------------------------------
if [[ -x "$LLAMA_DIR/build/bin/llama-server" ]]; then
    echo "==> llama.cpp already built, skipping (delete $LLAMA_DIR to rebuild)"
else
    echo "==> Cloning llama.cpp"
    if [[ ! -d "$LLAMA_DIR" ]]; then
        git clone https://github.com/ggml-org/llama.cpp.git "$LLAMA_DIR"
    fi
    cd "$LLAMA_DIR"

    # Pin to a known-good tag for reproducibility. Update if needed.
    # b5050 (April 2025) is the last version with confirmed Orin Nano stability.
    # If you want bleeding edge, comment this out — but you might hit the
    # CUDACachingAllocator NVML issue mentioned in the Jetson forums.
    git fetch --tags --quiet
    git checkout b5050 2>/dev/null || git checkout master

    echo "==> Building with CUDA (this is the slow step, ~20-30 min on Orin Nano)"
    rm -rf build
    mkdir -p build && cd build

    # Key flags:
    #   GGML_CUDA=ON           — enable CUDA backend (new spelling)
    #   GGML_CUDA_F16=ON       — use FP16 in CUDA kernels for speed
    #   LLAMA_CURL=ON          — enables `-hf user/repo` model auto-download
    #   CMAKE_CUDA_ARCHITECTURES=87 — Orin's SM 8.7 (Ampere)
    cmake .. \
        -DGGML_CUDA=ON \
        -DGGML_CUDA_F16=ON \
        -DLLAMA_CURL=ON \
        -DCMAKE_CUDA_ARCHITECTURES=87 \
        -DCMAKE_BUILD_TYPE=Release 2>&1 | tee ../cmake.log

    # Parallel build — Orin Nano has 6 cores, but RAM-limited so use 4
    cmake --build . --config Release -j 4 2>&1 | tee ../build.log

    echo "==> Verifying build"
    ls -la bin/llama-server bin/llama-cli || {
        echo "ERROR: build artifacts missing. Check $LLAMA_DIR/build.log"
        exit 1
    }
fi

# ---------------------------------------------------------------------------
# 5. Python deps for client / benchmarks / energy monitoring
# ---------------------------------------------------------------------------
echo "==> Installing Python packages"

# Use a venv to keep things clean. Jetson's system Python is shared.
VENV="$WORK_ROOT/venv"
if [[ ! -d "$VENV" ]]; then
    python3 -m venv "$VENV"
fi
# shellcheck disable=SC1091
source "$VENV/bin/activate"

pip install --upgrade pip
pip install \
    "openai>=1.40.0" \
    "tqdm>=4.66" \
    "requests>=2.31" \
    "tabulate>=0.9.0" \
    "jetson-stats>=4.2.9"     # provides jtop & Python jtop API for energy

# jetson-stats also installs a systemd service. Start it.
sudo systemctl enable jetson_stats.service 2>/dev/null || true
sudo systemctl start  jetson_stats.service 2>/dev/null || true

# ---------------------------------------------------------------------------
# 6. Quick sanity check
# ---------------------------------------------------------------------------
echo
echo "==> Quick GPU sanity check"
"$LLAMA_DIR/build/bin/llama-cli" --version || true
echo
echo "==> Available models in $MODELS_DIR:"
ls -lh "$MODELS_DIR" 2>/dev/null || echo "  (none yet — run download_model.sh)"
echo
echo "================================================================"
echo "Setup complete."
echo
echo "Next steps:"
echo "  1.  bash download_model.sh"
echo "  2.  bash start_server.sh &"
echo "  3.  bash test_curl.sh"
echo "================================================================"
