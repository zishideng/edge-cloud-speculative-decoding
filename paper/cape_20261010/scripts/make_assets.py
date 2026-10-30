"""Numbers, tables and figures of the paper from the 2026-10-28 rerun (results/rerun_20261028).

Step 1 condenses every raw request record into data/records.json (delete it to re-read the raw
records). Step 2 writes numbers.tex, tables/{speedup,ablation,weights}.tex and
figures/{sweep,frontier}.pdf. Throughput is total output tokens over total wall time and energy per
token is total board joules over total output tokens, both over the prompts that every method of a
phase completed. Intervals are paired prompt-cluster bootstrap 95% intervals (2000 draws, seed 0),
drawn exactly as in results/rerun_20261028/analysis_vs_sync.py. Run from the repository root.
"""
import collections, glob, json, os, random, re, statistics, sys, time
import numpy as np

ROOT = 'results/rerun_20261028'
PAPER = 'paper/cape_20261010'
CACHE = f'{PAPER}/data/records.json'
PAIRS = {'gemma3': 'gemma3_main', 'llama': 'llama_main', 'qwen': 'qwen_main', 'gemma2': 'gemma2_main'}
PHASES = list(PAIRS.values()) + ['gemma3_sweep', 'gemma3_ablation', 'gemma3_weights']
SHORT = {'sync_g4': 'sync', 'hf_default': 'hf', 'pipesd': 'pipesd', 'pearl': 'pearl', 'picospec_g2': 'g2',
         'picospec': 'g4', 'picospec_g8': 'g8', 'markov_w05_dist_int': 'E', 'markov_w0_dist_int': 'S',
         'markov_w0_fresh4_int': 'la', 'markov_w0_int': 'med', 'markov_w025_dist_int': 'w025',
         'markov_w1_dist_int': 'w1', 'markov_w2_dist_int': 'w2'}
NAME = {'sync': 'Sync-4', 'hf': 'HF assisted', 'pipesd': 'PipeSD', 'pearl': 'PEARL', 'g2': 'PicoSpec-2',
        'g4': 'PicoSpec-4', 'g8': 'PicoSpec-8', 'E': r'\capee{}', 'S': r'\capes{}'}
PAIR_NAME = {'gemma3': 'Gemma-3 270M/4B', 'llama': 'Llama 1B/8B', 'qwen': 'Qwen 0.5B/7B', 'gemma2': 'Gemma-2 2B/9B'}
MAIN_METHODS = ['sync', 'hf', 'pipesd', 'pearl', 'g2', 'g4', 'g8', 'E', 'S']
BASELINES = MAIN_METHODS[:7]
FIXED = ['g2', 'g4', 'g8']
SCENS = {'low': 'low', 'high': 'high', 'dynamic': 'dyn'}
DELAY_NAME = {'low': '2\\,ms', 'high': '100\\,ms', 'dyn': 'dynamic'}
FILE = re.compile(r'(\w+?)_(low|high|dynamic|d\d+)_p(\d+)_r\d+_(\w+)\.json')


def condense(path):
    d = json.load(open(path))
    rounds = d['rounds']
    r = dict(tok=d['output_tokens'], wall=d['wall_time_s'], joules=d['energy']['joules'],
             exact=d['output_ids'] == d['reference_ids'], correct=d.get('task_quality'),
             accepted=sum(x.get('n_accepted', 0) for x in rounds),
             examined=sum(x.get('n_examined', 0) for x in rounds))
    la = d.get('lookahead') or {}
    if 'service_ms' in la:
        r['discarded'] = la['discarded_tokens']
        r['busy_ms'] = la['service_ms'] + sum(x.get('draft_ms', 0) for x in rounds)
    windows = collections.defaultdict(lambda: [0, 0, 0])  # injected delay -> [rounds, sum fresh, sum h]
    for dec in la.get('decisions') or []:
        if dec['round'] < len(rounds):
            w = windows[str(rounds[dec['round']].get('injected_network_ms'))]
            w[0] += 1; w[1] += dec['fresh_gamma']; w[2] += dec['lookahead']
    if windows:
        r['windows'] = dict(windows)
    return r


def load():
    """Records per phase in raw-file glob order: list of (scenario, dataset, prompt, method, summary)."""
    if os.path.exists(CACHE):
        return json.load(open(CACHE))
    out = {}
    for phase in PHASES:
        rows = []
        for f in glob.glob(f'{ROOT}/{phase}/raw/*.json'):
            ds, scen, p, meth = FILE.match(os.path.basename(f)).groups()
            rows.append([scen, ds, p, SHORT[meth], condense(f)])
        out[phase] = rows
        print(phase, len(rows))
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    json.dump(out, open(CACHE, 'w'))
    return out


class Cell:
    """One phase and scenario: complete prompts, point estimates and paired bootstrap comparisons."""

    def __init__(self, rows, scen, methods=None, prompts=None):
        recs = collections.defaultdict(dict)
        for s, ds, p, m, r in rows:
            recs[(s, ds, p)][m] = r
        methods = methods or sorted({m for _, _, _, m, _ in rows})
        self.keys = [k for k, v in recs.items() if k[0] == scen and all(m in v for m in methods)
                     and (prompts is None or (k[1], int(k[2])) in prompts)]
        self.recs, self.methods = recs, methods
        rng = random.Random(0)
        n = len(self.keys)
        idx = np.array([[rng.randrange(n) for _ in range(n)] for _ in range(2000)])
        self.stats, self.boot = {}, {}
        for m in methods:
            t, w, j = (np.array([recs[k][m][f] for k in self.keys], dtype=float) for f in ('tok', 'wall', 'joules'))
            self.stats[m] = (sum(recs[k][m]['tok'] for k in self.keys) / sum(recs[k][m]['wall'] for k in self.keys),
                             sum(recs[k][m]['joules'] for k in self.keys) / sum(recs[k][m]['tok'] for k in self.keys))
            T, W, J = t[idx].sum(1), w[idx].sum(1), j[idx].sum(1)
            self.boot[m] = (T / W, J / T)

    def ci(self, a, b):
        """(speedup %, lo, hi, energy saving %, lo, hi) of a over b."""
        sp = np.sort(self.boot[a][0] / self.boot[b][0] - 1)
        en = np.sort(1 - self.boot[a][1] / self.boot[b][1])
        pt_s = self.stats[a][0] / self.stats[b][0] - 1
        pt_e = 1 - self.stats[a][1] / self.stats[b][1]
        return [round(100 * x, 1) for x in (pt_s, sp[50], sp[1949], pt_e, en[50], en[1949])]

    def mean(self, m, field, per='tok'):
        return sum(self.recs[k][m][field] for k in self.keys) / sum(self.recs[k][m][per] for k in self.keys)


def num(x, digits=1):
    x = round(x, digits) + 0.0
    return f'{x:.{digits}f}' if x >= 0 else f'$-${-x:.{digits}f}'


def signed(x):
    return f'${x:+.1f}$\\%'


def ci_text(lo, hi):
    return f'[{num(lo)}, {num(hi)}]'


def rng_text(vals):
    return f'{min(vals):.1f}--{max(vals):.1f}\\%'


V = {}


def put(key, value):
    V[key] = value


def put_cmp(prefix, c):
    sp, slo, shi, sv, vlo, vhi = c
    put(f'{prefix}:sp', signed(sp)); put(f'{prefix}:spm', f'{abs(sp):.1f}\\%'); put(f'{prefix}:spci', ci_text(slo, shi))
    put(f'{prefix}:sv', signed(sv)); put(f'{prefix}:svm', f'{abs(sv):.1f}\\%'); put(f'{prefix}:svci', ci_text(vlo, vhi))


def frontier(points):
    """Methods on the speed-energy frontier: no other method is at least as fast and as frugal."""
    return {m for m, (s, j) in points.items()
            if not any(s2 >= s and j2 <= j and (s2, j2) != (s, j) for m2, (s2, j2) in points.items())}


def main_cells(data):
    cells = {}
    for pair, phase in PAIRS.items():
        for scen, sc in SCENS.items():
            c = cells[(pair, sc)] = Cell(data[phase], scen, MAIN_METHODS)
            best = max(FIXED, key=lambda m: c.stats[m][0])
            c.best = best
            fastest = max(MAIN_METHODS, key=lambda m: c.stats[m][0])
            c.fastest = fastest
            put(f'{pair}:{sc}:n', str(len(c.keys)))
            put(f'{pair}:{sc}:best', NAME[best])
            put(f'{pair}:{sc}:fastest', NAME[fastest])
            for m in MAIN_METHODS:
                put(f'{pair}:{sc}:{m}:tps', f'{c.stats[m][0]:.1f}')
                put(f'{pair}:{sc}:{m}:jpt', f'{c.stats[m][1]:.3f}')
                for b in MAIN_METHODS + ['best']:
                    ref = best if b == 'best' else b
                    if ref != m:
                        put_cmp(f'{pair}:{sc}:{m}:{b}', c.ci(m, ref))
            for m in ('S', 'E'):
                put(f'{pair}:{sc}:{m}:disc', f'{100 * c.mean(m, "discarded"):.0f}')
                put(f'{pair}:{sc}:{m}:busy', f'{c.mean(m, "busy_ms"):.1f}')
                win = collections.defaultdict(lambda: [0, 0, 0])
                for k in c.keys:
                    for lvl, w in c.recs[k][m]['windows'].items():
                        for i in range(3):
                            win[lvl][i] += w[i]
                tot = [sum(w[i] for w in win.values()) for i in range(3)]
                put(f'{pair}:{sc}:{m}:fresh', f'{tot[1] / tot[0]:.1f}')
                put(f'{pair}:{sc}:{m}:h', f'{tot[2] / tot[0]:.1f}')
                if sc == 'dyn':
                    for lvl in ('2.0', '100.0'):
                        put(f'{pair}:dyn{lvl[:-2]}:{m}:fresh', f'{win[lvl][1] / win[lvl][0]:.1f}')
                        put(f'{pair}:dyn{lvl[:-2]}:{m}:h', f'{win[lvl][2] / win[lvl][0]:.1f}')
            for m in ('sync', 'g4'):
                put(f'{pair}:{sc}:{m}:disc', f'{100 * c.mean(m, "discarded"):.0f}')
                put(f'{pair}:{sc}:{m}:busy', f'{c.mean(m, "busy_ms"):.1f}')
    return cells


def aggregates(cells):
    allc = list(cells.items())
    for m in ('S', 'E'):
        cs = {k: c.ci(m, 'sync') for k, c in allc}
        put(f'x:{m}:sync:rng', rng_text([v[0] for v in cs.values()]))
        put(f'x:{m}:sync:sig', str(sum(v[1] > 0 for v in cs.values())))
        put(f'x:{m}:sync:lo', f'{min(v[1] for v in cs.values()):.1f}\\%')
        for sc in SCENS.values():
            put(f'x:{m}:sync:{sc}:rng', rng_text([v[0] for k, v in cs.items() if k[1] == sc]))
        cb = {k: c.ci(m, c.best) for k, c in allc}
        put(f'x:{m}:best:wins', str(sum(v[0] > 0 for v in cb.values())))
        put(f'x:{m}:best:sig', str(sum(v[1] > 0 for v in cb.values())))
        put(f'x:{m}:best:worst', signed(min(v[0] for v in cb.values())))
        put(f'x:{m}:best:top', signed(max(v[0] for v in cb.values())))
        for sc in SCENS.values():
            put(f'x:{m}:best:{sc}:sp:rng', rng_text([v[0] for k, v in cb.items() if k[1] == sc]))
            put(f'x:{m}:best:{sc}:sv:rng', rng_text([v[3] for k, v in cb.items() if k[1] == sc]))
        put(f'x:{m}:frontier', str(sum(m in frontier(c.stats) for _, c in allc)))
        put(f'x:{m}:frontier:dyn', str(sum(m in frontier(c.stats) for k, c in allc if k[1] == 'dyn')))
    for sc in SCENS.values():
        put(f'x:S:pearl:{sc}:rng', rng_text([c.ci('S', 'pearl')[0] for k, c in allc if k[1] == sc]))
    put('x:S:fastest', str(sum(c.fastest == 'S' for _, c in allc)))
    put('x:cape:fastest', str(sum(c.fastest in ('S', 'E') for _, c in allc)))
    put('x:cape:fastest:dyn', str(sum(c.fastest in ('S', 'E') for k, c in allc if k[1] == 'dyn')))
    # Worst-case shortfall of every method against the fastest method of each setting.
    regret = {m: max(1 - c.stats[m][0] / c.stats[c.fastest][0] for _, c in allc) for m in MAIN_METHODS}
    for m in MAIN_METHODS:
        put(f'x:{m}:regret', f'{100 * regret[m]:.1f}\\%')
    base = min(BASELINES, key=regret.get)
    put('x:base:regret', f'{100 * regret[base]:.1f}\\%'); put('x:base:regret:who', NAME[base])
    # Each fixed window's weakest setting relative to synchronous decoding.
    for g in FIXED + ['pipesd', 'hf', 'pearl']:
        k, c = min(allc, key=lambda kc: kc[1].ci(g, 'sync')[0])
        put(f'x:{g}:sync:worst', signed(c.ci(g, 'sync')[0]))
        put(f'x:{g}:sync:worst:where', f'{PAIR_NAME[k[0]].split()[0]}, {DELAY_NAME[k[1]]}')
    # CAPE-E against PicoSpec at its default window.
    ce = {k: c.ci('E', 'g4') for k, c in allc}
    put('x:E:g4:sv:rng', rng_text([v[3] for v in ce.values()]))
    put('x:E:g4:sv:sig', str(sum(v[4] > 0 for v in ce.values())))
    put('x:E:g4:faster', str(sum(v[0] > 0 for v in ce.values())))
    put('x:best:cells', ', '.join(f'{PAIR_NAME[p].split()[0]} ' + '/'.join(cells[(p, s)].best.replace('g', '')
                                   for s in SCENS.values()) for p in PAIRS))
    # Quality: GSM8K accuracy and exact reproduction of the reference output.
    gsm = []
    for (p, sc), c in allc:
        n = sum(1 for k in c.keys if k[1] == 'gsm8k')
        acc = {m: sum(c.recs[k][m]['correct'] for k in c.keys if k[1] == 'gsm8k') for m in MAIN_METHODS}
        gsm.append(int(max(abs(acc[m] - acc['sync']) for m in MAIN_METHODS)))
        put(f'{p}:{sc}:gsm:n', str(n))
    put('q:gsm:maxdiff', str(max(gsm)))
    for p in PAIRS:
        ex = [sum(c.recs[k][m]['exact'] for k in c.keys) / len(c.keys) for (q, _), c in allc if q == p for m in MAIN_METHODS]
        put(f'q:{p}:exact:rng', f'{100 * min(ex):.0f}--{100 * max(ex):.0f}\\%')
        acc = [(sum(c.recs[k][m]['correct'] for k in c.keys if k[1] == 'gsm8k') /
                sum(1 for k in c.keys if k[1] == 'gsm8k')) for (q, _), c in allc if q == p for m in MAIN_METHODS]
        put(f'q:{p}:gsm:rng', f'{min(acc):.2f}--{max(acc):.2f}')
    # Acceptance per workload: strict per-token acceptance of synchronous decoding over all conditions.
    for p in PAIRS:
        for ds in ('gsm8k', 'humaneval', 'mtbench'):
            ks = [(k, c) for (q, _), c in allc if q == p for k in c.keys if k[1] == ds]
            a = sum(c.recs[k]['sync']['accepted'] for k, c in ks) / sum(c.recs[k]['sync']['examined'] for k, c in ks)
            put(f'acc:{p}:{ds}', f'{a:.2f}')
    n_main = sum(len(c.keys) * len(MAIN_METHODS) for _, c in allc)
    put('n:main', f'{n_main:,}'.replace(',', '{,}'))


def sweep(data):
    prompts = {(ds, i) for ds in ('gsm8k', 'humaneval', 'mtbench') for i in range(10)}
    methods = ['g2', 'g4', 'g8', 'S', 'pearl']
    res = {}
    for ms, phase, scen in [(2, 'gemma3_main', 'low'), (10, 'gemma3_sweep', 'd10'), (25, 'gemma3_sweep', 'd25'),
                            (50, 'gemma3_sweep', 'd50'), (100, 'gemma3_main', 'high'), (200, 'gemma3_sweep', 'd200')]:
        c = Cell(data[phase], scen, methods, prompts)
        best = max(FIXED, key=lambda m: c.stats[m][0])
        res[ms] = (c, best)
        put(f'sw:d{ms}:best', NAME[best])
        for m in methods:
            put(f'sw:d{ms}:{m}:tps', f'{c.stats[m][0]:.1f}')
        for m in ('S', 'pearl'):
            put_cmp(f'sw:d{ms}:{m}:best', c.ci(m, best))
        put_cmp(f'sw:d{ms}:S:pearl', c.ci('S', 'pearl'))
    put('sw:S:pearl:rng', rng_text([c.ci('S', 'pearl')[0] for c, _ in res.values()]))
    put('sw:S:pearl:wins', str(sum(c.ci('S', 'pearl')[0] > 0 for c, _ in res.values())))
    put('sw:S:best:sv:rng', rng_text([c.ci('S', best)[3] for c, best in res.values()]))
    return res


def pooled(data, phase, methods):
    """Cell over all scenarios of a phase with each prompt (all its scenarios) as one cluster."""
    rows = []
    for s, ds, p, m, r in data[phase]:
        rows.append(['all', ds, p, m, r])
    merged = collections.defaultdict(lambda: dict(tok=0, wall=0.0, joules=0.0, n=0))
    for _, ds, p, m, r in rows:
        x = merged[(ds, p, m)]
        x['tok'] += r['tok']; x['wall'] += r['wall']; x['joules'] += r['joules']; x['n'] += 1
    full = max(x['n'] for x in merged.values())
    return Cell([['all', ds, p, m, x] for (ds, p, m), x in merged.items() if x['n'] == full], 'all', methods)


def ablation(data):
    methods = ['g4', 'la', 'S', 'med']
    cells = {sc: Cell(data['gemma3_ablation'], scen, methods) for scen, sc in SCENS.items()}
    cells['pool'] = pooled(data, 'gemma3_ablation', methods)
    for sc, c in cells.items():
        for m in methods:
            put(f'ab:{sc}:{m}:tps', f'{c.stats[m][0]:.1f}')
            put(f'ab:{sc}:{m}:jpt', f'{c.stats[m][1]:.3f}')
        for a, b in [('la', 'g4'), ('S', 'g4'), ('S', 'la'), ('med', 'g4'), ('S', 'med')]:
            put_cmp(f'ab:{sc}:{a}:{b}', c.ci(a, b))
    rows = [('g4', 'PicoSpec-4'), ('la', r'+ adaptive lookahead'), ('S', r'+ adaptive fresh (\capes{})')]
    lines = [r'\begin{tabular}{@{}lrrrrrr@{}}', r'\toprule',
             r' & \multicolumn{3}{c}{Throughput (tok/s)} & \multicolumn{3}{c}{J/token}\\',
             r'\cmidrule(lr){2-4}\cmidrule(lr){5-7}',
             r'Variant & 2\,ms & 100\,ms & dyn. & 2\,ms & 100\,ms & dyn.\\', r'\midrule']
    for m, label in rows:
        sp = ' & '.join(f'{cells[sc].stats[m][0]:.1f}' for sc in ('low', 'high', 'dyn'))
        jt = ' & '.join(f'{cells[sc].stats[m][1]:.3f}' for sc in ('low', 'high', 'dyn'))
        lines.append(f'{label} & {sp} & {jt}\\\\')
    lines += [r'\bottomrule', r'\end{tabular}']
    open(f'{PAPER}/tables/ablation.tex', 'w').write('\n'.join(lines) + '\n')


def weights(data):
    methods = ['S', 'w025', 'E', 'w1', 'w2']
    c = Cell(data['gemma3_weights'], 'dynamic', methods)
    w = {'S': '0', 'w025': '0.25', 'E': '0.5', 'w1': '1', 'w2': '2'}
    lines = [r'\begin{tabular}{@{}lrrll@{}}', r'\toprule',
             r'$w$ & tok/s & J/tok & Throughput (\%) & J/tok saving (\%)\\', r'\midrule']
    for m in methods:
        put(f'w:{m}:tps', f'{c.stats[m][0]:.1f}'); put(f'w:{m}:jpt', f'{c.stats[m][1]:.3f}')
        if m == 'S':
            lines.append(f'0 (\\capes{{}}) & {c.stats[m][0]:.1f} & {c.stats[m][1]:.3f} & -- & --\\\\')
            continue
        r = c.ci(m, 'S')
        put_cmp(f'w:{m}:S', r)
        name = w[m] + (r' (\capee{})' if m == 'E' else '')
        lines.append(f'{name} & {c.stats[m][0]:.1f} & {c.stats[m][1]:.3f} & ${r[0]:+.1f}$ {ci_text(r[1], r[2])} & '
                     f'${r[3]:+.1f}$ {ci_text(r[4], r[5])}\\\\')
    lines += [r'\bottomrule', r'\end{tabular}']
    open(f'{PAPER}/tables/weights.tex', 'w').write('\n'.join(lines) + '\n')
    put('w:n', str(len(c.keys)))


def speedup_table(cells):
    """Throughput change over Sync-4 for every method and setting; Sync-4 row in tok/s."""
    cols = [(p, sc) for p in PAIRS for sc in SCENS.values()]
    head = ' & '.join(rf'\multicolumn{{3}}{{c}}{{{PAIR_NAME[p]}}}' for p in PAIRS)
    rules = ''.join(rf'\cmidrule(lr){{{2 + 3 * i}-{4 + 3 * i}}}' for i in range(4))
    lines = [r'\begin{tabular}{@{}l' + 'r' * 12 + r'r@{}}', r'\toprule', f' & {head} & \\\\', rules,
             'Method & ' + ' & '.join(['2\\,ms', '100\\,ms', 'dyn.'] * 4) + r' & Worst\\', r'\midrule']
    sync = ' & '.join(f'{cells[k].stats["sync"][0]:.1f}' for k in cols)
    lines.append(f'Sync-4 (tok/s) & {sync} & {V["x:sync:regret"].replace(chr(92) + "%", "")}\\\\')
    lines.append(r'\midrule')
    for m in MAIN_METHODS[1:]:
        cellstr = []
        for k in cols:
            c = cells[k]
            v = f'{100 * (c.stats[m][0] / c.stats["sync"][0] - 1):+.1f}'.replace('-', '$-$')
            if m == c.best:
                v += r'$^\dagger$'
            if m == c.fastest:
                v = rf'\textbf{{{v}}}'
            cellstr.append(v)
        if m == 'E':
            lines.append(r'\midrule')
        worst = V[f'x:{m}:regret'].replace('\\%', '')
        lines.append(f'{NAME[m]} & ' + ' & '.join(cellstr) + f' & {worst}\\\\')
    lines += [r'\bottomrule', r'\end{tabular}']
    open(f'{PAPER}/tables/speedup.tex', 'w').write('\n'.join(lines) + '\n')


# Figure styling: CAPE in categorical slot 1 (blue), CAPE-E slot 3 (aqua), PEARL slot 2 (orange);
# every other method in neutral grays with its own marker, so identity never rests on hue alone.
STYLE = {'S': ('#2a78d6', '*', 8.5), 'E': ('#1baf7a', 'P', 6.5), 'pearl': ('#eb6834', 'D', 4.5),
         'g2': ('#9a9893', 'o', 4.5), 'g4': ('#6e6c67', 's', 4.5), 'g8': ('#3f3e3a', '^', 5),
         'sync': ('#3f3e3a', 'x', 5), 'hf': ('#9a9893', 'v', 5), 'pipesd': ('#6e6c67', '<', 5)}
LABEL = {'S': 'CAPE-S', 'E': 'CAPE-E', 'pearl': 'PEARL', 'g2': 'PicoSpec-2', 'g4': 'PicoSpec-4', 'g8': 'PicoSpec-8',
         'sync': 'Sync-4', 'hf': 'HF assisted', 'pipesd': 'PipeSD'}


# Direct-label offsets (points) where the default right-hand placement would collide.
LABEL_AT = {('gemma2', 'E'): (-5, 4, 'right'), ('gemma2', 'S'): (5, -4, 'left'), ('llama', 'E'): (-3, -7, 'right')}


def plt_setup():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family': 'serif', 'font.serif': ['Nimbus Roman', 'Times New Roman', 'Times', 'DejaVu Serif'],
                         'font.size': 7, 'axes.linewidth': 0.5, 'xtick.major.width': 0.5,
                         'ytick.major.width': 0.5, 'pdf.fonttype': 42, 'axes.edgecolor': '#52514e',
                         'xtick.color': '#52514e', 'ytick.color': '#52514e', 'axes.labelcolor': '#0b0b0b'})
    return plt


def sweep_figure(res):
    plt = plt_setup()
    D = sorted(res)
    fig, ax = plt.subplots(figsize=(3.4, 2.15))
    order = ['g2', 'g4', 'g8', 'pearl', 'S']
    for m in order:
        col, mk, ms = STYLE[m]
        ys = [res[d][0].stats[m][0] for d in D]
        ax.plot(D, ys, '-' if m == 'S' else (':' if m in FIXED else '--'), color=col, marker=mk,
                ms=ms if m == 'S' else 4, lw=2 if m == 'S' else 1, label=LABEL[m], zorder=3 if m == 'S' else 2,
                mec='white' if m == 'S' else col, mew=0.5)
    ax.set_xscale('log'); ax.set_xticks(D); ax.set_xticklabels([str(d) for d in D]); ax.minorticks_off()
    ax.set_xlabel('Added delay per verification (ms)'); ax.set_ylabel('Throughput (tok/s)')
    ax.grid(color='#e6e5e1', lw=0.5); ax.set_axisbelow(True)
    ax.legend(fontsize=6.5, frameon=False, ncol=1, loc='lower left')
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    fig.tight_layout(pad=0.3)
    fig.savefig(f'{PAPER}/figures/sweep.pdf'); fig.savefig(f'{PAPER}/build/sweep.png', dpi=200)


def frontier_figure(cells):
    plt = plt_setup()
    fig, axes = plt.subplots(2, 2, figsize=(3.4, 3.0))
    for ax, pair in zip(axes.flat, PAIRS):
        c = cells[(pair, 'dyn')]
        front = sorted(frontier(c.stats), key=lambda m: c.stats[m][1])
        ax.plot([c.stats[m][1] for m in front], [c.stats[m][0] for m in front], '-', color='#c3c2b7', lw=1.6,
                zorder=1, solid_capstyle='round')
        for m in MAIN_METHODS:
            col, mk, ms = STYLE[m]
            s, j = c.stats[m]
            ax.plot(j, s, mk, color=col, ms=ms, mec='white' if mk not in 'x' else col, mew=0.4,
                    zorder=3 if m in ('S', 'E') else 2, label=LABEL[m])
        for m in ('S', 'E'):
            s, j = c.stats[m]
            dx, dy, ha = LABEL_AT.get((pair, m), (5, 3 if m == 'S' else -4, 'left'))
            ax.annotate(LABEL[m], (j, s), xytext=(dx, dy), textcoords='offset points', fontsize=6,
                        color='#0b0b0b', va='center', ha=ha)
        ax.set_title(PAIR_NAME[pair], fontsize=7, pad=2)
        ax.grid(color='#e6e5e1', lw=0.5); ax.set_axisbelow(True)
        ax.tick_params(labelsize=6, length=2, pad=1)
        for s in ('top', 'right'):
            ax.spines[s].set_visible(False)
        xs = [c.stats[m][1] for m in MAIN_METHODS]; ys = [c.stats[m][0] for m in MAIN_METHODS]
        ax.set_xlim(min(xs) - 0.06 * (max(xs) - min(xs)), max(xs) + 0.22 * (max(xs) - min(xs)))
        ax.set_ylim(min(ys) - 0.08 * (max(ys) - min(ys)), max(ys) + 0.1 * (max(ys) - min(ys)))
    fig.supxlabel('Device energy per token (J)', fontsize=7, y=0.1)
    fig.supylabel('Throughput (tok/s)', fontsize=7, x=0.02)
    handles, labels = axes.flat[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=5, fontsize=5.8, frameon=False, handletextpad=0.2,
               columnspacing=0.7, bbox_to_anchor=(0.53, -0.01))
    fig.tight_layout(pad=0.3, rect=(0.02, 0.1, 1, 1), h_pad=0.6, w_pad=0.6)
    fig.savefig(f'{PAPER}/figures/frontier.pdf'); fig.savefig(f'{PAPER}/build/frontier.png', dpi=200)


def decision_time():
    """Median time of one window decision (64 candidates, 64 round-trip samples, interruption priced)
    on the machine running this script; the paper's value is measured on the Jetson CPU."""
    sys.path.insert(0, '.')
    from common.pipeline_model import choose_windows
    rng, times = random.Random(1), []
    for _ in range(400):
        samples = [100 + rng.expovariate(1 / 20) for _ in range(64)]
        t = time.perf_counter()
        choose_windows(0.8, 0.85, samples, 10.0, 24.5, 0.0, 2.3, 8, interrupt=True)
        times.append(1000 * (time.perf_counter() - t))
    put('ctl:decide', f'{statistics.median(times):.1f}\\,ms')


def main():
    data = load()
    decision_time()
    os.makedirs(f'{PAPER}/build', exist_ok=True)
    cells = main_cells(data)
    aggregates(cells)
    speedup_table(cells)
    res = sweep(data)
    ablation(data)
    weights(data)
    put('n:all', f'{sum(len(rows) for rows in data.values()):,}'.replace(',', '{,}'))
    with open(f'{PAPER}/numbers.tex', 'w') as f:
        f.write('% Generated by scripts/make_assets.py from results/rerun_20261028; do not edit by hand.\n')
        for k in sorted(V):
            f.write(f'\\expandafter\\def\\csname cape@{k}\\endcsname{{{V[k]}}}\n')
    sweep_figure(res)
    frontier_figure(cells)
    print(len(V), 'numbers')


if __name__ == '__main__':
    main()
