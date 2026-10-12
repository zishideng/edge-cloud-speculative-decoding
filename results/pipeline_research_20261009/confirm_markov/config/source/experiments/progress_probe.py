"""Small, preregistered development probes with repeated paired measurements.

The standard downloaded benchmark and its archived reports are unchanged.
All methods share strict K1, target probability cap1 and draft n_probs0.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import random
import sys
import time
import traceback

from common.experiment_config import ROOT, load_config, validate
from common.result_metrics import enrich
from edge.edge_client_lookahead import FixedLookaheadClient
from edge.edge_client_pipeline import MarkovPipelineClient, PipelineLookaheadClient
from edge.edge_client_regime import LatencyRegimeLookaheadClient
from edge.experiment_live import LiveExperiment
from experiments.adaptive_research import (
    balanced_method_orders, energy_check, hardware_snapshot, percentile,
    research_method_config, sha256, source_snapshot, write_json,
)
from experiments.isolation import ServiceLocks


METHODS = ('fixed_fast', 'regime', 'regime_guard', 'regime_short', 'fixed_g2', 'fixed_g3', 'fixed_g6', 'fixed_g8',
           'pipeline', 'pipeline_g3', 'markov', 'markov_w0', 'markov_w05')
DATASETS = {
    'gsm8k': ('common/data/gsm8k_test_50.jsonl', 'configs/research.downloaded.gsm8k.json'),
    'humaneval': ('common/data/humaneval_30.jsonl', 'configs/research.downloaded.humaneval.json'),
    'mtbench': ('common/data/mtbench_30.jsonl', 'configs/research.downloaded.mtbench.json'),
}


def summarize(records):
    tokens = sum(r['output_tokens'] for r in records)
    wall = sum(r['wall_time_s'] for r in records)
    checks = [energy_check(r) for r in records]
    valid = bool(records) and all(c['valid'] for c in checks)
    joules = sum(c['recomputed_joules'] for c in checks) if valid else None
    rounds = [v for r in records for v in r['rounds']]
    events = [e for r in records for e in r['lookahead']['events']]
    bg = sum(e['generated_tokens'] for e in events)
    return dict(requests=len(records), tokens=tokens, wall_s=wall,
                throughput_tps=tokens / wall if wall else None,
                joules=joules, joules_per_token=joules / tokens if valid and tokens else None,
                energy_valid_requests=sum(c['valid'] for c in checks),
                correct=sum(r['task_quality'] == 1 for r in records),
                scored=sum(r['task_quality'] is not None for r in records),
                truncated=sum(r['truncated'] for r in records), rounds=len(rounds),
                gamma_counts=dict(Counter(str(v['gamma']) for v in rounds)),
                background_tokens=bg,
                reused_tokens=sum(e['reused_tokens'] for e in events),
                discarded_tokens=sum(e['discarded_tokens'] for e in events),
                background_reuse_pct=100 * sum(e['reused_tokens'] for e in events) / bg if bg else 0,
                http_residual_s=sum(v['timing_residual_ms'] for v in rounds) / 1000,
                foreground_s=sum(v['draft_ms'] for v in rounds) / 1000,
                cloud_s=sum(v['cloud_verify_ms'] for v in rounds) / 1000,
                injected_s=sum(v['injected_network_ms'] for v in rounds) / 1000,
                background_wait_s=sum(e['wait_ms'] for e in events) / 1000)


def paired_effect(records, candidate, scenarios, draws=2000, baseline='fixed_fast'):
    subset = [r for r in records if r['scenario'] in scenarios]
    lookup = {(r['dataset'], r['request_index'], r['scenario'], r['repeat'], r['method']): r for r in subset}
    expected_pairs = sorted({k[:-1] for k in lookup})
    pairs = [(lookup[k + (baseline,)], lookup[k + (candidate,)])
             for k in expected_pairs if k + (baseline,) in lookup and k + (candidate,) in lookup]
    if not pairs:
        return None
    valid_energy=all(energy_check(r)['valid'] for pair in pairs for r in pair)
    clusters = {}
    for b, c in pairs:
        key = (b['dataset'], b['request_index'])
        values = clusters.setdefault(key, [0.] * 6)
        for j, value in enumerate((b['output_tokens'], b['wall_time_s'], b['energy'].get('joules') or 0,
                                   c['output_tokens'], c['wall_time_s'], c['energy'].get('joules') or 0)):
            values[j] += value

    def effect(sample):
        bt, bw, bj, ct, cw, cj = [sum(v[j] for v in sample) for j in range(6)]
        return (100 * ((ct / cw) / (bt / bw) - 1),
                100 * (1 - (cj / ct) / (bj / bt)) if valid_energy else 0.)

    values = list(clusters.values())
    speed, saving = effect(values)
    rng = random.Random(42)
    boot = [effect([rng.choice(values) for _ in values]) for _ in range(draws)]
    sensitivity = [effect(values[:i] + values[i + 1:])[0] for i in range(len(values))] if len(values)>1 else []
    return dict(candidate=candidate, baseline=baseline, request_pairs=len(pairs),
                independent_prompts=len(clusters), complete_pairs=len(pairs)==len(expected_pairs),
                throughput_gain_pct=speed, throughput_ci95=[percentile([v[0] for v in boot], q) for q in (.025, .975)],
                energy_saving_pct=saving if valid_energy else None,
                energy_ci95=[percentile([v[1] for v in boot], q) for q in (.025, .975)] if valid_energy else None,
                energy_valid=valid_energy,
                changed_sequences=sum(b['output_ids'] != c['output_ids'] for b,c in pairs),
                additional_truncations=sum(c['truncated'] and not b['truncated'] for b,c in pairs),
                scored_pairs=sum(b['task_quality'] is not None and c['task_quality'] is not None for b,c in pairs),
                quality_declines=sum(c['task_quality'] < b['task_quality'] for b,c in pairs
                                     if b['task_quality'] is not None and c['task_quality'] is not None),
                leave_one_prompt_out_speed_range=[min(sensitivity),max(sensitivity)] if sensitivity else None,
                bootstrap='2000 paired prompt-cluster percentile draws, seed42; repeats and scenarios retained together; exploratory, no multiplicity adjustment')


def make_report(directory):
    protocol=json.loads((directory/'config/protocol.json').read_text())
    status=json.loads((directory/'report/status.json').read_text())
    records=[json.loads(p.read_text()) for p in sorted((directory/'raw').glob('*.json'))]
    groups={}
    comparisons={}
    scenarios=[s['name'] for s in protocol['scenarios']]
    for dataset in ['all'] + list(dict.fromkeys(j['dataset'] for j in protocol['jobs'])):
        rr=records if dataset=='all' else [r for r in records if r['dataset']==dataset]
        for scene in scenarios+['pooled']:
            ss=scenarios if scene=='pooled' else [scene]
            key=dataset+'/'+scene
            groups[key]={m:summarize([r for r in rr if r['method']==m and r['scenario'] in ss])
                         for m in protocol['methods']}
            comparisons[key]={m:paired_effect(rr,m,ss) for m in protocol['methods'] if m!='fixed_fast'}
            if 'regime_short' in protocol['methods'] and 'regime' in protocol['methods']:
                comparisons[key]['regime_short_vs_regime']=paired_effect(rr,'regime_short',ss,baseline='regime')
    result=dict(protocol=protocol, status=status, summaries=groups, comparisons=comparisons)
    write_json(directory/'results.json',result)
    lines=[f'# Progress probe: {protocol["phase"]}', '',
           f'State: {status["state"]}; {len(records)}/{len(protocol["jobs"])} requests.', '',
           'Development evidence. Strict K1, target cap1, draft n_probs0 in every arm. Gross Jetson energy only. '
           'Pooled weights reflect this declared sample; they are not population estimates. '
           'Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.', '',
           '| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |',
           '|---|---|---:|---:|---:|---:|---:|---:|']
    for key,group in groups.items():
        for m,v in group.items():
            if v['requests']:
                energy=f'{v["joules_per_token"]:.4f}' if v['joules_per_token'] is not None else 'N/A'
                lines.append(f'| {key} | {m} | {v["requests"]} | {v["tokens"]} | {v["throughput_tps"]:.3f} | {energy} | {v["truncated"]} | {v["background_reuse_pct"]:.2f} |')
    lines+=['','Effects versus fixed_fast, except explicitly labelled regime_short_vs_regime. Positive energy saving means lower J/token.', '',
            '| Dataset/scenario | Method | Prompts | Speed % [95% CI] | Energy saving % [95% CI] | Changed sequences | Extra truncations |',
            '|---|---|---:|---|---|---:|---:|']
    for key,group in comparisons.items():
        for m,v in group.items():
            if v:
                lo,hi=v['throughput_ci95']
                energy='N/A'
                if v['energy_ci95']:
                    el,eh=v['energy_ci95'];energy=f'{v["energy_saving_pct"]:.2f} [{el:.2f}, {eh:.2f}]'
                lines.append(f'| {key} | {m} | {v["independent_prompts"]} | {v["throughput_gain_pct"]:.2f} [{lo:.2f}, {hi:.2f}] | {energy} | {v["changed_sequences"]} | {v["additional_truncations"]} |')
    lines+=['','No claim of task-quality preservation for unscored tasks. Check complete status, energy validity, '
            'paired sequences, output cap, per-dataset effects and leave-one-prompt sensitivity before interpreting gains. '
            'Background service overlaps verification; it is not an additive latency component.']
    (directory/'SUMMARY.md').write_text('\n'.join(lines)+'\n')
    return result


def run(args):
    plan=json.loads(Path(args.plan).read_text())
    if any(m not in METHODS for m in plan['methods']) or 'fixed_fast' not in plan['methods']:
        raise ValueError('Unsupported methods or missing fixed_fast baseline')
    directory=ROOT/plan.get('campaign','results/progress_review_20261009')/plan['phase']
    directory.mkdir(parents=True,exist_ok=False)
    rng=random.Random(plan['seed']);jobs=[]
    samples={name:[json.loads(line) for line in (ROOT/paths[0]).read_text().splitlines() if line.strip()]
             for name,paths in DATASETS.items()}
    cases=[(name,i) for name,indices in plan['indices'].items() for i in indices]
    for repeat in range(plan['repeats']):
        blocks=[(name,i,s) for name,i in cases for s in plan['scenarios']]
        rng.shuffle(blocks)
        orders=balanced_method_orders(plan['methods'],len(blocks),rng)
        for (name,i,s),order in zip(blocks,orders):
            for method in order:
                jobs.append(dict(id=f'{name}_{s["name"]}_p{i}_r{repeat}_{method}',
                                 dataset=name,request_index=i,scenario=s['name'],repeat=repeat,method=method))
    protocol=dict(plan,jobs=jobs,argv=sys.argv,created_utc=datetime.now(timezone.utc).isoformat(),
                  source_plan_sha256=sha256(args.plan),
                  dataset_sha256={name:sha256(ROOT/DATASETS[name][0]) for name in plan['indices']})
    write_json(directory/'config/protocol.json',protocol)
    source_snapshot(directory)
    status=dict(state='starting',completed=0,expected=len(jobs),failures=[])
    write_json(directory/'report/status.json',status)
    c=load_config(ROOT/'configs/research.downloaded.gsm8k.json')
    c.update(MAX_TOKENS=plan['max_tokens'],DRAFT_URL=plan.get('draft_url','http://127.0.0.1:8080'),
             CLOUD_URL=plan.get('cloud_url','http://172.23.119.64:9090'))
    c=research_method_config(c,'fixed_fast',True)
    live=None;lock=None
    try:
        lock=ServiceLocks([c['DRAFT_URL'],c['CLOUD_URL']],str(directory)).acquire()
        write_json(directory/'config/hardware_start.json',hardware_snapshot())
        write_json(directory/'config/resolved.json',c)
        live=LiveExperiment(c);live.client.token_only_parser=True
        write_json(directory/'config/service_info.json',live.info)
        write_json(directory/'config/model_pair.json',live.model)
        write_json(directory/'config/draft_props.json',live.client.props())
        with live.energy_profiler() as sensor:
            time.sleep(.2)
        write_json(directory/'config/power_preflight.json',sensor.record(0))
        if not sensor.record(0)['available']:
            raise RuntimeError('Board power unavailable')
        # References and equal warmup complete before the measured jobs.
        references={}; reference_stops={}
        for name,i in cases:
            live.c=dict(c,TASK=name);live.references={};live.reference_stops={}
            references[name,i]=live.reference(samples[name][i],i)
            reference_stops[name,i]=live.reference_stops[i]
            write_json(directory/f'config/references/{name}_p{i}.json',
                       dict(ids=references[name,i][0],text=references[name,i][1],stop=reference_stops[name,i]))
        for name in plan['indices']:
            i=plan['indices'][name][0];live.c=dict(c,TASK=name,MAX_TOKENS=16)
            live.references={i:references[name,i]};live.reference_stops={i:reference_stops[name,i]}
            for method in plan['methods']:
                warmup=execute(live,samples[name][i],i,dict(rtt_ms=2,jitter_ms=0),method)
                write_json(directory/f'config/warmup/{name}_{method}.json',warmup)
        status['state']='running'
        for job in jobs:
            name=job['dataset'];i=job['request_index']
            live.c=dict(c,TASK=name);live.references={i:references[name,i]};live.reference_stops={i:reference_stops[name,i]}
            scene=next(s for s in plan['scenarios'] if s['name']==job['scenario'])
            print(f'{status["completed"]+1}/{len(jobs)} {job["id"]}',flush=True)
            record=execute(live,samples[name][i],i,dict(rtt_ms=scene['delay_ms'],jitter_ms=0),job['method'])
            record.update(job,configured_target_probability_cap=1,configured_draft_n_probs=0,
                          configured_k=1,configured_max_tokens=plan['max_tokens'])
            enrich(record);record['energy_validation']=energy_check(record)
            for e in record['lookahead']['events']:
                if e['generated_tokens']!=sum(e[k] for k in ['reused_tokens','bridge_tokens','discarded_tokens','unused_tokens']):
                    raise RuntimeError('Background token accounting mismatch')
            write_json(directory/f'raw/{job["id"]}.json',record)
            status['completed']+=1
            write_json(directory/'report/status.json',status)
            print(f'  {record["output_tokens"]} tokens {record["wall_time_s"]:.3f}s '
                  f'{record["energy"]["joules_per_token"]:.4f} J/token',flush=True)
            if not record['energy_validation']['valid']:
                raise RuntimeError('Invalid energy measurement')
        status['state']='complete'
    except BaseException:
        status['state']='failed';status['failures'].append(traceback.format_exc())
        raise
    finally:
        write_json(directory/'report/status.json',status)
        write_json(directory/'config/hardware_end.json',hardware_snapshot())
        if live:
            live.client._session.close();live.remote._session.close()
        if lock:lock.close()
        make_report(directory)
    print(f'Artifacts: {directory}',flush=True)


def execute(live,example,index,scenario,method):
    c=live.c;original=live.client
    if method in ('regime','regime_guard','regime_short'):
        client=LatencyRegimeLookaheadClient(c['DRAFT_URL'],c,max_lookahead=10,
                                           feasibility_guard=method in ('regime_guard','regime_short'),
                                           short_windows=method=='regime_short')
        gamma=4
    elif method.startswith('markov'):
        weight={'markov':.25,'markov_w0':0.,'markov_w05':.5}[method]
        client=MarkovPipelineClient(c['DRAFT_URL'],c,energy_weight=weight)
        gamma=4
    elif method.startswith('pipeline'):
        client=PipelineLookaheadClient(c['DRAFT_URL'],c,fresh_gamma=3 if method=='pipeline_g3' else 2)
        gamma=4
    else:
        gamma=int(method.removeprefix('fixed_g')) if method.startswith('fixed_g') else 4
        client=FixedLookaheadClient(c['DRAFT_URL'],c,lookahead_tokens=gamma+1)
    client.draft_n_probs=0;client.token_only_parser=True
    client.stop_strings=live.model.get('stop_strings',[])
    live.client=client
    try:
        record=live.run('strict',False,gamma,1,example,index,scenario)
        record['lookahead']=client.last_lookahead
        return record
    finally:
        client._session.close();live.client=original


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--plan');ap.add_argument('--report',type=Path)
    args=ap.parse_args()
    if args.report:make_report(args.report)
    elif args.plan:run(args)
    else:ap.error('--plan or --report required')
