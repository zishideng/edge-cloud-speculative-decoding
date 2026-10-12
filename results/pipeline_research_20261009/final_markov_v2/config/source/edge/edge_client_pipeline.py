"""Critical-path-aware lookahead: short fresh drafts, budget-sized prefetch.

Freshly drafted tokens delay the verification request; prefetched tokens are
produced while the previous verification is in flight. After a prefetch miss
the client therefore drafts only a short fresh window. The prefetch length is
sized from the measured verification round trip so that background drafting
ends near the response, and on a prefetch hit every reusable token is sent.
Strict K=1 verification and complete-prefix reuse checks are unchanged.
"""
from collections import deque
from statistics import median
import time

from common.pipeline_model import choose_windows
from edge.edge_client_lookahead import FixedLookaheadClient


class PipelineLookaheadClient(FixedLookaheadClient):
    def __init__(self, draft_url='http://localhost:8080', config=None, fresh_gamma=2,
                 budget_fraction=1.0, min_lookahead=2, call_overhead_ms=20.0, token_ms=27.0):
        super().__init__(draft_url, config, lookahead_tokens=0)
        if type(fresh_gamma) is not int or fresh_gamma < 1:
            raise ValueError('fresh_gamma must be a positive integer')
        if not 0 < budget_fraction <= 2 or type(min_lookahead) is not int or min_lookahead < 1:
            raise ValueError('Invalid lookahead budget settings')
        self.fresh_gamma = fresh_gamma
        self.budget_fraction = budget_fraction
        self.min_lookahead = min_lookahead
        self.call_overhead_ms = call_overhead_ms
        self.token_ms = token_ms
        self._verify_history = deque(maxlen=3)
        self._background_history = deque(maxlen=16)
        self.pipeline_decisions = []

    def _choose_gamma(self, default, remaining):
        # Upper bound only: draft() returns all reusable prefetched tokens or
        # a short fresh window.
        self._remaining = remaining
        return min(self.config['GAMMA_MAX'], remaining)

    def draft(self, prompt_ids, gamma, temperature=0.0):
        cached, lps = self._take(prompt_ids, gamma)
        if self._lookahead_eos in cached:
            end = cached.index(self._lookahead_eos)+1
            return cached[:end], lps[:end]
        target = max(len(cached), min(self.fresh_gamma, gamma))
        if len(cached) < target:
            rest, rest_lps = self._fresh_draft(list(prompt_ids)+cached, target-len(cached), temperature)
            cached += rest
            lps += rest_lps
        return cached, lps

    def _verified(self, elapsed_ms):
        self._verify_history.append(elapsed_ms)

    def _consumed(self, event):
        if event['generated_tokens']:
            self._background_history.append((event['generated_tokens'], event['service_ms']))

    def _token_cost(self):
        samples = [(t-self.call_overhead_ms)/n for n, t in self._background_history if n]
        return max(5.0, median(samples)) if samples else self.token_ms

    def _choose_h(self, draft):
        after = self._remaining - len(draft) - 1
        if after <= 0:
            h, reason, budget = 0, 'terminal', None
        elif not self._verify_history:
            h, reason, budget = self.fresh_gamma+1, 'warmup', None
        else:
            budget = self.budget_fraction*median(self._verify_history)
            h = int((budget-self.call_overhead_ms)/self._token_cost())
            # The first prefetched token is the bonus guess; the rest may be
            # sent next round, bounded by the configured maximum window.
            h = max(self.min_lookahead, min(h, self.config['GAMMA_MAX']+1))
            reason = 'verification budget'
        h = min(h, after+1)
        self.pipeline_decisions.append(dict(round=len(self.pipeline_decisions), gamma=len(draft), h=h,
                                            reason=reason, budget_ms=budget, token_ms=self._token_cost()))
        return h

    def generate(self, messages, verifier, **kwargs):
        if (kwargs.get('strategy') != 'strict' or kwargs.get('adaptive_window', True)
                or kwargs.get('fixed_k') != 1):
            raise ValueError('Pipeline lookahead requires strictK1 without the legacy gamma controller')
        self._verify_history.clear()
        self._background_history.clear()
        self.pipeline_decisions = []
        self._remaining = kwargs.get('max_tokens', 512)
        text, metrics = super().generate(messages, verifier, **kwargs)
        metrics.lookahead.update(variant='pipeline_short_fresh_budget_prefetch', tokens=None,
            adaptive=True, adaptive_gamma=True, acceptance_k=1, decisions=self.pipeline_decisions,
            fresh_gamma=self.fresh_gamma, budget_fraction=self.budget_fraction,
            draft_probability_output=self.draft_n_probs)
        return text, metrics


class MarkovPipelineClient(PipelineLookaheadClient):
    """Chooses the fresh window and lookahead length each round from a
    two-state pipeline model (common.pipeline_model) with online estimates of
    state-dependent acceptance, verification round trip and draft token cost.

    energy_weight trades time against Jetson board energy; energy_ratio is
    draft-active power over base board power (about 10.0 W / 4.3 W on the
    Orin Nano 25 W mode, fitted from measured requests).
    """

    def __init__(self, draft_url='http://localhost:8080', config=None, energy_weight=0.25,
                 energy_ratio=2.3, call_overhead_ms=15.0, token_ms=24.0, verify_prior_ms=150.0,
                 acceptance_prior=(4, 5), robust_estimates=True, token_prior_weight=16,
                 state_prior_weight=6, min_fresh_gamma=1, min_lookahead=2):
        super().__init__(draft_url, config, fresh_gamma=2, call_overhead_ms=call_overhead_ms,
                         token_ms=token_ms)
        if energy_weight < 0 or energy_ratio < 0:
            raise ValueError('Energy weight and ratio must be nonnegative')
        self.energy_weight = energy_weight
        self.energy_ratio = energy_ratio
        self.verify_prior_ms = verify_prior_ms
        self.acceptance_prior = acceptance_prior
        self.robust_estimates = robust_estimates
        self.token_prior_weight = token_prior_weight
        self.state_prior_weight = state_prior_weight
        self.min_fresh_gamma = min_fresh_gamma
        self.min_lookahead = min_lookahead
        if robust_estimates:
            self._verify_history = deque(maxlen=8)
        self._rounds = deque(maxlen=32)
        self._prev_full = False
        self._planned_h = 0
        self._last_sent = 0

    def _alpha(self, after_full):
        accepted, examined = self.acceptance_prior
        if not self.robust_estimates:
            for state, gamma, n in self._rounds:
                if state == after_full:
                    accepted += n
                    examined += n + (n < gamma)
            return min(.99, accepted / examined)
        # Shrink each state's rate toward this request's pooled rate rather than
        # a fixed prior, so short high-acceptance requests are not biased down.
        pooled_a, pooled_e = accepted, examined
        state_a = state_e = 0
        for state, gamma, n in self._rounds:
            pooled_a += n
            pooled_e += n + (n < gamma)
            if state == after_full:
                state_a += n
                state_e += n + (n < gamma)
        pooled = pooled_a / pooled_e
        k = self.state_prior_weight
        return min(.99, (state_a + k*pooled)/(state_e + k))

    def _verify_estimate(self):
        if not self._verify_history:
            return self.verify_prior_ms
        if not self.robust_estimates:
            return median(self._verify_history)
        # Expected round time needs the mean of a heavy-tailed round trip;
        # winsorize single spikes at three times the recent median.
        cap = 3*median(self._verify_history)
        return sum(min(v, cap) for v in self._verify_history)/len(self._verify_history)

    def _token_cost(self):
        if not self.robust_estimates:
            return super()._token_cost()
        # Ratio of sums with a prior pseudo-count; per-call ratios are noisy
        # for short calls and early GPU-clock ramp-up.
        k = self.token_prior_weight
        work = sum(t-self.call_overhead_ms for n, t in self._background_history if n)
        tokens = sum(n for n, t in self._background_history)
        return max(5.0, (work + k*self.token_ms)/(tokens + k))

    def _choose_gamma(self, default, remaining):
        self._remaining = remaining
        verify = self._verify_estimate()
        alphas = self._alpha(False), self._alpha(True)
        samples = token_samples = None
        if self.robust_estimates and self._verify_history:
            cap = 3*median(self._verify_history)
            samples = [min(v, cap) for v in self._verify_history]
            token_samples = [max(5.0, (t-self.call_overhead_ms)/n)
                             for n, t in self._background_history if n] or None
        gamma_max = self.config['GAMMA_MAX']
        choice = choose_windows(*alphas, verify, self.call_overhead_ms, self._token_cost(),
                                self.energy_weight, self.energy_ratio, gamma_max,
                                fresh_options=range(self.min_fresh_gamma, gamma_max+1),
                                lookahead_options=range(self.min_lookahead, gamma_max+2),
                                verify_samples=samples, token_ms_samples=token_samples)
        self.fresh_gamma = choice['fresh_gamma']
        self._planned_h = choice['lookahead']
        self._choice = dict(choice, alpha_miss=alphas[0], alpha_hit=alphas[1], verify_ms=verify,
                            token_ms=self._token_cost(), after_full=self._prev_full)
        return min(self.config['GAMMA_MAX'], remaining)

    def draft(self, prompt_ids, gamma, temperature=0.0):
        ids, lps = super().draft(prompt_ids, gamma, temperature)
        self._last_sent = len(ids)
        return ids, lps

    def _choose_h(self, draft):
        after = self._remaining - len(draft) - 1
        h = 0 if after <= 0 else min(self._planned_h, after+1)
        self.pipeline_decisions.append(dict(self._choice, round=len(self.pipeline_decisions),
                                            gamma=len(draft), h=h))
        return h

    def _verification_result(self, result):
        sent = result.metadata.get('n_draft', self._last_sent)
        full = result.n_accepted == sent
        self._rounds.append((self._prev_full, sent, result.n_accepted))
        self._prev_full = full

    def generate(self, messages, verifier, **kwargs):
        self._rounds.clear()
        self._prev_full = False
        text, metrics = super().generate(messages, verifier, **kwargs)
        metrics.lookahead.update(variant='markov_pipeline', energy_weight=self.energy_weight,
                                 energy_ratio=self.energy_ratio, robust_estimates=self.robust_estimates,
                                 call_overhead_ms=self.call_overhead_ms, min_fresh_gamma=self.min_fresh_gamma,
                                 min_lookahead=self.min_lookahead)
        return text, metrics
