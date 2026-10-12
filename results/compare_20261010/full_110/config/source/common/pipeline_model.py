"""Two-state model of lookahead speculative decoding for window selection.

A round either follows a usable prefetch ("hit": the h-1 prefetched tokens are
sent, topped up to the fresh window if shorter) or not ("miss": a fresh window
is drafted on the critical path). Background lookahead of h tokens runs during
verification. Per-token acceptance is geometric with a separate rate for each
state. The objective is time per output token plus w times board energy per
token expressed in seconds of base power: (T + w*(T + ratio*B)) / tokens,
where B is draft-busy time and ratio = draft power / base power.
"""


def expected_tokens(alpha, gamma):
    return sum(alpha ** i for i in range(gamma + 1))


def choose_windows(alpha_miss, alpha_hit, verify_ms, call_ms, token_ms, energy_weight,
                   energy_ratio, gamma_max, fresh_options=None, lookahead_options=None):
    """Return dict(fresh_gamma, lookahead, cost, hit_share) minimizing the stationary objective."""
    for value in (alpha_miss, alpha_hit):
        if not 0 <= value < 1:
            raise ValueError('acceptance rates must be in [0, 1)')
    if min(verify_ms, call_ms, token_ms, energy_weight, energy_ratio) < 0 or gamma_max < 1:
        raise ValueError('Invalid pipeline model inputs')
    best = None
    for fresh in fresh_options or range(1, gamma_max + 1):
        for h in lookahead_options or range(2, gamma_max + 2):
            background = call_ms + token_ms * h
            overlap = max(verify_ms, background)
            miss_draft = call_ms + token_ms * fresh
            miss_time = miss_draft + overlap
            miss_busy = miss_draft + background
            miss_tokens = expected_tokens(alpha_miss, fresh)
            miss_to_hit = alpha_miss ** (fresh + 1)
            sent = max(h - 1, fresh)
            top_up = sent - (h - 1)
            hit_draft = call_ms + token_ms * top_up if top_up else 0.0
            hit_time = hit_draft + overlap
            hit_busy = hit_draft + background
            hit_tokens = expected_tokens(alpha_hit, sent)
            hit_to_hit = alpha_hit ** (sent + 1)
            hit_share = miss_to_hit / (1 - hit_to_hit + miss_to_hit)
            tokens = (1 - hit_share) * miss_tokens + hit_share * hit_tokens
            time = (1 - hit_share) * miss_time + hit_share * hit_time
            busy = (1 - hit_share) * miss_busy + hit_share * hit_busy
            cost = (time * (1 + energy_weight) + energy_weight * energy_ratio * busy) / tokens
            if best is None or cost < best['cost']:
                best = dict(fresh_gamma=fresh, lookahead=h, cost=cost, hit_share=hit_share)
    return best
