"""Fixed lookahead during verification; speculative work never commits output.

The first lookahead token predicts the verifier's bonus token. Reuse requires
the entire verified prefix, including that bonus, to match. All orphaned work
is drained and charged to request wall time before the next request starts.
"""
from concurrent.futures import ThreadPoolExecutor
import time

from edge.edge_client import EdgeClient
from edge.edge_client_smart import SmartEdgeClient


class _OverlappedVerifier:
    def __init__(self, remote, client):
        self.remote, self.client = remote, client

    @property
    def policy(self):
        return self.remote.policy

    @policy.setter
    def policy(self, value):
        self.remote.policy = value

    def verify(self, prompt_ids, draft_ids, *args, **kwargs):
        self.client._launch(prompt_ids, draft_ids, kwargs.get('eos_id'))
        return self.remote.verify(prompt_ids, draft_ids, *args, **kwargs)


class FixedLookaheadClient(SmartEdgeClient):
    def __init__(self, draft_url='http://localhost:8080', config=None, lookahead_tokens=5):
        super().__init__(draft_url, config)
        self.lookahead_tokens = lookahead_tokens
        self.lookahead_events = []
        self._pending = None
        self._pool = None

    def _prefetch(self, prefix, count):
        started = time.perf_counter()
        ids, lps = self._worker.draft(prefix, count, 0.0)
        if not ids or len(ids) > count:
            raise RuntimeError('Empty or oversized lookahead draft')
        return ids, lps, (time.perf_counter()-started)*1000

    def _launch(self, prompt, draft, eos_id):
        if not self.lookahead_tokens or eos_id in draft:
            return
        if self._pending is not None:
            raise RuntimeError('Previous lookahead was not consumed')
        prefix = list(prompt)+list(draft)
        event = dict(event_index=len(self.lookahead_events),prefix_tokens=len(prefix),
            requested_tokens=self.lookahead_tokens,generated_tokens=0,
            reused_tokens=0,bridge_tokens=0,discarded_tokens=0,unused_tokens=0,
            service_ms=0.0,wait_ms=0.0,outcome='pending')
        self.lookahead_events.append(event)
        future = self._pool.submit(self._prefetch, prefix, self.lookahead_tokens)
        self._pending = (prefix, future, event)

    def _take(self, prompt=None, gamma=0):
        if self._pending is None:
            return [], []
        prefix, future, event = self._pending
        self._pending = None
        started = time.perf_counter()
        try:
            ids, lps, service_ms = future.result()
        except BaseException:
            event['outcome'] = 'error'
            raise
        finally:
            event['wait_ms'] = (time.perf_counter()-started)*1000
        event.update(generated_tokens=len(ids),service_ms=service_ms)
        if prompt is None:
            event.update(unused_tokens=len(ids),outcome='terminal_drain')
            return [], []
        predicted = prefix+ids
        # A matching bonus token alone is insufficient if an earlier draft
        # token was rejected. Check the complete immutable prefix.
        compatible = (len(prefix) <= len(prompt) <= len(predicted)
                      and predicted[:len(prompt)] == list(prompt))
        if not compatible:
            event.update(discarded_tokens=len(ids),outcome='prefix_mismatch')
            return [], []
        offset = len(prompt)-len(prefix)
        count = min(gamma,len(ids)-offset)
        event.update(bridge_tokens=offset,reused_tokens=count,
                     unused_tokens=len(ids)-offset-count,outcome='reused' if count else 'bridge_only')
        return ids[offset:offset+count], lps[offset:offset+count]

    def draft(self, prompt_ids, gamma, temperature=0.0):
        cached, lps = self._take(prompt_ids, gamma)
        if self._lookahead_eos in cached:
            end = cached.index(self._lookahead_eos)+1
            return cached[:end], lps[:end]
        if len(cached) < gamma:
            rest, rest_lps = super().draft(list(prompt_ids)+cached,gamma-len(cached),temperature)
            cached += rest
            lps += rest_lps
        return cached, lps

    def generate(self, messages, verifier, **kwargs):
        if type(self.lookahead_tokens) is not int or self.lookahead_tokens < 0:
            raise ValueError('lookahead_tokens must be a nonnegative integer')
        self.lookahead_events = []
        self._pending = None
        self._lookahead_eos = kwargs.get('eos_id')
        self._worker = EdgeClient(self.draft_url)
        self._worker.seed = self.seed
        self._worker.draft_n_probs = self.draft_n_probs
        self._pool = ThreadPoolExecutor(max_workers=1)
        start = time.perf_counter()
        try:
            text, metrics = super().generate(messages,_OverlappedVerifier(verifier,self),**kwargs)
        finally:
            try:
                # No background request may contaminate the next measured job.
                self._take()
            finally:
                self._pool.shutdown(wait=True)
                self._worker._session.close()
                self._pool = None
        metrics.wall_time_s = time.perf_counter()-start
        metrics.lookahead = dict(tokens=self.lookahead_tokens,events=self.lookahead_events,
            generated_tokens=sum(e['generated_tokens'] for e in self.lookahead_events),
            reused_tokens=sum(e['reused_tokens'] for e in self.lookahead_events),
            bridge_tokens=sum(e['bridge_tokens'] for e in self.lookahead_events),
            discarded_tokens=sum(e['discarded_tokens'] for e in self.lookahead_events),
            unused_tokens=sum(e['unused_tokens'] for e in self.lookahead_events),
            service_ms=sum(e['service_ms'] for e in self.lookahead_events),
            wait_ms=sum(e['wait_ms'] for e in self.lookahead_events),
            timing_note='Round draft_ms measures foreground blocking only; prefetch overlaps verify/network. Request wall time includes terminal drain. Do not add overlapping service times.')
        self.last_lookahead = metrics.lookahead
        return text, metrics
