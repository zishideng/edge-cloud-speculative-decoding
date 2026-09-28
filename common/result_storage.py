"""Keep plotting/summary data small; full decisions remain in raw JSON."""
import json


def compact_record(record):
    compact = {k: v for k, v in record.items()
               if k not in ('rounds', 'output_ids', 'reference_ids', 'output_text', 'reference_text')}
    compact['rounds'] = []
    for row in record['rounds']:
        small = {k: v for k, v in row.items() if k not in ('decisions', 'controller')}
        small['controller'] = {'quality_risk': row['controller']['quality_risk']}
        compact['rounds'].append(small)
    return compact


def raw_rounds(directory):
    for path in sorted(directory.glob('*.json')):
        record = json.loads(path.read_text(encoding='utf-8'))
        for row in record['rounds']:
            yield dict(row, experiment_id=record['id'], method=record['method'], scenario=record['scenario'])
