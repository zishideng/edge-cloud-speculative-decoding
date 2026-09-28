"""Read-only audit of raw experiment records; output goes to a new directory."""
import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean, median, stdev

from analysis.paired import paired_comparisons
from experiments.run import create_output, write_csv, write_json


def summarize(values):
    return dict(mean=mean(values), median=median(values),
                std=stdev(values) if len(values) > 1 else None,
                min=min(values), max=max(values), n=len(values))


def audit(source, output_root):
    out = create_output(output_root)
    records, provenance = [], []
    for path in sorted((source/'raw').glob('*.json')):
        data = path.read_bytes()
        record = json.loads(data)
        if 'method' not in record or 'rounds' not in record:
            continue
        record['exact_match'] = record['output_ids'] == record['reference_ids']
        for key in ('draft_ms', 'cloud_verify_ms', 'cloud_queue_ms', 'network_rtt_ms',
                    'serialize_ms', 'deserialize_ms', 'round_total_ms'):
            record['sum_'+key] = sum(row[key] for row in record['rounds'])
        record['unattributed_ms'] = 1000 * record['wall_time_s'] - sum(record['sum_'+key]
            for key in ('draft_ms', 'cloud_verify_ms', 'cloud_queue_ms', 'network_rtt_ms',
                        'serialize_ms', 'deserialize_ms'))
        provenance.append(dict(path=str(path), sha256=hashlib.sha256(data).hexdigest()))
        # Summary needs no per-token details after their sums are captured.
        records.append({k:v for k,v in record.items() if k not in
                        ('rounds','output_ids','reference_ids','output_text','reference_text')})
    if not records:
        raise ValueError('No supported records')
    write_json(out/'config/source_manifest.json', provenance)
    groups = defaultdict(list)
    for record in records:
        groups[record['scenario'],record['method']].append(record)
    summary, profile = [], []
    for (scenario, method), group in sorted(groups.items()):
        for metric in ('wall_time_s', 'tokens_per_second', 'ttft_ms', 'tpot_ms',
                       'task_quality', 'reference_quality', 'exact_match', 'accepted_proposed_ratio',
                       'relaxed_acceptance_rate', 'truncated', 'quality_spent'):
            values = [r[metric] for r in group if r.get(metric) is not None]
            if values:
                summary.append(dict(scenario=scenario, method=method, metric=metric,
                                    **summarize(values)))
        total_ms = sum(r['wall_time_s'] for r in group)*1000
        if method == 'cloud_AR':
            continue  # AR has separate timing scope and no SD round components.
        for metric in ('draft_ms','cloud_verify_ms','cloud_queue_ms','network_rtt_ms',
                       'serialize_ms','deserialize_ms','unattributed_ms'):
            key = metric if metric == 'unattributed_ms' else 'sum_'+metric
            total = sum(r[key] for r in group)
            profile.append(dict(scenario=scenario,method=method,component=metric,
                                total_ms=total,wall_fraction=total/total_ms))
    write_csv(out/'tables/summary.csv', summary)
    write_csv(out/'tables/profile.csv', profile)
    write_csv(out/'tables/paired.csv', paired_comparisons(records))
    write_csv(out/'tables/requests.csv', records)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    methods = [m for m in ('cloud_AR','A','B','C','Proposed') if any(r['method']==m for r in records)]
    baseline = [r for r in records if r['method'] in methods]
    fig, axes = plt.subplots(1,2,figsize=(10,4))
    for ax, metric, title in zip(axes, ('exact_match','task_quality'),
                               ('Exact token agreement with AR','GSM8K final-answer accuracy')):
        values = [mean(r[metric] for r in baseline if r['method']==m) for m in methods]
        ax.bar(methods,values); ax.set_ylim(0,1.05); ax.set_title(title)
    n_prompts = len({r['request_index'] for r in records})
    fig.suptitle(f'Historical audit: {n_prompts} prompts; pooled descriptive rates, not independent trials')
    fig.tight_layout()
    fig.savefig(out/'figures/correctness.png',dpi=160)
    fig.savefig(out/'figures/correctness.svg')
    plt.close(fig)
    lines = ['# Historical evidence audit', '', f'Source: `{source}`', '',
        f'Records: {len(records)}; independent prompts: {len({r["request_index"] for r in records})}.',
        'Repeated prompts and network scenarios must not be counted as independent quality samples.', '',
        '| Method | Runs | Exact matches | Accuracy |', '|---|---:|---:|---:|']
    for method in methods:
        group = [r for r in baseline if r['method']==method]
        lines.append(f'| {method} | {len(group)} | {sum(r["exact_match"] for r in group)} | '
                     f'{mean(r["task_quality"] for r in group):.6f} |')
    lines += ['', '## Task quality and performance by condition', '',
        '| Scenario | Method | Requests | Latency mean (s) | TPS mean | TPS median | TPS std | Accuracy | Truncation |',
        '|---|---|---:|---:|---:|---:|---:|---:|---:|']
    for (scenario, method), group in sorted(groups.items()):
        rates = summarize([r['tokens_per_second'] for r in group])
        quality = [r['task_quality'] for r in group if r.get('task_quality') is not None]
        truncation = [r['truncated'] for r in group if r.get('truncated') is not None]
        lines.append(f'| {scenario} | {method} | {len(group)} | {mean(r["wall_time_s"] for r in group):.3f} | '
                     f'{rates["mean"]:.3f} | {rates["median"]:.3f} | {rates["std"] if rates["std"] is not None else "N/A"} | '
                     f'{mean(quality) if quality else "N/A"} | {mean(truncation) if truncation else "N/A"} |')
    lines += ['', 'Acceptance budget limits cumulative local logprob regret; it does not certify answer accuracy.',
        'Strict token mismatch is a diagnostic finding, not proof of its cause.',
        'Profile network time is an HTTP residual estimate. Unattributed time includes request setup,',
        'detokenization, control logic, sleeps/timers, and any measurement residual; it is not GPU synchronization time.',
        f'Per-scenario paired bootstrap uses {n_prompts} prompt clusters; small-sample uncertainty remains substantial.',
        'Token equality is diagnostic, not a requirement. Task quality and latency/throughput are primary.',
        'Cloud AR TTFT/TPOT are unavailable for its non-streaming endpoint; no SD component profile is assigned to AR.',
        'Source files were not rewritten. SHA-256 provenance is in config/source_manifest.json.']
    (out/'report/audit.md').write_text('\n'.join(lines)+'\n')
    print(out.resolve())
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--output-root', default='results')
    args = parser.parse_args()
    audit(args.source, args.output_root)
