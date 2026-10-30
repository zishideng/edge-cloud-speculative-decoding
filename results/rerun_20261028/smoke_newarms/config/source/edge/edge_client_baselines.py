"""Published adaptive and pipelined baselines, re-implemented on the edge side of this testbed.

All three keep strict K=1 greedy verification, one verification request in flight and the
unchanged KV-cache verify server, so only the edge-side policy differs from the other arms.

PicoSpec (arXiv 2603.19133): the edge drafts a fixed window (gamma=4, the paper's default) and,
while the cloud verifies it, optimistically drafts the next window from its tail. When the
verification shows a rejection, PicoSpec interrupts the now-invalid background drafting
instead of letting it finish. Not reproduced (cloud changes or unspecified): PreVerify fast
verification, sparse top-K probability compression (irrelevant to greedy K=1 verification)
and the latency-aware truncation rule, for which the paper gives no condition.

PipeSD (arXiv 2605.13319): the edge drafts token by token in one continuous stream and requests
verification when the cumulative confidence of the unverified tokens falls to R1 or a single
token's confidence falls to R2 (NAV trigger, the triggering token is sent). The stream never
pauses for verification: it keeps drafting from the tail, and those tokens are kept only if
the whole window and the bonus token match (PipeSD App. B); otherwise drafting restarts from
the last verified token. Confidence is the draft probability of the greedy token (top-1,
pre-sampling). R1 and R2 are tuned per model pair and delay by 16 trials over (0, 1)^2
minimizing time per token (experiments/tune_pipesd.py; random search with the paper's sample
budget, not its Bayesian optimizer). Not reproduced: splitting one window into several uploads
(the DP batch schedule), because uploading a few token ids costs well under a millisecond here.

HF default (transformers assisted generation, current defaults): synchronous drafting of at
most 20 tokens that stops after a token with draft probability below a confidence threshold
(0.4, re-fit every round by HF's ROC rule). HF heuristic (num_assistant_tokens_schedule=
'heuristic', the pre-4.45 default): synchronous drafting; the window starts at 5 and grows by
2 after a fully accepted round, otherwise shrinks by 1 (minimum 1), reset for every request
('heuristic_transient'), capped at max_draft (16) here.

PEARL (Liu et al., ICLR 2025): parallel drafting and verification in lockstep with pre-verify
and post-verify; see PEARLClient.
"""
import json
import math
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests

from common.controller import JointController
from edge.edge_client import TOKEN_ONLY_CHAT_PARSER, EdgeClient
from edge.edge_client_lookahead import FixedLookaheadClient
from edge.edge_client_smart import ExperimentMetrics, SmartEdgeClient


def stream_draft(client, session, prompt, count, n_probs, cancel=None, stop=None):
    """Greedy streamed draft of at most count tokens. Returns (ids, logprobs).
    Closing the stream (cancel set, or stop(ids, lps) true after a token) ends generation
    on llama-server, so an interrupted draft frees the single draft slot within one token."""
    payload = {'prompt': list(prompt), 'n_predict': count, 'temperature': 0.0, 'return_tokens': True,
               'cache_prompt': True, 'n_probs': n_probs, 'seed': client.seed, 'stream': True,
               'stop': getattr(client, 'stop_strings', []), 'samplers': ['top_k'], 'top_k': 1,
               'top_p': 1.0, 'min_p': 0.0}
    if getattr(client, 'token_only_parser', False):
        payload['chat_parser'] = TOKEN_ONLY_CHAT_PARSER
    ids, lps = [], []
    with session.post(f'{client.draft_url}/completion', json=payload, stream=True, timeout=120) as r:
        r.raise_for_status()
        for line in r.iter_lines():
            if cancel is not None and cancel.is_set():
                break
            if not line.startswith(b'data: '):
                continue
            event = json.loads(line[6:])
            probs = event.get('completion_probabilities') or []
            tokens = event.get('tokens') or [p['id'] for p in probs]
            for i, token in enumerate(tokens):
                ids.append(int(token))
                lps.append(float(probs[i]['logprob']) if i < len(probs) else 0.0)
            if event.get('stop') or len(ids) >= count or (tokens and stop is not None and stop(ids, lps)):
                break
    return ids[:count], lps[:count]


class InterruptibleLookaheadClient(FixedLookaheadClient):
    """Background drafting that can be stopped early. interrupt_on_reject stops it as soon as
    the verified prefix contradicts the window it was drafted from; stop_on_return stops it
    when the verification result arrives, whatever the outcome."""
    interrupt_on_reject = True
    stop_on_return = False
    prefetch_n_probs = 0

    def _launch(self, prompt, draft, eos_id):
        if eos_id in draft:
            return
        h = self._choose_h(draft)
        if not h:
            return
        if self._pending is not None:
            raise RuntimeError('Previous lookahead was not consumed')
        prefix = list(prompt)+list(draft)
        event = dict(event_index=len(self.lookahead_events), prefix_tokens=len(prefix),
                     requested_tokens=h, generated_tokens=0, reused_tokens=0, bridge_tokens=0,
                     discarded_tokens=0, unused_tokens=0, service_ms=0.0, wait_ms=0.0,
                     outcome='pending', interrupted=False)
        self.lookahead_events.append(event)
        self._cancel = threading.Event()
        future = self._pool.submit(self._interruptible_prefetch, prefix, h, self._cancel)
        self._pending = (prefix, future, event)

    def _interruptible_prefetch(self, prefix, count, cancel):
        started = time.perf_counter()
        ids, lps = stream_draft(self, self._worker._session, prefix, count, self.prefetch_n_probs, cancel)
        return ids, lps, (time.perf_counter()-started)*1000

    def _take(self, prompt=None, gamma=0):
        if self._pending is not None:
            prefix, _, event = self._pending
            rejected = prompt is not None and list(prompt[:len(prefix)]) != prefix
            if prompt is None or (rejected and self.interrupt_on_reject) or self.stop_on_return:
                event['interrupted'] = True
                self._cancel.set()
        return super()._take(prompt, gamma)


class PicoSpecClient(InterruptibleLookaheadClient):
    def __init__(self, draft_url='http://localhost:8080', config=None, gamma=4):
        # The optimistic next window starts at the bonus position, as for fixed_g<gamma>.
        super().__init__(draft_url, config, lookahead_tokens=gamma+1)
        self.window = gamma

    def _choose_gamma(self, default, remaining):
        return min(self.window, remaining)

    def generate(self, messages, verifier, **kwargs):
        text, metrics = super().generate(messages, verifier, **kwargs)
        metrics.lookahead.update(variant='picospec', window=self.window, interrupt_on_reject=True)
        return text, metrics


class _TokenStream:
    """One continuous greedy draft stream on its own thread and HTTP session. Tokens are
    published as they arrive; get(i) blocks until token i exists or the stream ends."""

    def __init__(self, client, prefix, count, n_probs):
        self.prefix, self.ids, self.lps = list(prefix), [], []
        self.cancel, self.done, self.error = threading.Event(), False, None
        self._cond = threading.Condition()
        self._thread = threading.Thread(target=self._run, args=(client, count, n_probs), daemon=True)
        self._thread.start()

    def _publish(self, ids, lps):
        with self._cond:
            self.ids, self.lps = list(ids), list(lps)
            self._cond.notify_all()
        return False

    def _run(self, client, count, n_probs):
        session = requests.Session()
        try:
            self._publish(*stream_draft(client, session, self.prefix, count, n_probs, self.cancel,
                                        stop=self._publish))
        except BaseException as error:
            self.error = error
        finally:
            session.close()
            with self._cond:
                self.done = True
                self._cond.notify_all()

    def available(self):
        with self._cond:
            return len(self.ids)

    def get(self, i):
        with self._cond:
            self._cond.wait_for(lambda: len(self.ids) > i or self.done)
            if len(self.ids) > i:
                return self.ids[i], self.lps[i]
            if self.error is not None and not self.cancel.is_set():
                raise self.error
            return None

    def close(self):
        self.cancel.set()
        self._thread.join()


class PipeSDClient(FixedLookaheadClient):
    """Drafting is one continuous stream: after NAV sends a window, the stream keeps drafting
    from its tail while the cloud verifies. If the whole window and the bonus token match the
    stream, the next window continues from the buffered tokens without a new draft request;
    otherwise the stream is stopped and drafting restarts from the last verified token."""

    def __init__(self, draft_url='http://localhost:8080', config=None, r1=0.5, r2=0.5, max_draft=16):
        super().__init__(draft_url, config, lookahead_tokens=0)
        if not (0 < r1 < 1 and 0 < r2 < 1) or max_draft < 1:
            raise ValueError('Invalid PipeSD settings')
        self.r1, self.r2, self.max_draft = r1, r2, max_draft
        self.draft_n_probs = 1
        self._stream = None

    def _nav_trigger(self, lps):
        """Index of the first token at which NAV fires, or None."""
        c1 = 1.0
        for i, lp in enumerate(lps):
            p = math.exp(lp)
            if p * c1 <= self.r1 or p <= self.r2:
                return i
            c1 *= p
        return None

    def _choose_gamma(self, default, remaining):
        return min(self.max_draft, self.config['GAMMA_MAX'], remaining)

    def _follows(self, stream, prompt):
        """Offset of prompt's end in the stream, or None if the stream contradicts prompt."""
        offset = len(prompt) - len(stream.prefix)
        if offset < 0 or prompt[:len(stream.prefix)] != stream.prefix:
            return None
        for j in range(offset):
            token = stream.get(j)
            if token is None or token[0] != prompt[len(stream.prefix)+j]:
                return None
        return offset

    def _stop_stream(self):
        if self._stream is not None:
            self._stream.close()
            self._stream = None

    def draft(self, prompt_ids, gamma, temperature=0.0):
        prompt = list(prompt_ids)
        offset = None if self._stream is None else self._follows(self._stream, prompt)
        restarted = offset is None
        if restarted:
            self._stop_stream()
            self._stream, offset = _TokenStream(self, prompt, self._budget-self._produced, 1), 0
        ready = self._stream.available() - offset
        ids, lps = [], []
        while len(ids) < gamma:
            token = self._stream.get(offset+len(ids))
            if token is None:
                break
            ids.append(token[0])
            lps.append(token[1])
            if token[0] == self._lookahead_eos or self._nav_trigger(lps) is not None:
                break
        if not ids:
            if restarted:
                raise RuntimeError('PipeSD draft stream returned no tokens')
            self._stop_stream()
            return self.draft(prompt_ids, gamma, temperature)
        self._windows.append(dict(sent=len(ids), ready=max(0, min(ready, len(ids))), restarted=restarted))
        return ids, lps

    def _verification_result(self, result):
        produced = result.accepted_ids + ([] if result.bonus_id is None else [result.bonus_id])
        self._produced += len(produced)
        if (self._produced >= self._budget or self._lookahead_eos in produced or result.should_stop
                or self._stream is None):
            self._stop_stream()     # charged to the request, as the terminal drain of other arms
        elif result.n_accepted < result.metadata.get('n_draft', result.n_accepted):
            self._stream.cancel.set()   # the edge sees the rejection on receipt (PipeSD App. B)

    def generate(self, messages, verifier, **kwargs):
        self._windows, self._produced, self._budget = [], 0, kwargs.get('max_tokens', 512)
        self._stream = None
        try:
            text, metrics = super().generate(messages, verifier, **kwargs)
        finally:
            self._stop_stream()
        metrics.lookahead.update(variant='pipesd', r1=self.r1, r2=self.r2, max_draft=self.max_draft,
                                 windows=self._windows, draft_probability_output=1, continuous_stream=True)
        return text, metrics


class HFHeuristicClient(FixedLookaheadClient):
    def __init__(self, draft_url='http://localhost:8080', config=None, initial=5, max_draft=16):
        super().__init__(draft_url, config, lookahead_tokens=0)
        self.initial, self.max_draft = initial, max_draft

    def _choose_gamma(self, default, remaining):
        return max(1, min(int(self._n), self.max_draft, self.config['GAMMA_MAX'], remaining))

    def _verification_result(self, result):
        sent = result.metadata.get('n_draft')
        self._n = self._n + 2 if result.n_accepted == sent else max(1, self._n - 1)
        self._trace.append(dict(sent=sent, accepted=result.n_accepted, next=self._n))

    def generate(self, messages, verifier, **kwargs):
        self._n, self._trace = self.initial, []
        text, metrics = super().generate(messages, verifier, **kwargs)
        metrics.lookahead.update(variant='hf_heuristic', initial=self.initial, max_draft=self.max_draft,
                                 windows=self._trace)
        return text, metrics


def roc_threshold(probs, matches):
    """Threshold minimizing fpr + 3*fnr over the ROC points of (matches, probs), as HF's
    AssistedCandidateGenerator does with sklearn.metrics.roc_curve (ties: highest threshold)."""
    pairs = sorted(zip(probs, matches), reverse=True)
    positives = sum(matches)
    negatives = len(matches) - positives
    best_cost, best = 3.0, math.inf
    tp = fp = 0
    for i, (p, m) in enumerate(pairs):
        tp, fp = tp + m, fp + (1 - m)
        if i + 1 < len(pairs) and pairs[i+1][0] == p:
            continue
        cost = fp/negatives + 3*(1 - tp/positives)
        if cost < best_cost:
            best_cost, best = cost, p
    return best


class HFDefaultClient(FixedLookaheadClient):
    """transformers assisted generation with its current defaults (num_assistant_tokens=20,
    schedule 'constant', assistant_confidence_threshold=0.4): synchronous drafting that stops
    after the first token whose draft probability is below the threshold; after every round
    the threshold is re-fit on this request's drafted tokens by the ROC rule above."""

    def __init__(self, draft_url='http://localhost:8080', config=None, max_draft=20, threshold=0.4):
        super().__init__(draft_url, config, lookahead_tokens=0)
        self.max_draft, self.initial_threshold = max_draft, threshold
        self.draft_n_probs = 1

    def _choose_gamma(self, default, remaining):
        return min(self.max_draft, self.config['GAMMA_MAX'], remaining)

    def draft(self, prompt_ids, gamma, temperature=0.0):
        ids, lps = stream_draft(self, self._session, prompt_ids, gamma, 1,
                                stop=lambda ids, l: math.exp(l[-1]) < self._threshold)
        if not ids:
            raise RuntimeError('HF draft returned no tokens')
        self._probs.extend(math.exp(lp) for lp in lps)
        self._sent = len(ids)
        return ids, lps

    def _verification_result(self, result):
        self._matches.extend([1] * result.n_accepted)
        if len(self._probs) > len(self._matches):
            self._matches.append(0)
        del self._probs[len(self._matches):]
        if len(self._probs) > 5 and {0, 1} <= set(self._matches):
            self._threshold = roc_threshold(self._probs, self._matches)
        self._trace.append(dict(sent=self._sent, accepted=result.n_accepted, next_threshold=self._threshold))

    def generate(self, messages, verifier, **kwargs):
        self._threshold, self._probs, self._matches, self._trace = self.initial_threshold, [], [], []
        text, metrics = super().generate(messages, verifier, **kwargs)
        metrics.lookahead.update(variant='hf_default', max_draft=self.max_draft,
                                 initial_threshold=self.initial_threshold, windows=self._trace)
        return text, metrics


class PEARLClient(SmartEdgeClient):
    """PEARL (Liu et al., ICLR 2025; ParallelSpeculativeDecoding src/engine.py,
    parallel_speculative_decoding) with the target behind the network. Every step the edge
    drafts gamma tokens while the cloud works, and the step ends when both are done (the
    reference code synchronizes with accelerator.wait_for_everyone):
      pre-verify: the cloud computes the target's next token while the edge drafts gamma tokens
        from the verified prefix. If the first draft equals it, the other gamma-1 drafts become
        the next window (post-verify); otherwise the drafts are discarded.
      post-verify: the cloud verifies the window while the edge drafts gamma tokens after it.
        On full acceptance the bonus token plays the role of PEARL's check of the first new
        draft: if it matches, the other gamma-1 new drafts are the next window; otherwise, or
        after a rejection, the drafts are discarded and the next step is pre-verify.
    gamma is fixed per request, set by the paper's rule gamma = round(c), c = target step time /
    draft token time, with the target step here being the measured verification round trip.
    The verify server needs a nonempty draft, so pre-verify sends the last verified token
    (always accepted) and reads the target's next token from the bonus. The first step of a
    request drafts synchronously, because the prompt's last token was not produced by the
    target and could be rejected. If the anchor is rejected anyway (a near-tie flipping between
    differently shaped forward passes), that step yields no token and its drafts are sent as an
    ordinary window; such steps are counted in steps[].anchor_rejected."""

    def __init__(self, draft_url='http://localhost:8080', config=None, gamma=4):
        super().__init__(draft_url, config)
        if gamma < 2:
            raise ValueError('PEARL needs gamma >= 2')
        self.gamma = gamma

    def _row(self, vr, sent, draft_ms, round_start, mode, control, m):
        decisions = vr.metadata['decisions'] if mode != 'pre' else []
        row = dict(vr.metadata['timing'], gamma=len(sent) if mode != 'pre' else 0, k=1,
                   n_accepted=vr.n_accepted if mode != 'pre' else 0, n_examined=len(decisions),
                   n_proposed=len(sent) if mode != 'pre' else 0,
                   strict_accepted=sum(d['strict_accepted'] for d in decisions),
                   relaxed_only=sum(d['relaxed_only'] for d in decisions),
                   draft_token_ms=draft_ms/max(1, len(sent)), draft_ms=draft_ms,
                   round_total_ms=(time.perf_counter()-round_start)*1000,
                   decisions=decisions, round_index=m.n_rounds, pearl_mode=mode)
        row['controller'] = (control.observe(row, decisions, vr.metadata['quality_spent'])
                             if mode != 'pre' else dict(reason='pearl pre-verify'))
        return row

    def generate(self, messages, verifier, gamma=None, max_tokens=512, temperature=0.0, eos_id=None,
                 no_think=False, strategy='strict', adaptive_window=False, fixed_k=None):
        if temperature != 0 or max_tokens < 1 or eos_id is None:
            raise ValueError('PEARL runs greedy with a positive max_tokens and an explicit eos_id')
        start = time.perf_counter()
        c = dict(self.config)
        control = JointController(c, 'strict', False, 1)
        ids = self.tokenize(self.apply_chat_template(messages), add_special=False)
        bos = getattr(self, 'prepend_bos_id', None)
        if bos is not None and ids[:1] != [bos]:
            ids = [bos] + ids
        worker = EdgeClient(self.draft_url)
        worker.seed, worker.draft_n_probs = self.seed, 0
        worker.token_only_parser = getattr(self, 'token_only_parser', False)
        worker.stop_strings = getattr(self, 'stop_strings', [])
        pool = ThreadPoolExecutor(max_workers=1)
        policy = {'strategy': 'strict', 'k': 1, 'spent': 0.0, 'config': c}
        m, trace = ExperimentMetrics(), []
        window, mode = None, 'start'
        try:
            while len(m.output_ids) < max_tokens:
                round_start = time.perf_counter()
                remaining = max_tokens - len(m.output_ids)
                first_ms = 0.0
                if mode == 'start':
                    window = self.draft(ids, min(self.gamma, remaining), 0.0)[0]
                    first_ms, mode = (time.perf_counter()-round_start)*1000, 'post'
                if mode == 'pre':
                    future = pool.submit(worker.draft, list(ids), self.gamma, 0.0)
                    sent, prompt = [ids[-1]], ids[:-1]
                else:
                    sent, prompt = list(window[:remaining]), list(ids)
                    future = pool.submit(worker.draft, prompt+sent, self.gamma, 0.0) \
                        if len(sent) < remaining and eos_id not in sent else None
                policy['spent'] = control.spent
                verifier.policy = policy
                vr = verifier.verify(prompt, sent, None, temperature=0.0, eos_id=eos_id)
                waited = time.perf_counter()
                drafts = future.result()[0] if future is not None else []
                draft_ms = first_ms + (time.perf_counter()-waited)*1000
                anchor_rejected = mode == 'pre' and (vr.n_accepted != 1 or vr.bonus_id is None)
                if anchor_rejected:
                    # Rare: re-verifying the target's own last token in a differently shaped
                    # forward pass flips a near-tie (the server is not batch invariant). Keep the
                    # committed output and send the drafts as an ordinary window next step.
                    produced = []
                elif mode == 'pre':
                    produced = [vr.bonus_id]
                else:
                    if vr.accepted_ids != sent[:vr.n_accepted]:
                        raise RuntimeError('Invalid accepted prefix from verifier')
                    produced = vr.accepted_ids + ([] if vr.bonus_id is None else [vr.bonus_id])
                produced = produced[:remaining]
                if eos_id in produced:
                    produced = produced[:produced.index(eos_id)+1]
                if not produced and not anchor_rejected:
                    raise RuntimeError('Verifier made no progress')
                row = self._row(vr, sent, draft_ms, round_start, mode, control, m)
                row['pearl_anchor_rejected'] = anchor_rejected
                if anchor_rejected:
                    trace.append(dict(mode=mode, sent=0, drafted=len(drafts), continued=False, anchor_rejected=True))
                    m.rounds.append(row)
                    m.n_rounds += 1
                    m.draft_time_ms += draft_ms
                    m.verify_time_ms += vr.verify_time_ms
                    m.network_time_ms += vr.network_time_ms
                    window, mode = (drafts, 'post') if drafts else (None, 'start')
                    continue
                full = mode == 'pre' or vr.n_accepted == len(sent)
                hit = full and vr.bonus_id is not None and drafts[:1] == [vr.bonus_id] and len(drafts) > 1
                trace.append(dict(mode=mode, sent=len(sent) if mode != 'pre' else 0, drafted=len(drafts),
                                  continued=hit))
                visible = (time.perf_counter()-start)*1000
                m.output_ids.extend(produced)
                m.token_visible_ms.extend([visible]*len(produced))
                ids.extend(produced)
                m.rounds.append(row)
                m.n_rounds += 1
                m.n_draft_proposed += row['n_proposed']
                m.n_accepted += row['n_accepted']
                m.n_bonus += int(vr.bonus_id is not None)
                m.draft_time_ms += draft_ms
                m.verify_time_ms += vr.verify_time_ms
                m.network_time_ms += vr.network_time_ms
                if eos_id in produced or vr.should_stop:
                    m.stop_reason = 'eos' if eos_id in produced else 'server_stop'
                    break
                window, mode = (drafts[1:], 'post') if hit else (None, 'pre')
        finally:
            pool.shutdown(wait=True)
            worker._session.close()
        m.total_output_tokens = len(m.output_ids)
        m.ttft_ms = m.token_visible_ms[0]
        if len(m.output_ids) > 1:
            m.tpot_ms = (m.token_visible_ms[-1]-m.token_visible_ms[0])/(len(m.output_ids)-1)
        m.quality_spent = control.spent
        text = self.detokenize([t for t in m.output_ids if t != eos_id])
        m.wall_time_s = time.perf_counter()-start
        m.lookahead = dict(variant='pearl', gamma=self.gamma, steps=trace)
        self.last_lookahead = m.lookahead
        return text, m
