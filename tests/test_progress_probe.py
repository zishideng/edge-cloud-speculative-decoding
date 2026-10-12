"""Check repeated-prompt statistics used by the live progress probes."""
import json
from pathlib import Path
import tempfile
import unittest
from experiments.adaptive_research import sha256, write_json
from experiments.progress_probe import paired_effect, resume_state


class ProbeStatisticsTests(unittest.TestCase):
    def records(self):
        rows=[]
        for dataset in ['gsm8k','mtbench']:
            for repeat in range(2):
                for scenario in ['low','very_high']:
                    for method,wall in [('fixed_fast',2.),('fixed_g2',1.)]:
                        rows.append(dict(dataset=dataset,request_index=0,repeat=repeat,
                            scenario=scenario,method=method,output_tokens=10,wall_time_s=wall,
                            output_ids=[1]*10,truncated=False,task_quality=None,
                            energy=dict(available=True,joules=wall*5,sample_hz=1,
                                samples=[dict(t=0.,power_w=5.),dict(t=wall,power_w=5.)])))
        return rows

    def test_repeats_and_scenarios_remain_in_two_independent_prompt_clusters(self):
        result=paired_effect(self.records(),'fixed_g2',['low','very_high'],draws=50)
        self.assertEqual(result['independent_prompts'],2)
        self.assertEqual(result['request_pairs'],8)
        self.assertEqual(result['throughput_gain_pct'],100.)
        self.assertEqual(result['energy_saving_pct'],50.)
        self.assertEqual(result['changed_sequences'],0)
        self.assertEqual(result['scored_pairs'],0)
        self.assertTrue(result['energy_valid'])
        self.assertTrue(result['complete_pairs'])

    def test_missing_method_pair_is_explicitly_incomplete(self):
        rows=self.records()[:-1]
        result=paired_effect(rows,'fixed_g2',['low','very_high'],draws=20)
        self.assertFalse(result['complete_pairs'])
        self.assertEqual(result['request_pairs'],7)

    def test_invalid_energy_is_unavailable_without_hiding_speed_or_pairs(self):
        rows=self.records();rows[-1]['energy']['available']=False
        result=paired_effect(rows,'fixed_g2',['low','very_high'],draws=20)
        self.assertFalse(result['energy_valid'])
        self.assertIsNone(result['energy_saving_pct'])
        self.assertIsNone(result['energy_ci95'])
        self.assertEqual(result['throughput_gain_pct'],100.)
        self.assertEqual(result['request_pairs'],8)



class ResumeTests(unittest.TestCase):
    def test_resume_skips_valid_records_and_reruns_invalid_energy(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp);plan=d/'plan.json';plan.write_text('{"phase": "x"}')
            jobs=[dict(id=f'j{i}') for i in range(3)]
            write_json(d/'config/protocol.json',dict(jobs=jobs,source_plan_sha256=sha256(plan)))
            write_json(d/'report/status.json',dict(state='failed',completed=2,expected=3,failures=['x']))
            write_json(d/'raw/j0.json',dict(energy_validation=dict(valid=True)))
            write_json(d/'raw/j1.json',dict(energy_validation=dict(valid=False)))
            got,done,status=resume_state(d,plan)
            self.assertEqual(got,jobs);self.assertEqual(done,{'j0'})
            self.assertEqual(status['completed'],1);self.assertEqual(len(status['resumed_utc']),1)
            self.assertFalse((d/'raw/j1.json').exists());self.assertTrue((d/'failed/j1_resume1.json').exists())
            plan.write_text('{"phase": "y"}')
            with self.assertRaises(ValueError):
                resume_state(d,plan)


if __name__=='__main__':
    unittest.main()
