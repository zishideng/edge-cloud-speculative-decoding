"""Paired end-to-end SD ablation; no cloud-AR comparison."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import random
from statistics import mean

from common.metrics import percentile
from experiments.run import create_output, write_csv, write_json


def report(source, output_root):
    out=create_output(output_root)
    groups=defaultdict(dict); manifest=[]
    for path in sorted((source/'raw').glob('*.json')):
        data=path.read_bytes(); r=json.loads(data)
        groups[r['request_index'],r['repeat']][r['method']]=r
        manifest.append(dict(path=str(path),sha256=hashlib.sha256(data).hexdigest()))
    write_json(out/'config/source_manifest.json',manifest)
    pairs=[]
    for (prompt,repeat), variants in sorted(groups.items()):
        if set(variants)!={'control','candidate'}:
            continue
        a,b=variants['control'],variants['candidate']
        pairs.append(dict(prompt_index=prompt,repeat=repeat,
            throughput_gain=b['tokens_per_second']/a['tokens_per_second']-1,
            latency_reduction=1-b['wall_time_s']/a['wall_time_s'],
            quality_change=b['task_quality']-a['task_quality'],
            control_quality=a['task_quality'],candidate_quality=b['task_quality'],
            control_truncated=a['truncated'],candidate_truncated=b['truncated'],
            control_tps=a['tokens_per_second'],candidate_tps=b['tokens_per_second'],
            control_tokens=a['output_tokens'],candidate_tokens=b['output_tokens'],
            ids_equal=a['output_ids']==b['output_ids']))
    if not pairs:
        raise ValueError('No complete variant pairs')
    write_csv(out/'tables/pairs.csv',pairs)
    summary=[]
    for metric in ('throughput_gain','latency_reduction','quality_change'):
        clusters=defaultdict(list)
        for p in pairs: clusters[p['prompt_index']].append(p[metric])
        values=[mean(v) for v in clusters.values()]
        rng=random.Random(42)
        boot=[mean(rng.choices(values,k=len(values))) for _ in range(5000)] if len(values)>1 else []
        summary.append(dict(metric=metric,mean=mean(values),
            ci95_low=percentile(boot,.025) if boot else None,
            ci95_high=percentile(boot,.975) if boot else None,
            independent_prompts=len(values),pairs=len(pairs)))
    write_csv(out/'tables/summary.csv',summary)
    status=json.loads((source/'report/status.json').read_text())
    complete=not status['failures'] and status['completed']==status['expected'] and len(pairs)*2==status['expected']
    speed=summary[0]
    supported=complete and speed['mean']>=.02 and speed['ci95_low'] is not None and speed['ci95_low']>0
    quality_delta=summary[2]['mean']
    decision=('INCOMPLETE' if not complete else 'ADVANCE_TO_REPLICATION' if supported and quality_delta>=0
              else 'QUALITY_REGRESSION_REQUIRES_INVESTIGATION' if supported else 'END_TO_END_GAIN_NOT_ESTABLISHED')
    write_json(out/'report/decision.json',dict(decision=decision,speed_supported=supported,
        quality_change=quality_delta,complete=complete,summary=summary,
        note='Same pilot prompts; no held-out quality or noninferiority claim; bootstrap with few clusters is descriptive'))
    lines=['# End-to-end speculative-decoding ablation','',f'Source: `{source}`','',
        'Both variants use Proposed; only draft probability telemetry changes (1 → 0).',
        'RTT injection is 2 ms on top of the actual network. No direct-cloud comparator.',
        '',f'Decision: **{decision}**.','',
        '| Metric | Paired mean | Prompt bootstrap 95% interval |','|---|---:|---|']
    for r in summary:
        lines.append(f'| {r["metric"]} | {r["mean"]:.6f} | [{r["ci95_low"]}, {r["ci95_high"]}] |')
    lines += ['',f'Complete pairs: {len(pairs)}; token-identical pairs (diagnostic): {sum(p["ids_equal"] for p in pairs)}.',
        f'Control/candidate correct: {sum(p["control_quality"] for p in pairs):g}/{sum(p["candidate_quality"] for p in pairs):g}.',
        f'Control/candidate truncations: {sum(p["control_truncated"] for p in pairs)}/{sum(p["candidate_truncated"] for p in pairs)}.',
        'Latency depends on output length; TPS and the saved per-pair token counts must be inspected together.',
        'Zero observed quality change does not prove population noninferiority. Token identity is not an acceptance gate.']
    (out/'report/report.md').write_text('\n'.join(lines)+'\n')
    print(out.resolve())
    return out


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('source',type=Path)
    ap.add_argument('--output-root',default='results');args=ap.parse_args()
    report(args.source,args.output_root)
