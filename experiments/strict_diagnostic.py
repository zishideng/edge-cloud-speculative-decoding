"""Real-service strict decoding audit; saves every request for differential replay.

This is a correctness experiment, not a production performance benchmark.
Diagnostic replay timings are never included in generation timing.
"""
import argparse
import hashlib
import json
import random
import subprocess
import sys
import time
import traceback
from pathlib import Path

import requests

from common.experiment_config import load_config
from edge.experiment_live import LiveExperiment
from edge.verifier import RemoteVerifier
from experiments.isolation import ServiceLocks, environment_snapshot
from experiments.run import create_output, write_json


def first_difference(a, b):
    return next((i for i, (x, y) in enumerate(zip(a, b)) if x != y),
                min(len(a), len(b)) if len(a) != len(b) else None)


class RecordingVerifier(RemoteVerifier):
    def __init__(self, *args):
        super().__init__(*args)
        self.calls = []

    def verify(self, prompt_ids, draft_ids, draft_logprobs=None, **kwargs):
        result = super().verify(prompt_ids, draft_ids, draft_logprobs, **kwargs)
        self.calls.append(dict(prompt_ids=list(prompt_ids), draft_ids=list(draft_ids),
                               accepted_ids=result.accepted_ids, bonus_id=result.bonus_id,
                               should_stop=result.should_stop, metadata=result.metadata))
        return result


def post(session, url, endpoint, body, timeout):
    start = time.perf_counter()
    response = session.post(url + endpoint, json=body, timeout=timeout)
    elapsed = time.perf_counter() - start
    response.raise_for_status()
    return dict(request=body, response=response.json(), http_wall_s=elapsed)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--config')
    ap.add_argument('--output-root', default='results')
    ap.add_argument('--n', type=int, default=4)
    ap.add_argument('--repeats', type=int, default=2)
    ap.add_argument('--max-tokens', type=int, default=512)
    ap.add_argument('--gammas', type=int, nargs='+', default=[2, 8])
    ap.add_argument('--hardware-label', required=True)
    args = ap.parse_args()
    out = create_output(args.output_root)
    print(f'Artifacts: {out.resolve()}', flush=True)
    c = load_config(args.config)
    c['MAX_TOKENS'] = args.max_tokens
    write_json(out/'config/resolved.json', c)
    write_json(out/'config/protocol.json', dict(arguments=vars(args), command=sys.argv,
        hypothesis='Strict prefill verification may diverge from autoregressive target decoding.',
        scope='Correctness diagnostic; warm cache, no network injection; hardware label must be respected',
        git_head=subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()))
    (out/'config/source.patch').write_bytes(subprocess.check_output(['git', 'diff', 'HEAD']))
    locks = ServiceLocks([c['DRAFT_URL'], c['CLOUD_URL']], str(out)).acquire()
    rows, failures = [], []
    live = None
    session = requests.Session()
    try:
        write_json(out/'config/hardware_start.json', environment_snapshot())
        live = LiveExperiment(c)
        write_json(out/'config/service_info.json', live.info)
        write_json(out/'config/draft_props.json', live.client.props())
        write_json(out/'config/draft_models.json', live.client.models())
        data = Path(c['DATASET']).read_bytes()
        samples = [json.loads(line) for line in data.decode().splitlines() if line.strip()][:args.n]
        write_json(out/'config/dataset.json', dict(sha256=hashlib.sha256(data).hexdigest(), samples=samples))
        for index, example in enumerate(samples):
            messages = live.messages(example)
            template = live.client.apply_chat_template(messages)
            prompt = live.client.tokenize(template, add_special=False)
            write_json(out/'config'/f'prompt_{index}.json', dict(messages=messages, template=template, prompt_ids=prompt))
            for repeat in range(args.repeats):
                ar = post(session, c['CLOUD_URL'], '/generate', dict(prompt_ids=prompt,
                    max_tokens=args.max_tokens, temperature=0, eos_id=live.model['eos_id']), c['REQUEST_TIMEOUT_S'])
                write_json(out/'raw'/f'ar_{index}_{repeat}.json', ar)
                ref = ar['response']['token_ids']
                print(f'prompt={index} repeat={repeat} AR tokens={len(ref)} wall={ar["http_wall_s"]:.3f}s', flush=True)
                gammas = list(args.gammas)
                random.Random(c['SEED'] + repeat + index).shuffle(gammas)
                for gamma in gammas:
                    name = f'strict_{index}_{repeat}_g{gamma}'
                    verifier = RecordingVerifier(c['CLOUD_URL'], c['REQUEST_TIMEOUT_S'])
                    try:
                        text, m = live.client.generate(messages, verifier, gamma=gamma,
                            max_tokens=args.max_tokens, eos_id=live.model['eos_id'],
                            strategy='strict', adaptive_window=False, fixed_k=1)
                        mismatch = first_difference(ref, m.output_ids)
                        record = dict(prompt_index=index, repeat=repeat, gamma=gamma,
                            output_text=text, output_ids=m.output_ids, reference_ids=ref,
                            first_difference=mismatch, metrics=vars(m), calls=verifier.calls)
                        write_json(out/'raw'/f'{name}.json', record)
                        rows.append(dict(name=name, prompt_index=index, repeat=repeat, gamma=gamma,
                            first_difference=mismatch, exact=mismatch is None, wall_time_s=m.wall_time_s,
                            output_tokens=len(m.output_ids), tokens_per_second=m.tokens_per_second,
                            ar_http_wall_s=ar['http_wall_s'], ar_output_tokens=len(ref)))
                        write_json(out/'tables/summary.json', rows)
                        print(f'{name}: exact={mismatch is None} first_difference={mismatch} tps={m.tokens_per_second:.2f}', flush=True)
                        if mismatch is not None and mismatch < min(len(ref), len(m.output_ids)):
                            # Match both the original batch shape and the exact divergent prefix.
                            ctx = prompt + ref[:mismatch]
                            original = next(call for call in verifier.calls
                                if len(call['prompt_ids']) <= len(ctx) < len(call['prompt_ids']) +
                                len(call['accepted_ids']) + int(call['bonus_id'] is not None))
                            replays = []
                            for diagnostic_repeat in range(3):
                                for kind, ids, draft in [('original_batch', original['prompt_ids'], original['draft_ids']),
                                                       ('single_reference', ctx, [ref[mismatch]]),
                                                       ('single_output', ctx, [m.output_ids[mismatch]])]:
                                    item = post(session, c['CLOUD_URL'], '/verify', dict(prompt_ids=ids,
                                        draft_ids=draft, temperature=0, eos_id=live.model['eos_id'],
                                        policy={'strategy':'strict', 'k':1, 'spent':0}, diagnostics=True), c['REQUEST_TIMEOUT_S'])
                                    replays.append(dict(kind=kind, repeat=diagnostic_repeat, **item))
                                replays.append(dict(kind='generate_next', repeat=diagnostic_repeat,
                                    **post(session, c['CLOUD_URL'], '/generate', dict(prompt_ids=ctx,
                                        max_tokens=1, temperature=0, eos_id=live.model['eos_id']), c['REQUEST_TIMEOUT_S'])))
                            write_json(out/'raw'/f'{name}_replay.json', replays)
                    except Exception:
                        failures.append(name)
                        (out/'logs'/f'{name}.log').write_text(traceback.format_exc())
                        print(f'{name}: FAILED (see log)', flush=True)
                    finally:
                        verifier._session.close()
    except BaseException:
        failures.append('pipeline')
        (out/'logs/pipeline.log').write_text(traceback.format_exc())
        raise
    finally:
        write_json(out/'report/status.json', dict(successful_runs=len(rows), failures=failures))
        write_json(out/'config/hardware_end.json', environment_snapshot())
        session.close()
        if live:
            live.client._session.close()
            live.remote._session.close()
        locks.close()
    return int(bool(failures))


if __name__ == '__main__':
    sys.exit(main())
