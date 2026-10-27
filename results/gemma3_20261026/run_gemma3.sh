#!/usr/bin/env bash
# Gemma-3 pair after gemma3_smoke15: retune PipeSD, then all 10 arms on the 110 prompts of
# the other pairs (one phase, unlike the other pairs whose core and new arms ran separately).
# PEARL gamma = round(c) from gemma3_smoke15 sync_g4: low 2.39, high 6.67, dynamic 4.29.
cd "$(dirname "$0")/../.."
D=results/gemma3_20261026; MODEL=gemma-3-4b-it
python3 -m experiments.tune_pipesd make --pair gemma3_270m_4b --phase gemma3_pipesd_tune --campaign $D --out $D/gemma3_pipesd_tune_plan.json || exit 1
bash $D/run_full.sh gemma3_pipesd_tune "$MODEL" || exit 1
python3 -m experiments.tune_pipesd pick --dir $D/gemma3_pipesd_tune > $D/gemma3_pipesd_tuned.txt || exit 1
python3 - <<'PY'
import json
from pathlib import Path
D = Path('results/gemma3_20261026')
gammas = dict(low=2, high=7, dynamic=4)
tuned = json.loads((D / 'gemma3_pipesd_tuned.txt').read_text().splitlines()[-1])
smoke = json.loads((D / 'gemma3_smoke15_plan.json').read_text())
full = json.loads(Path('results/final_20261020/gemma_full_dist_110_plan.json').read_text())
new = json.loads(Path('results/baselines_20261022/gemma_new_110_plan.json').read_text())
plan = dict(smoke, phase='gemma3_full_110', indices=full['indices'],
    methods=full['methods'] + new['methods'], baselines=full['baselines'],
    scenarios=[dict(s, pipesd=tuned[s['name']], pearl=dict(gamma=gammas[s['name']])) for s in smoke['scenarios']],
    role='Full 110-prompt evaluation of the fourth pair (Gemma-3-270M-it Q8_0 draft, Gemma-3-4B-it FP8 target), same prompts and scenarios as the other pairs: CAPE (markov_*_dist) vs sync and fixed g2/g4/g8, plus PEARL (gamma=round(c) from gemma3_smoke15: 2/7/4), PicoSpec, PipeSD (R1/R2 from gemma3_pipesd_tune), HF assisted generation with current defaults.',
    candidate_definition=full['candidate_definition'] + ' ' + new['candidate_definition'],
    stopping='Exactly 3300 timed requests; resumed with the same plan after a lost connection once the cloud serves the same model again.')
(D / 'gemma3_full_110_plan.json').write_text(json.dumps(plan, indent=1))
PY
bash $D/run_full.sh gemma3_full_110 "$MODEL"
