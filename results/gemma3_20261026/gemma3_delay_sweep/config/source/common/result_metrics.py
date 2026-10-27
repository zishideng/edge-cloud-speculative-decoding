"""Derived request metrics shared by the current real-service experiments."""
from common.metrics import summary
from common.quality import difference_rate


def enrich(record):
    rows=record['rounds']; examined=sum(r['n_examined'] for r in rows)
    record['strict_acceptance_rate']=sum(r['strict_accepted'] for r in rows)/max(1,examined)
    record['relaxed_acceptance_rate']=sum(r['n_accepted'] for r in rows)/max(1,examined)
    record['relaxed_only_rate']=sum(r['relaxed_only'] for r in rows)/max(1,examined)
    record['accepted_proposed_ratio']=sum(r['n_accepted'] for r in rows)/max(1,sum(r['n_proposed'] for r in rows))
    record['text_difference_rate']=difference_rate(record['reference_text'],record['output_text'])
    record['token_difference_rate']=difference_rate(record['reference_ids'],record['output_ids'])
    record['task_quality_drop']=(record['reference_quality']-record['task_quality']) if record['task_quality'] is not None else None
    record['round_latency']=summary([r['round_total_ms'] for r in rows]) if rows else None
    if not rows:
        for key in ('strict_acceptance_rate','relaxed_acceptance_rate','relaxed_only_rate','accepted_proposed_ratio'):
            record[key] = None  # Autoregressive generation has no acceptance decisions.
    return record
