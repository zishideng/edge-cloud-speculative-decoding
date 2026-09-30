"""Randomized paired end-to-end ablation of draft probability telemetry."""
import argparse
import hashlib
import json
from pathlib import Path
import random
import subprocess
import traceback

from common.experiment_config import load_config, ROOT
from edge.experiment_live import LiveExperiment
from experiments.isolation import ServiceLocks, environment_snapshot
from experiments.run import create_output, write_json, enrich


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output-root', default='results')
    ap.add_argument('--n', type=int, default=8)
    ap.add_argument('--repeats', type=int, default=2)
    args = ap.parse_args()
    c = load_config('configs/research.pilot.json')
    c.update(N_REQUESTS=args.n, REPEATS=args.repeats,
             NETWORK_SCENARIOS={'low': {'rtt_ms':2, 'jitter_ms':0}})
    out = create_output(args.output_root)
    print(f'Artifacts: {out.resolve()}', flush=True)
    write_json(out/'config/resolved.json', c)
    write_json(out/'config/protocol.json', dict(
        hypothesis='n_probs=0 reduces end-to-end cost of Proposed without reducing task accuracy',
        methods={'control':'Proposed with n_probs=1','candidate':'Proposed with n_probs=0'},
        seed=42,requests=2*args.n*args.repeats,
        primary='paired throughput gain; bootstrap by prompt; >=2% and CI low >0',
        quality='Report all final-answer scores, truncations and paired changes; pilot cannot certify noninferiority',
        sampling='Same first GSM8K pilot prompts; engineering confirmation, not held-out generalization'))
    write_json(out/'config/git.json', dict(
        head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
        diff=subprocess.check_output(['git','diff','--','edge','common','configs','experiments'],text=True)))
    for folder in ('edge','common','experiments'):
        for source in (ROOT/folder).glob('*.py'):
            target=out/'config/source'/folder/source.name
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(source.read_bytes())
    data=(ROOT/c['DATASET']).read_bytes()
    samples=[json.loads(line) for line in data.decode().splitlines() if line.strip()][:args.n]
    write_json(out/'config/dataset.json',dict(sha256=hashlib.sha256(data).hexdigest(),samples=samples))
    lock=ServiceLocks([c['DRAFT_URL'],c['CLOUD_URL']],str(out)).acquire()
    failures=[]; completed=0; live=None
    try:
        write_json(out/'config/hardware_start.json',environment_snapshot())
        live=LiveExperiment(c)
        write_json(out/'config/service_info.json',live.info)
        for repeat in range(args.repeats):
            indices=list(range(len(samples)))
            random.Random(42+repeat).shuffle(indices)
            for index in indices:
                order=[1,0]
                random.Random(42+repeat*100+index).shuffle(order)
                for n_probs in order:
                    method='control' if n_probs else 'candidate'
                    name=f'r{repeat}_p{index}_{method}'
                    print(f'{name}: starting',flush=True)
                    try:
                        live.c['DRAFT_N_PROBS']=n_probs
                        live.client.draft_n_probs=n_probs
                        record=live.run('adaptive',True,c['GAMMA_INITIAL'],None,
                                        samples[index],index,c['NETWORK_SCENARIOS']['low'])
                        record.update(id=name,mode='real',method=method,scenario='low',
                            repeat=repeat,request_index=index,draft_n_probs=n_probs)
                        enrich(record)
                        write_json(out/'raw'/f'{name}.json',record)
                        completed+=1
                        print(f'{name}: {record["tokens_per_second"]:.3f} TPS; quality={record["task_quality"]}',flush=True)
                    except Exception:
                        failures.append(name)
                        (out/'logs'/f'{name}.log').write_text(traceback.format_exc())
                        raise
    except BaseException:
        (out/'logs/pipeline.log').write_text(traceback.format_exc())
        raise
    finally:
        write_json(out/'report/status.json',dict(completed=completed,expected=2*len(samples)*args.repeats,failures=failures))
        write_json(out/'config/hardware_end.json',environment_snapshot())
        if live:
            live.client._session.close(); live.remote._session.close()
        lock.close()


if __name__ == '__main__':
    main()
