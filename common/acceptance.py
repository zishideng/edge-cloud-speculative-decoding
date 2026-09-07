"""Deterministic strict and quality-constrained relaxed prefix acceptance.

Relaxation changes target output and is NOT distribution preserving.
Budget is cumulative accepted-token logprob regret per request (nats).
"""
import math


def accept_prefix(distributions, draft_ids, *, k, config, spent=0.0, eos_id=None):
    if not config['K_MIN'] <= k <= config['K_MAX']:
        raise ValueError('K outside configured bounds')
    if not math.isfinite(spent) or not 0 <= spent <= config['QUALITY_BUDGET']:
        raise ValueError('Invalid cumulative quality budget')
    if len(distributions) != len(draft_ids) or not draft_ids:
        raise ValueError('Missing target distributions or draft tokens')
    decisions, accepted, correction = [], [], None
    for dist, token in zip(distributions, draft_ids):
        # Each entry includes the GLOBAL rank from the model backend. The
        # observed prompt token may be returned even when outside top-k.
        if not dist or not any(v['rank'] == 1 for v in dist.values()):
            raise ValueError('Target distribution has no rank-1 token')
        top_id = min((t for t in dist if dist[t]['rank'] == 1))
        top = dist[top_id]
        candidate = dist.get(token)
        for v in dist.values():
            if not math.isfinite(v['logprob']) or v['logprob'] > 0 or v['rank'] < 1:
                raise ValueError('Invalid target logprob/rank')
        regret = max(0.0, top['logprob'] - candidate['logprob']) if candidate else None
        ratio = math.exp(-regret) if regret is not None else 0.0
        p_top1 = math.exp(top['logprob'])
        strict = token == top_id
        risk = min(1.0, regret / max(config['MAX_LOGPROB_REGRET'], 1e-12)) if candidate else 1.0
        effective_k = 1 if spent >= config['QUALITY_BUDGET'] * config['BUDGET_TIGHTEN_FRACTION'] else k
        relaxed = bool(candidate and candidate['rank'] <= effective_k
                       and p_top1 >= config['MIN_TOP1_CONFIDENCE']
                       and regret <= config['MAX_LOGPROB_REGRET']
                       and ratio >= config['MIN_PROBABILITY_RATIO']
                       and spent + regret <= config['QUALITY_BUDGET'])
        ok = strict or relaxed
        if ok and not strict:
            spent += regret
        decisions.append(dict(token_id=token, k=effective_k, target_rank=candidate['rank'] if candidate else None,
                              p_draft=math.exp(candidate['logprob']) if candidate else None,
                              p_top1=p_top1, probability_ratio=ratio, logprob_regret=regret,
                              quality_risk=risk, strict_accepted=strict, accepted=ok,
                              relaxed_only=ok and not strict, quality_spent=spent))
        if not ok:
            correction = top_id
            break
        accepted.append(token)
        if token == eos_id:
            break
    return accepted, correction, decisions, spent
