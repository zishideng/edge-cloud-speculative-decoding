# tokens/s, J/token from SUMMARY.md files (unpaired, aggregate)
D={
'Llama':{'low':dict(bf=(26.77,.5559,'g2'),S=(26.30,.5562),E=(26.69,.5341),PEARL=(27.666,.5000),Pico=(24.340,.6666),PipeSD=(24.905,.6292),HF=(21.972,.6607),Sync=(23.60,.4985)),
 'high':dict(bf=(18.15,.7699,'g4'),S=(18.74,.7839),E=(17.27,.7197),PEARL=(18.187,.7580),Pico=(17.997,.7806),PipeSD=(15.544,.9951),HF=(13.379,.7518),Sync=(12.73,.6159)),
 'dyn':dict(bf=(20.68,.7251,'g4'),S=(21.68,.6700),E=(21.18,.6235),PEARL=(20.005,.6173),Pico=(21.160,.7125),PipeSD=(20.274,.7682),HF=(17.373,.7045),Sync=(17.60,.5381))},
'Qwen':{'low':dict(bf=(37.46,.2934,'g2'),S=(36.30,.3082),E=(36.16,.2856),PEARL=(30.493,.2659),Pico=(35.069,.3599),PipeSD=(32.025,.3713),HF=(22.849,.3699),Sync=(26.46,.2806)),
 'high':dict(bf=(20.32,.5836,'g8'),S=(20.74,.5144),E=(18.55,.4414),PEARL=(17.765,.4833),Pico=(17.751,.4677),PipeSD=(18.446,.6355),HF=(12.902,.5058),Sync=(13.35,.4480)),
 'dyn':dict(bf=(26.28,.3989,'g4'),S=(27.67,.3898),E=(26.04,.3459),PEARL=(24.858,.3632),Pico=(25.678,.4022),PipeSD=(24.209,.4899),HF=(17.388,.4198),Sync=(19.20,.3456))},
'Gemma2':{'low':dict(bf=(15.18,1.0677,'g2'),S=(16.07,.9841),E=(16.14,.9720),PEARL=(16.671,.9482),Pico=(13.798,1.2169),PipeSD=(13.818,1.1547),HF=(12.662,1.2209),Sync=(14.07,.9537)),
 'high':dict(bf=(13.15,1.1347,'g2'),S=(13.40,1.1664),E=(13.26,1.1305),PEARL=(13.823,1.1061),Pico=(12.559,1.3342),PipeSD=(11.546,1.3746),HF=(10.829,1.3057),Sync=(9.71,1.0665)),
 'dyn':dict(bf=(14.17,1.0989,'g2'),S=(14.35,1.0899),E=(14.43,1.0564),PEARL=(13.485,1.0346),Pico=(13.191,1.2711),PipeSD=(12.718,1.2516),HF=(11.671,1.2659),Sync=(11.82,1.0116))},
'Gemma3':{'low':dict(bf=(36.806,.2183,'g2'),S=(36.967,.2149),E=(34.808,.2125),PEARL=(35.264,.2075),Pico=(39.288,.2849),PipeSD=(23.043,.3369),HF=(21.924,.3258),Sync=(24.972,.2650)),
 'high':dict(bf=(18.501,.5005,'g8'),S=(19.865,.4368),E=(17.358,.3830),PEARL=(17.865,.4140),Pico=(17.178,.4013),PipeSD=(15.100,.4817),HF=(13.316,.4616),Sync=(13.912,.4098)),
 'dyn':dict(bf=(24.273,.3354,'g4'),S=(26.662,.2987),E=(24.999,.2790),PEARL=(24.344,.2979),Pico=(25.181,.3326),PipeSD=(19.079,.3892),HF=(16.555,.3943),Sync=(18.945,.3214))}}
M=['S','E','PEARL','Pico','PipeSD','HF','Sync']
for d in ['low','high','dyn']:
  print(f'\n== {d}: speed % vs per-delay best fixed (energy saving %) ; rank of CAPE-S by speed')
  for p,v in D.items():
    bf=v[d]['bf']; row=[]
    for m in M:
      s,e=v[d][m][:2]; row.append(f'{m}:{100*(s/bf[0]-1):+.1f}({100*(1-e/bf[1]):+.0f})')
    allm={m:v[d][m][0] for m in M+['bf']}
    rk=sorted(allm,key=lambda k:-allm[k])
    print(f'{p:7s} bf={bf[2]} '+' '.join(row)+f' | fastest: {rk[0]},{rk[1]}')
print('\n== frontier check (per pair, delay): methods not dominated in (speed,J)')
for p,v in D.items():
  for d in ['low','high','dyn']:
    pts={m:v[d][m][:2] for m in M+['bf']}
    nd=[m for m in pts if not any(pts[o][0]>=pts[m][0] and pts[o][1]<=pts[m][1] and o!=m for o in pts)]
    print(p,d,nd)
