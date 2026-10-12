import unittest
import random
import tempfile
from pathlib import Path
from collections import Counter
from types import SimpleNamespace
from unittest.mock import Mock, patch

from common.experiment_config import load_config
from edge.edge_client import EdgeClient
from edge.edge_client_regime import LatencyRegimeLookaheadClient
from edge.experiment_live import LiveExperiment
from experiments.adaptive_research import balanced_method_orders,research_method_config,report,write_json


class RegimeTests(unittest.TestCase):
    def setUp(self):
        self.c = LatencyRegimeLookaheadClient(config=load_config('configs/research.pilot.json'))
        self.addCleanup(self.c._session.close)

    def observe(self, v):
        self.c._verify_history.extend([v]*8)
        self.c._outcomes.extend([dict(accepted=4, examined=4, gamma=4, verify_ms=v)]*8)
        self.c._foreground_history.extend([(4,88)]*8)
        self.c._background_history.extend([(5,125)]*8)
        self.c._match_history.extend([True]*8)

    def test_long_latency_amortizes_verification_with_larger_window(self):
        self.observe(450)
        self.assertEqual(self.c._choose_gamma(4,512),4)
        g = self.c._choose_gamma(4,512)
        self.assertGreater(g,4)
        self.assertEqual(self.c._selected_h,g+1)
        self.assertEqual(self.c.joint_decisions[-1]['regime'],'long')

    def test_very_short_latency_keeps_drafting_enabled(self):
        self.observe(20)
        self.assertEqual(self.c._choose_gamma(4,512),4)
        self.assertEqual(self.c._selected_h,5)
        self.assertEqual(self.c.joint_decisions[-1]['regime'],'short_or_medium')

    def test_initial_prompt_prefill_is_not_marginal_draft_cost(self):
        with patch.object(EdgeClient,'draft',return_value=([1,2,3,4],[0.]*4)):
            self.c._fresh_draft([7]*200,4,0)
            self.assertEqual(len(self.c._foreground_history),0)
            self.c._fresh_draft([7]*204,4,0)
            self.assertEqual(len(self.c._foreground_history),1)

    def test_usual_short_interval_retains_full_block(self):
        self.observe(100)
        self.assertEqual(self.c._choose_gamma(4,512),4)
        self.assertEqual(self.c._selected_h,5)

    def test_marginal_overlap_budget_does_not_expand_gamma(self):
        self.observe(200)
        self.c._choose_gamma(4,512)
        self.assertEqual(self.c._choose_gamma(4,512),4)
        self.assertEqual({x['gamma'] for x in self.c.joint_decisions[-1]['candidates']},{4})

    def test_terminal_round_cannot_launch_useless_prefetch(self):
        self.observe(450)
        self.assertEqual(self.c._choose_gamma(4,3),3)
        self.assertEqual(self.c._selected_h,0)

    def test_fixed_ablation_propagates_probability_setting_and_restores_client(self):
        live = object.__new__(LiveExperiment)
        original = Mock(draft_n_probs=0,token_only_parser=True)
        live.client = original
        live.c = load_config('configs/research.pilot.json')
        live.model = {'stop_strings':[]}
        def run(*args):
            self.assertEqual(live.client.draft_n_probs,0)
            self.assertTrue(live.client.token_only_parser)
            live.client.last_lookahead = {}
            return {}
        live.run = run
        live.run_lookahead({},0,{},4,5)
        self.assertIs(live.client,original)

    def test_balanced_orders_cover_positions_and_permutations(self):
        orders=balanced_method_orders(['fixed','fixed_fast','regime'],12,random.Random(42))
        self.assertEqual(set(Counter(tuple(x) for x in orders).values()),{2})
        for i in range(3):
            self.assertEqual(set(Counter(x[i] for x in orders).values()),{4})

    def test_compact_request_keeps_acceptance_strict_and_base_unchanged(self):
        c=load_config('configs/research.pilot.json');c['FIXED_K']=1
        optimized=research_method_config(c,'regime',True)
        self.assertEqual((optimized['K_MAX'],optimized['K_INITIAL'],optimized['FIXED_K']),(1,1,1))
        self.assertEqual(optimized['K_SWEEP'],[1]);self.assertEqual(optimized['DRAFT_N_PROBS'],0)
        self.assertEqual(c['K_MAX'],4);self.assertEqual(c['DRAFT_N_PROBS'],1)
        self.assertEqual(research_method_config(c,'fixed',True),c)

    def test_exact_verified_output_and_zero_probability_worker_with_window_changes(self):
        output=list(range(2,82))+[999]
        self.c.draft_n_probs=0
        self.c.apply_chat_template=Mock(return_value='prompt')
        self.c.tokenize=Mock(return_value=[1]);self.c.detokenize=Mock(return_value='verified')
        seen_probs=[]
        def draft(client,prefix,count,temperature):
            seen_probs.append(client.draft_n_probs)
            start=len(prefix)-1;ids=output[start:start+count].copy()
            if start<=17<start+len(ids):ids[17-start]=12345
            return ids,[0.]*len(ids)
        def verify(prefix,ids,*args,**kwargs):
            start=len(prefix)-1;self.assertEqual(prefix,[1]+output[:start])
            n=0
            for a,b in zip(ids,output[start:]):
                if a!=b:break
                n+=1
            accepted=ids[:n];bonus=None if 999 in accepted else output[start+n]
            produced=accepted+([] if bonus is None else [bonus])
            ds=[dict(accepted=i<n,strict_accepted=i<n,relaxed_only=False,quality_risk=0.,p_top1=1.,target_rank=1 if i<n else 2,probability_ratio=1.,logprob_regret=0.) for i in range(min(len(ids),n+1))]
            return SimpleNamespace(accepted_ids=accepted,n_accepted=n,bonus_id=bonus,
                should_stop=999 in produced,verify_time_ms=450.,network_time_ms=0.,
                metadata=dict(quality_spent=0.,decisions=ds,timing=dict(network_rtt_ms=0.,cloud_verify_ms=450.,serialize_ms=0.,deserialize_ms=0.,cloud_queue_ms=0.)))
        remote=Mock();remote.verify.side_effect=verify
        with patch.object(EdgeClient,'draft',draft),patch.object(self.c,'_verified',side_effect=lambda elapsed:self.c._verify_history.append(450.)):
            _,m=self.c.generate([],remote,gamma=4,max_tokens=160,eos_id=999,strategy='strict',adaptive_window=False,fixed_k=1)
        self.assertEqual(m.output_ids,output);self.assertEqual(set(seen_probs),{0})
        self.assertGreater(len({r['gamma'] for r in m.rounds}),1)
        self.assertIsNone(self.c._pending)
        for e in m.lookahead['events']:
            self.assertEqual(e['generated_tokens'],sum(e[k] for k in ['reused_tokens','bridge_tokens','discarded_tokens','unused_tokens']))

    def test_secondary_long_delay_cannot_make_failed_primary_target_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)
            write_json(p/'config/protocol.json',dict(methods=['fixed','regime'],
                network_scenarios={x:{} for x in ['low','high','very_high']},
                primary_scenarios=['low','high'],expected_requests=6,target_candidate='regime'))
            write_json(p/'report/status.json',dict(state='complete',failures=[]))
            for scene in ['low','high','very_high']:
                for method in ['fixed','regime']:
                    wall=(100 if method=='fixed' else 5) if scene=='very_high' else (10 if method=='fixed' else 12)
                    name=scene+'_'+method
                    write_json(p/'raw'/f'{name}.json',dict(id=name,scenario=scene,method=method,
                        request_index=0,wall_time_s=wall,output_tokens=100,task_quality=1.,truncated=False,
                        output_ids=[1]*100,reference_ids=[1]*100,energy=dict(available=True,
                            samples=[dict(t=t,power_w=1.) for t in range(wall+1)],
                            sample_hz=1,joules=wall,joules_per_token=wall/100)))
            result=report(p)
            self.assertTrue(result['complete'])
            self.assertFalse(result['target']['point_estimate_met'])
            self.assertLess(result['comparisons']['pooled']['regime_vs_fixed']['throughput_gain_pct'],0)
            self.assertNotIn('very_high', result['comparisons'])
            self.assertNotIn('very_high', result['summaries'])
            self.assertEqual(result['summaries']['pooled']['fixed']['requests'],2)


if __name__ == '__main__':
    unittest.main()
