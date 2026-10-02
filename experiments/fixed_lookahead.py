"""Fixed lookahead versus synchronous SD, paired on identical gamma and K."""
import argparse
import hashlib
import json
from pathlib import Path
import random
import subprocess
import traceback

from common.experiment_config import load_config, validate, ROOT
from edge.experiment_live import LiveExperiment
from edge.edge_client_lookahead import FixedLookaheadClient
from experiments.isolation import ServiceLocks, environment_snapshot
from experiments.run import create_output, write_json, enrich


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output-root', default='results')
    ap.add_argument('--n', type=int, default=4)
    ap.add_argument('--gamma', type=int, default=4)
    ap.add_argument('--lookahead', type=int, default=5)
    ap.add_argument('--repeats', type=int, default=2)
    args = ap.parse_args()
    c = load_config('configs/research.pilot.json')
    c.update(N_REQUESTS=args.n, REPEATS=args.repeats,
             GAMMA_INITIAL=args.gamma,
             NETWORK_SCENARIOS={'low': {'rtt_ms':2, 'jitter_ms':0},'high':{'rtt_ms':100,'jitter_ms':0}})
    if args.lookahead < 1 or not c['GAMMA_MIN'] <= args.gamma <= c['GAMMA_MAX']:
        raise ValueError('Invalid fixed gamma/lookahead')
    validate(c)
    out = create_output(args.output_root)
    print(f'Artifacts: {out.resolve()}', flush=True)
    write_json(out/'config/resolved.json', c)
    write_json(out/'config/protocol.json', dict(
        hypothesis='Fixed lookahead hides verification/network time sufficiently to offset discarded work',
        methods={'control':'Strict fixed-window SD; no lookahead','candidate':'Same SD with fixed lookahead'},
        gamma=args.gamma,lookahead=args.lookahead,
        bridge_note='Lookahead count includes prediction of the verifier bonus token; full verified prefix must match',
        seed=42,requests=4*args.n*args.repeats,
        primary='Per-condition paired throughput gain; >=5% and prompt-bootstrap CI low >0 for an exploratory positive signal',
        quality='Report all final-answer scores, truncations and paired changes; pilot cannot certify noninferiority',
        sampling='First four GSM8K pilot prompts; feasibility study, not held-out generalization'))
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
        live.client._session.close()
        live.client=FixedLookaheadClient(c['DRAFT_URL'],c,lookahead_tokens=0)
        live.client.stop_strings=live.model.get('stop_strings', [])
        for scenario_name,scenario in c['NETWORK_SCENARIOS'].items():
            for repeat in range(args.repeats):
                indices=list(range(len(samples)))
                random.Random(42+repeat).shuffle(indices)
                for index in indices:
                    order=[1,0]
                    random.Random(42+repeat*100+index).shuffle(order)
                    for enabled in order:
                        method='control' if not enabled else 'candidate'
                        name=f'{scenario_name}_r{repeat}_p{index}_{method}'
                        print(f'{name}: starting',flush=True)
                        try:
                            live.client.lookahead_tokens=args.lookahead if enabled else 0
                            record=live.run('strict',False,args.gamma,1,
                                            samples[index],index,scenario)
                            record.update(id=name,mode='real',method=method,scenario=scenario_name,
                                repeat=repeat,request_index=index,lookahead=live.client.last_lookahead,
                                configured_gamma=args.gamma,configured_k=1,adaptive_window=False)
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
        write_json(out/'report/status.json',dict(completed=completed,expected=4*len(samples)*args.repeats,failures=failures))
        write_json(out/'config/hardware_end.json',environment_snapshot())
        if live:
            live.client._session.close(); live.remote._session.close()
        lock.close()


if __name__ == '__main__':
    main()
