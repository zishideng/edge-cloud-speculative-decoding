"""Critical-path-aware lookahead with a two-state window controller.

Freshly drafted tokens delay the verification request; lookahead tokens are
drafted while the previous verification is in flight. Each round the client
chooses the fresh window and the lookahead length from a two-state (prefetch
hit/miss) model (common.pipeline_model) using online estimates of
state-dependent acceptance, verification round trip and draft token cost.
On a prefetch hit every reusable token is sent. Strict K=1 verification and
complete-prefix reuse checks are unchanged.

acceptance_model='position' (CAPE v2) replaces the geometric rate of each state by
a survival curve: its shape is the per-position acceptance measured over earlier
rounds and requests, its level the acceptance of the current request. Measured
per-position acceptance rises along the window, so the geometric model
undervalues long windows when the round trip is long.

cost_model='fit' estimates the draft call cost as intercept + slope * tokens by least
squares over recent background calls (instead of a fixed 10 ms call overhead) and the
round trip as the mean of recent verifications (instead of the median of the last 3),
because the objective is an expected time per token and the round trip is long-tailed.
cost_model='mean' keeps the v1 draft costs and only estimates the round trip as the mean
of the last 64 verifications: rare Wi-Fi stalls (power save) dominate the mean but seldom
fall inside a short window.
cost_model='robust' splits the round trip into a level and a tail: the median of the last 5
verifications (tracks delay changes within a few rounds) plus the mean excess of each round
over the median of the 5 before it, averaged over the last 64 rounds (rare stalls), floored at 0.
"""
from collections import deque
from statistics import fmean, median

from common.pipeline_model import choose_windows
from edge.edge_client_lookahead import FixedLookaheadClient

# Per-position acceptance history kept across requests of one history key (for the
# lifetime of the process): {key: {after_full: deque of (sent, accepted)}}.
POSITION_HISTORY = {}


def position_curve(history, alpha_local, prior_alpha, length, strength=10.0):
    """Survival curve S[0..length-1] with the per-position shape of history and the
    level of alpha_local. A position with little data keeps the previous position's
    rate, so an empty history gives the geometric curve of alpha_local."""
    accepted, examined = [0] * length, [0] * length
    for sent, n in history:
        for k in range(min(n + 1, sent, length)):
            examined[k] += 1
            accepted[k] += k < n
    pooled = (sum(accepted) + strength * prior_alpha) / (sum(examined) + strength)
    rate, scale, curve = pooled, alpha_local / pooled, [1.0]
    for k in range(length - 1):
        rate = (accepted[k] + strength * rate) / (examined[k] + strength)
        curve.append(curve[-1] * min(.99, rate * scale))
    return curve


class MarkovPipelineClient(FixedLookaheadClient):
    """energy_weight trades time against Jetson board energy (0 = speed only);
    energy_ratio is draft-active power over base board power (about
    10.0 W / 4.3 W on the Orin Nano 25 W mode, fitted from measured requests).
    """

    def __init__(self, draft_url='http://localhost:8080', config=None, energy_weight=0.25,
                 energy_ratio=2.3, call_overhead_ms=10.0, token_ms=24.5, verify_prior_ms=150.0,
                 acceptance_prior=(8, 10), fresh_max=None, lookahead_max=None, fresh_min=1,
                 acceptance_model='geometric', history_key=None, history_rounds=1024,
                 cost_model='v1'):
        super().__init__(draft_url, config, lookahead_tokens=0)
        if cost_model not in ('v1', 'fit', 'mean', 'robust', 'dist'):
            raise ValueError('cost_model must be v1, fit, mean, robust or dist')
        self.cost_model = cost_model
        if acceptance_model not in ('geometric', 'position'):
            raise ValueError('acceptance_model must be geometric or position')
        self.acceptance_model = acceptance_model
        self._position_history = None
        if acceptance_model == 'position':
            self._position_history = POSITION_HISTORY.setdefault(
                history_key, {s: deque(maxlen=history_rounds) for s in (False, True)})
        # Search ranges; by default fresh <= GAMMA_MAX and lookahead <= GAMMA_MAX+1.
        # fresh_min > 1 also raises the lookahead floor, so hit rounds send at least fresh_min tokens.
        if fresh_min < 1:
            raise ValueError('fresh_min must be at least 1')
        self.fresh_min = fresh_min
        self.fresh_max = fresh_max
        self.lookahead_max = lookahead_max
        if energy_weight < 0 or energy_ratio < 0:
            raise ValueError('Energy weight and ratio must be nonnegative')
        self.energy_weight = energy_weight
        self.energy_ratio = energy_ratio
        self.call_overhead_ms = call_overhead_ms
        self.token_ms = token_ms
        self.verify_prior_ms = verify_prior_ms
        self.acceptance_prior = acceptance_prior
        self.fresh_gamma = 2
        self._verify_history = deque(maxlen={'v1': 3, 'fit': 8, 'mean': 64, 'robust': 64, 'dist': 64}[cost_model])
        self._verify_excess = deque(maxlen=64)
        self._background_history = deque(maxlen=16 if cost_model == 'v1' else 32)
        self._rounds = deque(maxlen=32)
        self._prev_full = False
        self._planned_h = 0
        self._last_sent = 0
        self.pipeline_decisions = []

    def _alpha(self, after_full):
        accepted, examined = self.acceptance_prior
        for state, gamma, n in self._rounds:
            if state == after_full:
                accepted += n
                examined += n + (n < gamma)
        return min(.99, accepted / examined)

    def _verify_estimate(self):
        if not self._verify_history:
            return self.verify_prior_ms
        if self.cost_model == 'robust':
            level = median(list(self._verify_history)[-5:])
            # A drop in delay gives large negative excesses for a few rounds; the tail is never negative.
            return level + max(0.0, fmean(self._verify_excess)) if self._verify_excess else level
        if self.cost_model == 'dist':
            # Recent round-trip distribution shifted to the current level, so a delay change moves
            # the whole distribution within five rounds while the jitter shape is kept.
            level = median(list(self._verify_history)[-5:])
            if len(self._verify_excess) < 5:
                return [level]
            return [max(0.0, level + e) for e in self._verify_excess]
        return (median if self.cost_model == 'v1' else fmean)(self._verify_history)

    def _draft_cost(self):
        """(call overhead ms, ms per token). v1: fixed overhead and the median per-token time
        of background calls; fit: least squares over background calls when their lengths vary."""
        samples = [(n, t) for n, t in self._background_history if n]
        if self.cost_model == 'fit' and len(samples) >= 4 and len({n for n, _ in samples}) >= 2:
            mx, my = fmean(n for n, _ in samples), fmean(t for _, t in samples)
            slope = (sum((n-mx)*(t-my) for n, t in samples) / sum((n-mx)**2 for n, _ in samples))
            slope = max(2.0, slope)
            return max(0.0, my - slope*mx), slope
        per_token = [(t-self.call_overhead_ms)/n for n, t in samples]
        return self.call_overhead_ms, (max(5.0, median(per_token)) if per_token else self.token_ms)

    def _token_cost(self):
        return self._draft_cost()[1]

    def _choose_gamma(self, default, remaining):
        # The returned gamma is only an upper bound: draft() sends all
        # reusable prefetched tokens or a fresh window of self.fresh_gamma.
        self._remaining = remaining
        verify = self._verify_estimate()
        alphas = self._alpha(False), self._alpha(True)
        gamma_max = self.config['GAMMA_MAX']
        fresh_max, lookahead_max = self.fresh_max or gamma_max, self.lookahead_max or gamma_max + 1
        acceptance = alphas
        if self._position_history is not None:
            prior = self.acceptance_prior[0] / self.acceptance_prior[1]
            length = max(fresh_max, lookahead_max - 1) + 2
            acceptance = tuple(position_curve(self._position_history[s], a, prior, length)
                               for s, a in zip((False, True), alphas))
        call_ms, token_ms = self._draft_cost()
        choice = choose_windows(*acceptance, verify, call_ms, token_ms,
                                self.energy_weight, self.energy_ratio, gamma_max,
                                fresh_options=range(self.fresh_min, fresh_max + 1),
                                lookahead_options=range(self.fresh_min + 1, lookahead_max + 1))
        self.fresh_gamma = choice['fresh_gamma']
        self._planned_h = choice['lookahead']
        # Decisions log the mean of the round-trip samples, not the samples themselves.
        verify_ms = fmean(verify) if isinstance(verify, list) else verify
        self._choice = dict(choice, alpha_miss=alphas[0], alpha_hit=alphas[1], verify_ms=verify_ms,
                            token_ms=token_ms, call_ms=call_ms, after_full=self._prev_full)
        if self._position_history is not None:
            self._choice.update(survival_miss=[round(v, 4) for v in acceptance[0]],
                                survival_hit=[round(v, 4) for v in acceptance[1]])
        return min(self.config['GAMMA_MAX'], remaining)

    def draft(self, prompt_ids, gamma, temperature=0.0):
        cached, lps = self._take(prompt_ids, gamma)
        if self._lookahead_eos in cached:
            end = cached.index(self._lookahead_eos)+1
            cached, lps = cached[:end], lps[:end]
        else:
            target = max(len(cached), min(self.fresh_gamma, gamma))
            if len(cached) < target:
                rest, rest_lps = self._fresh_draft(list(prompt_ids)+cached, target-len(cached), temperature)
                cached += rest
                lps += rest_lps
        self._last_sent = len(cached)
        return cached, lps

    def _verified(self, elapsed_ms):
        if self.cost_model in ('robust', 'dist') and len(self._verify_history) >= 5:
            self._verify_excess.append(elapsed_ms - median(list(self._verify_history)[-5:]))
        self._verify_history.append(elapsed_ms)

    def _consumed(self, event):
        if event['generated_tokens']:
            self._background_history.append((event['generated_tokens'], event['service_ms']))

    def _choose_h(self, draft):
        after = self._remaining - len(draft) - 1
        h = 0 if after <= 0 else min(self._planned_h, after+1)
        self.pipeline_decisions.append(dict(self._choice, round=len(self.pipeline_decisions),
                                            gamma=len(draft), h=h))
        return h

    def _verification_result(self, result):
        sent = result.metadata.get('n_draft', self._last_sent)
        self._rounds.append((self._prev_full, sent, result.n_accepted))
        if self._position_history is not None:
            self._position_history[self._prev_full].append((sent, result.n_accepted))
        self._prev_full = result.n_accepted == sent

    def generate(self, messages, verifier, **kwargs):
        if (kwargs.get('strategy') != 'strict' or kwargs.get('adaptive_window', True)
                or kwargs.get('fixed_k') != 1):
            raise ValueError('Pipeline lookahead requires strictK1 without the legacy gamma controller')
        for history in (self._verify_history, self._verify_excess, self._background_history, self._rounds):
            history.clear()
        self._prev_full = False
        self.pipeline_decisions = []
        self._remaining = kwargs.get('max_tokens', 512)
        text, metrics = super().generate(messages, verifier, **kwargs)
        metrics.lookahead.update(variant='markov_pipeline', tokens=None, adaptive=True,
                                 adaptive_gamma=True, acceptance_k=1, decisions=self.pipeline_decisions,
                                 energy_weight=self.energy_weight, energy_ratio=self.energy_ratio,
                                 draft_probability_output=self.draft_n_probs,
                                 acceptance_model=self.acceptance_model, cost_model=self.cost_model,
                                search=dict(fresh_min=self.fresh_min,
                                            fresh_max=self.fresh_max or self.config['GAMMA_MAX'],
                                            lookahead_max=self.lookahead_max or self.config['GAMMA_MAX'] + 1))
        return text, metrics
