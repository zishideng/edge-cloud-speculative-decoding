"""Small, preregistered development probes with repeated paired measurements.

The standard downloaded benchmark and its archived reports are unchanged.
All methods share strict K1 and target probability cap1; draft n_probs is 0 except for
AdaEDL, which needs draft probabilities (their cost is part of that method).
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
from edge.edge_client_adaedl import DEFAULT_TOP_K, AdaEDLClient
from edge.edge_client_pipeline import MarkovPipelineClient
from edge.experiment_live import LiveExperiment
from experiments.adaptive_research import (
    balanced_method_orders, energy_check, hardware_snapshot, percentile,
    research_method_config, sha256, source_snapshot, write_json,
)
from experiments.isolation import ServiceLocks


METHODS = ('fixed_fast', 'fixed_g2', 'fixed_g8', 'sync_g4', 'adaedl', 'markov', 'markov_w0', 'markov_w05')
MARKOV_WEIGHTS = {'markov': .25, 'markov_w0': 0., 'markov_w05': .5}


def draft_n_probs(method):
    return DEFAULT_TOP_K if method == 'adaedl' else 0
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
    baselines=protocol.get('baselines',['fixed_fast'])
    # Only primary delays are reported; pooled combines them (very_high is not reported).
    run_scenarios=[s['name'] for s in protocol['scenarios']]
    scenarios=protocol.get('primary_scenarios') or run_scenarios
    excluded=[s for s in run_scenarios if s not in scenarios]
    for dataset in ['all'] + list(dict.fromkeys(j['dataset'] for j in protocol['jobs'])):
        rr=records if dataset=='all' else [r for r in records if r['dataset']==dataset]
        for scene in scenarios+['pooled']:
            ss=scenarios if scene=='pooled' else [scene]
            key=dataset+'/'+scene
            groups[key]={m:summarize([r for r in rr if r['method']==m and r['scenario'] in ss])
                         for m in protocol['methods']}
            comparisons[key]={(m if b=='fixed_fast' else f'{m}_vs_{b}'):paired_effect(rr,m,ss,baseline=b)
                              for b in baselines for m in protocol['methods'] if m!=b and b in protocol['methods']}
    result=dict(protocol=protocol, status=status, summaries=groups, comparisons=comparisons)
    write_json(directory/'results.json',result)
    lines=[f'# Progress probe: {protocol["phase"]}', '',
           f'State: {status["state"]}; {len(records)}/{len(protocol["jobs"])} requests.', '',
           'Development evidence. Strict K1 and target cap1 in every arm; draft n_probs0 except AdaEDL. Gross Jetson energy only. '
           'Pooled weights reflect this declared sample; they are not population estimates. '
           'Repeated requests are clustered by dataset/prompt, not treated as new independent prompts.', '',
           f'Reported scenarios: {", ".join(scenarios)}; pooled = {"+".join(scenarios)}.'
           + (f' Run but not reported: {", ".join(excluded)}.' if excluded else ''), '',
           '| Dataset/scenario | Method | Requests | Tokens | tokens/s | J/token | Truncated | Reuse % |',
           '|---|---|---:|---:|---:|---:|---:|---:|']
    for key,group in groups.items():
        for m,v in group.items():
            if v['requests']:
                energy=f'{v["joules_per_token"]:.4f}' if v['joules_per_token'] is not None else 'N/A'
                lines.append(f'| {key} | {m} | {v["requests"]} | {v["tokens"]} | {v["throughput_tps"]:.3f} | {energy} | {v["truncated"]} | {v["background_reuse_pct"]:.2f} |')
    lines+=['','Effects versus fixed_fast unless labelled <method>_vs_<baseline>. Positive energy saving means lower J/token.', '',
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


def resume_state(directory, plan_path):
    """Jobs of an interrupted phase and the ids already measured. Records with invalid
    energy are moved to failed/ and run again; the plan must be byte-identical."""
    protocol=json.loads((directory/'config/protocol.json').read_text())
    if protocol['source_plan_sha256']!=sha256(plan_path):
        raise ValueError('Plan changed since the phase started; refusing to resume')
    status=json.loads((directory/'report/status.json').read_text())
    if status['state']=='complete':
        raise ValueError('Phase already complete')
    status.setdefault('resumed_utc',[]).append(datetime.now(timezone.utc).isoformat())
    done=set()
    for path in sorted((directory/'raw').glob('*.json')):
        if json.loads(path.read_text())['energy_validation']['valid']:
            done.add(path.stem)
        else:
            (directory/'failed').mkdir(exist_ok=True)
            path.rename(directory/'failed'/f'{path.stem}_resume{len(status["resumed_utc"])}.json')
    status.update(state='resuming',completed=len(done))
    return protocol['jobs'],done,status


def run(args):
    plan=json.loads(Path(args.plan).read_text())
    if any(m not in METHODS for m in plan['methods']) or 'fixed_fast' not in plan['methods']:
        raise ValueError('Unsupported methods or missing fixed_fast baseline')
    directory=ROOT/plan.get('campaign','results/progress_review_20261009')/plan['phase']
    samples={name:[json.loads(line) for line in (ROOT/paths[0]).read_text().splitlines() if line.strip()]
             for name,paths in DATASETS.items()}
    cases=[(name,i) for name,indices in plan['indices'].items() for i in indices]
    resume=getattr(args,'resume',False)
    if resume:
        jobs,done,status=resume_state(directory,args.plan)
        tag=f'_resume{len(status["resumed_utc"])}'
    else:
        directory.mkdir(parents=True,exist_ok=False)
        rng=random.Random(plan['seed']);jobs=[]
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
        done=set();tag=''
    write_json(directory/'report/status.json',status)
    c=load_config(ROOT/'configs/research.downloaded.gsm8k.json')
    c.update(MAX_TOKENS=plan['max_tokens'],DRAFT_URL=plan.get('draft_url','http://127.0.0.1:8080'),
             CLOUD_URL=plan.get('cloud_url','http://172.23.119.64:9090'),
             MODEL_PAIR=plan.get('model_pair',c['MODEL_PAIR']))
    c=research_method_config(c,'fixed_fast',True)
    live=None;lock=None
    try:
        lock=ServiceLocks([c['DRAFT_URL'],c['CLOUD_URL']],str(directory)).acquire()
        write_json(directory/f'config/hardware_start{tag}.json',hardware_snapshot())
        write_json(directory/f'config/resolved{tag}.json',c)
        live=LiveExperiment(c);live.client.token_only_parser=True
        write_json(directory/f'config/service_info{tag}.json',live.info)
        write_json(directory/f'config/model_pair{tag}.json',live.model)
        write_json(directory/f'config/draft_props{tag}.json',live.client.props())
        with live.energy_profiler() as sensor:
            time.sleep(.2)
        write_json(directory/f'config/power_preflight{tag}.json',sensor.record(0))
        if not sensor.record(0)['available']:
            raise RuntimeError('Board power unavailable')
        # References and equal warmup complete before the measured jobs.
        references={}; reference_stops={}
        for name,i in cases:
            if resume:   # reuse the stored cloud references
                saved=json.loads((directory/f'config/references/{name}_p{i}.json').read_text())
                references[name,i]=(saved['ids'],saved['text']);reference_stops[name,i]=saved['stop']
                continue
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
                write_json(directory/f'config/warmup/{name}_{method}{tag}.json',warmup)
        status['state']='running'
        for job in jobs:
            if job['id'] in done:
                continue
            name=job['dataset'];i=job['request_index']
            live.c=dict(c,TASK=name);live.references={i:references[name,i]};live.reference_stops={i:reference_stops[name,i]}
            scene=next(s for s in plan['scenarios'] if s['name']==job['scenario'])
            print(f'{status["completed"]+1}/{len(jobs)} {job["id"]}',flush=True)
            record=execute(live,samples[name][i],i,dict(rtt_ms=scene['delay_ms'],jitter_ms=0),job['method'])
            record.update(job,configured_target_probability_cap=1,configured_draft_n_probs=draft_n_probs(job['method']),
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
    gamma=4
    if method in MARKOV_WEIGHTS:
        client=MarkovPipelineClient(c['DRAFT_URL'],c,energy_weight=MARKOV_WEIGHTS[method])
    elif method=='adaedl':
        client=AdaEDLClient(c['DRAFT_URL'],c)
    elif method=='sync_g4':
        client=FixedLookaheadClient(c['DRAFT_URL'],c,lookahead_tokens=0)
    else:
        gamma=int(method.removeprefix('fixed_g')) if method.startswith('fixed_g') else 4
        client=FixedLookaheadClient(c['DRAFT_URL'],c,lookahead_tokens=gamma+1)
    client.draft_n_probs=draft_n_probs(method);client.token_only_parser=True
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
    ap.add_argument('--resume',action='store_true',help='continue an interrupted phase of the same plan')
    args=ap.parse_args()
    if args.report:make_report(args.report)
    elif args.plan:run(args)
    else:ap.error('--plan or --report required')
