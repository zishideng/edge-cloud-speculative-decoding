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


def audit(source, output_root, sd_only=False):
    out = create_output(output_root)
    records, provenance = [], []
    for path in sorted((source/'raw').glob('*.json')):
        data = path.read_bytes()
        record = json.loads(data)
        if 'method' not in record or 'rounds' not in record:
            continue
        if sd_only and record['method'] == 'cloud_AR':
            continue
        record['exact_match'] = record['output_ids'] == record['reference_ids']
        round_ms = sum(row['round_total_ms'] for row in record['rounds'])
        record['trace_oracle_tokens_per_second'] = (
            1000*sum(row['n_proposed']+1 for row in record['rounds'])/round_ms if round_ms else None)
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
                       'relaxed_acceptance_rate', 'truncated', 'quality_spent','trace_oracle_tokens_per_second'):
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
    cloud = {(r['scenario'],r['repeat'],r['request_index']):r for r in records if r['method']=='cloud_AR'}
    oracle_rows=[]
    for r in records:
        ar=cloud.get((r['scenario'],r['repeat'],r['request_index']))
        if ar and r['trace_oracle_tokens_per_second'] is not None:
            oracle_rows.append(dict(id=r['id'],scenario=r['scenario'],method=r['method'],
                prompt_index=r['request_index'],repeat=r['repeat'],measured_tps=r['tokens_per_second'],
                trace_oracle_tps=r['trace_oracle_tokens_per_second'],cloud_ar_tps=ar['tokens_per_second'],
                trace_oracle_vs_ar=r['trace_oracle_tokens_per_second']/ar['tokens_per_second']))
    if oracle_rows:
        write_csv(out/'tables/trace_oracle.csv',oracle_rows)
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
    fig.suptitle(f'Descriptive diagnostics: {n_prompts} prompts; pooled descriptive rates, not independent trials')
    fig.tight_layout()
    fig.savefig(out/'figures/correctness.png',dpi=160)
    fig.savefig(out/'figures/correctness.svg')
    plt.close(fig)
    # Primary outcomes after the researcher clarified that token equality is not required.
    fig, axes = plt.subplots(1,2,figsize=(12,4))
    scenarios=sorted({r['scenario'] for r in baseline})
    width=.8/max(1,len(scenarios))
    for si,scenario in enumerate(scenarios):
        for ax,metric,title in zip(axes,('tokens_per_second','task_quality'),
                                   ('Request throughput','GSM8K final-answer accuracy')):
            values=[mean(r[metric] for r in baseline if r['method']==m and r['scenario']==scenario) for m in methods]
            ax.bar([i+si*width for i in range(len(methods))],values,width=width,label=scenario)
            ax.set_xticks([i+(len(scenarios)-1)*width/2 for i in range(len(methods))],methods)
            ax.set_title(title)
    axes[0].set_ylabel('Tokens/s');axes[1].set_ylim(0,1.05);axes[0].legend()
    fig.suptitle(f'{n_prompts} independent prompts; descriptive means (paired uncertainty in tables)')
    fig.tight_layout()
    for extension in ('png','svg'):
        fig.savefig(out/'figures'/f'quality_performance.{extension}',dpi=160)
    plt.close(fig)
    lines = ['# Task-quality and performance evidence audit', '', f'Source: `{source}`', '',
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
    if oracle_rows:
        lines += ['', '## Optimistic acceptance-only trace replay', '',
            f'{sum(r["trace_oracle_vs_ar"]<1 for r in oracle_rows)}/{len(oracle_rows)} SD traces remain below paired cloud AR throughput',
            'even when every recorded round is credited with gamma+1 tokens at its recorded cost.',
            'This deliberately optimistic replay removes all draft rejection and excludes request setup costs.',
            'It freezes the observed gamma, context and timing trajectories. It is NOT a universal upper bound:',
            'a new policy can change future contexts, round costs, cache behavior and stopping length.',
            'The replay tests whether acceptance improvements alone are sufficient on the recorded cost trajectories.']
    (out/'report/audit.md').write_text('\n'.join(lines)+'\n')
    print(out.resolve())
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--output-root', default='results')
    parser.add_argument('--sd-only', action='store_true', help='Compare speculative-decoding methods only')
    args = parser.parse_args()
    audit(args.source, args.output_root, args.sd_only)
