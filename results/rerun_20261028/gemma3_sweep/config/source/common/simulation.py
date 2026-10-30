"""Deterministic synthetic model and virtual-time experiments, NOT LLM measurements."""
import math
import random
from common.acceptance import accept_prefix
from common.controller import JointController
from common.metrics import latency_breakdown


def target_next(context):
    return (sum(context) * 7 + 11) % 97 + 1


def target_distribution(context, c):
    top = target_next(context)
    return {top: {'rank':1, 'logprob':math.log(c['SIM_TOP1_PROBABILITY'])},
            top+100: {'rank':2, 'logprob':math.log(c['SIM_TOP2_PROBABILITY'])},
            top+200: {'rank':3, 'logprob':math.log(1-c['SIM_TOP1_PROBABILITY']-c['SIM_TOP2_PROBABILITY'])}}


def reference(prompt, n):
    ids=list(prompt); output=[]
    for _ in range(n):
        token=target_next(ids); ids.append(token); output.append(token)
    return output


def network_condition(scenario, seed, round_index, request_bytes, response_bytes):
    rng=random.Random(seed + round_index)
    rtt=max(0,scenario['rtt_ms']+rng.uniform(-scenario.get('jitter_ms',0),scenario.get('jitter_ms',0)))
    if round_index >= scenario.get('burst_at',float('inf')):
        rtt += scenario.get('burst_ms',0)
    if scenario.get('bandwidth_mbps'):
        rtt += (request_bytes+response_bytes)*8/(scenario['bandwidth_mbps']*1000)
    queue=max(0,scenario.get('queue_ms',0)+rng.uniform(-scenario.get('queue_jitter_ms',0),scenario.get('queue_jitter_ms',0)))
    return rtt,queue


def run_simulation(c, strategy, adaptive_window, gamma, k, request_id, scenario):
    cfg=dict(c,GAMMA_INITIAL=gamma)
    controller=JointController(cfg,strategy,adaptive_window,k)
    prompt=[request_id+1]; ids=list(prompt); output=[]; rows=[]; visible=[]; elapsed=0.0
    while len(output)<c['MAX_TOKENS']:
        g=min(controller.window.gamma,c['MAX_TOKENS']-len(output))
        draft=[]; distributions=[]; ctx=list(ids)
        for _ in range(g):
            dist=target_distribution(ctx,c)
            # Counter-based pseudo-random draft: repeatable across window sizes.
            rng=random.Random(c['SEED']+sum(ctx)*1009+len(ctx)*9176)
            token=target_next(ctx)+(0 if rng.random()<c['SIM_DRAFT_ACCURACY'] else 100)
            draft.append(token); distributions.append(dist); ctx.append(token)
        accepted,correction,decisions,spent=accept_prefix(distributions,draft,k=controller.k,config=cfg,spent=controller.spent)
        produced=accepted+[correction if correction is not None else target_next(ctx)]
        produced=produced[:c['MAX_TOKENS']-len(output)]
        request_bytes=len(str(ids+draft).encode())
        response_bytes=len(str(decisions).encode())
        rtt,queue=network_condition(scenario,c['SEED'],len(rows),request_bytes,response_bytes)
        verify=c['SIM_VERIFY_FIXED_MS']+c['SIM_VERIFY_TOKEN_MS']*g
        draft_ms=c['SIM_DRAFT_TOKEN_MS']*g
        timing=latency_breakdown(rtt+queue+verify,0,0,queue,verify,request_bytes,response_bytes)
        total=draft_ms+rtt+queue+verify
        elapsed+=total; visible.extend([elapsed]*len(produced))
        row=dict(timing,gamma=g,k=controller.k,n_accepted=len(accepted),n_examined=len(decisions),
                 n_proposed=g,strict_accepted=sum(d['strict_accepted'] for d in decisions),
                 relaxed_only=sum(d['relaxed_only'] for d in decisions),
                 draft_token_ms=c['SIM_DRAFT_TOKEN_MS'],draft_ms=draft_ms,round_total_ms=total,
                 decisions=decisions,round_index=len(rows),measurement_mode='synthetic_virtual_time')
        row['controller']=controller.observe(row,decisions,spent)
        rows.append(row); output.extend(produced); ids.extend(produced)
    ref=reference(prompt,c['MAX_TOKENS'])
    return dict(output_ids=output,reference_ids=ref,output_text=' '.join(map(str,output)),
                reference_text=' '.join(map(str,ref)),rounds=rows,wall_time_s=elapsed/1000,
                output_tokens=len(output),ttft_ms=visible[0],tpot_ms=(visible[-1]-visible[0])/(len(output)-1) if len(output)>1 else None,
                tokens_per_second=len(output)*1000/elapsed,quality_spent=controller.spent,
                task_quality=None,reference_quality=None,
                synthetic_token_agreement=sum(a==b for a,b in zip(ref,output))/len(ref))
