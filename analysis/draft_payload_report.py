"""Paired latency analysis, clustering by original prompt rather than repetitions."""
import argparse
import csv
import json
import random
from collections import defaultdict
from pathlib import Path
from statistics import mean

from analysis.research_audit import summarize
from common.metrics import percentile
from experiments.run import create_output, write_csv, write_json


def report(source,output_root):
    out=create_output(output_root)
    rows=list(csv.DictReader((source/'tables/requests.csv').open(encoding='utf-8-sig')))
    paired=defaultdict(dict)
    for r in rows:
        key=tuple(int(r[k]) for k in ('prompt_index','offset','gamma','repeat'))
        paired[key][int(r['n_probs'])]=r
    pairs=[]
    for key,group in sorted(paired.items()):
        if set(group)!={0,1}:continue
        a,b=group[1],group[0]
        pairs.append(dict(prompt_index=key[0],offset=key[1],gamma=key[2],repeat=key[3],
            latency_reduction=1-float(b['wall_ms'])/float(a['wall_ms']),
            ids_equal=json.loads(a['output_ids'])==json.loads(b['output_ids']),
            baseline_ms=float(a['wall_ms']),candidate_ms=float(b['wall_ms']),
            response_bytes_saved=int(a['response_bytes'])-int(b['response_bytes'])))
    write_csv(out/'tables/pairs.csv',pairs)
    aggregated=[]
    for gamma in [None,*sorted({r['gamma'] for r in pairs})]:
        by_prompt=defaultdict(list)
        for r in pairs:
            if gamma is None or r['gamma']==gamma:
                by_prompt[r['prompt_index']].append(r['latency_reduction'])
        values=[mean(v) for v in by_prompt.values()]
        rng=random.Random(42)
        boot=[mean(rng.choices(values,k=len(values))) for _ in range(5000)] if len(values)>1 else []
        aggregated.append(dict(gamma='all' if gamma is None else gamma,**summarize(values),
            ci95_low=percentile(boot,.025) if boot else None,
            ci95_high=percentile(boot,.975) if boot else None))
    write_csv(out/'tables/summary.csv',aggregated)
    primary=aggregated[0]
    status=json.loads((source/'report/status.json').read_text())
    supported=not status['failures'] and primary['mean']>=.03 and primary['ci95_low'] is not None and primary['ci95_low']>0
    write_json(out/'report/decision.json',dict(source=str(source.resolve()),
        decision='ADVANCE_TO_END_TO_END' if supported else 'NOT_SUPPORTED',primary=primary,
        pairs=len(pairs),incomplete_pair_groups=len(paired)-len(pairs),
        token_equal_pairs=sum(r['ids_equal'] for r in pairs),
        note='Exploratory microbenchmark; only original prompts are bootstrap clusters. No task-quality or whole-system claim.'))
    lines=['# Draft telemetry microbenchmark','',f'Source: `{source}`','',
        f'Paired calls: {len(pairs)}; matching token outputs: {sum(r["ids_equal"] for r in pairs)}.',
        f'Primary decision: {"advance to end-to-end validation" if supported else "hypothesis not supported at the preregistered threshold"}.','',
        '| Gamma | Prompt clusters | Mean latency reduction | Bootstrap 95% interval |',
        '|---|---:|---:|---|']
    for r in aggregated:
        lines.append(f'| {r["gamma"]} | {r["n"]} | {r["mean"]:.4f} | [{r["ci95_low"]}, {r["ci95_high"]}] |')
    lines += ['', 'Positive values favor n_probs=0. Primary analysis pools all predeclared gamma/prefix strata with equal prompt weight.',
              'Repeated timings do not increase the independent prompt count. Few-cluster intervals are descriptive.',
              'This measures only draft HTTP latency. Target acceptance, network round trips and end-to-end accuracy require separate experiments.']
    (out/'report/report.md').write_text('\n'.join(lines)+'\n');print(out.resolve())
    return out


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('source',type=Path)
    ap.add_argument('--output-root',default='results');args=ap.parse_args()
    report(args.source,args.output_root)
