"""Compare fixed-lookahead SD with paired synchronous SD controls."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import random
from statistics import mean

from common.metrics import percentile
from experiments.run import create_output, write_csv, write_json


def report(source,output_root):
    out=create_output(output_root)
    protocol=json.loads((source/'config/protocol.json').read_text())
    groups=defaultdict(dict); manifest=[]
    for path in sorted((source/'raw').glob('*.json')):
        data=path.read_bytes();r=json.loads(data)
        groups[r['scenario'],r['request_index'],r['repeat']][r['method']]=r
        manifest.append(dict(path=str(path),sha256=hashlib.sha256(data).hexdigest()))
    write_json(out/'config/source_manifest.json',manifest)
    pairs=[]
    for (scenario,index,repeat),variants in sorted(groups.items()):
        if set(variants)!={'control','candidate'}:continue
        a,b=variants['control'],variants['candidate'];stats=b['lookahead']
        pairs.append(dict(scenario=scenario,prompt_index=index,repeat=repeat,
            throughput_gain=b['tokens_per_second']/a['tokens_per_second']-1,
            latency_reduction=1-b['wall_time_s']/a['wall_time_s'],
            control_tps=a['tokens_per_second'],candidate_tps=b['tokens_per_second'],
            control_latency_s=a['wall_time_s'],candidate_latency_s=b['wall_time_s'],
            control_quality=a['task_quality'],candidate_quality=b['task_quality'],
            quality_change=b['task_quality']-a['task_quality'],
            control_truncated=a['truncated'],candidate_truncated=b['truncated'],
            control_tokens=a['output_tokens'],candidate_tokens=b['output_tokens'],
            generated=stats['generated_tokens'],reused=stats['reused_tokens'],
            bridge=stats['bridge_tokens'],discarded=stats['discarded_tokens'],unused=stats['unused_tokens'],
            wait_ms=stats['wait_ms'],prefetch_service_ms=stats['service_ms'],
            prefetch_events=len(stats['events']),
            reusable_events=sum(e['reused_tokens']>0 for e in stats['events'])))
    if not pairs:raise ValueError('No complete paired requests')
    write_csv(out/'tables/pairs.csv',pairs)
    status=json.loads((source/'report/status.json').read_text())
    complete=not status['failures'] and status['completed']==status['expected'] and len(pairs)*2==status['expected']
    summary=[];outcomes=[]
    lines=['# Fixed-lookahead SD feasibility experiment','',f'Source: `{source}`','',
        f'Both variants use strict K=1 and fixed gamma={protocol["gamma"]}; candidate predicts {protocol["lookahead"]} future tokens per launch.',
        'One predicted token bridges the cloud bonus; the remaining matching continuation can become the next draft.',
        'All continuation tokens still undergo target verification. Request time includes final orphan-work drain.',
        'Network scenarios specify extra delay, in addition to the actual network.','',
        '| Extra-delay condition | Control TPS | Lookahead TPS | Paired gain | 95% prompt interval | Correct control / candidate |',
        '|---|---:|---:|---:|---|---|']
    for scenario in sorted({p['scenario'] for p in pairs}):
        selected=[p for p in pairs if p['scenario']==scenario]
        stats={}
        for metric in ('throughput_gain','latency_reduction','quality_change'):
            clusters=defaultdict(list)
            for p in selected:clusters[p['prompt_index']].append(p[metric])
            values=[mean(v) for v in clusters.values()];rng=random.Random(42)
            boot=[mean(rng.choices(values,k=len(values))) for _ in range(5000)] if len(values)>1 else []
            row=dict(scenario=scenario,metric=metric,mean=mean(values),
                ci95_low=percentile(boot,.025) if boot else None,
                ci95_high=percentile(boot,.975) if boot else None,
                independent_prompts=len(values),pairs=len(selected))
            summary.append(row);stats[metric]=row
        speed=stats['throughput_gain']
        signal=complete and speed['mean']>=.05 and speed['ci95_low'] is not None and speed['ci95_low']>0
        generated=sum(p['generated'] for p in selected)
        outcomes.append(dict(scenario=scenario,
            decision='INCOMPLETE' if not complete else 'POSITIVE_PILOT_SIGNAL' if signal and stats['quality_change']['mean']>=0 else 'GAIN_NOT_ESTABLISHED',
            generated=generated,reused=sum(p['reused'] for p in selected),
            bridge=sum(p['bridge'] for p in selected),discarded=sum(p['discarded'] for p in selected),
            unused=sum(p['unused'] for p in selected),wait_ms=sum(p['wait_ms'] for p in selected),
            reusable_event_fraction=sum(p['reusable_events'] for p in selected)/max(1,sum(p['prefetch_events'] for p in selected))))
        lines.append(f'| {scenario} | {mean(p["control_tps"] for p in selected):.3f} | {mean(p["candidate_tps"] for p in selected):.3f} | '
            f'{speed["mean"]:.2%} | [{speed["ci95_low"]}, {speed["ci95_high"]}] | '
            f'{sum(p["control_quality"] for p in selected):g}/{len(selected)} ; {sum(p["candidate_quality"] for p in selected):g}/{len(selected)} |')
    write_csv(out/'tables/summary.csv',summary)
    write_json(out/'report/decision.json',dict(complete=complete,outcomes=outcomes,summary=summary))
    lines+=['','## Reuse and waste','',
        '| Condition | Generated ahead | Reused as draft | Matching bridge | Discarded | Terminal/excess unused | Foreground wait (s) |',
        '|---|---:|---:|---:|---:|---:|---:|']
    for r in outcomes:
        lines.append(f'| {r["scenario"]} | {r["generated"]} | {r["reused"]} | {r["bridge"]} | {r["discarded"]} | {r["unused"]} | {r["wait_ms"]/1000:.3f} |')
    lines+=['','Reuse means use as a later draft, not automatic acceptance or committed output.',
        'Bridge work predicts a target-issued token and must be counted separately from reusable continuation.',
        'Overlapped service times are not additive components of end-to-end latency.',
        'Few independent prompts and repeated timings support only a feasibility pilot, not generalization or quality noninferiority.',
        'Token equality is not an acceptance criterion. Raw outputs and final-answer scores are retained.']
    (out/'report/report.md').write_text('\n'.join(lines)+'\n')
    print(out.resolve());return out


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('source',type=Path)
    ap.add_argument('--output-root',default='results');args=ap.parse_args()
    report(args.source,args.output_root)
