"""Cross-pair summary against the best fixed window, with draft acceptance rates.

The raw arm ``fixed_fast`` is the fixed gamma=4 window and is reported as fixed_g4. For every
model pair and delay, best_fixed is whichever of fixed_g2/g4/g8 has the highest throughput at
that delay; pooled combines the per-delay choices. This is an oracle choice made after the
measurement, so it is a stronger baseline than any single fixed window chosen in advance.

Acceptance is computed over all verification rounds of an arm:
  alpha   strict accepted / examined draft tokens (examined stops at the first rejection)
  tau     accepted draft tokens per verification round
  util    accepted / proposed draft tokens (proposed includes tokens after the first rejection)
"""
import argparse
import json
from pathlib import Path

from experiments.adaptive_research import write_json
from experiments.progress_probe import paired_effect, summarize

ROOT = Path(__file__).resolve().parents[1]
PAIRS = {
    'llama': ('Llama-3.2-1B -> Llama-3.1-8B-AWQ', 'results/compare_20261010/full_110'),
    'qwen': ('Qwen2.5-0.5B -> Qwen2.5-7B-AWQ', 'results/qwen_20261014/full_110'),
    'gemma': ('Gemma-2-2B -> Gemma-2-9B-AWQ', 'results/gemma_20261015/full_110'),
}
FIXED = ('fixed_g2', 'fixed_fast', 'fixed_g8')
ROWS = ('sync_g4', 'fixed_g2', 'fixed_fast', 'fixed_g8', 'best_fixed', 'adaedl', 'markov_w0', 'markov_w0_pos',
        'markov_w0_fit', 'markov_w0_mean', 'markov_w0_robust', 'markov_w05', 'markov_w05_pos', 'markov_w05_fit', 'markov_w05_mean',
        'markov_w05_robust', 'markov_w0_floor2', 'markov_w05_floor2', 'markov_w0_dist',
        'markov_w05_dist')
CANDIDATES = ('sync_g4', 'adaedl', 'markov_w0', 'markov_w0_pos', 'markov_w0_fit', 'markov_w0_mean', 'markov_w05',
              'markov_w05_pos', 'markov_w05_fit', 'markov_w05_mean', 'markov_w0_robust', 'markov_w05_robust',
              'markov_w0_floor2', 'markov_w05_floor2', 'markov_w0_dist',
        'markov_w05_dist')
LABEL = {'fixed_fast': 'fixed_g4', 'markov_w0': 'CAPE-S (w=0)', 'markov_w05': 'CAPE-E (w=0.5)',
         'markov_w0_pos': 'CAPE-S v2 (w=0)', 'markov_w05_pos': 'CAPE-E v2 (w=0.5)',
         'markov_w0_fit': 'CAPE-S fit (w=0)', 'markov_w05_fit': 'CAPE-E fit (w=0.5)',
         'markov_w0_mean': 'CAPE-S mean (w=0)', 'markov_w05_mean': 'CAPE-E mean (w=0.5)',
         'markov_w0_robust': 'CAPE-S (w=0)', 'markov_w05_robust': 'CAPE-E (w=0.5)',
         'markov_w0_floor2': 'CAPE-S floor2 (w=0)', 'markov_w05_floor2': 'CAPE-E floor2 (w=0.5)',
         'markov_w0_dist': 'CAPE-S dist (w=0)', 'markov_w05_dist': 'CAPE-E dist (w=0.5)'}


def label(method):
    return LABEL.get(method, method)


def acceptance(records):
    rounds = [v for r in records for v in r['rounds']]
    examined = sum(v['n_examined'] for v in rounds)
    proposed = sum(v['n_proposed'] for v in rounds)
    accepted = sum(v['n_accepted'] for v in rounds)
    return dict(rounds=len(rounds),
                alpha=sum(v['strict_accepted'] for v in rounds) / examined if examined else None,
                tau=accepted / len(rounds) if rounds else None,
                util=accepted / proposed if proposed else None)


def analyse(directory):
    protocol = json.loads((directory / 'config/protocol.json').read_text())
    status = json.loads((directory / 'report/status.json').read_text())
    records = [json.loads(p.read_text()) for p in sorted((directory / 'raw').glob('*.json'))]
    scenarios = protocol.get('primary_scenarios') or [s['name'] for s in protocol['scenarios']]
    best = {}
    for s in scenarios:
        speed = {m: summarize([r for r in records if r['method'] == m and r['scenario'] == s])['throughput_tps']
                 for m in FIXED if m in protocol['methods']}
        best[s] = max(speed, key=speed.get)
    records += [dict(r, method='best_fixed') for r in records
                if r['scenario'] in best and r['method'] == best[r['scenario']]]
    tables, effects = {}, {}
    for scene in scenarios + ['pooled']:
        ss = scenarios if scene == 'pooled' else [scene]
        rows = {}
        for m in ROWS:
            rr = [r for r in records if r['method'] == m and r['scenario'] in ss]
            if rr:
                rows[m] = dict(summarize(rr), **acceptance(rr))
        tables[scene] = rows
        effects[scene] = {m: paired_effect(records, m, ss, baseline='best_fixed') for m in CANDIDATES}
    return dict(directory=str(directory.relative_to(ROOT)), state=status['state'],
                requests=sum(r['method'] != 'best_fixed' for r in records), jobs=len(protocol['jobs']),
                scenarios=scenarios, best_fixed=best, tables=tables, effects=effects)


def pct(value):
    return 'N/A' if value is None else f'{100 * value:.1f}'


def render(results):
    lines = ['# Cross-pair results against the best fixed window', '',
             'fixed_g4 is the raw arm fixed_fast. best_fixed is, per delay, the fixed window (g2/g4/g8) '
             'with the highest throughput; pooled combines those per-delay choices. It is chosen after '
             'the measurement, so it is an oracle baseline.', '',
             'alpha = strict accepted / examined draft tokens; tau = accepted draft tokens per verification '
             'round; util = accepted / proposed draft tokens. sync_g4 and fixed_g4 use the same window, '
             'so their acceptance differs only through prefetch reuse.', '']
    for key, res in results.items():
        name = PAIRS[key][0] if key in PAIRS else key
        done = '' if res['state'] == 'complete' else f' -- INCOMPLETE ({res["state"]})'
        choice = ', '.join(f'{s}: {label(m)}' for s, m in res['best_fixed'].items())
        lines += [f'## {name}', '', f'{res["directory"]}: {res["requests"]}/{res["jobs"]} requests{done}. '
                  f'Best fixed window: {choice}.', '',
                  '| Delay | Method | Requests | tokens/s | J/token | alpha % | tau | util % |',
                  '|---|---|---:|---:|---:|---:|---:|---:|']
        for scene, rows in res['tables'].items():
            for m, v in rows.items():
                name_m = f'**best_fixed** ({label(res["best_fixed"][scene])})' if m == 'best_fixed' and scene != 'pooled' \
                    else ('**best_fixed**' if m == 'best_fixed' else label(m))
                energy = f'{v["joules_per_token"]:.4f}' if v['joules_per_token'] is not None else 'N/A'
                tau = f'{v["tau"]:.2f}' if v['tau'] is not None else 'N/A'
                lines.append(f'| {scene} | {name_m} | {v["requests"]} | {v["throughput_tps"]:.2f} | {energy} | '
                             f'{pct(v["alpha"])} | {tau} | {pct(v["util"])} |')
        lines += ['', 'Paired effects versus best_fixed (prompt-cluster bootstrap, 2000 draws). '
                  'Positive energy saving means lower J/token.', '',
                  '| Delay | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences |',
                  '|---|---|---:|---|---|---:|']
        for scene, group in res['effects'].items():
            for m, v in group.items():
                if not v:
                    continue
                lo, hi = v['throughput_ci95']
                energy = 'N/A'
                if v['energy_ci95']:
                    el, eh = v['energy_ci95']
                    energy = f'{v["energy_saving_pct"]:.2f} [{el:.2f}, {eh:.2f}]'
                lines.append(f'| {scene} | {label(m)} | {v["independent_prompts"]} | '
                             f'{v["throughput_gain_pct"]:.2f} [{lo:.2f}, {hi:.2f}] | {energy} | {v["changed_sequences"]} |')
        lines.append('')
    return '\n'.join(lines)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--pairs', nargs='+', choices=list(PAIRS), default=list(PAIRS))
    ap.add_argument('--dirs', nargs='+', default=[], help='analyse these phase directories instead of --pairs')
    ap.add_argument('--out', type=Path, default=ROOT / 'results/cross_pair_20261019')
    args = ap.parse_args()
    results = ({d: analyse(ROOT / d) for d in args.dirs} if args.dirs
               else {k: analyse(ROOT / PAIRS[k][1]) for k in args.pairs})
    args.out.mkdir(parents=True, exist_ok=True)
    write_json(args.out / 'results.json', results)
    (args.out / 'SUMMARY.md').write_text(render(results))
    print(render(results))
