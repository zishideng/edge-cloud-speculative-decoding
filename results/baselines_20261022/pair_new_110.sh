#!/usr/bin/env bash
# For one pair: retune PipeSD (continuous stream), then run the new arms on the 110 prompts of
# results/final_20261020/<key>_full_dist_110 (same seed and scenarios) for merging, as llama_new_110.
# Only the published baselines: pre-verification was not adopted (llama_new_110), so CAPE stays as in full_dist_110.
# Usage: pair_new_110.sh <key> <model_pair> <target model substring> <pearl gamma low> <high> <dynamic>
cd "$(dirname "$0")/../.."
D=results/baselines_20261022; K=$1; PAIR=$2; MODEL=$3
echo "$(date -Is) waiting for cloud model $MODEL with prefix_cache_verify" >> $D/${K}_pipesd_tune_v2_maintenance.log
until curl -s -m 5 http://172.23.123.195:9090/info | python3 -c "import json,sys;d=json.load(sys.stdin);sys.exit(0 if '$MODEL' in d['target_model'] and d['backend_settings'].get('prefix_cache_verify') else 1)" 2>/dev/null; do sleep 60; done
sleep 60   # let a freshly started server settle
python3 -m experiments.tune_pipesd make --pair "$PAIR" --phase ${K}_pipesd_tune_v2 --out $D/${K}_pipesd_tune_v2_plan.json || exit 1
bash $D/run_full.sh ${K}_pipesd_tune_v2 "$MODEL" || exit 1
python3 -m experiments.tune_pipesd pick --dir $D/${K}_pipesd_tune_v2 > $D/${K}_pipesd_tuned_v2.txt || exit 1
python3 - "$K" "$4" "$5" "$6" <<'PY'
import json, sys
from pathlib import Path
k, gammas = sys.argv[1], dict(zip(['low', 'high', 'dynamic'], map(int, sys.argv[2:])))
D = Path('results/baselines_20261022')
tuned = json.loads((D / f'{k}_pipesd_tuned_v2.txt').read_text().splitlines()[-1])
base = json.loads(Path(f'results/final_20261020/{k}_full_dist_110_plan.json').read_text())
llama = json.loads((D / 'llama_new_110_plan.json').read_text())
plan = dict(base, phase=f'{k}_new_110', campaign=str(D), methods=['pearl', 'picospec', 'pipesd', 'hf_default'], baselines=[], tuning=True,
    role=f'Full 110-prompt {k} evaluation of the published baselines only, merged with {k}_full_dist_110 (same prompts, scenarios and seed): PEARL (gamma=round(c): {"/".join(map(str, gammas.values()))}), PicoSpec, PipeSD (continuous stream, R1/R2 from {k}_pipesd_tune_v2), HF assisted generation with current defaults.',
    scenarios=[dict(s, pipesd=tuned[s['name']], pearl=dict(gamma=gammas[s['name']])) for s in base['scenarios']],
    candidate_definition=llama['candidate_definition'], stopping='Exactly 1320 timed requests; resumed with the same plan after a lost connection once the cloud serves the same model again.')
(D / f'{k}_new_110_plan.json').write_text(json.dumps(plan, indent=1))
PY
bash $D/run_full.sh ${K}_new_110 "$MODEL"
