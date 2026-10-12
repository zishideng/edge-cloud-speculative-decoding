#!/usr/bin/env python3
"""Build figures, tables and number macros from data/evidence.json.

    python3 paper/cape_20261010/scripts/make_assets.py
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

PAPER = Path(__file__).resolve().parents[1]
D = json.loads((PAPER / 'data/evidence.json').read_text())
FIG, TAB = PAPER / 'figures', PAPER / 'tables'
FIG.mkdir(exist_ok=True)
TAB.mkdir(exist_ok=True)

SHORT = {'sync_g4': 'sync4', 'fixed_g2': 'fixed2', 'fixed_fast': 'fixed4', 'fixed_g8': 'fixed8', 'adaedl': 'adaedl',
         'markov_w0': 'capes', 'markov': 'cape', 'markov_w05': 'capee', 'regime_short': 'regime',
         'markov_v2': 'caperobust'}
NAME = {'sync_g4': 'Sync-4', 'fixed_g2': 'Fixed-2', 'fixed_fast': 'Fixed-4', 'fixed_g8': 'Fixed-8',
        'adaedl': 'AdaEDL', 'markov_w0': 'CAPE-S', 'markov': 'CAPE', 'markov_w05': 'CAPE-E',
        'regime_short': 'Regime', 'markov_v2': 'CAPE-robust'}
COLOR = {'sync_g4': '#7f7f7f', 'fixed_g2': '#9ecae1', 'fixed_fast': '#3182bd', 'fixed_g8': '#08519c',
         'adaedl': '#e6550d', 'markov_w0': '#31a354', 'markov': '#41ab5d', 'markov_w05': '#006d2c',
         'regime_short': '#756bb1', 'markov_v2': '#a1d99b'}
PHASE = {'heldout1': 'h1', 'heldout2': 'h2', 'full': 'full'}
METHODS = ['sync_g4', 'fixed_g2', 'fixed_fast', 'fixed_g8', 'adaedl', 'markov_w0', 'markov_w05']

plt.rcParams.update({'font.family': 'serif', 'font.size': 8, 'axes.labelsize': 8, 'axes.titlesize': 8,
                     'legend.fontsize': 6.5, 'xtick.labelsize': 7, 'ytick.labelsize': 7, 'pdf.fonttype': 42,
                     'axes.spines.top': False, 'axes.spines.right': False, 'savefig.bbox': 'tight',
                     'savefig.pad_inches': 0.02})


def num(x, digits=1, sign=False):
    text = f'{x:+.{digits}f}' if sign else f'{x:.{digits}f}'
    return text.replace('-', '$-$').replace('+', '$+$')


def ci(pair, digits=1):
    lo, hi = (f'{v:.{digits}f}'.replace('-', '$-$') for v in pair)
    return f'[{lo}, {hi}]'


macros = {}


def put(key, value):
    if key in macros:
        raise KeyError(key)
    macros[key] = value


def put_effect(key, e):
    put(f'{key}:sp', num(e['speed_pct'], sign=True) + '\\%')
    put(f'{key}:spci', ci(e['speed_ci']))
    put(f'{key}:sv', num(e['saving_pct'], sign=True) + '\\%')
    put(f'{key}:svci', ci(e['saving_ci']))
    put(f'{key}:dj', num(-e['saving_pct'], sign=True) + '\\%')
    put(f'{key}:djci', ci([-e['saving_ci'][1], -e['saving_ci'][0]]))
    put(f'{key}:abssp', num(abs(e['speed_pct'])) + '\\%')
    put(f'{key}:abssv', num(abs(e['saving_pct'])) + '\\%')
    put(f'{key}:n', str(e['prompts']))
    put(f'{key}:chg', str(e['changed_sequences']))
    put(f'{key}:trunc', str(e['extra_truncations']))


# Paired effects: \E{full:capes:fixed4:pooled:sp} and friends.
for phase, short in PHASE.items():
    for comp, rows in D[phase]['effects'].items():
        cand, base = comp.split('_vs_')
        for scene, e in rows.items():
            if e:
                put_effect(f'{short}:{SHORT[cand]}:{SHORT[base]}:{scene.replace("_", "-")}', e)
    for m, rows in D[phase]['methods'].items():
        for scene, v in rows.items():
            key = f'{short}:{SHORT[m]}:{scene}'
            put(f'{key}:tps', num(v['tps'], 2))
            put(f'{key}:jpt', num(v['j_per_token'], 3))
            put(f'{key}:busy', num(v['busy_ms_per_token'], 1))
            put(f'{key}:waste', num(v['discarded_per_100_tokens'], 0))
            put(f'{key}:reuse', num(v['reuse_pct'], 0))
            put(f'{key}:req', str(v['requests']))
    put(f'{short}:prompts', str(D['phases'][phase]['prompts']))
    put(f'{short}:requests', str(D['phases'][phase]['requests']))
put('total:requests', f"{sum(D['phases'][p]['requests'] for p in PHASE):,}".replace(',', '{,}'))
put('total:prompts', str(len({p for ph in PHASE for p in D['phases'][ph]['prompt_ids']})))
put('full:requests:fmt', f"{D['phases']['full']['requests']:,}".replace(',', '{,}'))

M = D['measurement']
em, eh = M['energy_model'], M['energy_model_heldout']
for key, block in (('energy', em), ('energyheld', eh)):
    put(f'{key}:base', num(block['base_w'], 2))
    put(f'{key}:draft', num(block['draft_w'], 2))
    put(f'{key}:ratio', num(block['ratio'], 1))
    put(f'{key}:rsq', f"{block['r2']:.3f}")
    put(f'{key}:mape', num(block['mape_pct'], 1) + '\\%')
    put(f'{key}:n', f"{block['n']:,}".replace(',', '{,}'))
put('energy:busyshare', num(em['busy_share_pct'], 0) + '\\%')
dc = M['draft_cost']
put('draft:call', num(dc['call_ms'], 1))
put('draft:token', num(dc['token_ms'], 1))
put('draft:rsq', f"{dc['r2']:.2f}")
put('draft:calls', f"{dc['calls']:,}".replace(',', '{,}'))
put('draft:joule', f"{em['draft_w'] * dc['token_ms'] / 1000:.2f}")
vc = M['verify_cost']
put('verify:mean', num(vc['mean_ms'], 0))
put('verify:ctx', num(vc['ms_per_context_token'], 2))
put('verify:draft', num(vc['ms_per_proposed_token'], 2))
put('verify:rounds', f"{vc['rounds']:,}".replace(',', '{,}'))
for n, word in (('1', 'one'), ('4', 'four'), ('8', 'eight')):
    put(f'verify:{word}', num(vc['by_proposed'][n]['mean'], 0))
for s, v in M['sync_round'].items():
    for k in ('draft_ms', 'verify_ms', 'transport_ms', 'total_ms'):
        put(f'sync:{s}:{k.split("_")[0]}', num(v[k], 0))
    put(f'sync:{s}:share', num(v['draft_share_pct'], 0) + '\\%')
    put(f'sync:{s}:tokens', num(v['tokens_per_round'], 1))
net = M['network']['pooled']
put('net:median', num(net['median'], 0))
put('net:mean', num(net['mean'], 0))
put('net:p90', num(net['p90'], 0))
put('net:p99', num(net['p99'], 0))
put('net:over100', num(net['over_100ms_pct'], 0) + '\\%')
jpts = [v['pooled']['j_per_token'] for v in D['full']['methods'].values()]
put('full:jpt:min', f'{min(jpts):.2f}')
put('full:jpt:max', f'{max(jpts):.2f}')

C = D['controller']
for src, block in (('full', C['full']), ('held', C['heldout'])):
    for key, v in block.items():
        m, s = key.rsplit('_', 1)
        base = f'ctl:{src}:{SHORT[m]}:{s}'
        put(f'{base}:h', num(v['mean_h'], 1))
        put(f'{base}:fresh', num(v['mean_fresh'], 1))
        put(f'{base}:sent', num(v['mean_sent'], 1))
        put(f'{base}:amiss', f"{v['mean_alpha_miss']:.2f}")
        put(f'{base}:ahit', f"{v['mean_alpha_hit']:.2f}")
        put(f'{base}:rounds', f"{v['rounds']:,}".replace(',', '{,}'))
for m, counts in C['outcomes'].items():
    events = sum(counts.values())
    if events:
        put(f'reuse:{SHORT[m]}', num(100 * counts.get('reused', 0) / events, 0) + '\\%')
put('overhead:ms', num(C['overhead_us'] / 1000, 2))
for src, block in D['acceptance'].items():
    for ds, v in block.items():
        put(f'acc:{src}:{ds}', f'{v:.2f}')
for phase, short in PHASE.items():
    v = D['identical'][phase]
    put(f'ident:{short}:blocks', str(v['blocks']))
    put(f'ident:{short}:differing', str(v['differing']))
Q = D['quality']
for m, v in Q.items():
    put(f'q:{SHORT[m]}:gsm8k', str(v['gsm8k_correct']))
    put(f'q:{SHORT[m]}:trunc', str(v['truncated']))
    put(f'q:{SHORT[m]}:ref', str(v['reference_match']))
put('q:gsm8k:min', str(min(v['gsm8k_correct'] for v in Q.values())))
put('q:gsm8k:max', str(max(v['gsm8k_correct'] for v in Q.values())))
put('q:ref:min', str(min(v['reference_match'] for v in Q.values())))
put('q:ref:max', str(max(v['reference_match'] for v in Q.values())))
put('div:median', num(D['divergence']['median_first_difference'], 0))
put('div:min', str(D['divergence']['min_first_difference']))
R = D['robustness']
put('rob:blocks', str(R['touched_blocks']))
put('rob:requests', str(R['touched_requests']))
put('rob:fresh', str(R['fresh_prompts']))
for kind in ('clean', 'fresh'):
    for m, e in R[kind].items():
        put_effect(f'rob:{kind}:{SHORT[m]}', e)
ratios = [em['ratio'], eh['ratio']]
put('energy:rmin', num(min(ratios), 1))
put('energy:rmax', num(max(ratios), 1))

lines = ['% Generated by scripts/make_assets.py from data/evidence.json; do not edit by hand.']
for key, value in sorted(macros.items()):
    lines.append(f'\\expandafter\\def\\csname cape@{key}\\endcsname{{{value}}}')
(PAPER / 'numbers.tex').write_text('\n'.join(lines) + '\n')


# ---------------------------------------------------------------- tables
def cell(e, field):
    if field == 'speed':
        return f"${e['speed_pct']:+.1f}$ {ci(e['speed_ci'])}"
    return f"${e['saving_pct']:+.1f}$ {ci(e['saving_ci'])}"


def write_table(name, spec, head, rows):
    body = [f'\\begin{{tabular}}{{{spec}}}', '\\toprule'] + head + ['\\midrule'] + rows + ['\\bottomrule', '\\end{tabular}']
    (TAB / name).write_text('\n'.join(body) + '\n')


rows = []
for phase, label, methods in (('heldout1', 'Set 1', ['fixed_fast', 'regime_short', 'markov', 'markov_w05']),
                              ('heldout2', 'Set 2', ['fixed_fast', 'markov', 'markov_v2'])):
    block = D[phase]
    rows.append(f'\\multicolumn{{5}}{{@{{}}l}}{{\\emph{{{label}: {D["phases"][phase]["prompts"]} prompts, '
                f'{D["phases"][phase]["requests"]} requests}}}} \\\\')
    for m in methods:
        v = block['methods'][m]['pooled']
        if m == 'fixed_fast':
            cells = '\\multicolumn{2}{c}{baseline}'
        else:
            e = block['effects'][f'{m}_vs_fixed_fast']['pooled']
            cells = f'{cell(e, "speed")} & {cell(e, "saving")}'
        rows.append(f"{NAME[m]} & {v['tps']:.2f} & {v['j_per_token']:.3f} & {cells} \\\\")
    rows.append('\\midrule')
write_table('heldout.tex', '@{}lrrll@{}',
            ['Method & tok/s & J/tok & Throughput gain (\\%) & J/token saving (\\%)\\\\'], rows[:-1])

rows = []
F = D['full']
for m in METHODS:
    v = F['methods'][m]
    if m == 'fixed_fast':
        cells = '\\multicolumn{2}{c}{baseline}'
    else:
        e = F['effects'][f'{m}_vs_fixed_fast']['pooled']
        cells = f'{cell(e, "speed")} & {cell(e, "saving")}'
    name = f'\\textbf{{{NAME[m]}}}' if m.startswith('markov') else NAME[m]
    rows.append(f"{name} & {v['low']['tps']:.2f} & {v['high']['tps']:.2f} & {v['pooled']['tps']:.2f} & "
                f"{v['pooled']['j_per_token']:.3f} & {cells} & {v['pooled']['busy_ms_per_token']:.1f} & "
                f"{v['pooled']['discarded_per_100_tokens']:.0f} \\\\")
write_table('main.tex', '@{}lrrrrllrr@{}',
            [' & \\multicolumn{3}{c}{Throughput (tok/s)} & J/token & \\multicolumn{2}{c}{Relative to Fixed-4, 2 and 100\\,ms pooled}'
             ' & Draft busy & Discarded\\\\',
             '\\cmidrule(lr){2-4}\\cmidrule(lr){6-7}',
             'Method & 2\\,ms & 100\\,ms & pooled & pooled & Throughput gain (\\%) & J/token saving (\\%) & ms/token & per 100 tok.\\\\'],
            rows)

rows = []
for m in ('markov_w0', 'markov_w05'):
    e = F['effects'][f'{m}_vs_fixed_fast']
    for field, label in (('speed', 'throughput gain'), ('saving', 'J/token saving')):
        cells = [cell(e[k], field) for k in ('gsm8k', 'humaneval', 'mtbench', 'low', 'high')]
        rows.append(f'{NAME[m]} & {label} & ' + ' & '.join(cells) + ' \\\\')
write_table('breakdown.tex', '@{}llccccc@{}',
            ['Method & Effect (\\%) & GSM8K & HumanEval & MT-Bench & 2\\,ms & 100\\,ms\\\\'], rows)

rows = []
for m in METHODS:
    v = Q[m]
    chg = '---' if m == 'fixed_fast' else str(F['effects'][f'{m}_vs_fixed_fast']['pooled']['changed_sequences'])
    rows.append(f"{NAME[m]} & {v['gsm8k_correct']}/{v['gsm8k_requests']} & {v['truncated']}/{v['requests']} & "
                f"{chg} & {v['reference_match']}/{v['requests']} \\\\")
write_table('quality.tex', '@{}lcccc@{}',
            ['Method & GSM8K & Truncated & $\\neq$ Fixed-4 & $=$ cloud AR\\\\'], rows)


# ---------------------------------------------------------------- figures
def fig_measurement():
    fig, axes = plt.subplots(1, 3, figsize=(7.1, 1.95), gridspec_kw=dict(width_ratios=[1.15, 1, 1]))
    ax = axes[0]
    parts = [('draft_ms', 'Local drafting', '#31a354'), ('transport_ms', 'Network + delay', '#bdbdbd'),
             ('verify_ms', 'Cloud verification', '#3182bd')]
    for y, s in enumerate(['high', 'low']):
        left = 0
        v = M['sync_round'][s]
        for key, label, color in parts:
            ax.barh(y, v[key], left=left, color=color, label=label if y == 0 else None, height=0.55)
            ax.text(left + v[key] / 2, y, f'{v[key]:.0f}', ha='center', va='center', fontsize=6.5,
                    color='white' if key != 'transport_ms' else 'black')
            left += v[key]
        ax.text(left + 6, y, f'{left:.0f} ms', va='center', fontsize=6.5)
    ax.set_yticks([0, 1], ['100 ms', '2 ms'])
    ax.set_xlabel('Mean round time of Sync-4 (ms)')
    ax.set_xlim(0, 450)
    ax.set_ylim(-0.5, 2.4)
    ax.legend(loc='upper left', ncol=2, frameon=False, handlelength=1, columnspacing=0.8, fontsize=6.3)
    ax.set_title('(a) Where a synchronous round goes', fontsize=8)

    ax = axes[1]
    byn = M['verify_cost']['by_proposed']
    n = sorted(int(k) for k in byn)
    ax.bar(n, [byn[str(k)]['mean'] for k in n], color='#3182bd', width=0.6)
    ax.plot(n, [byn[str(k)]['median'] for k in n], 'o', color='black', ms=2.5)
    ax.set_xlabel('Draft tokens sent for verification')
    ax.set_ylabel('Cloud verification (ms)')
    ax.set_ylim(0, 160)
    ax.text(0.03, 0.97, f"+{M['verify_cost']['ms_per_proposed_token']:.2f} ms per draft token\n"
                        f"+{M['verify_cost']['ms_per_context_token']:.2f} ms per context token",
            transform=ax.transAxes, va='top', fontsize=6.5)
    ax.set_title('(b) Verification cost vs. draft length', fontsize=8)

    ax = axes[2]
    pts = M['energy_model']['points']
    for m in METHODS:
        xs = [p['predicted'] for p in pts if p['method'] == m]
        ys = [p['measured'] for p in pts if p['method'] == m]
        ax.scatter(xs, ys, s=3, color=COLOR[m], label=NAME[m], linewidths=0, alpha=0.7)
    lim = [0, max(p['measured'] for p in pts) * 1.05]
    ax.plot(lim, lim, '--', color='black', lw=0.6)
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_xlabel('Predicted request energy (J)')
    ax.set_ylabel('Measured (J)')
    ax.text(0.03, 0.97, f"$E={em['base_w']:.2f}\\,T+{em['draft_w']:.2f}\\,B$\n$R^2={em['r2']:.3f}$",
            transform=ax.transAxes, va='top', fontsize=6.5)
    ax.legend(loc='lower right', frameon=True, framealpha=0.9, edgecolor='none', ncol=2, handletextpad=0.1,
              columnspacing=0.4, markerscale=2.5, borderpad=0.2)
    ax.set_title('(c) Board energy model', fontsize=8)
    fig.tight_layout(w_pad=1.2)
    fig.savefig(FIG / 'measurement.pdf')
    plt.close(fig)


LABEL_OFFSET = {('high', 'fixed_g2'): (-5, 3, 'right'), ('high', 'adaedl'): (4, -9, 'left'),
                ('high', 'sync_g4'): (4, -8, 'left'), ('low', 'markov_w0'): (5, 1, 'left'),
                ('low', 'markov_w05'): (5, -8, 'left'), ('low', 'fixed_fast'): (-5, 3, 'right'),
                ('high', 'markov_w05'): (-5, -9, 'right'), ('high', 'fixed_fast'): (4, -9, 'left')}


def fig_tradeoff():
    fig, axes = plt.subplots(1, 2, figsize=(7.1, 2.05))
    for ax, scene, title in zip(axes, ['low', 'high'], ['(a) 2 ms added delay', '(b) 100 ms added delay']):
        for m in METHODS:
            v = D['full']['methods'][m][scene]
            marker = '*' if m.startswith('markov') else 'o'
            ax.scatter(v['tps'], v['j_per_token'], s=70 if marker == '*' else 28, marker=marker, color=COLOR[m],
                       zorder=3, edgecolors='black', linewidths=0.4)
            dx, dy, ha = LABEL_OFFSET.get((scene, m), (4, 3, 'left'))
            ax.annotate(NAME[m], (v['tps'], v['j_per_token']), xytext=(dx, dy), textcoords='offset points',
                        fontsize=6.5, ha=ha)
        ax.set_xlabel('Throughput (tokens/s)')
        ax.set_ylabel('Jetson energy (J/token)')
        ax.set_title(title, fontsize=8)
        ax.margins(x=0.15, y=0.12)
    fig.tight_layout(w_pad=2)
    fig.savefig(FIG / 'tradeoff.pdf')
    plt.close(fig)


def fig_controller():
    fig, axes = plt.subplots(1, 2, figsize=(3.45, 1.75), sharey=True)
    series = [('markov_w0', 'low', 'CAPE-S, 2 ms', '#a1d99b', ''), ('markov_w0', 'high', 'CAPE-S, 100 ms', '#31a354', ''),
              ('markov_w05', 'low', 'CAPE-E, 2 ms', '#c6dbef', '////'), ('markov_w05', 'high', 'CAPE-E, 100 ms', '#3182bd', '////')]
    for ax, field, values, xlabel in ((axes[0], 'fresh', range(1, 9), r'Fresh window $\gamma_f$'),
                                      (axes[1], 'h', range(2, 10), r'Lookahead $h$')):
        width = 0.2
        for k, (m, s, label, color, hatch) in enumerate(series):
            v = D['controller']['full'][f'{m}_{s}']
            counts = {int(a): b for a, b in v[field].items()}
            total = sum(counts.values())
            ax.bar([x + (k - 1.5) * width for x in values], [100 * counts.get(x, 0) / total for x in values],
                   width=width, color=color, hatch=hatch, label=label, edgecolor='black', linewidth=0.3)
        ax.set_xticks(list(values))
        ax.set_xlabel(xlabel)
    axes[0].set_ylabel('Share of rounds (%)')
    axes[0].legend(loc='upper right', frameon=False, fontsize=5.8, handlelength=1.2)
    fig.tight_layout(w_pad=0.6)
    fig.savefig(FIG / 'controller.pdf')
    plt.close(fig)


def fig_effects():
    rows = [('full', 'markov_w0', 'Main: CAPE-S'), ('full', 'markov_w05', 'Main: CAPE-E'),
            ('full', 'adaedl', 'Main: AdaEDL'), ('full', 'fixed_g2', 'Main: Fixed-2'),
            ('full', 'fixed_g8', 'Main: Fixed-8'), ('full', 'sync_g4', 'Main: Sync-4'),
            ('heldout1', 'markov', 'Set 1: CAPE'), ('heldout1', 'markov_w05', 'Set 1: CAPE-E'),
            ('heldout1', 'regime_short', 'Set 1: Regime'), ('heldout2', 'markov', 'Set 2: CAPE'),
            ('heldout2', 'markov_v2', 'Set 2: CAPE-robust')]
    fig, axes = plt.subplots(1, 2, figsize=(3.45, 2.6), sharey=True)
    y = np.arange(len(rows))[::-1]
    for ax, field, cfield, xlabel in ((axes[0], 'speed_pct', 'speed_ci', 'Throughput\ngain (%)'),
                                      (axes[1], 'saving_pct', 'saving_ci', 'J/token\nsaving (%)')):
        for yy, (phase, cand, label) in zip(y, rows):
            e = D[phase]['effects'][f'{cand}_vs_fixed_fast']['pooled']
            lo, hi = e[cfield]
            ax.plot([lo, hi], [yy, yy], color=COLOR[cand], lw=1.4)
            ax.plot(e[field], yy, 'o', color=COLOR[cand], ms=3.5, markeredgecolor='black', markeredgewidth=0.3)
        ax.axvline(0, color='black', lw=0.6)
        ax.axhline(4.5, color='black', lw=0.4, ls=':')
        ax.set_xlabel(xlabel)
        ax.grid(axis='x', lw=0.3, alpha=0.5)
    axes[0].set_yticks(y, [r[2] for r in rows])
    axes[0].set_xlim(-30, 16)
    axes[0].set_xticks([-20, -10, 0, 10])
    axes[1].set_xlim(-35, 20)
    axes[1].set_xticks([-30, -15, 0, 15])
    fig.tight_layout(w_pad=0.5)
    fig.savefig(FIG / 'effects.pdf')
    plt.close(fig)


fig_measurement()
fig_tradeoff()
fig_controller()
fig_effects()
for old in ('compare.tex',):
    (TAB / old).unlink(missing_ok=True)
print(f'{len(macros)} macros; figures and tables written')
