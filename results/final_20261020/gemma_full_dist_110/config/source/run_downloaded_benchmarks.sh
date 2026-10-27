#!/usr/bin/env bash
# Run only the user's three existing local dataset files, once per condition.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

if [[ $# -gt 1 ]]; then
  echo 'Usage: bash run_downloaded_benchmarks.sh [--plan]' >&2
  exit 2
fi
plan_flags=()
case "${1:-}" in
  '') ;;
  --plan) plan_flags=(--plan) ;;
  -h|--help)
    echo 'Usage: bash run_downloaded_benchmarks.sh [--plan]'
    echo 'Uses common/data/{gsm8k_test_50,humaneval_30,mtbench_30}.jsonl.'
    echo 'Three methods, added delays 2/100 ms, one run per condition.'
    echo 'HumanEval and MT-Bench provide speed/energy measurements; task scoring is unavailable.'
    echo 'Optional environment: PYTHON, DRAFT_URL, CLOUD_URL, DOWNLOADED_RESULTS_ROOT.'
    exit 0 ;;
  *) echo 'Usage: bash run_downloaded_benchmarks.sh [--plan]' >&2; exit 2 ;;
esac

if [[ -z "${PYTHON:-}" ]]; then
  if [[ -x .venv/bin/python ]]; then PYTHON=.venv/bin/python; else PYTHON=python3; fi
fi

# Validate all dataset files before starting any model requests.
"$PYTHON" - <<'PY'
from pathlib import Path
import json
for task in ('gsm8k', 'humaneval', 'mtbench'):
    config = json.loads(Path(f'configs/research.downloaded.{task}.json').read_text())
    path = Path(config['DATASET'])
    rows = [json.loads(s) for s in path.read_text().splitlines() if s.strip()]
    if not rows or any(not isinstance(r.get('question'), str) or not r['question'].strip() for r in rows):
        raise ValueError(f'Empty or invalid downloaded dataset: {path}')
PY

for task in gsm8k humaneval mtbench; do
  config="configs/research.downloaded.${task}.json"
  dataset=$(
    "$PYTHON" - "$config" <<'PY'
import json, sys
from pathlib import Path
print(json.loads(Path(sys.argv[1]).read_text())['DATASET'])
PY
  )
  indices=$(
    "$PYTHON" - "$dataset" <<'PY'
from pathlib import Path
import sys
rows = [s for s in Path(sys.argv[1]).read_text().splitlines() if s.strip()]
print(','.join(map(str, range(len(rows)))))
PY
  )
  "$PYTHON" -m experiments.adaptive_research \
    --phase "downloaded_${task}" --phase-role development \
    --indices "$indices" --dataset "$dataset" --config "$config" \
    --methods fixed fixed_fast regime --compact-target-logprobs \
    --low-ms 2 --high-ms 100 \
    --max-tokens 512 --buffer-max 10 \
    --draft-url "${DRAFT_URL:-http://127.0.0.1:8080}" \
    --cloud-url "${CLOUD_URL:-http://172.23.119.64:9090}" \
    --output-root "${DOWNLOADED_RESULTS_ROOT:-results/downloaded_benchmarks}" \
    "${plan_flags[@]}"
done
