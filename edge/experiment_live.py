"""Real-service adapter. Network impairment is application-level injection."""
import json
import time
from dataclasses import asdict
from common.model_config import load_model_config, validate_pair
from common.quality import task_quality
from common.simulation import network_condition
from edge.edge_client_smart import SmartEdgeClient
from edge.verifier import RemoteVerifier


class ImpairedVerifier(RemoteVerifier):
    def __init__(self,url,c,scenario):
        super().__init__(url,c['REQUEST_TIMEOUT_S'])
        self.c,self.scenario,self.round=c,scenario,0

    def verify(self,*args,**kwargs):
        size=len(json.dumps({'args':args,'kwargs':kwargs}).encode())
        # Download bandwidth delay is computed AFTER receiving the actual response.
        delay,queue=network_condition(self.scenario,self.c['SEED'],self.round,size,0)
        self.experiment_queue_ms=queue
        time.sleep(delay/1000)
        result=super().verify(*args,**kwargs)
        down=0.0
        if self.scenario.get('bandwidth_mbps'):
            down=len(json.dumps(result.metadata).encode())*8/(self.scenario['bandwidth_mbps']*1000)
            time.sleep(down/1000)
        injected=delay+down
        timing=result.metadata['timing']
        timing['network_rtt_ms']+=injected
        timing['upload_ms']+=delay
        timing['download_ms']+=down
        timing['injected_network_ms']=injected
        timing['injected_queue_ms']=queue
        timing['measurement_mode']='real_model_with_application_delay_injection'
        result.network_time_ms+=injected
        self.round+=1
        return result


class LiveExperiment:
    def __init__(self,c):
        missing=[key for key in ('DRAFT_URL','CLOUD_URL','MODEL_PAIR') if not c[key]]
        if missing:
            raise ValueError('真实实验缺少配置: '+', '.join(missing))
        self.c=c
        self.client=SmartEdgeClient(c['DRAFT_URL'],c)
        self.remote=RemoteVerifier(c['CLOUD_URL'],c['REQUEST_TIMEOUT_S'])
        self.model=load_model_config(c['MODEL_PAIR'])
        self.remote.health()
        if not validate_pair(self.client,self.remote,self.model):
            raise RuntimeError('Model vocabulary validation could not be confirmed')
        info=self.remote.info()
        if info['target_model'] != self.model['target']:
            raise ValueError('Running target does not match MODEL_PAIR target')
        self.info=info
        self.references={}

    def messages(self,example):
        question=example.get('question') or example.get('prompt') or example.get('turns',[''])[0]
        instruction='Solve the problem. End with: Final answer: <number>.' if self.c['TASK']=='gsm8k' else 'You are a helpful assistant.'
        return [{'role':'system','content':instruction},{'role':'user','content':question}]

    def reference(self,example,index):
        if index not in self.references:
            ids=self.client.tokenize(self.client.apply_chat_template(self.messages(example)),add_special=False)
            response=self.remote._session.post(self.remote.base+'/generate',json={
                'prompt_ids':ids,'max_tokens':self.c['MAX_TOKENS'],'temperature':0,
                'eos_id':self.model['eos_id']},timeout=self.c['REQUEST_TIMEOUT_S'])
            response.raise_for_status(); data=response.json()
            text=self.client.detokenize([t for t in data['token_ids'] if t != self.model['eos_id']])
            self.references[index]=(data['token_ids'],text)
        return self.references[index]

    def run(self,strategy,adaptive_window,gamma,k,example,index,scenario):
        ref_ids,ref_text=self.reference(example,index)
        remote=ImpairedVerifier(self.c['CLOUD_URL'],self.c,scenario)
        try:
            text,m=self.client.generate(self.messages(example),remote,gamma=gamma,
                max_tokens=self.c['MAX_TOKENS'],eos_id=self.model['eos_id'],
                strategy=strategy,adaptive_window=adaptive_window,fixed_k=k)
        finally:
            remote._session.close()
        return dict(output_ids=m.output_ids,reference_ids=ref_ids,output_text=text,reference_text=ref_text,
                    rounds=m.rounds,wall_time_s=m.wall_time_s,output_tokens=m.total_output_tokens,
                    ttft_ms=m.ttft_ms,tpot_ms=m.tpot_ms,tokens_per_second=m.tokens_per_second,
                    quality_spent=m.quality_spent,task_quality=task_quality(self.c['TASK'],text,example),
                    reference_quality=task_quality(self.c['TASK'],ref_text,example),synthetic_token_agreement=None)
