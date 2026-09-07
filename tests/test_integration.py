import asyncio
import json
import math
import socket
import sys
import threading
import time
import unittest
from types import SimpleNamespace
from unittest.mock import patch
import requests
import uvicorn
from fastapi.testclient import TestClient
from cloud import verify_server as server
from common.simulation import target_distribution, target_next
from edge.verifier import RemoteVerifier
from edge.edge_client_smart import SmartEdgeClient
from test_core import config


class FakeLLM:
    def __init__(self):
        self.llm_engine=SimpleNamespace(model_config=SimpleNamespace(max_model_len=4096))

    def generate(self,prompts,sampling_params,use_tqdm=False):
        ids=prompts[0]['prompt_token_ids']; lp=[None]
        for i in range(1,len(ids)):
            dist=target_distribution(ids[:i],config())
            if ids[i] not in dist: dist[ids[i]]={'logprob':math.log(.0001),'rank':100}
            lp.append({k:SimpleNamespace(**v) for k,v in dist.items()})
        return [SimpleNamespace(prompt_logprobs=lp,outputs=[SimpleNamespace(token_ids=[target_next(ids)])])]


class IntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake=patch.dict(sys.modules,{'vllm':SimpleNamespace(SamplingParams=lambda **kw:SimpleNamespace(**kw))})
        cls.fake.start(); server.STATE['llm']=FakeLLM()
        cls.client=TestClient(server.app)

    @classmethod
    def tearDownClass(cls):
        cls.client.close(); cls.fake.stop(); server.STATE['llm']=None

    def test_verify_protocol(self):
        token=target_next([1])
        response=self.client.post('/verify',json={'prompt_ids':[1],'draft_ids':[token]})
        self.assertEqual(response.status_code,200,response.text)
        data=response.json(); self.assertEqual(data['accepted_ids'],[token])
        self.assertGreaterEqual(data['cloud_queue_ms'],0)
        self.assertGreater(data['cloud_verify_ms'],0)

    def test_temperature_and_invalid_policy(self):
        for extra in ({'temperature':1},{'policy':{'strategy':'unknown','k':1}}):
            self.assertEqual(self.client.post('/verify',json=dict(prompt_ids=[1],draft_ids=[2],**extra)).status_code,400)

    def test_eos_and_rejection(self):
        token=target_next([1])
        d=self.client.post('/verify',json={'prompt_ids':[1],'draft_ids':[token,5],'eos_id':token}).json()
        self.assertTrue(d['should_stop']); self.assertEqual(d['n_accepted'],1); self.assertIsNone(d['bonus_id'])
        d=self.client.post('/verify',json={'prompt_ids':[1],'draft_ids':[999]}).json()
        self.assertEqual(d['bonus_id'],token); self.assertTrue(d['bonus_is_correction'])

    def test_timeout_and_http_errors_propagate(self):
        verifier=RemoteVerifier('http://unused',timeout=.01)
        with patch.object(verifier._session,'post',side_effect=requests.Timeout('test timeout')):
            with self.assertRaises(requests.Timeout): verifier.verify([1],[2])
        response=requests.Response(); response.status_code=500
        with patch.object(verifier._session,'post',return_value=response):
            with self.assertRaises(requests.HTTPError): verifier.verify([1],[2])

    def test_real_http_and_client_loop(self):
        sock=socket.socket(); sock.bind(('127.0.0.1',0)); sock.listen()
        port=sock.getsockname()[1]
        runner=uvicorn.Server(uvicorn.Config(server.app,log_level='error',lifespan='off'))
        thread=threading.Thread(target=runner.run,kwargs={'sockets':[sock]},daemon=True)
        thread.start()
        try:
            deadline=time.monotonic()+5
            while not runner.started and time.monotonic()<deadline: time.sleep(.01)
            self.assertTrue(runner.started,'Local HTTP server failed to start')
            remote=RemoteVerifier(f'http://127.0.0.1:{port}')
            client=SmartEdgeClient(config=config())
            def draft(ids,g,t):
                ctx=list(ids); result=[]
                for _ in range(g): result.append(target_next(ctx)); ctx.append(result[-1])
                return result,[0.0]*len(result)
            with patch.object(client,'apply_chat_template',return_value='prompt'),patch.object(client,'tokenize',return_value=[1]),patch.object(client,'draft',side_effect=draft),patch.object(client,'detokenize',side_effect=lambda x:str(x)):
                _,metrics=client.generate([{'role':'user','content':'hi'}],remote,max_tokens=9,eos_id=999,strategy='strict')
            self.assertEqual(metrics.total_output_tokens,9)
            self.assertGreater(metrics.ttft_ms,0)
            self.assertTrue(all(r['n_accepted']==r['gamma'] for r in metrics.rounds))
            self.assertTrue(all(r['network_rtt_estimated'] for r in metrics.rounds))
        finally:
            runner.should_exit=True; thread.join(timeout=5); sock.close()

    def test_empty_draft_raises(self):
        client=SmartEdgeClient(config=config())
        with patch.object(client,'apply_chat_template',return_value='p'),patch.object(client,'tokenize',return_value=[1]),patch.object(client,'draft',return_value=([],[])):
            with self.assertRaises(RuntimeError):
                client.generate([],RemoteVerifier('http://unused'),max_tokens=2,eos_id=999)

    def test_injected_queue_is_separate(self):
        response=self.client.post('/verify',json={'prompt_ids':[1],'draft_ids':[2],'experiment_queue_ms':15})
        self.assertEqual(response.status_code,200,response.text)
        self.assertGreaterEqual(response.json()['cloud_queue_ms'],14)

    def test_relaxed_protocol_consumes_budget(self):
        token=target_next([1])+100
        response=self.client.post('/verify',json={'prompt_ids':[1],'draft_ids':[token],
            'policy':{'strategy':'fixed','k':2,'spent':0,'config':config()}})
        self.assertEqual(response.status_code,200,response.text)
        d=response.json();self.assertEqual(d['accepted_ids'],[token])
        self.assertGreater(d['metadata']['quality_spent'],0)

    def test_invalid_spent_and_unloaded_service(self):
        response=self.client.post('/verify',json={'prompt_ids':[1],'draft_ids':[2],
            'policy':{'strategy':'fixed','k':2,'spent':99}})
        self.assertEqual(response.status_code,400)
        with patch.dict(server.STATE,{'llm':None}):
            self.assertEqual(self.client.post('/verify',json={'prompt_ids':[1],'draft_ids':[2]}).status_code,503)


if __name__=='__main__': unittest.main()
