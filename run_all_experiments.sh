#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
if [[ -z "${PYTHON:-}" ]]; then
  if [[ -x .venv/bin/python ]]; then PYTHON=.venv/bin/python; else PYTHON=python3; fi
fi
exec "$PYTHON" -m experiments.run "$@"
