#!/usr/bin/env python3
"""Extract every number used in the CAPE manuscript from retained raw records.

Only the 2 ms (low) and 100 ms (high) delay scenarios are used. Run from the
repository root (no model or sensor access):

    nice -n 19 python3 paper/cape_20261010/scripts/extract_evidence.py
"""
import json
import sys
import timeit
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
PAPER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from common.pipeline_model import choose_windows  # noqa: E402
import experiments.progress_probe as probe  # noqa: E402
from experiments.progress_probe import paired_effect, summarize  # noqa: E402

# Use the energy check stored with each record at run time (power samples are not loaded).
probe.energy_check = lambda r: r['energy_validation']

PHASES = {
    'heldout1': 'results/pipeline_research_20261009/confirm_markov',
    'heldout2': 'results/pipeline_research_20261009/final_markov_v2',
    'full': 'results/compare_20261010/full_110',
}
MAINTENANCE_LOG = 'results/compare_20261010/full_110_maintenance.log'
METHODS = ['sync_g4', 'fixed_g2', 'fixed_fast', 'fixed_g8', 'adaedl', 'markov_w0', 'markov_w05']
LH = ['low', 'high']
DATASETS = ['gsm8k', 'humaneval', 'mtbench']


def load(phase):
    """Records of the 2 and 100 ms conditions, without power samples and token-id lists that the
    analysis does not use (the energy check computed at run time is kept in energy_validation)."""
    out = []
    for p in sorted((ROOT / PHASES[phase] / 'raw').glob('*.json')):
        r = json.loads(p.read_text())
        if r['scenario'] not in LH:
            continue
        r['energy'].pop('samples', None)
        r.pop('output_text', None)
        r.pop('reference_text', None)
        for e in r['lookahead']['events']:
            for key in ('prefetch_ids', 'prefetch_prefix_ids', 'reuse_prefix_ids'):
                e.pop(key, None)
        out.append(r)
    return out


def busy_s(r):
    """Draft-server busy time: foreground drafting plus background lookahead calls."""
    return (sum(v['draft_ms'] for v in r['rounds'])
            + sum(e['service_ms'] for e in r['lookahead']['events'])) / 1000


def method_rows(records, methods):
    out = {}
    for m in methods:
        out[m] = {}
        for scene in LH + ['pooled']:
            rr = [r for r in records if r['method'] == m and (scene == 'pooled' or r['scenario'] == scene)]
            s = summarize(rr)
            out[m][scene] = dict(
                requests=s['requests'], tokens=s['tokens'], tps=s['throughput_tps'],
                j_per_token=s['joules_per_token'], j_per_request=s['joules'] / s['requests'],
                mean_w=s['joules'] / s['wall_s'], energy_valid=s['energy_valid_requests'],
                truncated=s['truncated'], reuse_pct=s['background_reuse_pct'],
                background_tokens=s['background_tokens'], discarded_tokens=s['discarded_tokens'],
                discarded_per_100_tokens=100 * s['discarded_tokens'] / s['tokens'],
                busy_ms_per_token=1000 * sum(busy_s(r) for r in rr) / s['tokens'],
                rounds_per_100_tokens=100 * s['rounds'] / s['tokens'])
    return out


def effect(records, cand, base, scenes=LH):
    e = paired_effect(records, cand, scenes, baseline=base)
    if e is None:
        return None
    return dict(candidate=cand, baseline=base, scenarios=scenes, speed_pct=e['throughput_gain_pct'],
                speed_ci=e['throughput_ci95'], saving_pct=e['energy_saving_pct'], saving_ci=e['energy_ci95'],
                prompts=e['independent_prompts'], pairs=e['request_pairs'],
                changed_sequences=e['changed_sequences'], extra_truncations=e['additional_truncations'],
                leave_one_out_speed=e['leave_one_prompt_out_speed_range'])


def effects(records, pairs):
    out = {}
    for cand, base in pairs:
        key = f'{cand}_vs_{base}'
        out[key] = {'pooled': effect(records, cand, base)}
        for s in LH:
            out[key][s] = effect(records, cand, base, [s])
        for d in DATASETS:
            rr = [r for r in records if r['dataset'] == d]
            out[key][d] = effect(rr, cand, base)
            for s in LH:
                out[key][f'{d}_{s}'] = effect(rr, cand, base, [s])
    return out


def energy_model(records):
    t = np.array([r['wall_time_s'] for r in records])
    b = np.array([busy_s(r) for r in records])
    j = np.array([r['energy_validation']['recomputed_joules'] for r in records])
    x = np.column_stack([t, b])
    coef, *_ = np.linalg.lstsq(x, j, rcond=None)
    pred = x @ coef
    r2 = 1 - ((j - pred) ** 2).sum() / ((j - j.mean()) ** 2).sum()
    return dict(base_w=coef[0], draft_w=coef[1], ratio=coef[1] / coef[0], r2=r2, n=len(j),
                mape_pct=float(np.mean(np.abs(pred - j) / j) * 100),
                busy_share_pct=float(100 * b.sum() / t.sum()),
                points=[dict(method=r['method'], scenario=r['scenario'], measured=float(jj), predicted=float(pp))
                        for r, jj, pp in zip(records, j, pred)])


def draft_cost(records):
    events = [(e['generated_tokens'], e['service_ms']) for r in records for e in r['lookahead']['events']
              if e['generated_tokens'] > 0 and r['method'] in ('fixed_g2', 'fixed_fast', 'fixed_g8')]
    n, t = np.array(events, dtype=float).T
    slope, intercept = np.polyfit(n, t, 1)
    pred = intercept + slope * n
    r2 = 1 - ((t - pred) ** 2).sum() / ((t - t.mean()) ** 2).sum()
    sync = [v['draft_ms'] / v['n_proposed'] for r in records if r['method'] == 'sync_g4'
            for v in r['rounds'] if v['n_proposed'] == 4]
    return dict(call_ms=intercept, token_ms=slope, r2=r2, calls=len(n), token_range=[int(n.min()), int(n.max())],
                sync4_ms_per_token=float(np.median(sync)), sync4_rounds=len(sync))


def verify_cost(records):
    """cloud_verify_ms against context position and proposed tokens, with per-request intercepts."""
    rows = []
    for k, r in enumerate(records):
        pos = 0
        for v in r['rounds']:
            rows.append((k, pos, v['n_proposed'], v['cloud_verify_ms']))
            pos += v['n_accepted'] + 1
    a = np.array(rows, dtype=float)
    demeaned = a.copy()
    for k in np.unique(a[:, 0]):
        mask = a[:, 0] == k
        demeaned[mask, 1:] -= a[mask, 1:].mean(axis=0)
    coef, *_ = np.linalg.lstsq(demeaned[:, 1:3], demeaned[:, 3], rcond=None)
    by_n = {}
    for n in sorted(set(a[:, 2].astype(int))):
        values = a[a[:, 2] == n, 3]
        if len(values) >= 20:
            by_n[int(n)] = dict(mean=float(values.mean()), median=float(np.median(values)), rounds=len(values))
    return dict(ms_per_context_token=coef[0], ms_per_proposed_token=coef[1], rounds=len(a),
                requests=len(records), mean_ms=float(a[:, 3].mean()), median_ms=float(np.median(a[:, 3])),
                by_proposed=by_n)


def network_path(records):
    """Real path per verification: HTTP round trip minus cloud verification and queueing time
    (the injected delay is a sleep outside the HTTP call), i.e. Wi-Fi transport plus HTTP overhead."""
    out = {}
    for scene in LH + ['pooled']:
        x = np.array([v['timing_residual_ms'] for r in records if scene == 'pooled' or r['scenario'] == scene
                      for v in r['rounds']])
        out[scene] = dict(rounds=len(x), median=float(np.median(x)), mean=float(x.mean()),
                          p10=float(np.percentile(x, 10)), p90=float(np.percentile(x, 90)),
                          p99=float(np.percentile(x, 99)), over_100ms_pct=float(100 * (x > 100).mean()))
    return out


def round_breakdown(records, method='sync_g4'):
    out = {}
    for s in LH:
        rounds = [v for r in records if r['method'] == method and r['scenario'] == s for v in r['rounds']]
        draft = np.mean([v['draft_ms'] for v in rounds])
        verify = np.mean([v['cloud_verify_ms'] for v in rounds])
        total = np.mean([v['round_total_ms'] for v in rounds])
        tokens = np.mean([v['n_accepted'] + 1 for v in rounds])
        out[s] = dict(draft_ms=draft, verify_ms=verify, transport_ms=total - draft - verify, total_ms=total,
                      draft_share_pct=100 * draft / total, tokens_per_round=tokens, rounds=len(rounds))
    return out


def decisions(records, methods):
    out = {}
    for m in methods:
        for s in LH:
            d = [x for r in records if r['method'] == m and r['scenario'] == s for x in r['lookahead']['decisions']]
            if not d:
                continue
            h = [x['h'] for x in d if x['h'] > 0]
            late = [x for x in d if x['round'] >= 10]
            out[f'{m}_{s}'] = dict(
                mean_alpha_miss=float(np.mean([x['alpha_miss'] for x in late])),
                mean_alpha_hit=float(np.mean([x['alpha_hit'] for x in late])),
                rounds=len(d), fresh=dict(Counter(x['fresh_gamma'] for x in d)), h=dict(Counter(h)),
                mean_fresh=float(np.mean([x['fresh_gamma'] for x in d])), mean_h=float(np.mean(h)),
                mean_sent=float(np.mean([x['gamma'] for x in d])),
                after_full_pct=100 * float(np.mean([x['after_full'] for x in d])),
                mean_verify_estimate_ms=float(np.mean([x['verify_ms'] for x in d])))
    return out


def acceptance_by_dataset(records, method='fixed_fast'):
    return {ds: float(np.mean([r['strict_acceptance_rate'] for r in records
                               if r['method'] == method and r['dataset'] == ds])) for ds in DATASETS}


def identical_outputs(records):
    blocks = {}
    for r in records:
        blocks.setdefault((r['dataset'], r['request_index'], r['scenario']), set()).add(tuple(r['output_ids']))
    return dict(blocks=len(blocks), differing=sum(len(v) > 1 for v in blocks.values()), requests=len(records))


def outcomes(records, methods):
    return {m: dict(Counter(e['outcome'] for r in records if r['method'] == m for e in r['lookahead']['events']))
            for m in methods}


def quality(records):
    """GSM8K accuracy, truncations and agreement with the cloud autoregressive reference per method."""
    out = {}
    for m in METHODS:
        rr = [r for r in records if r['method'] == m]
        g = [r for r in rr if r['dataset'] == 'gsm8k']
        out[m] = dict(gsm8k_correct=sum(r['task_quality'] == 1 for r in g), gsm8k_requests=len(g),
                      truncated=sum(r['truncated'] for r in rr), requests=len(rr),
                      reference_match=sum(r['output_ids'] == r['reference_ids'] for r in rr))
    return out


def divergence(records, a='fixed_fast', b='markov_w0'):
    blocks = {}
    for r in records:
        blocks.setdefault((r['dataset'], r['request_index'], r['scenario']), {})[r['method']] = r['output_ids']
    pos = []
    for v in blocks.values():
        x, y = v.get(a), v.get(b)
        if x is not None and y is not None and x != y:
            pos.append(next((i for i, (s, t) in enumerate(zip(x, y)) if s != t), min(len(x), len(y))))
    return dict(pairs=len(pos), median_first_difference=float(np.median(pos)) if pos else None,
                min_first_difference=min(pos) if pos else None)


def robustness(records, used_phases):
    """Effects excluding blocks that overlap logged host work, and on prompts unused by earlier phases."""
    import re
    from datetime import datetime
    windows, start = [], None
    for line in (ROOT / MAINTENANCE_LOG).read_text().splitlines():
        m = re.match(r'(\S+) (start|end) ', line)
        if m:
            t = datetime.fromisoformat(m.group(1)).timestamp()
            if m.group(2) == 'start':
                start = t
            elif start is not None:
                windows.append((start, t))
                start = None
    touched = {(r['dataset'], r['request_index'], r['scenario']) for r in records for w0, w1 in windows
               if r['started_at_unix'] <= w1 + 1 and r['finished_at_unix'] >= w0 - 1}
    clean = [r for r in records if (r['dataset'], r['request_index'], r['scenario']) not in touched]
    used = {('gsm8k', 25), ('humaneval', 5), ('mtbench', 5)}   # AdaEDL threshold sweep and smoke prompts
    # Pilot comparison (results/compare_20261010/small_compare, deleted on 2026-10-12).
    used |= {('gsm8k', 16), ('gsm8k', 40), ('humaneval', 4), ('humaneval', 18), ('mtbench', 6), ('mtbench', 26)}
    for phase in used_phases:
        protocol = json.loads((ROOT / phase / 'config/protocol.json').read_text())
        used |= {(d, i) for d, idx in protocol['indices'].items() for i in idx}
    fresh = [r for r in records if (r['dataset'], r['request_index']) not in used]
    return dict(windows=len(windows), touched_blocks=len(touched),
                touched_requests=sum((r['dataset'], r['request_index'], r['scenario']) in touched for r in records),
                clean={m: effect(clean, m, 'fixed_fast') for m in ('markov_w0', 'markov_w05')},
                fresh_prompts=len({(r['dataset'], r['request_index']) for r in fresh}),
                fresh={m: effect(fresh, m, 'fixed_fast') for m in ('markov_w0', 'markov_w05')})


def overhead_us():
    call = lambda: choose_windows(.8, .85, 150., 10., 24.5, .25, 2.3, 8)  # noqa: E731
    return min(timeit.repeat(call, number=200, repeat=5)) / 200 * 1e6


def main():
    data = {'note': 'Generated by scripts/extract_evidence.py from retained raw records; 2 ms and 100 ms only.'}
    h1, h2, full = load('heldout1'), load('heldout2'), load('full')
    data['phases'] = {k: dict(directory=v, requests=len(r), prompts=len({(x['dataset'], x['request_index']) for x in r}),
                              prompt_ids=sorted({f"{x['dataset']}:{x['request_index']}" for x in r}))
                      for (k, v), r in zip(PHASES.items(), (h1, h2, full))}
    data['heldout1'] = dict(methods=method_rows(h1, ['fixed_fast', 'regime_short', 'markov', 'markov_w05']),
                            effects=effects(h1, [('markov', 'fixed_fast'), ('markov_w05', 'fixed_fast'),
                                                 ('regime_short', 'fixed_fast'), ('markov', 'regime_short')]))
    data['heldout2'] = dict(methods=method_rows(h2, ['fixed_fast', 'markov', 'markov_v2']),
                            effects=effects(h2, [('markov', 'fixed_fast'), ('markov_v2', 'fixed_fast'),
                                                 ('markov_v2', 'markov')]))
    pairs = [(m, 'fixed_fast') for m in METHODS if m != 'fixed_fast']
    pairs += [(m, 'sync_g4') for m in METHODS if m != 'sync_g4']
    pairs += [('markov_w0', 'adaedl'), ('markov_w05', 'adaedl'), ('markov_w0', 'fixed_g8'), ('markov_w05', 'fixed_g8'),
              ('markov_w0', 'fixed_g2'), ('markov_w05', 'fixed_g2'), ('markov_w05', 'markov_w0')]
    data['full'] = dict(methods=method_rows(full, METHODS), effects=effects(full, pairs))
    data['measurement'] = dict(energy_model=energy_model(full), energy_model_heldout=energy_model(h1 + h2),
                               draft_cost=draft_cost(full), verify_cost=verify_cost(full),
                               sync_round=round_breakdown(full), network=network_path(full))
    data['measurement']['energy_model_heldout'].pop('points')
    data['controller'] = dict(full=decisions(full, ['markov_w0', 'markov_w05']),
                              heldout=decisions(h1 + h2, ['markov', 'markov_w05']),
                              outcomes=outcomes(full, METHODS), overhead_us=overhead_us())
    data['acceptance'] = dict(full=acceptance_by_dataset(full), heldout=acceptance_by_dataset(h1 + h2))
    data['identical'] = {k: identical_outputs(r) for k, r in (('heldout1', h1), ('heldout2', h2), ('full', full))}
    data['quality'] = quality(full)
    data['divergence'] = divergence(full)
    data['robustness'] = robustness(full, [PHASES['heldout1'], PHASES['heldout2']])
    (PAPER / 'data').mkdir(exist_ok=True)
    (PAPER / 'data/evidence.json').write_text(json.dumps(data, indent=1, default=float) + '\n')
    print('wrote', PAPER / 'data/evidence.json')


if __name__ == '__main__':
    main()
