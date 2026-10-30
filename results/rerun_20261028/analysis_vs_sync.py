"""Rerun 10-28 analysis: per pair x delay, speed/energy of every method, ratios vs sync_g4 (and best interrupt
fixed window, PEARL) with prompt-cluster paired bootstrap 95% CIs; only prompts complete in all methods."""
import collections, glob, json, os, random, re, sys
D = '/home/jetson/zishi_edge-cloud-speculative-decoding/results/rerun_20261028'
PAIRS = ['gemma3_main', 'llama_main', 'qwen_main', 'gemma2_main']
FIXED = ['picospec_g2', 'picospec', 'picospec_g8']
out = {}
for pair in PAIRS:
    recs = collections.defaultdict(dict)  # (scen, prompt) -> method -> (tok, wall, J, quality, exact)
    for f in glob.glob(f'{D}/{pair}/raw/*.json'):
        m = re.match(r'(\w+?)_(low|high|dynamic)_p(\d+)_r\d+_(\w+)\.json', os.path.basename(f))
        ds, scen, p, meth = m.groups()
        d = json.load(open(f))
        recs[(scen, ds, p)][meth] = (d['output_tokens'], d['wall_time_s'], d['energy']['joules'],
                                     d.get('task_quality') if ds == 'gsm8k' else None,
                                     d['output_ids'] == d['reference_ids'])
    methods = sorted({m for v in recs.values() for m in v})
    res = out[pair] = {}
    for scen in ('low', 'high', 'dynamic'):
        keys = [k for k, v in recs.items() if k[0] == scen and len(v) == len(methods)]
        def agg(meth, ks):
            t = sum(recs[k][meth][0] for k in ks); w = sum(recs[k][meth][1] for k in ks)
            j = sum(recs[k][meth][2] for k in ks)
            return t / w, j / t
        stats = {m: agg(m, keys) for m in methods}
        best = max(FIXED, key=lambda m: stats[m][0])
        rng = random.Random(0)
        boots = [[rng.choice(keys) for _ in keys] for _ in range(2000)]
        def ci(a, b):  # speed ratio a/b and energy saving 1 - Ja/Jb, paired bootstrap over prompts
            sp, en = [], []
            for ks in boots:
                sa, ja = agg(a, ks); sb, jb = agg(b, ks)
                sp.append(sa / sb - 1); en.append(1 - ja / jb)
            sp.sort(); en.sort()
            pt_s = stats[a][0] / stats[b][0] - 1; pt_e = 1 - stats[a][1] / stats[b][1]
            return [round(100 * x, 1) for x in (pt_s, sp[50], sp[1949], pt_e, en[50], en[1949])]
        res[scen] = {'n_prompts': len(keys), 'best_fixed': best,
                     'stats': {m: [round(s, 2), round(j, 4)] for m, (s, j) in stats.items()},
                     'vs_sync': {m: ci(m, 'sync_g4') for m in methods if m != 'sync_g4'},
                     'vs_best_fixed': {m: ci(m, best) for m in ('markov_w0_dist_int', 'markov_w05_dist_int', 'pearl')},
                     'gsm8k_acc': {m: round(sum(recs[k][m][3] for k in keys if k[1] == 'gsm8k') /
                                            max(1, sum(1 for k in keys if k[1] == 'gsm8k')), 3) for m in methods},
                     'exact_match_ref': {m: round(sum(recs[k][m][4] for k in keys) / len(keys), 3) for m in methods}}
    print(pair, {s: res[s]['n_prompts'] for s in res}, file=sys.stderr)
json.dump(out, open(f'{D}/analysis_vs_sync.json', 'w'), indent=1)
