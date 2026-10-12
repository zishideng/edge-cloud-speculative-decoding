"""Energy units, integration, missing data, measurement scope and reporting."""
import json
from pathlib import Path
import tempfile
import time
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from edge.energy_profiler import EnergyProfiler, local_draft_url
from edge.experiment_live import LiveExperiment
from experiments.adaptive_research import aggregate, compare, report, write_json


class EnergyTests(unittest.TestCase):
    def test_integrates_irregular_samples_and_time_weighted_power(self):
        ep = EnergyProfiler()
        ep.samples = [dict(t=0,power_w=10),dict(t=.2,power_w=20),dict(t=1,power_w=20)]
        result = ep.record(19)
        self.assertEqual(result['joules'], 19)
        self.assertEqual(result['avg_watts'], 19)
        self.assertEqual(result['joules_per_token'], 1)

    def test_missing_failed_or_gapped_samples_are_null(self):
        ep = EnergyProfiler()
        self.assertIsNone(ep.summary()['joules'])
        ep.samples = [dict(t=0,power_w=10),dict(t=2,power_w=10)]
        self.assertFalse(ep.summary()['available'])
        ep.samples[-1]['t'] = .5
        ep.read_errors = 1
        self.assertIsNone(ep.record(2)['joules_per_token'])
        with patch.object(ep, '_select_reader', side_effect=RuntimeError('no sensor')):
            with ep:
                pass
        self.assertFalse(ep.summary()['available'])
        self.assertIn('no sensor', ep.summary()['reason'])

    def test_sysfs_units_use_only_total_rail(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            label=root/'in1_label'
            label.write_text('VDD_IN')
            (root/'in1_input').write_text('5000')  # mV
            (root/'curr1_input').write_text('2000')  # mA
            with patch('edge.energy_profiler.Path.glob', return_value=[label]):
                ep=EnergyProfiler()
                self.assertEqual(ep._select_reader()(), 10)
            self.assertIn('VDD_IN', ep.source)

    def test_live_sampling_stops_and_disabled_does_not_probe(self):
        ep=EnergyProfiler(sample_hz=100)
        with patch.object(ep, '_select_reader', return_value=lambda: 10):
            with ep:
                time.sleep(.025)
        result=ep.summary()
        self.assertTrue(result['available'])
        self.assertAlmostEqual(result['joules'], 10*result['duration_s'])
        self.assertFalse(ep._thr.is_alive())
        with patch.object(EnergyProfiler, '_select_reader') as select:
            with EnergyProfiler(disabled_reason='off') as disabled:
                pass
            select.assert_not_called()
        self.assertIsNone(disabled.summary()['joules'])
        self.assertTrue(local_draft_url('http://127.0.0.1:8080'))
        self.assertFalse(local_draft_url('http://192.0.2.1:8080'))

    def test_generation_scope_excludes_reference_and_includes_drain(self):
        live=LiveExperiment.__new__(LiveExperiment)
        live.c=dict(CLOUD_URL='http://test',REQUEST_TIMEOUT_S=2,MAX_TOKENS=4,TASK='gsm8k')
        live.model={'eos_id':2}
        live.reference_stops={0:'eos'}
        events=[]
        live.reference=Mock(side_effect=lambda *a: (events.append('reference') or ([1],'answer')))
        metric=SimpleNamespace(stop_reason='eos',output_ids=[1],rounds=[],wall_time_s=.5,
                               total_output_tokens=1,ttft_ms=2,tpot_ms=2,tokens_per_second=2,quality_spent=0)
        def generate(*a,**kw):
            events.extend(['generate','drain'])
            return 'answer',metric
        live.client=Mock(generate=Mock(side_effect=generate))
        profiler=Mock()
        profiler.__enter__=Mock(side_effect=lambda: (events.append('start') or profiler))
        profiler.__exit__=Mock(side_effect=lambda *a: events.append('stop'))
        profiler.record.return_value={'available':True,'joules':10}
        live.energy_profiler=Mock(return_value=profiler)
        with patch('edge.experiment_live.ImpairedVerifier'), \
             patch('edge.experiment_live.evaluate_quality',return_value={'task_quality':1}):
            result=live.run('strict',False,4,1,{'question':'test'},0,{})
        self.assertEqual(events,['reference','start','generate','drain','stop'])
        self.assertEqual(result['energy']['joules'],10)



    def test_current_aggregation_weights_tokens_and_duration_and_rejects_partial(self):
        def row(method,j,d,t,idx):
            return dict(id=f'{method}_{idx}',method=method,scenario='low',wall_time_s=d,
                output_tokens=t,request_index=idx,rounds=[],task_quality=1,truncated=False,
                energy=dict(available=True,scope='jetson_board',source='test',joules=j,
                    sample_hz=1,samples=[dict(t=0,power_w=j/d),dict(t=d,power_w=j/d)]))
        base=[row('fixed',10,1,2,0),row('fixed',30,3,8,1)]
        candidate=[row('regime',5,1,2,0),row('regime',15,2,8,1)]
        summary=aggregate(base)
        self.assertEqual(summary['avg_watts'],10)
        self.assertEqual(summary['joules_per_token'],4)
        pair=compare(base+candidate,'fixed','regime',['low'],draws=100)
        self.assertEqual(pair['energy_saving_pct'],50)
        base[1]['energy']['available']=False
        self.assertIsNone(aggregate(base)['joules'])
        self.assertIsNone(compare(base+candidate,'fixed','regime',['low'],draws=100)['energy_saving_pct'])

    def test_current_report_preserves_energy_and_marks_unsupported_quality(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            write_json(root/'config/protocol.json',dict(methods=['fixed'],
                network_scenarios={'low':{}},primary_scenarios=['low'],expected_requests=1))
            write_json(root/'report/status.json',dict(state='complete',failures=[]))
            record=dict(id='low_fixed',method='fixed',scenario='low',request_index=0,
                wall_time_s=1,task_quality=None,truncated=False,output_tokens=2,rounds=[],
                energy=dict(available=True,scope='jetson_board',source='test',joules=10,
                    joules_per_token=5,sample_hz=1,
                    samples=[dict(t=0,power_w=10),dict(t=1,power_w=10)]))
            write_json(root/'raw/low_fixed.json',record)
            data=report(root)
            self.assertTrue(data['complete'])
            self.assertEqual(data['summaries']['low']['fixed']['joules_per_token'],5)
            self.assertIsNone(data['summaries']['low']['fixed']['quality'])
            self.assertIn('| N/A | 0 |',(root/'SUMMARY.md').read_text())
            self.assertEqual(json.loads((root/'raw/low_fixed.json').read_text()),record)


if __name__=='__main__':
    unittest.main()
