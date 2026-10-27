"""Tune PipeSD's NAV thresholds (R1, R2) per model pair and delay, as the PipeSD autotuner does.

PipeSD searches (R1, R2) in (0, 1)^2 with 16 samples and keeps the pair with the lowest time per
token. We use the same budget and objective with seeded uniform samples (the paper uses
Bayesian optimization), shared across delays, on development prompts outside the evaluation set.

  make: write a progress_probe plan with one scenario per (delay, sample)
  pick: read the finished run and print the best (R1, R2) per delay as JSON
"""
import argparse
import json
import random
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DELAYS = {'low': dict(delay_ms=2), 'high': dict(delay_ms=100),
          'dynamic': dict(delay_ms=None, schedule=dict(levels=[2, 100], mean_dwell_ms=1500, horizon_ms=180000))}
DEV = {'gsm8k': [49], 'humaneval': [29], 'mtbench': [29]}


def samples(n=16, seed=20261022):
    rng = random.Random(seed)
    return [(round(rng.uniform(0.01, 0.99), 3), round(rng.uniform(0.01, 0.99), 3)) for _ in range(n)]


def make(args):
    scenarios = [dict(DELAYS[d], name=f'{d}__s{j:02d}', pipesd=dict(r1=r1, r2=r2))
                 for d in args.delays for j, (r1, r2) in enumerate(samples())]
    plan = dict(phase=args.phase, campaign=args.campaign, model_pair=args.pair, seed=20261022,
                role='PipeSD threshold tuning: 16 (R1, R2) samples per delay on development prompts.',
                methods=['pipesd'], baselines=[], tuning=True, indices=DEV, scenarios=scenarios,
                primary_scenarios=[s['name'] for s in scenarios], repeats=1, max_tokens=args.max_tokens,
                candidate_definition='pipesd with the scenario\'s (r1, r2)', criteria='time per token',
                measurement='As the evaluation runs; shorter outputs to bound tuning time.',
                stopping=f'Exactly {len(scenarios) * sum(map(len, DEV.values()))} timed requests.')
    Path(args.out).write_text(json.dumps(plan, indent=1))
    print(f'{args.out}: {len(scenarios)} scenarios, {len(scenarios) * sum(map(len, DEV.values()))} requests')


def pick(args):
    directory = ROOT / args.dir
    plan = json.loads((directory / 'config/protocol.json').read_text())
    params = {s['name']: s['pipesd'] for s in plan['scenarios']}
    wall, tokens = defaultdict(float), defaultdict(int)
    for path in (directory / 'raw').glob('*.json'):
        r = json.loads(path.read_text())
        wall[r['scenario']] += r['wall_time_s']
        tokens[r['scenario']] += r['output_tokens']
    best = {}
    for name in params:
        delay = name.split('__')[0]
        ms = 1000 * wall[name] / tokens[name]
        if delay not in best or ms < best[delay][0]:
            best[delay] = (ms, params[name])
    for delay, (ms, p) in best.items():
        print(f'{delay}: r1={p["r1"]} r2={p["r2"]} ({ms:.1f} ms/token)')
    print(json.dumps({d: p for d, (_, p) in best.items()}))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('make')
    m.add_argument('--pair', required=True)
    m.add_argument('--phase', required=True)
    m.add_argument('--campaign', default='results/baselines_20261022')
    m.add_argument('--delays', nargs='+', default=list(DELAYS))
    m.add_argument('--max-tokens', type=int, default=128)
    m.add_argument('--out', required=True)
    p = sub.add_parser('pick')
    p.add_argument('--dir', required=True)
    args = ap.parse_args()
    make(args) if args.cmd == 'make' else pick(args)
