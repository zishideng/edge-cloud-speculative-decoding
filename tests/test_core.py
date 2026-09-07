import copy
import math
import unittest
import warnings
from common.experiment_config import load_config, validate
from common.acceptance import accept_prefix
from common.controller import JointController
from common.window_estimator import expected_tokens, estimate, WindowController
from common.metrics import summary, latency_breakdown


def config():
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        return load_config()


def distribution():
    return {1: {'logprob': math.log(.45), 'rank': 1},
            2: {'logprob': math.log(.40), 'rank': 2},
            3: {'logprob': math.log(.1), 'rank': 3},
            99: {'logprob': math.log(.001), 'rank': 99}}


def row(g=2, rtt=100):
    return dict(gamma=g, n_accepted=g, n_examined=g, network_rtt_ms=rtt,
                cloud_verify_ms=3+g*.3, draft_token_ms=2)


class AcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.c = config()

    def accept(self, ids, k=1, **kw):
        return accept_prefix([distribution() for _ in ids], ids, k=k, config=self.c, **kw)

    def test_strict_prefix(self):
        accepted, correction, decisions, _ = self.accept([1,2,1])
        self.assertEqual(accepted, [1]); self.assertEqual(correction,1)
        self.assertEqual(len(decisions),2)

    def test_topk_boundaries(self):
        self.assertEqual(self.accept([2],2)[0],[2])
        self.assertEqual(self.accept([2],1)[0],[])
        self.assertEqual(self.accept([3],3)[0],[])
        self.assertEqual(self.accept([99],4)[0],[])

    def test_k_bounds(self):
        for k in (0,5):
            with self.assertRaises(ValueError): self.accept([1],k)
        self.assertEqual(self.accept([1],4)[0],[1])

    def test_budget_hard_limit_within_round(self):
        self.c['QUALITY_BUDGET'] = .15
        a, _, decisions, spent = self.accept([2,2],2)
        self.assertEqual(a,[2]); self.assertLessEqual(spent,.15)

    def test_budget_exhaustion_k1(self):
        _,_,d,_ = self.accept([2],4,spent=self.c['QUALITY_BUDGET'])
        self.assertEqual(d[0]['k'],1); self.assertFalse(d[0]['accepted'])

    def test_eos_stops_prefix(self):
        self.assertEqual(self.accept([1,1],eos_id=1)[0],[1])

    def test_missing_distribution_errors(self):
        with self.assertRaises(ValueError):
            accept_prefix([{}],[1],k=1,config=self.c)

    def test_no_missing_token_infinite_json(self):
        d = self.accept([999],2)[2][0]
        self.assertIsNone(d['logprob_regret'])

    def test_flat_confidence_rejected(self):
        self.c['MIN_TOP1_CONFIDENCE'] = .5
        self.assertEqual(self.accept([2],2)[0],[])


class ControlTests(unittest.TestCase):
    def test_formula_edges(self):
        self.assertEqual(expected_tokens(0,8),1)
        self.assertEqual(expected_tokens(1,8),9)
        self.assertAlmostEqual(expected_tokens(.5,2),1.75)
        self.assertAlmostEqual(expected_tokens(1-1e-12,8),9,places=8)

    def test_extreme_rtt(self):
        self.assertEqual(estimate(0,2,100,3,.3,1,8)[0],1)
        self.assertEqual(estimate(1,2,100000,3,.3,1,8)[0],8)

    def test_invalid_estimates(self):
        for a in (-1,2,float('nan')):
            with self.assertRaises(ValueError): estimate(a,2,1,3,1,1,8)

    def test_fixed_vs_adaptive_window(self):
        c=config(); fixed=WindowController(c,False); adaptive=WindowController(c,True)
        self.assertEqual(adaptive.choose()['gamma'],c['GAMMA_INITIAL'])
        for _ in range(6):
            fixed.observe(row()); adaptive.observe(row())
        self.assertEqual(fixed.choose()['gamma'],2)
        result=adaptive.choose(); self.assertEqual(result['gamma'],3)
        self.assertFalse(result['fit_identifiable'])
        self.assertEqual(len(result['candidates']),8)

    def test_fixed_vs_adaptive_k(self):
        c=config(); fixed=JointController(c,'fixed',True,2); adaptive=JointController(c,'adaptive',True)
        d=accept_prefix([distribution()],[2],k=1,config=c)[2]
        for _ in range(2):
            fixed.observe(row(),d,0); result=adaptive.observe(row(),d,0)
        self.assertEqual(fixed.k,2); self.assertEqual(adaptive.k,2)
        self.assertIn('hold',result['window']['reason']) if result['window']['candidates'] else None

    def test_quality_priority(self):
        c=config(); ctrl=JointController(c,'fixed',True,4)
        result=ctrl.observe(row(),[],c['QUALITY_BUDGET'])
        self.assertEqual(result['next_k'],1)

    def test_config_missing_and_invalid(self):
        with self.assertRaisesRegex(ValueError,'K_MIN'):
            load_config('configs/experiment.template.json')
        for key,value in [('K_MIN',2),('K_MAX',0),('QUALITY_BUDGET',-1),('GAMMA_INITIAL',100),('MIN_PROBABILITY_RATIO',2)]:
            c=config(); c[key]=value
            with self.assertRaises(ValueError): validate(c)


class TimingTests(unittest.TestCase):
    def test_percentiles(self):
        s=summary([1,2,3,4,5]); self.assertEqual(s['p50'],3)
        self.assertAlmostEqual(s['p95'],4.8); self.assertAlmostEqual(s['p99'],4.96)
        with self.assertRaises(ValueError): summary([])

    def test_network_excludes_queue_compute(self):
        m=latency_breakdown(100,2,3,20,60,100,300)
        self.assertEqual(m['network_rtt_ms'],20)
        self.assertEqual(m['upload_ms'],5); self.assertEqual(m['download_ms'],15)
        self.assertTrue(m['upload_download_estimated'])

    def test_inconsistent_clock_measurement_is_flagged(self):
        m=latency_breakdown(10,0,0,5,10,1,1)
        self.assertTrue(m['timing_inconsistent'])
        self.assertEqual(m['timing_residual_ms'],-5)


class RegressionTests(unittest.TestCase):
    def test_artifact_directories_are_isolated(self):
        import tempfile
        from experiments.run import create_output
        with tempfile.TemporaryDirectory() as tmp:
            a,b=create_output(tmp),create_output(tmp)
            self.assertNotEqual(a,b)
            self.assertTrue((a/'raw').is_dir())
            self.assertTrue((b/'report').is_dir())

    def test_strict_matches_target_for_all_windows(self):
        from common.simulation import run_simulation
        c=config()
        for g in c['GAMMA_SWEEP']:
            result=run_simulation(c,'strict',False,g,1,0,c['NETWORK_SCENARIOS']['high'])
            self.assertEqual(result['output_ids'],result['reference_ids'])

    def test_adaptive_strict_matches_reference(self):
        from common.simulation import run_simulation
        c=config(); r=run_simulation(c,'strict',True,2,1,0,c['NETWORK_SCENARIOS']['burst'])
        self.assertEqual(r['output_ids'],r['reference_ids'])

    def test_simulation_determinism_and_budget(self):
        from common.simulation import run_simulation
        c=config(); args=(c,'adaptive',True,2,None,0,c['NETWORK_SCENARIOS']['high'])
        a=run_simulation(*args); b=run_simulation(*args)
        self.assertEqual(a,b); self.assertLessEqual(a['quality_spent'],c['QUALITY_BUDGET'])
        self.assertIsNone(a['task_quality'])
        self.assertTrue(any(r['k']>1 for r in a['rounds']))
        self.assertEqual(a['rounds'][-1]['controller']['next_k'],1)

    def test_joint_changes_only_one_axis(self):
        from common.simulation import run_simulation
        c=config(); a=run_simulation(c,'adaptive',True,2,None,0,c['NETWORK_SCENARIOS']['high'])
        for row_ in a['rounds']:
            next_=row_['controller']
            if row_['k']!=next_['next_k']:
                self.assertEqual(next_['next_gamma'],row_['gamma'])

    def test_delay_jump_reestimates_during_cooldown(self):
        c=config(); w=WindowController(c,True)
        for _ in range(4): w.observe(row(rtt=2))
        w.observe(row(rtt=1000))
        result=w.choose(); self.assertEqual(result['reason'],'latency jump')

    def test_regression_model_fit(self):
        w=WindowController(config(),True)
        for g in (1,2,3,4): w.observe(row(g))
        r=w.choose(); self.assertTrue(r['fit_identifiable'])
        self.assertAlmostEqual(r['verify_fixed_ms'],3)
        self.assertAlmostEqual(r['verify_token_ms'],.3)

    def test_quality_and_missing_answer(self):
        from common.quality import task_quality, difference_rate
        self.assertEqual(task_quality('gsm8k','Final answer: 18',{'gold_answer':'18'}),1)
        self.assertEqual(task_quality('gsm8k','No result',{'gold_answer':'18'}),0)
        self.assertIsNone(task_quality('humaneval','pass',{}))
        self.assertEqual(difference_rate([1,2],[1,2]),0)

    def test_removed_route_static_check(self):
        from experiments.static_check import main
        main()


if __name__ == '__main__': unittest.main()
