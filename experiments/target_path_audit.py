"""Teacher-forced fixed-prefix audit of target inference paths (no speedup claim)."""
import argparse
import hashlib
import json
import random
import sys
import traceback
from pathlib import Path

import requests

from common.experiment_config import load_config
from edge.experiment_live import LiveExperiment
from experiments.isolation import ServiceLocks
from experiments.run import create_output, write_json, write_csv
from experiments.strict_diagnostic import post


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config')
    parser.add_argument('--output-root', default='results')
    parser.add_argument('--n', type=int, default=4)
    parser.add_argument('--repeats', type=int, default=3)
    parser.add_argument('--position-selection', choices=['fixed','low_margin'], default='fixed')
    args = parser.parse_args()
    out = create_output(args.output_root)
    print(f'Artifacts: {out.resolve()}', flush=True)
    c = load_config(args.config)
    write_json(out/'config/resolved.json', c)
    write_json(out/'config/protocol.json', dict(command=sys.argv, n=args.n, repeats=args.repeats,
        offsets=[0,1,2,3,7,15,31,63], position_selection=args.position_selection,
        gammas=[1,2,4,8], reference_max_tokens=128,
        mode='real target; teacher-forced correctness diagnostic, not draft performance'))
    (out/'config/runner.py').write_bytes(Path(__file__).read_bytes())
    lock = ServiceLocks([c['DRAFT_URL'], c['CLOUD_URL']], str(out)).acquire()
    session = requests.Session()
    rows, failures = [], []
    live = None
    try:
        live = LiveExperiment(c)
        if not live.info.get('strict_diagnostics_available'):
            raise RuntimeError('Target diagnostics are required for this experiment')
        write_json(out/'config/service_info.json', live.info)
        for task, filename in [('gsm8k','gsm8k_test_50.jsonl'),
                               ('humaneval','humaneval_30.jsonl'), ('mtbench','mtbench_30.jsonl')]:
            c['TASK'] = task
            data = (Path('common/data')/filename).read_bytes()
            examples = [json.loads(line) for line in data.decode().splitlines() if line.strip()][:args.n]
            write_json(out/'config'/f'{task}_dataset.json', dict(sha256=hashlib.sha256(data).hexdigest(), examples=examples))
            for index, example in enumerate(examples):
                template = live.client.apply_chat_template(live.messages(example))
                prompt = live.client.tokenize(template, add_special=False)
                ar = post(session, c['CLOUD_URL'], '/generate', dict(prompt_ids=prompt,
                    max_tokens=128, temperature=0, eos_id=live.model['eos_id']), c['REQUEST_TIMEOUT_S'])
                write_json(out/'raw'/f'{task}_{index}_reference.json', dict(template=template, **ar))
                ref = ar['response']['token_ids']
                offsets = [i for i in [0,1,2,3,7,15,31,63] if i < len(ref) and ref[i] != live.model['eos_id']]
                if args.position_selection == 'low_margin':
                    screening = post(session, c['CLOUD_URL'], '/verify', dict(prompt_ids=prompt,
                        draft_ids=ref, temperature=0, eos_id=live.model['eos_id'],
                        policy={'strategy':'strict','k':1,'spent':0}, diagnostics=True), c['REQUEST_TIMEOUT_S'])
                    write_json(out/'raw'/f'{task}_{index}_screening.json', screening)
                    candidates = []
                    for position, dist in enumerate(screening['response']['metadata']['target_distributions']):
                        if ref[position] == live.model['eos_id']:
                            continue
                        ordered = sorted(dist.items(), key=lambda item: (-item[1]['logprob'], int(item[0])))
                        gap = ordered[0][1]['logprob'] - ordered[1][1]['logprob']
                        top = min(int(k) for k,v in dist.items() if v['rank']==1)
                        candidates.append((top == ref[position], gap, position))
                    # Disagreements first, then small top-1/top-2 margins. Selection
                    # is deliberately biased toward failure cases, not incidence estimation.
                    offsets = sorted(item[2] for item in sorted(candidates)[:8])
                    write_json(out/'config'/f'{task}_{index}_selected_positions.json',
                               dict(offsets=offsets, ranked_candidates=sorted(candidates)))
                for offset in offsets:
                    ctx = prompt + ref[:offset]
                    for repeat in range(args.repeats):
                        name = f'{task}_{index}_p{offset}_r{repeat}'
                        calls = []
                        try:
                            next_token = post(session, c['CLOUD_URL'], '/generate', dict(prompt_ids=ctx,
                                max_tokens=1, temperature=0, eos_id=live.model['eos_id']), c['REQUEST_TIMEOUT_S'])
                            calls.append(dict(kind='single_ar', **next_token))
                            single_ids = next_token['response']['token_ids']
                            if not single_ids:
                                raise ValueError('AR returned no token')
                            gammas = [1,2,4,8]
                            random.Random(c['SEED'] + index*100 + offset*10 + repeat).shuffle(gammas)
                            for gamma in gammas:
                                draft = ref[offset:offset+gamma]
                                if len(draft) != gamma:
                                    continue
                                result = post(session, c['CLOUD_URL'], '/verify', dict(prompt_ids=ctx,
                                    draft_ids=draft, temperature=0, eos_id=live.model['eos_id'],
                                    policy={'strategy':'strict','k':1,'spent':0}, diagnostics=True), c['REQUEST_TIMEOUT_S'])
                                calls.append(dict(kind='verify', gamma=gamma, **result))
                                dist = result['response']['metadata']['target_distributions'][0]
                                top = min(int(k) for k,v in dist.items() if v['rank']==1)
                                top_lp = dist[str(top)]['logprob']
                                original_lp = dist.get(str(ref[offset]),{}).get('logprob')
                                rows.append(dict(task=task,prompt_index=index,offset=offset,repeat=repeat,
                                    gamma=gamma,original_ar=ref[offset],single_ar=single_ids[0],prefill_top=top,
                                    matches_original=top==ref[offset],matches_single=top==single_ids[0],
                                    single_matches_original=single_ids[0]==ref[offset],
                                    tied_top_count=sum(v['rank']==1 for v in dist.values()),
                                    original_regret=None if original_lp is None else top_lp-original_lp,
                                    raw_file=f'raw/{name}.json'))
                            write_json(out/'raw'/f'{name}.json', calls)
                        except Exception:
                            write_json(out/'raw'/f'{name}_partial.json', calls)
                            failures.append(name)
                            (out/'logs'/f'{name}.log').write_text(traceback.format_exc())
                        if rows:
                            write_csv(out/'tables/positions.csv',rows)
                print(f'{task} prompt={index}: completed; rows={len(rows)} failures={len(failures)}', flush=True)
    except BaseException:
        failures.append('pipeline')
        (out/'logs/pipeline.log').write_text(traceback.format_exc())
        raise
    finally:
        write_json(out/'report/status.json', dict(measurements=len(rows),failures=failures))
        session.close()
        if live:
            live.client._session.close()
            live.remote._session.close()
        lock.close()
    return int(bool(failures))


if __name__ == '__main__':
    sys.exit(main())
