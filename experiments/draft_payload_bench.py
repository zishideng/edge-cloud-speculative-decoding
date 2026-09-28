"""Paired llama.cpp n_probs=1 vs 0 microbenchmark on saved token prefixes.

No target model calls. Measures draft HTTP service cost, not end-to-end SD.
"""
import argparse
import hashlib
import json
import random
import time
import traceback
from pathlib import Path

import requests

from experiments.isolation import ServiceLocks, environment_snapshot
from experiments.run import create_output, write_json, write_csv


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source',type=Path,help='Completed strict_diagnostic run with prompt and AR files')
    ap.add_argument('--draft-url',default='http://127.0.0.1:8080')
    ap.add_argument('--repeats',type=int,default=10)
    ap.add_argument('--output-root',default='results')
    args=ap.parse_args()
    out=create_output(args.output_root)
    print(f'Artifacts: {out.resolve()}',flush=True)
    write_json(out/'config/protocol.json',dict(command=vars(args)|{'source':str(args.source)},
        hypothesis='Unused draft probability telemetry costs CPU work and response bytes',
        seed=42,gammas=[1,2,4,8],prefix_offsets=[0,32,64],
        acceptance_rule='Consider deployment only if draft latency reduction >=3% and paired prompt CI excludes zero; then validate end-to-end quality separately'))
    (out/'config/runner.py').write_bytes(Path(__file__).read_bytes())
    lock=ServiceLocks([args.draft_url],str(out)).acquire()
    session=requests.Session()
    rows,failures=[],[]
    try:
        write_json(out/'config/hardware_start.json',environment_snapshot())
        for p in sorted((args.source/'config').glob('prompt_*.json')):
            index=int(p.stem.split('_')[-1])
            prompt=json.loads(p.read_text())['prompt_ids']
            reference_path=args.source/'raw'/f'ar_{index}_0.json'
            ref=json.loads(reference_path.read_text())['response']['token_ids']
            for offset in [0,32,64]:
                if offset>=len(ref):continue
                ctx=prompt+ref[:offset]
                write_json(out/'config'/f'prefix_{index}_{offset}.json',dict(prompt_ids=ctx,
                    source_prompt=str(p),source_reference=str(reference_path),
                    prompt_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                    reference_sha256=hashlib.sha256(reference_path.read_bytes()).hexdigest()))
                base=dict(prompt=ctx,temperature=0.0,return_tokens=True,cache_prompt=True,
                          seed=42,stop=['<|eot_id|>','<|end_of_text|>'],
                          samplers=['top_k'],top_k=1,top_p=1.0,min_p=0.0)
                for gamma in [1,2,4,8]:
                    # Save warm-up too; never count it as a timed observation.
                    warm=session.post(args.draft_url+'/completion',json=dict(base,n_predict=gamma,n_probs=1),timeout=120)
                    warm.raise_for_status()
                    write_json(out/'raw'/f'warm_{index}_{offset}_{gamma}.json',warm.json())
                    for repeat in range(args.repeats):
                        order=[0,1];random.Random(42+index*1000+offset*10+gamma+repeat).shuffle(order)
                        for n_probs in order:
                            name=f'p{index}_o{offset}_g{gamma}_r{repeat}_n{n_probs}'
                            try:
                                body=dict(base,n_predict=gamma,n_probs=n_probs)
                                start=time.perf_counter()
                                response=session.post(args.draft_url+'/completion',json=body,timeout=120)
                                wall=(time.perf_counter()-start)*1000
                                response.raise_for_status();data=response.json()
                                ids=data.get('tokens') or data.get('output_tokens')
                                if not ids:raise ValueError('Missing generated token IDs')
                                write_json(out/'raw'/f'{name}.json',dict(request=body,response=data,wall_ms=wall))
                                rows.append(dict(id=name,prompt_index=index,offset=offset,gamma=gamma,
                                    repeat=repeat,n_probs=n_probs,wall_ms=wall,tokens=len(ids),
                                    response_bytes=len(response.content),output_ids=ids))
                            except Exception:
                                failures.append(name);(out/'logs'/f'{name}.log').write_text(traceback.format_exc())
                    if rows:write_csv(out/'tables/requests.csv',rows)
                print(f'prompt={index} offset={offset}: observations={len(rows)}, failures={len(failures)}',flush=True)
    except BaseException:
        failures.append('pipeline')
        (out/'logs/pipeline.log').write_text(traceback.format_exc())
        raise
    finally:
        write_json(out/'report/status.json',dict(observations=len(rows),failures=failures))
        write_json(out/'config/hardware_end.json',environment_snapshot())
        session.close();lock.close()
    return int(bool(failures))


if __name__=='__main__':
    raise SystemExit(main())
