# Gemma-3 throughput vs added delay on the 30 sweep prompts (first 10 per dataset).
# 2 and 100 ms come from the same prompts in gemma3_full_110 (same pair, services and seeds).
import json, os, sys
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
base='results/gemma3_20261026'
M={'fixed_g2':'Fixed-2','fixed_fast':'Fixed-4','fixed_g8':'Fixed-8','pearl':'PEARL','markov_w0_dist':'CAPE-S'}
pts={(10,'d10'):'gemma3_delay_sweep',(25,'d25'):'gemma3_delay_sweep',(50,'d50'):'gemma3_delay_sweep',(200,'d200'):'gemma3_delay_sweep',(2,'low'):'gemma3_full_110',(100,'high'):'gemma3_full_110'}
res={}
for (ms,sc),ph in pts.items():
  for m in M:
    tok=wall=j=0
    for ds in ['gsm8k','humaneval','mtbench']:
      for i in range(10):
        r=json.load(open(f'{base}/{ph}/raw/{ds}_{sc}_p{i}_r0_{m}.json'))
        tok+=r['output_tokens']; wall+=r['wall_time_s']; j+=r['energy']['joules']
    res[(ms,m)]=(tok/wall,j/tok)
D=sorted({ms for ms,_ in res})
for ms in D:
  best=max(res[(ms,m)][0] for m in ['fixed_g2','fixed_fast','fixed_g8'])
  print(ms, ' '.join(f"{M[m]}={res[(ms,m)][0]:.2f}" for m in M), f"CAPE-S/best={100*(res[(ms,'markov_w0_dist')][0]/best-1):+.1f}")
fig,ax=plt.subplots(figsize=(3.4,2.3))
sty={'fixed_g2':('#9aa5b1','o',':'),'fixed_fast':('#6b7785','s',':'),'fixed_g8':('#3d4752','^',':'),'pearl':('#d08c2f','D','--'),'markov_w0_dist':('#1f5fbf','*','-')}
for m,(c,mk,ls) in sty.items():
  ys=[res[(ms,m)][0] for ms in D]
  ax.plot(D,ys,ls,color=c,marker=mk,ms=6 if mk=='*' else 4,lw=1.8 if m=='markov_w0_dist' else 1.1,label=M[m])
ax.set_xscale('log'); ax.set_xticks(D); ax.set_xticklabels([str(d) for d in D]); ax.minorticks_off()
ax.set_xlabel('Added delay per verification (ms)'); ax.set_ylabel('Throughput (tok/s)')
ax.grid(alpha=.3,lw=.5); ax.legend(fontsize=6.5,frameon=False,ncol=2)
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig(sys.argv[1]); print('saved')
