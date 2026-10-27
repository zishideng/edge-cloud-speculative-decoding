# PROVISIONAL paper numbers from SUMMARY.md aggregates (unpaired ratios, no CIs).
# Replaced by the paired extraction after the timed Gemma-3 phases finish.
import sys; sys.path.insert(0,'.')
exec(open('xpair.py').read().split("M=['S'")[0])
out=sys.argv[1]
PAIRS=['Llama','Qwen','Gemma2','Gemma3']; KEY={'Llama':'llama','Qwen':'qwen','Gemma2':'gemmatwo','Gemma3':'gemmathree'}
DL={'low':'low','high':'high','dyn':'dyn'}
M=['S','E','PEARL','Pico','PipeSD','HF','Sync']
defs={}
def pct(x): return f"{x:.1f}"
for p in PAIRS:
  for d in DL:
    v=D[p][d]; bf=v['bf']; k=f"x:{KEY[p]}:{d}"
    defs[k+':bf']='Fixed-'+bf[2][1:]
    for m in M+['bf']:
      s,e=v[m][:2]
      defs[f"{k}:{m}:tps"]=f"{s:.1f}"; defs[f"{k}:{m}:jpt"]=f"{e:.3f}"
      if m!='bf':
        defs[f"{k}:{m}:sp"]=f"${100*(s/bf[0]-1):+.1f}$"; defs[f"{k}:{m}:abssp"]=pct(abs(100*(s/bf[0]-1)))+r'\%'
        defs[f"{k}:{m}:sv"]=f"${100*(1-e/bf[1]):+.1f}$"; defs[f"{k}:{m}:abssv"]=pct(abs(100*(1-e/bf[1])))+r'\%'
    for m in ['S','E']:
      for o in ['PEARL','Pico']:
        r=100*(v[m][0]/v[o][0]-1); defs[f"{k}:{m}:{o}:abssp"]=pct(abs(r))+r'\%'; defs[f"{k}:{m}:{o}:sp"]=f"${r:+.1f}$"
# headline aggregates
def rng(vals): return pct(min(vals))+r'--'+pct(max(vals))+r'\%'
sp=lambda p,d,m,ref='bf': 100*(D[p][d][m][0]/D[p][d][ref][0]-1)
sv=lambda p,d,m: 100*(1-D[p][d][m][1]/D[p][d]['bf'][1])
defs['x:dyn:S:sp:rng']=rng([sp(p,'dyn','S') for p in PAIRS])
defs['x:dyn:S:sp:max']=pct(max(sp(p,'dyn','S') for p in PAIRS))+r'\%'
defs['x:dyn:S:pearl:rng']=rng([sp(p,'dyn','S','PEARL') for p in PAIRS])
defs['x:dyn:E:sv:rng']=rng([sv(p,'dyn','E') for p in PAIRS])
defs['x:dyn:E:sp:min']=f"${min(sp(p,'dyn','E') for p in PAIRS):+.1f}$"
defs['x:dyn:E:sp:max']=f"${max(sp(p,'dyn','E') for p in PAIRS):+.1f}$"
wins=sum(sp(p,d,'S')>0 for p in PAIRS for d in DL); defs['x:wins']=str(wins)
defs['x:high:S:sp:rng']=rng([sp(p,'high','S') for p in PAIRS])
defs['x:sync:dyn:rng']=rng([sp(p,'dyn','S','Sync') for p in PAIRS])
defs['x:hf:dyn:rng']=rng([sp(p,'dyn','S','HF') for p in PAIRS])
defs['x:requests']='13{,}200'
with open(out+'/numbers_draft.tex','w') as f:
  f.write('% PROVISIONAL: unpaired aggregates from the SUMMARY.md reports (see scratchpad provisional.py).\n% Replaced by the paired extraction (scripts/extract_evidence.py) after the timed phases.\n')
  for k,val in sorted(defs.items()): f.write(f"\\expandafter\\def\\csname cape@{k}\\endcsname{{{val}}}\n")
NAME={'Sync':'Sync-4','bf':'Best fixed$^\\dagger$','PEARL':'PEARL','Pico':'PicoSpec','PipeSD':'PipeSD','HF':'HF assisted','S':'\\textbf{\\capes{}}','E':'\\textbf{\\capee{}}'}
ORDER=['Sync','HF','PipeSD','PicoSpec' and 'Pico','PEARL','bf','S','E']
with open(out+'/tables/dynamic.tex','w') as f:
  f.write('\\begin{tabular}{@{}l'+'rrr'*4+'@{}}\n\\toprule\n & '+' & '.join(f'\\multicolumn{{3}}{{c}}{{{n}}}' for n in ['Llama 1B/8B','Qwen 0.5B/7B','Gemma-2 2B/9B','Gemma-3 270M/4B'])+'\\\\\n')
  f.write(''.join(f'\\cmidrule(lr){{{2+3*i}-{4+3*i}}}' for i in range(4))+'\n')
  f.write('Method'+' & tok/s & J/tok & $\\Delta$\\%'*4+'\\\\\n\\midrule\n')
  for m in ORDER:
    cells=[]
    for p in PAIRS:
      s,e=D[p]['dyn'][m][:2]; bf=D[p]['dyn']['bf']
      dlt='--' if m=='bf' else f"${100*(s/bf[0]-1):+.1f}$"
      fastest = max((D[p]['dyn'][x][0],x) for x in ORDER)[1]==m
      cells.append((f"\\textbf{{{s:.1f}}}" if fastest else f"{s:.1f}")+f" & {e:.3f} & {dlt}")
    f.write(NAME[m]+' & '+' & '.join(cells)+' \\\\\n')
  f.write('\\bottomrule\n\\end{tabular}\n')
with open(out+'/tables/fixed.tex','w') as f:
  f.write('\\begin{tabular}{@{}l'+'rr'*4+'@{}}\n\\toprule\n & '+' & '.join(f'\\multicolumn{{2}}{{c}}{{{n}}}' for n in ['Llama','Qwen','Gemma-2','Gemma-3'])+'\\\\\n')
  f.write(''.join(f'\\cmidrule(lr){{{2+2*i}-{3+2*i}}}' for i in range(4))+'\n')
  f.write('Method'+' & 2\\,ms & 100\\,ms'*4+'\\\\\n\\midrule\n')
  f.write('Best fixed window'+''.join(f" & {D[p]['low']['bf'][2].replace('g','Fixed-')} & {D[p]['high']['bf'][2].replace('g','Fixed-')}" for p in PAIRS)+' \\\\\n\\midrule\n')
  for m in ['Sync','HF','PipeSD','Pico','PEARL','S','E']:
    cells=[]
    for p in PAIRS:
      for d in ['low','high']:
        r=sp(p,d,m); top=max((D[p][d][x][0],x) for x in ORDER)[1]==m
        cells.append(f"$\\mathbf{{{r:+.1f}}}$" if top else f"${r:+.1f}$")
    f.write(NAME[m]+' & '+' & '.join(cells)+' \\\\\n')
  f.write('\\bottomrule\n\\end{tabular}\n')
print(len(defs),'defs; wins',wins)
