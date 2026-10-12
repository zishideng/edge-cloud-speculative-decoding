"""AdaEDL early draft stopping (Agrawal et al., arXiv:2410.18351), re-implemented
for this edge-cloud setting as synchronous strict-K=1 speculative decoding.

Drafting streams tokens from llama-server with top-k probabilities and stops
before a token whose entropy-based acceptance bound 1 - sqrt(gamma * H) falls
below the threshold lambda (the first token of a round is always kept). After
each verification lambda is adapted with the paper's Algorithm 1 and default
hyperparameters (gamma=0.2, beta1=0.5, beta2=0.9, eps=0.01, alpha=0.9).

Deviations, because llama-server exposes only top-k probabilities: entropy is
computed from the top-k probabilities plus the residual mass treated as one
token (a lower bound on the full-vocabulary entropy). The paper does not state
the initial lambda; lambda0 is a parameter. No lookahead is used, as in the
paper; the cost of probability output and streaming is part of the method.
"""
import json
import math
import time

from edge.edge_client import TOKEN_ONLY_CHAT_PARSER
from edge.edge_client_lookahead import FixedLookaheadClient

DEFAULT_TOP_K = 20


def entropy_lower_bound(logprobs):
    probs = [math.exp(lp) for lp in logprobs]
    residual = max(0.0, 1.0 - sum(probs))
    terms = [p for p in probs if p > 0] + ([residual] if residual > 1e-12 else [])
    return -sum(p * math.log(p) for p in terms)


class AdaEDLClient(FixedLookaheadClient):
    def __init__(self, draft_url='http://localhost:8080', config=None, max_draft=8, gamma=0.2,
                 lambda0=0.5, beta1=0.5, beta2=0.9, eps=0.01, alpha=0.9, top_k=DEFAULT_TOP_K):
        super().__init__(draft_url, config, lookahead_tokens=0)
        if type(max_draft) is not int or max_draft < 1 or top_k < 2:
            raise ValueError('Invalid AdaEDL settings')
        self.max_draft, self.gamma_coef, self.lambda0 = max_draft, gamma, lambda0
        self.beta1, self.beta2, self.eps, self.alpha, self.top_k = beta1, beta2, eps, alpha, top_k
        self.draft_n_probs = top_k

    def stop_bound(self, logprobs):
        return 1 - math.sqrt(self.gamma_coef * entropy_lower_bound(logprobs))

    def _choose_gamma(self, default, remaining):
        return min(self.max_draft, self.config['GAMMA_MAX'], remaining)

    def _fresh_draft(self, prompt, count, temperature):
        payload = {'prompt': list(prompt), 'n_predict': count, 'temperature': 0.0,
                   'return_tokens': True, 'cache_prompt': True, 'n_probs': self.top_k,
                   'seed': self.seed, 'stream': True, 'stop': getattr(self, 'stop_strings', []),
                   'samplers': ['top_k'], 'top_k': 1, 'top_p': 1.0, 'min_p': 0.0}
        if getattr(self, 'token_only_parser', False):
            payload['chat_parser'] = TOKEN_ONLY_CHAT_PARSER
        ids, lps, bounds = [], [], []
        started = time.perf_counter()
        with self._session.post(f'{self.draft_url}/completion', json=payload, stream=True, timeout=120) as r:
            r.raise_for_status()
            for line in r.iter_lines():
                if not line.startswith(b'data: '):
                    continue
                event = json.loads(line[6:])
                for entry in event.get('completion_probabilities') or []:
                    bound = self.stop_bound([x['logprob'] for x in entry['top_logprobs']])
                    if ids and bound < self._lambda:
                        break
                    ids.append(int(entry['id']))
                    lps.append(float(entry['logprob']))
                    bounds.append(bound)
                else:
                    if event.get('stop') or len(ids) >= count:
                        break
                    continue
                break   # closing the stream cancels the remaining generation
        if not ids:
            raise RuntimeError('AdaEDL draft returned no tokens')
        self._rounds.append(dict(round=len(self._rounds), drafted=len(ids), requested=count,
                                 lambda_=self._lambda, bounds=bounds,
                                 draft_ms=(time.perf_counter()-started)*1000))
        self._last_sent = len(ids)
        return ids, lps

    def _verification_result(self, result):
        drafted = result.metadata.get('n_draft', self._last_sent)
        accepted = result.n_accepted
        rate = accepted / drafted
        self._ar = rate if self._ar is None else self.beta1*self._ar + (1-self.beta1)*rate
        if self._ar < self.alpha:
            target = self._lambda + self.eps
        elif accepted != self.max_draft:
            target = self._lambda - self.eps
        else:
            target = self._lambda
        self._lambda = self.beta2*self._lambda + (1-self.beta2)*target
        self._rounds[-1].update(accepted=accepted, acceptance_ema=self._ar, lambda_next=self._lambda)

    def generate(self, messages, verifier, **kwargs):
        self._lambda, self._ar, self._rounds, self._last_sent = self.lambda0, None, [], 0
        text, metrics = super().generate(messages, verifier, **kwargs)
        metrics.lookahead.update(variant='adaedl_sync', tokens=0, decisions=self._rounds,
                                 adaedl=dict(max_draft=self.max_draft, gamma=self.gamma_coef,
                                             lambda0=self.lambda0, beta1=self.beta1, beta2=self.beta2,
                                             eps=self.eps, alpha=self.alpha, top_k=self.top_k),
                                 draft_probability_output=self.top_k)
        return text, metrics
