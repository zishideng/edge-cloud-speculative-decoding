"""Generate a traceable report for experiments.strict_diagnostic artifacts."""
import argparse
import hashlib
import json
from pathlib import Path
from statistics import mean

from analysis.research_audit import summarize
from experiments.run import create_output, write_json, write_csv


def report(source, output_root):
    out = create_output(output_root)
    rows = json.loads((source/'tables/summary.json').read_text())
    files = sorted((source/'raw').glob('*.json'))
    write_json(out/'config/source_manifest.json', [dict(path=str(p.resolve()),
        sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in files])
    groups, ar_rows, replay_rows = [], [], []
    for gamma in sorted({r['gamma'] for r in rows}):
        group = [r for r in rows if r['gamma']==gamma]
        for metric in ('tokens_per_second','wall_time_s','exact','output_tokens'):
            groups.append(dict(gamma=gamma,metric=metric,**summarize([r[metric] for r in group])))
    for index in sorted({r['prompt_index'] for r in rows}):
        ars = [json.loads(p.read_text()) for p in sorted((source/'raw').glob(f'ar_{index}_*.json'))]
        outputs = [r['response']['token_ids'] for r in ars]
        ar_rows.append(dict(prompt_index=index,repeats=len(ars),
            identical_across_repeats=all(x==outputs[0] for x in outputs),
            lengths=list(map(len,outputs)),
            mean_http_wall_s=mean(r['http_wall_s'] for r in ars)))
    for path in (source/'raw').glob('*_replay.json'):
        calls = json.loads(path.read_text())
        for repeat in sorted({r['repeat'] for r in calls}):
            group = [r for r in calls if r['repeat']==repeat]
            single = next(r for r in group if r['kind']=='generate_next')['response']['token_ids'][0]
            verify = next(r for r in group if r['kind']=='single_reference')
            dist = verify['response']['metadata']['target_distributions'][0]
            top = min(int(k) for k,v in dist.items() if v['rank']==1)
            original = verify['request']['draft_ids'][0]
            replay_rows.append(dict(raw_file=str(path),repeat=repeat,original_ar=original,
                single_ar=single,prefill_top=top,prefill_matches_single=top==single,
                single_matches_original=single==original))
    write_csv(out/'tables/strict_summary.csv',groups)
    write_csv(out/'tables/ar_repeat_stability.csv',ar_rows)
    if replay_rows:
        write_csv(out/'tables/replay.csv',replay_rows)
    protocol = json.loads((source/'config/protocol.json').read_text())
    hardware_label = protocol['arguments']['hardware_label']
    lines = ['# Strict decoding diagnostic', '', f'Source: `{source}`',
        f'Hardware label: {hardware_label}.',
        ('NGL=0 places model weights on CPU; this does not certify absence of GPU operations. These are not full-GPU baseline timings.'
         if 'NGL=0' in hardware_label else 'Timings characterize this deployment and warm service state; remote load/cache state is not controlled.'), '',
        '| Gamma | Runs | Exact matches to paired AR | Mean tokens/s | Median tokens/s | Sample std |',
        '|---|---:|---:|---:|---:|---:|']
    for gamma in sorted({r['gamma'] for r in rows}):
        group = [r for r in rows if r['gamma']==gamma]
        stats = summarize([r['tokens_per_second'] for r in group])
        lines.append(f'| {gamma} | {len(group)} | {sum(r["exact"] for r in group)} | '
                     f'{stats["mean"]:.3f} | {stats["median"]:.3f} | {stats["std"]:.3f} |')
    lines += ['', f'AR changed across repeats for {sum(not r["identical_across_repeats"] for r in ar_rows)}/{len(ar_rows)} prompts.',
        f'Fixed-prefix replay prefill vs single AR disagreements: '
        f'{sum(not r["prefill_matches_single"] for r in replay_rows)}/{len(replay_rows)} replay calls.',
        'Replay cases were selected at observed first divergences; this fraction is not a population error rate.',
        'Raw AR calls include full token IDs and HTTP wall time. No streaming AR TTFT was measured.',
        'A fixed seed did not guarantee identical references in this deployment. Both changed outputs are retained.',
        'Exact agreement checks include EOS and length. Task answer agreement cannot substitute for token equivalence.',
        'The local tied-rank acceptance fix was not deployed on the remote target. Kernel/precision causation remains unproven.']
    ar_records = [json.loads(p.read_text()) for p in (source/'raw').glob('ar_*.json')]
    ar_metrics = []
    for metric, values in [('wall_time_s',[r['http_wall_s'] for r in ar_records]),
                           ('tokens_per_second',[len(r['response']['token_ids'])/r['http_wall_s'] for r in ar_records])]:
        ar_metrics.append(dict(method='cloud_AR',metric=metric,**summarize(values)))
    write_csv(out/'tables/ar_summary.csv',ar_metrics)
    lines += ['', '## Cloud AR descriptive baseline', '',
              '| Metric | Mean | Median | Sample std | Runs |', '|---|---:|---:|---:|---:|']
    for r in ar_metrics:
        lines.append(f'| {r["metric"]} | {r["mean"]:.4f} | {r["median"]:.4f} | {r["std"]:.4f} | {r["n"]} |')
    lines += ['', 'AR time covers the generate HTTP call. SD time also includes template/tokenization and detokenization.',
              'Neither has artificial network injection. AR is measured before SD within each prompt/repeat.',
              'Output sequences and lengths may differ; these descriptive rates are not an equal-output speedup estimate.']
    (out/'report/report.md').write_text('\n'.join(lines)+'\n')
    print(out.resolve())
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path)
    parser.add_argument('--output-root',default='results')
    args=parser.parse_args()
    report(args.source,args.output_root)
