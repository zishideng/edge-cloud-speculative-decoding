"""Light progress check of the rerun campaign from console logs only (no raw records, so it does not
disturb energy measurement). Per phase: progress, resumes, and per scenario/method mean tok/s, J/token."""
import collections
import glob
import json
import re
import statistics
from pathlib import Path

D = Path(__file__).resolve().parent
print((D/'campaign.log').read_text().strip().splitlines()[-1])
for plan in sorted(D.glob('*_plan.json')):
    phase = plan.name.removesuffix('_plan.json')
    status = D/phase/'report/status.json'
    if not status.exists():
        continue
    s = json.loads(status.read_text())
    resumes = (D/f'{phase}_maintenance.log').read_text().count('run attempt') - 1
    print(f'\n== {phase}: {s["state"]} {s.get("completed")}/{s.get("expected", "?")}, resumes {resumes}')
    rows = collections.defaultdict(list)
    name = None
    for log in sorted(D.glob(f'{phase}_console_*.log')):
        for line in log.read_text(errors='replace').splitlines():
            m = re.match(r'\d+/\d+ (\w+?)_(low|high|dynamic|d\d+)_p\d+_r\d+_(\w+)$', line.strip())
            if m:
                name = (m.group(2), m.group(3))
                continue
            m = re.match(r'\s*(\d+) tokens ([\d.]+)s ([\d.]+) J/token', line)
            if m and name:
                rows[name].append((int(m.group(1)), float(m.group(2)), float(m.group(3))))
                name = None
    for scen in sorted({k[0] for k in rows}):
        cells = []
        for (sc, method), v in sorted(rows.items()):
            if sc == scen:
                tps = sum(t for t, _, _ in v) / sum(w for _, w, _ in v)
                jpt = sum(t*j for t, _, j in v) / sum(t for t, _, _ in v)
                cells.append(f'{method} {tps:.1f}/{jpt:.3f} (n={len(v)})')
        print(f'  {scen}: ' + ' | '.join(cells))
