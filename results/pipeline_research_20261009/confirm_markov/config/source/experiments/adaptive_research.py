"""Paired real-service AdaptiveLookahead research; reporting never contacts models.

Run with ``python3 -m experiments.adaptive_research --phase development ...``.
Every selected prompt is run once per method/scenario. The fixed window is
strict K=1, gamma=4; the baseline requests h=5. No simulation or result filtering
is performed. All model outputs, round decisions and power samples are retained.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import random
import shutil
import statistics
import subprocess
import sys
import time
import traceback
import uuid

from common.experiment_config import ROOT, load_config, validate
from experiments.isolation import ServiceLocks, environment_snapshot


METHODS = ('fixed', 'fixed_fast', 'regime')
SCENARIOS = ('low', 'high')


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2,
                                   allow_nan=False), encoding='utf-8')
    temporary.replace(path)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def finite(value):
    return isinstance(value, (int, float)) and math.isfinite(value)


def energy_check(record):
    """Independently validate stored trapezoidal integration and sample coverage."""
    energy = record.get('energy') or {}
    samples = energy.get('samples') or []
    if not energy.get('available'):
        return dict(valid=False, reason=energy.get('reason') or 'Energy unavailable')
    if len(samples) < 2 or energy.get('read_errors'):
        return dict(valid=False, reason='Incomplete or failed sampling')
    if any(not finite(s.get('t')) or not finite(s.get('power_w'))
           or s['power_w'] <= 0 for s in samples):
        return dict(valid=False, reason='Invalid sample values')
    gaps = [b['t'] - a['t'] for a, b in zip(samples, samples[1:])]
    hz = energy.get('sample_hz', 10.0)
    if not finite(hz) or hz <= 0 or min(gaps) <= 0 or max(gaps) > max(1.0, 5.0 / hz):
        return dict(valid=False, reason='Nonmonotonic or incomplete sample coverage')
    duration = samples[-1]['t'] - samples[0]['t']
    calculated = sum((a['power_w'] + b['power_w']) * (b['t'] - a['t']) / 2
                     for a, b in zip(samples, samples[1:]))
    if not finite(energy.get('joules')) or not math.isclose(
            calculated, energy['joules'], rel_tol=1e-9, abs_tol=1e-8):
        return dict(valid=False, reason='Stored joules disagree with power samples')
    if abs(duration - record['wall_time_s']) > max(0.25, 0.05 * record['wall_time_s']):
        return dict(valid=False, reason='Power duration does not cover measured generation')
    return dict(valid=True, recomputed_joules=calculated, duration_s=duration,
                max_gap_s=max(gaps), n_samples=len(samples), source=energy.get('source'))


def diagnostics(record):
    lookahead = record.get('lookahead') or {}
    events = lookahead.get('events') or []
    decisions = lookahead.get('decisions') or []
    counts = Counter(str(d['h']) for d in decisions if 'h' in d)
    if not counts:
        counts = Counter(str(e.get('requested_tokens', '?')) for e in events)
    rounds = record.get('rounds') or []
    return dict(h_counts=dict(sorted(counts.items())),
                h_count_basis='controller decisions' if decisions else 'launched events',
                background_generated_tokens=lookahead.get('generated_tokens', sum(e.get('generated_tokens', 0) for e in events)),
                reused_tokens=lookahead.get('reused_tokens', sum(e.get('reused_tokens', 0) for e in events)),
                discarded_tokens=lookahead.get('discarded_tokens', sum(e.get('discarded_tokens', 0) for e in events)),
                unused_tokens=lookahead.get('unused_tokens', sum(e.get('unused_tokens', 0) for e in events)),
                background_wait_ms=lookahead.get('wait_ms', sum(e.get('wait_ms', 0.0) for e in events)),
                background_service_ms=lookahead.get('service_ms', sum(e.get('service_ms', 0.0) for e in events)),
                n_rounds=len(rounds),
                foreground_draft_ms=sum(r.get('draft_ms', 0.0) for r in rounds),
                cloud_verify_ms=sum(r.get('cloud_verify_ms', 0.0) for r in rounds),
                injected_network_ms=sum(r.get('injected_network_ms', 0.0) for r in rounds),
                round_total_ms=sum(r.get('round_total_ms', 0.0) for r in rounds),
                n_proposed=sum(r.get('n_proposed', 0) for r in rounds),
                n_accepted=sum(r.get('n_accepted', 0) for r in rounds))


def aggregate(records):
    if not records:
        return None
    tokens = sum(r['output_tokens'] for r in records)
    wall = sum(r['wall_time_s'] for r in records)
    checks = [energy_check(r) for r in records]
    valid_energy = all(c['valid'] for c in checks)
    joules = sum(c['recomputed_joules'] for c in checks) if valid_energy else None
    power_duration = sum(c['duration_s'] for c in checks) if valid_energy else None
    scores = [r.get('task_quality') for r in records]
    all_scores = all(s is not None for s in scores)
    counts = Counter()
    diag = [diagnostics(r) for r in records]
    for d in diag:
        counts.update(d['h_counts'])
    extra = {key: sum(d[key] for d in diag) for key in diag[0]
             if key not in ('h_counts', 'h_count_basis')}
    return dict(requests=len(records), prompts=len({r['request_index'] for r in records}),
                output_tokens=tokens, wall_time_s=wall,
                throughput_tps=tokens / wall if wall else None,
                mean_latency_s=wall / len(records),
                quality=sum(scores) / len(scores) if all_scores else None,
                correct=sum(s == 1 for s in scores),
                truncated=sum(bool(r.get('truncated')) for r in records),
                exact_reference_matches=sum(r.get('output_ids') == r.get('reference_ids') for r in records),
                energy_valid_requests=sum(c['valid'] for c in checks),
                joules=joules, joules_per_token=joules / tokens if joules is not None and tokens else None,
                joules_per_request=joules / len(records) if joules is not None else None,
                avg_watts=joules / power_duration if joules is not None and power_duration else None,
                h_counts=dict(sorted(counts.items())), **extra)


def percentile(values, q):
    ordered = sorted(values)
    position = (len(ordered) - 1) * q
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (position - lower)


def effect(base, candidate, multiplicities=None):
    """Aggregate ratios; bootstrap weights entire prompt clusters, never rounds."""
    weights = multiplicities or {r['request_index']: 1 for r in base}
    bt = sum(r['output_tokens'] * weights.get(r['request_index'], 0) for r in base)
    ct = sum(r['output_tokens'] * weights.get(r['request_index'], 0) for r in candidate)
    bw = sum(r['wall_time_s'] * weights.get(r['request_index'], 0) for r in base)
    cw = sum(r['wall_time_s'] * weights.get(r['request_index'], 0) for r in candidate)
    speed = ((ct / cw) / (bt / bw) - 1) * 100
    checks = [energy_check(r) for r in base + candidate]
    if not all(c['valid'] for c in checks):
        return speed, None
    bj = sum(r['energy']['joules'] * weights.get(r['request_index'], 0) for r in base)
    cj = sum(r['energy']['joules'] * weights.get(r['request_index'], 0) for r in candidate)
    saving = (1 - (cj / ct) / (bj / bt)) * 100
    return speed, saving


def compare(records, baseline, candidate, scenarios, draws=2000, seed=42):
    lookup = {(r['request_index'], r['scenario'], r['method']): r for r in records}
    indices = sorted({r['request_index'] for r in records})
    complete = [i for i in indices if all((i, s, m) in lookup
                for s in scenarios for m in (baseline, candidate))]
    if not complete:
        return None
    base = [lookup[i, s, baseline] for i in complete for s in scenarios]
    cand = [lookup[i, s, candidate] for i in complete for s in scenarios]
    point_speed, point_saving = effect(base, cand)
    # Cache prompt-cluster sums: resampling whole prompts across both scenarios
    # preserves within-prompt correlation without repeatedly parsing power traces.
    clusters = []
    have_energy = point_saving is not None
    for i in complete:
        br = [lookup[i, s, baseline] for s in scenarios]
        cr = [lookup[i, s, candidate] for s in scenarios]
        clusters.append((sum(r['output_tokens'] for r in br),
                         sum(r['wall_time_s'] for r in br),
                         sum(r['output_tokens'] for r in cr),
                         sum(r['wall_time_s'] for r in cr),
                         sum(r['energy']['joules'] for r in br) if have_energy else 0,
                         sum(r['energy']['joules'] for r in cr) if have_energy else 0))
    rng = random.Random(seed)
    speeds, savings = [], []
    for _ in range(draws):
        sampled = [clusters[rng.randrange(len(clusters))] for _ in clusters]
        bt, bw, ct, cw, bj, cj = [sum(c[j] for c in sampled) for j in range(6)]
        speeds.append(((ct / cw) / (bt / bw) - 1) * 100)
        if have_energy:
            savings.append((1 - (cj / ct) / (bj / bt)) * 100)
    paired_gains = [(c['output_tokens'] / c['wall_time_s']) /
                    (b['output_tokens'] / b['wall_time_s']) * 100 - 100
                    for b, c in zip(base, cand)]
    quality_comparable = all(r.get('task_quality') is not None for r in base + cand)
    quality_declines = sum(c['task_quality'] < b['task_quality'] for b, c in zip(base, cand)) if quality_comparable else None
    more_truncations = sum(bool(c.get('truncated')) and not bool(b.get('truncated'))
                           for b, c in zip(base, cand))
    sequence_changes = sum(c.get('output_ids') != b.get('output_ids') for b, c in zip(base, cand))
    return dict(baseline=baseline, candidate=candidate, scenarios=list(scenarios),
                independent_prompts=len(complete), request_pairs=len(base), prompt_indices=complete,
                throughput_gain_pct=point_speed,
                throughput_gain_ci95_pct=[percentile(speeds, 0.025), percentile(speeds, 0.975)],
                mean_paired_throughput_gain_pct=statistics.mean(paired_gains),
                energy_saving_pct=point_saving,
                energy_saving_ci95_pct=[percentile(savings, 0.025), percentile(savings, 0.975)] if savings else None,
                quality_declines=quality_declines, additional_truncations=more_truncations,
                changed_output_sequences=sequence_changes,
                no_observed_quality_regression=quality_declines == 0 and more_truncations == 0,
                target_point_estimate=(point_speed > 5 and point_saving is not None and point_saving > 0
                                       and quality_declines == 0 and more_truncations == 0),
                target_supported_by_ci=(percentile(speeds, 0.025) > 5 and savings
                                        and percentile(savings, 0.025) > 0
                                        and quality_declines == 0 and more_truncations == 0) is True,
                bootstrap=dict(unit='independent prompt; all scenarios kept together',
                               draws=draws, seed=seed, kind='paired percentile',
                               warning='Exploratory interval; no multiplicity adjustment or quality guarantee'))


def format_number(value, places=3):
    return 'N/A' if value is None else f'{value:.{places}f}'


def report(directory):
    directory = Path(directory).resolve()
    plan_path = directory / 'config/protocol.json'
    protocol = json.loads(plan_path.read_text(encoding='utf-8')) if plan_path.exists() else {}
    records = []
    for path in sorted((directory / 'raw').glob('*.json')):
        record = json.loads(path.read_text(encoding='utf-8'))
        if 'wall_time_s' in record and 'output_tokens' in record:
            if record['wall_time_s'] <= 0 or record['output_tokens'] <= 0:
                raise ValueError(f'Invalid successful request: {path}')
            records.append(record)
    keys = [(r['request_index'], r['scenario'], r['method']) for r in records]
    if len(keys) != len(set(keys)):
        raise ValueError('Duplicate prompt/scenario/method records; single-repeat protocol violated')
    status_path = directory / 'report/status.json'
    status = json.loads(status_path.read_text(encoding='utf-8')) if status_path.exists() else {}
    expected = protocol.get('expected_requests', status.get('expected', len(records)))
    methods = protocol.get('methods') or [m for m in METHODS if any(r['method'] == m for r in records)]
    scenarios = list((protocol.get('network_scenarios') or {}).keys()) or list(SCENARIOS)
    primary_scenarios=protocol.get('primary_scenarios',scenarios)
    summaries = {}
    comparisons = {}
    for scenario in scenarios + ['pooled']:
        group = [r for r in records if r['scenario'] in primary_scenarios] if scenario == 'pooled' else [r for r in records if r['scenario'] == scenario]
        summaries[scenario] = {m: aggregate([r for r in group if r['method'] == m]) for m in methods}
        comparisons[scenario] = {}
        for base, cand in [('fixed', 'original')] + [
                (base, candidate) for candidate in ('buffered', 'streaming', 'joint', 'fixed_g2', 'fixed_g6', 'fixed_fast', 'regime')
                for base in ('fixed', 'original') if base != candidate] + [('fixed_g2','joint'), ('fixed_g6','joint'), ('fixed_fast','regime')]:
            if base in methods and cand in methods:
                result = compare(records, base, cand, primary_scenarios if scenario == 'pooled' else [scenario])
                if result:
                    comparisons[scenario][f'{cand}_vs_{base}'] = result
    validation = {r['id']: energy_check(r) for r in records}
    complete = len(records) == expected and not status.get('failures') and status.get('state') == 'complete'
    target_candidate = protocol.get('target_candidate', 'joint' if 'joint' in methods else 'streaming' if 'streaming' in methods else 'buffered')
    main = comparisons.get('pooled', {}).get(target_candidate+'_vs_fixed')
    pooled_point = bool(complete and main and main['target_point_estimate'])
    pooled_ci = bool(complete and main and main['target_supported_by_ci'])
    request_table = [dict(id=r['id'], scenario=r['scenario'], method=r['method'],
                          request_index=r['request_index'], output_tokens=r['output_tokens'],
                          wall_time_s=r['wall_time_s'], throughput_tps=r['output_tokens'] / r['wall_time_s'],
                          task_quality=r.get('task_quality'), truncated=r.get('truncated'),
                          exact_reference_match=r.get('output_ids') == r.get('reference_ids'),
                          joules=r['energy'].get('joules'),
                          joules_per_token=r['energy'].get('joules_per_token'),
                          energy_valid=validation[r['id']]['valid'], **diagnostics(r)) for r in records]
    result = dict(phase=protocol.get('phase', directory.name), artifact_directory=str(directory),
                  regenerated_at_utc=datetime.now(timezone.utc).isoformat(),
                  expected_requests=expected, completed_requests=len(records), complete=complete,
                  status=status, summaries=summaries, comparisons=comparisons,
                  energy_validation=validation, per_request=request_table,
                  target=dict(candidate=target_candidate, point_estimate_met=pooled_point, ci_supported=pooled_ci,
                              criterion='Pooled equal-prompt low/high throughput gain >5%, Jetson J/token saving >0%, no observed paired quality decline or additional truncation',
                              confirmation=protocol.get('phase_role', 'Unspecified; treat as development')),
                  notes=['Jetson gross board input energy only; cloud/network energy not measured.',
                         'Reference generation is excluded from timed/energy generation.',
                         'Request wall time includes waiting and terminal background drain.',
                         'Exactly one observation per prompt/scenario/method; bootstrap clusters independent prompts.',
                         'Pooled totals include both scenarios equally by prompt count when the complete protocol succeeds.',
                         'Paired comparisons use only prompts complete for all included scenarios and both methods.',
                         'Failed/incomplete phases cannot satisfy the target; no failed request is silently deleted.',
                         'Sequence agreement between methods is distinct from agreement with cloud AR reference.',
                         'Background service and verification overlap; their times must not be added as a latency decomposition.'])
    write_json(directory / 'results.json', result)
    write_json(directory / 'tables/per_request.json', request_table)
    lines = [f'# AdaptiveLookahead research: {result["phase"]}', '',
             f'Completed **{len(records)}/{expected}** timed requests. Phase state: **{status.get("state", "unknown")}**.',
             f'Phase role: {protocol.get("phase_role", "Unspecified; development only")}.', '',
             f'Primary pooled scenarios: {primary_scenarios}. Any additional delay scenario is reported separately and excluded from the primary target.', '',
             'One repeat, strict K=1; fixed and fixed_fast use gamma=4/h=5, while regime adapts gamma/h. Throughput = total output tokens / total request wall time. Historical method labels in archived reports describe their frozen configurations.', '',
             '| Scenario | Method | Requests | Tokens/s | Mean latency (s) | J/token | J/request | Mean W | Correct | Truncated |',
             '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for scenario, group in summaries.items():
        for method, s in group.items():
            if s:
                correct = f'{s["correct"]}/{s["requests"]}' if s['quality'] is not None else 'N/A'
                lines.append(f'| {scenario} | {method} | {s["requests"]} | {format_number(s["throughput_tps"])} | {format_number(s["mean_latency_s"])} | {format_number(s["joules_per_token"], 4)} | {format_number(s["joules_per_request"])} | {format_number(s["avg_watts"])} | {correct} | {s["truncated"]} |')
    lines.extend(['', 'Paired aggregate effects; brackets are 95% prompt-cluster bootstrap intervals (2,000 draws, seed 42). Positive energy saving means lower J/token.', '',
                  '| Scenario | Comparison | Prompts | Throughput gain % [95% CI] | J/token saving % [95% CI] | Quality declines | Extra truncations | Changed sequences |',
                  '|---|---|---:|---|---|---:|---:|---:|'])
    for scenario, group in comparisons.items():
        for key, c in group.items():
            speed = f'{c["throughput_gain_pct"]:.2f} [{c["throughput_gain_ci95_pct"][0]:.2f}, {c["throughput_gain_ci95_pct"][1]:.2f}]'
            energy = ('N/A' if c['energy_saving_pct'] is None else
                      f'{c["energy_saving_pct"]:.2f} [{c["energy_saving_ci95_pct"][0]:.2f}, {c["energy_saving_ci95_pct"][1]:.2f}]')
            lines.append(f'| {scenario} | {key} | {c["independent_prompts"]} | {speed} | {energy} | {c["quality_declines"]} | {c["additional_truncations"]} | {c["changed_output_sequences"]} |')
    lines.extend(['', f'**Target point estimate met: {pooled_point}. Supported by these bootstrap intervals: {pooled_ci}.**',
                  'A development-phase result is not held-out confirmation; a small sample cannot establish general quality preservation.', '',
                  '| Scenario | Method | h selections/events | Background tokens | Reused | Discarded | Background wait (ms) | Exact cloud-reference matches | Valid energy requests |',
                  '|---|---|---|---:|---:|---:|---:|---:|---:|'])
    for scenario, group in summaries.items():
        for method, s in group.items():
            if s:
                lines.append(f'| {scenario} | {method} | {json.dumps(s["h_counts"], sort_keys=True)} | {s["background_generated_tokens"]} | {s["reused_tokens"]} | {s["discarded_tokens"]} | {format_number(s["background_wait_ms"])} | {s["exact_reference_matches"]}/{s["requests"]} | {s["energy_valid_requests"]}/{s["requests"]} |')
    lines.extend(['', 'For fixed lookahead, h counts cover launched events; controllers with decision traces include zero selections. EOS rounds may not launch work.', ''])
    lines.extend('- ' + note for note in result['notes'])
    if status.get('failures'):
        lines.extend(['', 'Failures retained in logs and report/status.json:', '',
                      '```json', json.dumps(status['failures'], indent=2), '```'])
    (directory / 'SUMMARY.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return result


def source_snapshot(directory):
    manifest = []
    for folder in ('edge', 'common', 'experiments'):
        for source in sorted((ROOT / folder).glob('*.py')):
            relative = source.relative_to(ROOT)
            target = directory / 'config/source' / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            manifest.append(dict(path=str(relative), sha256=sha256(source)))
    for relative in ('configs/experiment.defaults.json', 'configs/research.pilot.json', 'configs/models.yaml',
                     'configs/research.downloaded.gsm8k.json', 'configs/research.downloaded.humaneval.json',
                     'configs/research.downloaded.mtbench.json', 'run_downloaded_benchmarks.sh',
                     'edge/scripts/start_draft_server.sh'):
        source = ROOT / relative
        if source.exists():
            target = directory / 'config/source' / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            manifest.append(dict(path=relative, sha256=sha256(source)))
    write_json(directory / 'config/source_manifest.json', manifest)
    def git_output(arguments):
        result = subprocess.run(['git', *arguments], cwd=ROOT, capture_output=True, text=True, check=False)
        return dict(exit_code=result.returncode, stdout=result.stdout, stderr=result.stderr)
    write_json(directory / 'config/git.json', dict(
        head=git_output(['rev-parse', 'HEAD']), status=git_output(['status', '--short']),
        diff=git_output(['diff', '--', 'edge', 'common', 'experiments', 'configs'])))


def hardware_snapshot():
    result = environment_snapshot()
    result['platform'] = platform.platform()
    result['kernel'] = platform.release()
    result['launch_environment_if_present'] = {name: os.environ[name] for name in (
        'CUDA_VISIBLE_DEVICES', 'SPECDECODE_DRAFT_NGL', 'SPECDECODE_DRAFT_CTX',
        'SPECDECODE_DRAFT_MODEL', 'LLAMA_ARG_MMAP') if name in os.environ}
    for key, path in [('memory', '/proc/meminfo'), ('uptime', '/proc/uptime')]:
        try:
            result[key] = Path(path).read_text()
        except (OSError, TypeError) as exc:
            result[key] = {'unavailable': str(exc)}
    result['thermal_zones'] = {}
    for zone in sorted(Path('/sys/class/thermal').glob('thermal_zone*')):
        try:
            result['thermal_zones'][zone.name] = dict(
                type=(zone / 'type').read_text().strip(),
                temperature_millidegrees=int((zone / 'temp').read_text().strip()))
        except (OSError, ValueError, TypeError):
            pass
    result['devfreq'] = {}
    for device in sorted(Path('/sys/class/devfreq').glob('*')):
        fields = {}
        for name in ('cur_freq', 'min_freq', 'max_freq', 'load', 'governor'):
            try:
                fields[name] = (device / name).read_text().strip()
            except (OSError, TypeError):
                pass
        if fields:
            result['devfreq'][device.name] = fields
    return result


def parse_indices(value):
    try:
        indices = [int(v.strip()) for v in value.split(',')]
    except ValueError as exc:
        raise argparse.ArgumentTypeError('Indices must be comma-separated integers') from exc
    if not indices or len(indices) != len(set(indices)) or any(i < 0 for i in indices):
        raise argparse.ArgumentTypeError('Indices must be unique nonnegative dataset-row indices')
    return indices


def balanced_method_orders(methods, count, rng):
    """Randomized Latin rotations balance each method's within-prompt position."""
    base=list(methods)
    rng.shuffle(base)
    orders=[]
    cycle=0
    while len(orders)<count:
        direction=base if cycle%2==0 else list(reversed(base))
        rotations=[direction[i:]+direction[:i] for i in range(len(base))]
        rng.shuffle(rotations)
        orders.extend(rotations)
        cycle+=1
    return orders[:count]


def research_method_config(config, method, compact_target=False):
    c=dict(config)
    if method in ('fixed_fast','regime'):
        c['DRAFT_N_PROBS']=0
        if compact_target:
            c.update(K_MAX=1,K_INITIAL=1,K_SWEEP=[1],FIXED_K=1)
    return validate(c)


def parser():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--report', type=Path, help='Regenerate an existing phase report; no model or sensor access')
    ap.add_argument('--phase', default='development')
    ap.add_argument('--phase-role', choices=['development', 'held-out-confirmation'], default='development',
                    help='Declare before running; the caller must ensure confirmation indices are unused')
    ap.add_argument('--indices', type=parse_indices, default=parse_indices('0,1,2,3'))
    ap.add_argument('--dataset', default='common/data/gsm8k_test_50.jsonl')
    ap.add_argument('--methods', nargs='+', choices=METHODS, default=['fixed', 'fixed_fast', 'regime'])
    ap.add_argument('--output-root', default='results/adaptive_research_20261007')
    ap.add_argument('--max-tokens', type=int, default=512)
    ap.add_argument('--buffer-max', type=int, default=10)
    ap.add_argument('--low-ms', type=float, default=2.0)
    ap.add_argument('--high-ms', type=float, default=100.0)
    ap.add_argument('--extra-delay-ms',type=float,
                    help='Optional very_high secondary scenario; excluded from the low/high primary pooled target')
    ap.add_argument('--config', default='configs/research.pilot.json')
    ap.add_argument('--draft-url', default='http://127.0.0.1:8080')
    ap.add_argument('--cloud-url', help='Defaults to the existing project configuration')
    ap.add_argument('--token-only-parser', action=argparse.BooleanOptionalAction, default=True,
                    help='Use formatting-only native parser for byte-fragment-safe exact token IDs, equally for all arms')
    ap.add_argument('--compact-target-logprobs', action='store_true',
                    help='For fixed_fast/regime, request target top1 instead of top4; acceptance remains strictK1')
    ap.add_argument('--plan', action='store_true', help='Print the fully resolved protocol without accessing services')
    return ap


def run_phase(args):
    from edge.experiment_live import LiveExperiment
    from common.result_metrics import enrich
    if len(args.methods) != len(set(args.methods)):
        raise ValueError('Method names must be unique')
    if args.max_tokens < 1 or args.buffer_max < 5:
        raise ValueError('max-tokens must be positive and buffer-max >=5')
    if any(not math.isfinite(v) or v < 0 for v in (args.low_ms, args.high_ms)):
        raise ValueError('Network injection must be finite and nonnegative')
    if not args.phase or any(ch not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-' for ch in args.phase):
        raise ValueError('Phase names may contain only letters, digits, underscore and hyphen')
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = ROOT / config_path
    c = load_config(config_path)
    c.update(N_REQUESTS=len(args.indices), REPEATS=1, GAMMA_INITIAL=4, FIXED_K=1,
             MAX_TOKENS=args.max_tokens, DRAFT_URL=args.draft_url,
             NETWORK_SCENARIOS={'low': {'rtt_ms': args.low_ms, 'jitter_ms': 0},
                                'high': {'rtt_ms': args.high_ms, 'jitter_ms': 0}})
    if args.extra_delay_ms is not None:
        if not math.isfinite(args.extra_delay_ms) or args.extra_delay_ms<0:
            raise ValueError('Extra delay must be finite and nonnegative')
        c['NETWORK_SCENARIOS']['very_high']={'rtt_ms':args.extra_delay_ms,'jitter_ms':0}
    if args.cloud_url:
        c['CLOUD_URL'] = args.cloud_url
    dataset_path = Path(args.dataset)
    if not dataset_path.is_absolute():
        dataset_path = ROOT / dataset_path
    c['DATASET'] = str(dataset_path.resolve())
    validate(c)
    dataset_bytes = dataset_path.read_bytes()
    samples = [json.loads(line) for line in dataset_bytes.decode('utf-8').splitlines() if line.strip()]
    if max(args.indices) >= len(samples):
        raise ValueError(f'Dataset has {len(samples)} nonempty rows, requested index {max(args.indices)}')
    rng = random.Random(c['SEED'])
    jobs = []
    for scenario in c['NETWORK_SCENARIOS']:
        indices = list(args.indices)
        rng.shuffle(indices)
        orders=balanced_method_orders(args.methods,len(indices),rng)
        for index,methods in zip(indices,orders):
            for method in methods:
                jobs.append(dict(id=f'{scenario}_p{index}_{method}', method=method,
                                 scenario=scenario, request_index=index, repeat=0))
    protocol = dict(phase=args.phase, phase_role=args.phase_role,
                    methods=list(args.methods), indices=args.indices, repeats=1,
                    target_candidate='regime' if 'regime' in args.methods else 'fixed_fast',
                    method_parameters={
                        'fixed':{'gamma':4,'h':5},
                        'fixed_fast':{'gamma':4,'h':5,'draft_n_probs':0,'target_probability_cap':1 if args.compact_target_logprobs else c['K_MAX']},
                        'regime':{'gamma_candidates':[4,6,8],'h':'gamma+1 on useful nonterminal rounds; measured latency regimes','draft_n_probs':0,'target_probability_cap':1 if args.compact_target_logprobs else c['K_MAX'],'K':1}},
                    token_only_parser=args.token_only_parser,
                    compact_target_logprobs=args.compact_target_logprobs,
                    order_design='Randomized Latin rotations; method position counts differ by at most1',
                    gamma=4, strict_k=1, fixed_lookahead=5, buffer_max=args.buffer_max,
                    seed=c['SEED'], network_scenarios=c['NETWORK_SCENARIOS'],
                    primary_scenarios=['low','high'],
                    expected_requests=len(jobs), job_order=jobs,
                    dataset_sha256=hashlib.sha256(dataset_bytes).hexdigest(),
                    primary_metric='Total output tokens / total measured request wall time',
                    energy_metric='Gross Jetson board input joules / total output tokens',
                    target='Pooled equal-prompt low/high throughput improvement >5% versus h=5, lower J/token, no observed quality decline or additional truncation',
                    bootstrap=dict(draws=2000, seed=42, unit='independent prompt; both scenarios together'),
                    stopping='Development iteration; held-out confirmation must be declared and separately reserved',
                    reference_timing='All cloud reference generations precede the timed request jobs',
                    warmup='Service loading and health checks excluded; no benchmark warmup requests',
                    disclaimer='Cooperative locks isolate host-local participating runners, not other clients of the remote GPU')
    if args.plan:
        print(json.dumps(dict(config=c, protocol=protocol), ensure_ascii=False, indent=2))
        return None
    output_root = Path(args.output_root)
    if not output_root.is_absolute():
        output_root = ROOT / output_root
    directory = output_root / (args.phase + '_' + datetime.now().strftime('%Y%m%d_%H%M%S_%f') + '_' + uuid.uuid4().hex[:8])
    for name in ('config', 'raw', 'logs', 'tables', 'report'):
        (directory / name).mkdir(parents=True, exist_ok=False)
    print(f'Artifacts: {directory.resolve()}', flush=True)
    write_json(directory / 'config/resolved.json', c)
    write_json(directory / 'config/input.json', dict(path=str(config_path.resolve()),
               sha256=sha256(config_path), content=json.loads(config_path.read_text(encoding='utf-8'))))
    write_json(directory / 'config/protocol.json', protocol)
    write_json(directory / 'config/command.json', dict(argv=sys.argv, cwd=str(Path.cwd()), executable=sys.executable))
    write_json(directory / 'config/dataset.json', dict(path=str(dataset_path.resolve()),
                sha256=protocol['dataset_sha256'], selected_rows=[dict(index=i, example=samples[i]) for i in args.indices]))
    source_snapshot(directory)
    live = None
    lock = None
    status = dict(state='starting', expected=len(jobs), completed=0, failures=[],
                  started_at_utc=datetime.now(timezone.utc).isoformat())
    write_json(directory / 'report/status.json', status)
    try:
        lock = ServiceLocks([c['DRAFT_URL'], c['CLOUD_URL']], str(directory.resolve())).acquire()
        write_json(directory / 'config/hardware_start.json', hardware_snapshot())
        live = LiveExperiment(c)
        live.energy_mode = 'auto'
        live.client.token_only_parser = args.token_only_parser
        write_json(directory / 'config/service_info.json', live.info)
        write_json(directory / 'config/model_pair.json', live.model)
        write_json(directory / 'config/draft_props.json', live.client.props())
        with live.energy_profiler() as sensor:
            time.sleep(0.15)
        sensor_check = sensor.record(0)
        write_json(directory / 'config/power_preflight.json', sensor_check)
        if not sensor_check['available']:
            raise RuntimeError('Real local-board energy required: ' + str(sensor_check.get('reason')))
        for index in args.indices:
            ref_ids, ref_text = live.reference(samples[index], index)
            write_json(directory / 'config/references' / f'p{index}.json',
                       dict(request_index=index, reference_ids=ref_ids, reference_text=ref_text,
                            reference_stop_reason=live.reference_stops[index]))
        status['state'] = 'running'
        for position, job in enumerate(jobs):
            status['current_job'] = job
            write_json(directory / 'report/status.json', status)
            print(f'[{position + 1}/{len(jobs)}] {job["id"]}: starting', flush=True)
            try:
                index, scenario = job['request_index'], c['NETWORK_SCENARIOS'][job['scenario']]
                method_config=research_method_config(c,job['method'],args.compact_target_logprobs)
                if job['method'] in ('fixed', 'fixed_fast'):
                    previous_probs = live.client.draft_n_probs
                    previous_config=live.c
                    live.c=method_config
                    live.client.draft_n_probs = 0 if job['method']=='fixed_fast' else c.get('DRAFT_N_PROBS',1)
                    try:
                        record = live.run_lookahead(samples[index], index, scenario, 4, 5)
                    finally:
                        live.client.draft_n_probs = previous_probs
                        live.c=previous_config
                else:
                    from edge.edge_client_regime import LatencyRegimeLookaheadClient
                    candidate_class = LatencyRegimeLookaheadClient
                    previous = live.client
                    candidate = candidate_class(c['DRAFT_URL'], method_config, max_lookahead=args.buffer_max)
                    candidate.stop_strings = live.model.get('stop_strings', [])
                    candidate.token_only_parser = args.token_only_parser
                    if job['method']=='regime':
                        candidate.draft_n_probs = 0
                    live.client = candidate
                    try:
                        record = live.run('strict', False, 4, 1, samples[index], index, scenario)
                        record['lookahead'] = candidate.last_lookahead
                    finally:
                        candidate._session.close()
                        live.client = previous
                record.update(job, mode='real', configured_gamma=(None if job['method']=='regime' else 4), configured_k=1,
                              configured_draft_n_probs=(0 if job['method'] in ('fixed_fast','regime') else c.get('DRAFT_N_PROBS',1)),
                              configured_target_probability_cap=method_config['K_MAX'],
                              adaptive_window=False, phase=args.phase, configured_buffer_max=args.buffer_max)
                enrich(record)
                settings=record['lookahead'].get('backend_settings',{})
                record['draft_backend_settings_valid']=(bool(settings.get('foreground')) and all(
                    values is None or values.get('n_probs')==record['configured_draft_n_probs']
                    for values in settings.values()))
                record['energy_validation'] = energy_check(record)
                write_json(directory / 'raw' / (job['id'] + '.json'), record)
                status['completed'] += 1
                if not record['draft_backend_settings_valid']:
                    raise RuntimeError('Draft backend reported an unexpected probability-output setting')
                # Preserve invalid-energy measurements, but stop rather than
                # continue an energy study whose primary metric is unavailable.
                if not record['energy_validation']['valid']:
                    raise RuntimeError('Power record failed validation: ' + record['energy_validation']['reason'])
                print(f'{job["id"]}: {record["output_tokens"] / record["wall_time_s"]:.3f} token/s; '
                      f'{record["energy"]["joules_per_token"]:.4f} J/token; quality={record["task_quality"]}; '
                      f'truncated={record["truncated"]}', flush=True)
                write_json(directory / 'report/status.json', status)
            except BaseException as exc:
                failure = dict(job=job, error_type=type(exc).__name__, error=str(exc),
                               raw_record_retained=(directory / 'raw' / (job['id'] + '.json')).exists())
                status['failures'].append(failure)
                (directory / 'logs' / (job['id'] + '.log')).write_text(traceback.format_exc(), encoding='utf-8')
                raise
        status['state'] = 'complete'
    except BaseException as exc:
        status['state'] = 'interrupted' if isinstance(exc, KeyboardInterrupt) else 'failed'
        if not status['failures']:
            status['failures'].append(dict(stage='startup_or_reference', error_type=type(exc).__name__, error=str(exc)))
        (directory / 'logs/pipeline.log').write_text(traceback.format_exc(), encoding='utf-8')
        raise
    finally:
        status['finished_at_utc'] = datetime.now(timezone.utc).isoformat()
        status.pop('current_job', None)
        write_json(directory / 'report/status.json', status)
        if live is not None:
            live.client._session.close()
            live.remote._session.close()
        if lock is not None:
            write_json(directory / 'config/hardware_end.json', hardware_snapshot())
            lock.close()
        result = report(directory)
        print(f'Summary: {directory.resolve() / "SUMMARY.md"}', flush=True)
        print(f'Target point estimate met: {result["target"]["point_estimate_met"]}', flush=True)
    return directory


def main():
    args = parser().parse_args()
    if args.report:
        result = report(args.report)
        print(f'Summary: {Path(args.report).resolve() / "SUMMARY.md"}')
        print(json.dumps(result['target'], indent=2))
    else:
        run_phase(args)


if __name__ == '__main__':
    main()
