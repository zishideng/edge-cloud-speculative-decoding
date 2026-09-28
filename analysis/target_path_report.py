"""Summarize fixed-prefix path audits without treating tokens as independent trials."""
import argparse
import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean

from analysis.research_audit import summarize
from experiments.run import create_output, write_csv, write_json


def report(source, output_root):
    out = create_output(output_root)
    source_csv = source/'tables/positions.csv'
    rows = list(csv.DictReader(source_csv.open(encoding='utf-8-sig')))
    protocol = json.loads((source/'config/protocol.json').read_text())
    for r in rows:
        for key in ('prompt_index','offset','repeat','gamma','original_ar','single_ar','prefill_top','tied_top_count'):
            r[key] = int(r[key])
        for key in ('matches_original','matches_single','single_matches_original'):
            r[key] = r[key] == 'True'
    write_json(out/'config/source.json', dict(path=str(source.resolve()),
        positions_sha256=hashlib.sha256(source_csv.read_bytes()).hexdigest(),
        status=json.loads((source/'report/status.json').read_text())))
    prompt_groups, repeats, windows = defaultdict(list), defaultdict(set), defaultdict(set)
    for r in rows:
        prompt_groups[r['task'],r['prompt_index'],r['gamma']].append(r)
        repeats[r['task'],r['prompt_index'],r['offset'],r['gamma']].add(r['prefill_top'])
        windows[r['task'],r['prompt_index'],r['offset'],r['repeat']].add(r['prefill_top'])
    prompt_rows = [dict(task=t,prompt_index=p,gamma=g,n=len(v),
                       matches_original=mean(r['matches_original'] for r in v),
                       matches_single=mean(r['matches_single'] for r in v),
                       single_matches_original=mean(r['single_matches_original'] for r in v))
                   for (t,p,g),v in sorted(prompt_groups.items())]
    write_csv(out/'tables/per_prompt.csv',prompt_rows)
    aggregate = []
    for task in sorted({r['task'] for r in rows}):
        for gamma in sorted({r['gamma'] for r in rows}):
            group = [r for r in prompt_rows if r['task']==task and r['gamma']==gamma]
            for metric in ('matches_original','matches_single','single_matches_original'):
                if group:
                    aggregate.append(dict(task=task,gamma=gamma,metric=metric,
                                          **summarize([r[metric] for r in group])))
    write_csv(out/'tables/summary.csv',aggregate)
    repeat_changes = [dict(task=k[0],prompt_index=k[1],offset=k[2],gamma=k[3],tokens=sorted(v))
                      for k,v in repeats.items() if len(v)>1]
    window_changes = [dict(task=k[0],prompt_index=k[1],offset=k[2],repeat=k[3],tokens=sorted(v))
                      for k,v in windows.items() if len(v)>1]
    write_json(out/'tables/sensitivity.json',dict(repeat_changes=repeat_changes,window_changes=window_changes))
    lines = ['# Target path diagnostic', '', f'Source: `{source}`', '',
        f'Position selection: {protocol.get("position_selection", "fixed")}.',
        'Real target, teacher-forced proposals; these are correctness observations, not speedup measurements.',
        'Summary rates first average sampled positions/repeats within each prompt. Only prompts are independent clusters.', '',
        '| Workload | Gamma | Prompts | Prefill vs long AR | Prefill vs single AR |',
        '|---|---:|---:|---:|---:|']
    for task in sorted({r['task'] for r in rows}):
        for gamma in sorted({r['gamma'] for r in rows}):
            group = [r for r in prompt_rows if r['task']==task and r['gamma']==gamma]
            if group:
                lines.append(f'| {task} | {gamma} | {len(group)} | '
                    f'{mean(r["matches_original"] for r in group):.4f} | {mean(r["matches_single"] for r in group):.4f} |')
    lines += ['', f'Repeat-sensitive prefix/gamma groups: {len(repeat_changes)}/{len(repeats)}.',
        f'Window-sensitive prefix/repeat groups: {len(window_changes)}/{len(windows)}.', '',
        ('Disagreement was observed in the sampled positions.' if any(not r['matches_single'] or not r['matches_original'] for r in rows)
         else 'No disagreement was observed at the sampled positions. This experiment does not support broad path sensitivity.'),
        'Original long AR and single-token AR differ in generation history/cache/scheduling. Fixed-prefix',
        'verification uses prompt probabilities. Where observed, differences establish path sensitivity, but do not',
        'identify its kernel, precision, cache, or scheduling cause without backend interventions.',
        'Exact ties are counted separately in raw measurements. Corrected local K=1 tie handling is not',
        'assumed deployed on the remote service. Sparse prefix coverage can miss later divergences.',
        'Low-margin selection deliberately enriches possible failures; its disagreement rate is not a workload error rate.',
        'HumanEval is a chat-wrapped code prompt here; no generated code is executed. MT-Bench uses',
        'the first turn. Truncated references do not establish task accuracy or a paper-ready quality claim.']
    (out/'report/report.md').write_text('\n'.join(lines)+'\n')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(8,4))
    for task in sorted({r['task'] for r in rows}):
        values = [r for r in aggregate if r['task']==task and r['metric']=='matches_single']
        ax.plot([r['gamma'] for r in values],[1-r['mean'] for r in values],'o-',label=task)
    ax.set(xlabel='Verification window gamma',ylabel='Prefill vs single-AR disagreement',
           title='Fixed-prefix target path audit (prompt-weighted, diagnostic only)')
    ax.legend();fig.tight_layout()
    for ext in ('png','svg'):
        fig.savefig(out/'figures'/f'path_disagreement.{ext}',dpi=160)
    plt.close(fig)
    print(out.resolve())
    return out


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path)
    parser.add_argument('--output-root',default='results')
    args=parser.parse_args()
    report(args.source,args.output_root)
