"""Describe an observed Jetson board-monitoring window, not model-only energy."""
import argparse
from datetime import datetime
import hashlib
from pathlib import Path
import re
from zoneinfo import ZoneInfo

from analysis.research_audit import summarize
from experiments.run import create_output, write_csv, write_json


def report(source, output_root, timezone='Pacific/Auckland'):
    data = source.read_bytes()
    rows, skipped = [], []
    for number, line in enumerate(data.decode().splitlines(), 1):
        stamp = re.match(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}', line)
        if not stamp:
            skipped.append(number)
            continue
        time = datetime.strptime(stamp[0], '%m-%d-%Y %H:%M:%S').replace(tzinfo=ZoneInfo(timezone))
        row = dict(timestamp=time.isoformat(), epoch_s=time.timestamp(), source_line=number)
        for name, pattern, scale in (
            ('ram_mb', r'RAM (\d+)/', 1),
            ('swap_mb', r'SWAP (\d+)/', 1),
            ('gpu_utilization_percent', r'GR3D_FREQ (\d+)%', 1),
            ('gpu_temperature_c', r'gpu@([\d.]+)C', 1),
            ('board_power_w', r'VDD_IN (\d+)mW/', .001),
        ):
            match = re.search(pattern, line)
            row[name] = float(match[1])*scale if match else None
        rows.append(row)
    if len(rows) < 2:
        raise ValueError('Need at least two timestamped resource samples')
    out = create_output(output_root)
    write_csv(out/'tables/samples.csv', rows)
    summaries = []
    for metric in ('ram_mb','swap_mb','gpu_utilization_percent','gpu_temperature_c','board_power_w'):
        values = [r[metric] for r in rows if r[metric] is not None]
        if values:
            summaries.append(dict(metric=metric, **summarize(values)))
    write_csv(out/'tables/summary.csv', summaries)
    covered_s, energy_j, excluded_intervals = 0., 0., 0
    for a, b in zip(rows, rows[1:]):
        dt = b['epoch_s']-a['epoch_s']
        if not 0 < dt <= 2.5 or a['board_power_w'] is None or b['board_power_w'] is None:
            excluded_intervals += 1
            continue
        covered_s += dt
        energy_j += .5*(a['board_power_w']+b['board_power_w'])*dt
    evidence = dict(source=str(source.resolve()),sha256=hashlib.sha256(data).hexdigest(),
        timezone=timezone,samples=len(rows),unparsed_lines=skipped,
        first_timestamp=rows[0]['timestamp'],last_timestamp=rows[-1]['timestamp'],
        covered_power_seconds=covered_s,observed_board_energy_j=energy_j if covered_s else None,
        excluded_power_intervals=excluded_intervals,
        scope='Whole Jetson board including desktop and other processes; no idle subtraction; incomplete request coverage; no cloud energy or model-only attribution')
    write_json(out/'report/resource_window.json', evidence)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(3,1,figsize=(10,7),sharex=True)
    x = [(r['epoch_s']-rows[0]['epoch_s'])/60 for r in rows]
    for ax, metric, label in zip(axes,('board_power_w','ram_mb','gpu_temperature_c'),
                                ('Board power (W)','System RAM (MB)','GPU temperature (C)')):
        ax.plot(x,[r[metric] for r in rows],linewidth=.8)
        ax.set_ylabel(label)
    axes[-1].set_xlabel('Minutes from first recorded sample')
    fig.suptitle('Shared Jetson board: observed monitoring window only')
    fig.tight_layout()
    for extension in ('png','svg'):
        fig.savefig(out/'figures'/f'resources.{extension}',dpi=160)
    plt.close(fig)
    (out/'report/report.md').write_text(
        '# Observed board resource window\n\n'
        f'Source: `{source}`. Samples: {len(rows)}.\n\n'
        'This monitor covers the whole Jetson board, including desktop applications. '
        'It started after the pilot began, so it cannot establish full-run energy, '
        'per-method energy, model-only memory, or cloud resource use.\n\n'
        f'Power integration covers {covered_s:.1f} seconds. '
        'Gaps above 2.5 seconds and missing power readings are excluded. '
        'Raw timestamps, parsed samples, descriptive statistics, and source hash are saved.\n')
    print(out.resolve())
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path)
    parser.add_argument('--output-root',default='results')
    parser.add_argument('--timezone',default='Pacific/Auckland')
    args=parser.parse_args()
    report(args.source,args.output_root,args.timezone)
