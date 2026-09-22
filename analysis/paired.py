"""Prompt-cluster bootstrap: repeats of a prompt are not independent samples."""
from collections import defaultdict
import random
from statistics import mean
from common.metrics import percentile


def paired_comparisons(records, seed=42, draws=2000):
    output = []
    for scenario in sorted({r['scenario'] for r in records}):
        for baseline in ('A', 'B', 'C', 'gamma_4'):
            groups = {method: {(r['request_index'], r['repeat']): r for r in records
                               if r['scenario'] == scenario and r['method'] == method}
                      for method in ('Proposed', baseline)}
            shared = sorted(groups['Proposed'].keys() & groups[baseline].keys())
            for metric in ('tokens_per_second', 'task_quality'):
                by_prompt = defaultdict(list)
                for key in shared:
                    proposed, control = (groups[m][key].get(metric) for m in ('Proposed', baseline))
                    if proposed is None or control is None:
                        continue
                    if metric == 'tokens_per_second' and control <= 0:
                        continue
                    by_prompt[key[0]].append(proposed/control-1 if metric == 'tokens_per_second' else proposed-control)
                values = [mean(v) for v in by_prompt.values()]
                if not values:
                    continue
                rng = random.Random(seed)
                # Synthetic repetitions never establish real-world uncertainty.
                real = all(r['mode'] == 'real' for r in records)
                boot = [mean(rng.choices(values, k=len(values))) for _ in range(draws)] if real and len(values) >= 2 else []
                output.append(dict(scenario=scenario, baseline=baseline, method='Proposed',
                                   metric=metric, effect='relative_gain' if metric == 'tokens_per_second' else 'accuracy_difference',
                                   mean=mean(values), ci95_low=percentile(boot, .025) if boot else None,
                                   ci95_high=percentile(boot, .975) if boot else None,
                                   prompt_count=len(values), pair_count=sum(map(len, by_prompt.values())),
                                   note='Paired repeats averaged per prompt; percentile bootstrap over prompts; descriptive only for very small samples'))
    return output
