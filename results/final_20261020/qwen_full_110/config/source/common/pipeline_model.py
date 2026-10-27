"""Two-state model of lookahead speculative decoding for window selection.

A round either follows a usable prefetch ("hit": the h-1 prefetched tokens are
sent, topped up to the fresh window if shorter) or not ("miss": a fresh window
is drafted on the critical path). Background lookahead of h tokens runs during
verification. Acceptance in each state is either geometric (one rate) or a
survival curve S[k] = P(first k draft tokens accepted), which lets the
per-position acceptance change along the window. The objective is time per
output token plus w times board energy per token expressed in seconds of base
power: (T + w*(T + ratio*B)) / tokens, where B is draft-busy time and
ratio = draft power / base power.
"""


def expected_tokens(alpha, gamma):
    return sum(alpha ** i for i in range(gamma + 1))


def survival(acceptance, length):
    """Survival list S[0..length-1] from a geometric rate or from a given curve."""
    if isinstance(acceptance, (int, float)):
        if not 0 <= acceptance < 1:
            raise ValueError('acceptance rates must be in [0, 1)')
        return [acceptance ** i for i in range(length)]
    curve = list(acceptance)
    if (len(curve) < length or curve[0] != 1 or any(not 0 <= v < 1 for v in curve[1:])
            or any(b > a for a, b in zip(curve, curve[1:]))):
        raise ValueError('survival curves must start at 1, stay in [0, 1) and not increase')
    return curve[:length]


def choose_windows(alpha_miss, alpha_hit, verify_ms, call_ms, token_ms, energy_weight,
                   energy_ratio, gamma_max, fresh_options=None, lookahead_options=None):
    """Return dict(fresh_gamma, lookahead, cost, hit_share) minimizing the stationary objective.
    alpha_miss and alpha_hit are geometric rates or survival curves."""
    if min(verify_ms, call_ms, token_ms, energy_weight, energy_ratio) < 0 or gamma_max < 1:
        raise ValueError('Invalid pipeline model inputs')
    fresh_options = list(fresh_options or range(1, gamma_max + 1))
    lookahead_options = list(lookahead_options or range(2, gamma_max + 2))
    length = max(max(fresh_options), max(lookahead_options) - 1) + 2
    s_miss, s_hit = survival(alpha_miss, length), survival(alpha_hit, length)
    best = None
    for fresh in fresh_options:
        for h in lookahead_options:
            background = call_ms + token_ms * h
            overlap = max(verify_ms, background)
            miss_draft = call_ms + token_ms * fresh
            miss_time = miss_draft + overlap
            miss_busy = miss_draft + background
            miss_tokens = sum(s_miss[:fresh + 1])
            miss_to_hit = s_miss[fresh + 1]
            sent = max(h - 1, fresh)
            top_up = sent - (h - 1)
            hit_draft = call_ms + token_ms * top_up if top_up else 0.0
            hit_time = hit_draft + overlap
            hit_busy = hit_draft + background
            hit_tokens = sum(s_hit[:sent + 1])
            hit_to_hit = s_hit[sent + 1]
            hit_share = miss_to_hit / (1 - hit_to_hit + miss_to_hit)
            tokens = (1 - hit_share) * miss_tokens + hit_share * hit_tokens
            time = (1 - hit_share) * miss_time + hit_share * hit_time
            busy = (1 - hit_share) * miss_busy + hit_share * hit_busy
            cost = (time * (1 + energy_weight) + energy_weight * energy_ratio * busy) / tokens
            if best is None or cost < best['cost']:
                best = dict(fresh_gamma=fresh, lookahead=h, cost=cost, hit_share=hit_share)
    return best
