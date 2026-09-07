"""Synchronous cloud-edge experiment client with quality-aware joint control."""
import time
from dataclasses import dataclass, field
from edge.edge_client import EdgeClient, GenerationMetrics
from common.controller import JointController
from common.experiment_config import load_config


@dataclass
class ExperimentMetrics(GenerationMetrics):
    ttft_ms: float = 0.0
    tpot_ms: float | None = None
    output_ids: list = field(default_factory=list)
    token_visible_ms: list = field(default_factory=list)
    quality_spent: float = 0.0


class SmartEdgeClient(EdgeClient):
    def __init__(self, draft_url='http://localhost:8080', config=None):
        super().__init__(draft_url)
        self.config = config if config is not None else load_config()
        self.seed = self.config['SEED']

    def generate(self, messages, verifier, gamma=None, max_tokens=512,
                 temperature=0.0, eos_id=None, no_think=False,
                 strategy='adaptive', adaptive_window=True, fixed_k=None):
        if temperature != 0:
            raise ValueError('Experiments require temperature=0; relaxed acceptance is lossy')
        if max_tokens < 1 or eos_id is None:
            raise ValueError('Positive max_tokens and explicit model eos_id required')
        start = time.perf_counter()
        c = dict(self.config)
        if gamma is not None:
            if not c['GAMMA_MIN'] <= gamma <= c['GAMMA_MAX']:
                raise ValueError('Gamma outside configured bounds')
            c['GAMMA_INITIAL'] = gamma
        control = JointController(c, strategy, adaptive_window, fixed_k)
        if no_think:
            messages = [dict(m) for m in messages]
            for message in reversed(messages):
                if message['role'] == 'user':
                    message['content'] += ' /no_think'
                    break
        ids = self.tokenize(self.apply_chat_template(messages), add_special=False)
        if not ids:
            raise ValueError('Prompt tokenization returned no tokens')
        m = ExperimentMetrics()
        while len(m.output_ids) < max_tokens:
            round_start = time.perf_counter()
            g = min(control.window.gamma, max_tokens-len(m.output_ids))
            draft_start = time.perf_counter()
            draft, lps = self.draft(ids, g, 0.0)
            draft_ms = (time.perf_counter()-draft_start)*1000
            if not draft or len(draft) > g:
                raise RuntimeError('Draft backend returned empty or oversized token sequence')
            verifier.policy = {'strategy': strategy, 'k': control.k,
                               'spent': control.spent, 'config': c}
            vr = verifier.verify(ids, draft, lps, temperature=0.0, eos_id=eos_id)
            if vr.accepted_ids != draft[:vr.n_accepted] or not 0 <= vr.n_accepted <= len(draft):
                raise RuntimeError('Invalid accepted prefix from verifier')
            produced = vr.accepted_ids + ([] if vr.bonus_id is None else [vr.bonus_id])
            produced = produced[:max_tokens-len(m.output_ids)]
            if eos_id in produced:
                produced = produced[:produced.index(eos_id)+1]
            if not produced:
                raise RuntimeError('Verifier made no progress')
            visible = (time.perf_counter()-start)*1000
            m.output_ids.extend(produced)
            m.token_visible_ms.extend([visible]*len(produced))
            ids.extend(produced)
            decisions = vr.metadata['decisions']
            row = dict(vr.metadata['timing'], gamma=len(draft), k=control.k,
                       n_accepted=vr.n_accepted, n_examined=len(decisions), n_proposed=len(draft),
                       strict_accepted=sum(d['strict_accepted'] for d in decisions),
                       relaxed_only=sum(d['relaxed_only'] for d in decisions),
                       draft_token_ms=draft_ms/len(draft), draft_ms=draft_ms,
                       round_total_ms=(time.perf_counter()-round_start)*1000,
                       decisions=decisions, round_index=m.n_rounds)
            row['controller'] = control.observe(row, decisions, vr.metadata['quality_spent'])
            m.rounds.append(row)
            m.n_rounds += 1
            m.n_draft_proposed += len(draft)
            m.n_accepted += vr.n_accepted
            m.n_bonus += int(vr.bonus_id is not None)
            m.draft_time_ms += draft_ms
            m.verify_time_ms += vr.verify_time_ms
            m.network_time_ms += vr.network_time_ms
            if c['VERBOSE_TOKENS']:
                print(decisions)
            if eos_id in produced or vr.should_stop:
                break
        m.total_output_tokens = len(m.output_ids)
        m.ttft_ms = m.token_visible_ms[0]
        if len(m.output_ids) > 1:
            m.tpot_ms = (m.token_visible_ms[-1]-m.token_visible_ms[0])/(len(m.output_ids)-1)
        m.quality_spent = control.spent
        text = self.detokenize([t for t in m.output_ids if t != eos_id])
        m.wall_time_s = time.perf_counter()-start
        return text, m
