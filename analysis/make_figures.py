"""Repeatable PNG/SVG experiment plots. No hardcoded result directory."""
import argparse
import json
from pathlib import Path
from statistics import mean
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from common.window_estimator import estimate


def make_figures(directory):
    root=Path(directory)
    records=[json.loads(p.read_text(encoding='utf-8')) for p in (root/'raw').glob('*.json')]
    if not records:
        raise ValueError('No successful raw experiments; refusing to create empty charts')
    c=json.loads((root/'config/resolved.json').read_text(encoding='utf-8'))
    out=root/'figures'; out.mkdir(exist_ok=True)
    mode=records[0]['mode']; prefix='SYNTHETIC / virtual time' if mode=='simulate' else 'Real model / injected network'
    scenarios=list(dict.fromkeys(r['scenario'] for r in records))
    base=[r for r in records if r['study']=='baseline']
    sweep=[r for r in records if r['study']=='gamma_sweep']
    ksweep=[r for r in records if r['study']=='k_sweep']
    if not base or not sweep or not ksweep:
        raise ValueError('Incomplete baseline or parameter sweeps; see failure logs')
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

    def save(fig,name):
        fig.suptitle(prefix,fontsize=10)
        fig.tight_layout()
        for ext in ('png','svg'):
            fig.savefig(out/f'{name}.{ext}',dpi=140,bbox_inches='tight')
        plt.close(fig)

    def curve(data,xkey,yfn,name,title,xlabel,ylabel):
        fig,ax=plt.subplots(figsize=(8,5))
        for scenario in scenarios:
            group=[r for r in data if r['scenario']==scenario]
            xs=sorted({r[xkey] for r in group})
            if not xs: continue
            ys=[mean(yfn(r) for r in group if r[xkey]==x) for x in xs]
            ax.plot(xs,ys,'o-',label=scenario)
        ax.set(title=title,xlabel=xlabel,ylabel=ylabel); ax.legend(fontsize=8)
        save(fig,name)

    curve(sweep,'configured_gamma',lambda r:r['tokens_per_second'],'gamma_throughput',
          'Fixed-window strict acceptance','Draft window gamma','Throughput (tokens/s)')
    curve(sweep,'configured_gamma',lambda r:r['wall_time_s']*1000,'gamma_latency',
          'Request end-to-end latency','Draft window gamma','Request latency (ms)')
    curve(ksweep,'configured_k',lambda r:r['relaxed_acceptance_rate'],'k_acceptance',
          'Quality-constrained fixed K','Configured K','Accepted / examined tokens')
    quality_available=all(r['task_quality_drop'] is not None for r in records)
    qkey='task_quality_drop' if quality_available else 'token_difference_rate'
    qlabel='Task accuracy drop (fraction)' if quality_available else 'Token difference vs strict reference (proxy, not task quality)'
    curve(ksweep,'configured_k',lambda r:r[qkey],'k_quality',
          'Quality change under fixed K','Configured K',qlabel)

    # Compare each scheme within a scenario; mixed jitter/queue scenarios are categorical.
    fig,ax=plt.subplots(figsize=(9,5))
    for method in ('A','B','C','Proposed'):
        ys=[mean(r['tokens_per_second'] for r in base if r['method']==method and r['scenario']==s) for s in scenarios]
        ax.plot(range(len(scenarios)),ys,'o-',label=method)
    ax.set_xticks(range(len(scenarios)),scenarios,rotation=20)
    ax.set(title='Scheme comparison under network conditions',xlabel='Network scenario',ylabel='Throughput (tokens/s)');ax.legend()
    save(fig,'scheme_comparison')

    steady=[s for s in scenarios if not any(c['NETWORK_SCENARIOS'][s].get(k,0) for k in ('jitter_ms','queue_ms','burst_ms','bandwidth_mbps'))]
    steady.sort(key=lambda s:c['NETWORK_SCENARIOS'][s]['rtt_ms'])
    fig,ax=plt.subplots(figsize=(8,5))
    for method in ('A','B','C','Proposed'):
        group=[r for r in base if r['method']==method]
        ax.plot([c['NETWORK_SCENARIOS'][s]['rtt_ms'] for s in steady],
                [mean(r['tokens_per_second'] for r in group if r['scenario']==s) for s in steady],'o-',label=method)
    ax.set(title='Steady network latency vs throughput',xlabel='Configured RTT (ms)',ylabel='Throughput (tokens/s)');ax.legend()
    save(fig,'network_throughput')

    estimates=[]
    for scenario in scenarios:
        group=[r for r in sweep if r['scenario']==scenario]
        rows=[row for r in group for row in r['rounds']]
        xs=[r['gamma'] for r in rows]; ys=[r['cloud_verify_ms'] for r in rows]
        mx,my=mean(xs),mean(ys); variance=sum((x-mx)**2 for x in xs)
        slope=max(0,sum((x-mx)*(y-my) for x,y in zip(xs,ys))/variance) if variance else 0
        intercept=max(0,my-slope*mx)
        alpha=sum(r['n_accepted'] for r in rows)/sum(r['n_examined'] for r in rows)
        overhead=mean(r['cloud_queue_ms']+r['serialize_ms']+r['deserialize_ms'] for r in rows)
        best,candidates=estimate(alpha,mean(r['draft_token_ms'] for r in rows),mean(r['network_rtt_ms'] for r in rows),intercept+overhead,slope,c['GAMMA_MIN'],c['GAMMA_MAX'])
        gs=sorted({r['configured_gamma'] for r in group})
        actual=max(gs,key=lambda g:mean(r['tokens_per_second'] for r in group if r['configured_gamma']==g))
        estimates.append(dict(scenario=scenario,estimated=best,measured_grid_best=actual,error=best-actual,candidates=candidates))
    (root/'tables/window_estimates.json').write_text(json.dumps(estimates,indent=2),encoding='utf-8')
    fig,ax=plt.subplots(figsize=(8,5))
    ax.plot([c['NETWORK_SCENARIOS'][s]['rtt_ms'] for s in steady],
            [next(e['estimated'] for e in estimates if e['scenario']==s) for s in steady],'o-',label='Mathematical estimate')
    ax.plot([c['NETWORK_SCENARIOS'][s]['rtt_ms'] for s in steady],
            [next(e['measured_grid_best'] for e in estimates if e['scenario']==s) for s in steady],'s--',label='Best in measured sweep grid')
    ax.set(title='RTT vs best draft window (strict policy)',xlabel='Configured RTT (ms)',ylabel='Gamma');ax.legend()
    save(fig,'rtt_best_gamma')
    fig,ax=plt.subplots(figsize=(9,5));ax.bar(scenarios,[e['error'] for e in estimates],label='Estimated minus grid best')
    ax.axhline(0,color='black',linewidth=.7);ax.set(title='Window estimation error (sampled-grid reference)',xlabel='Network scenario',ylabel='Gamma error');ax.legend()
    save(fig,'window_error')

    fig,axes=plt.subplots(1,3,figsize=(14,4))
    for ax,stat in zip(axes,('mean','p95','p99')):
        for mi,method in enumerate(('A','B','C','Proposed')):
            ys=[mean(r['round_latency'][stat] for r in base if r['method']==method and r['scenario']==s) for s in scenarios]
            ax.bar([i+mi*.2 for i in range(len(scenarios))],ys,width=.2,label=method)
        ax.set_xticks([i+.3 for i in range(len(scenarios))],scenarios,rotation=45)
        ax.set(title=f'Mean of per-request round {stat}',xlabel='Network scenario',ylabel='Round latency (ms)')
    axes[0].legend(fontsize=8);save(fig,'latency_percentiles')

    fig,ax=plt.subplots(figsize=(9,5))
    for s in scenarios:
        pts=[]
        for method in ('A','B','C','Proposed'):
            group=[r for r in base if r['scenario']==s and r['method']==method]
            q=mean(r[qkey] for r in group); speed=mean(r['tokens_per_second'] for r in group)
            pts.append((q,speed,method));ax.scatter(q,speed,s=30)
        front=sorted(p for p in pts if not any(q<=p[0] and v>=p[1] and (q<p[0] or v>p[1]) for q,v,_ in pts))
        ax.plot([p[0] for p in front],[p[1] for p in front],'o-',label=s)
    ax.set(title='Quality-speed Pareto fronts within each scenario',xlabel=qlabel,ylabel='Throughput (tokens/s)');ax.legend(fontsize=8)
    save(fig,'quality_speed_pareto')

    fig,axes=plt.subplots(5,1,figsize=(10,13),sharex=True)
    labels=['K','Gamma','RTT estimate (ms)','Accepted / examined','Quality risk']
    for s in scenarios:
        rec=next(r for r in base if r['method']=='Proposed' and r['scenario']==s and r['repeat']==0 and r['request_index']==0)
        rows=rec['rounds']; elapsed=[]; t=0
        for r in rows: t+=r['round_total_ms'];elapsed.append(t/1000)
        values=[[r['k'] for r in rows],[r['gamma'] for r in rows],[r['network_rtt_ms'] for r in rows],
                [r['n_accepted']/max(1,r['n_examined']) for r in rows],[r['controller']['quality_risk'] for r in rows]]
        for ax,label,ys in zip(axes,labels,values):ax.plot(elapsed,ys,label=s);ax.set_ylabel(label)
    axes[0].set_title('Joint controller trace: first request / first repeat');axes[0].legend(ncol=4,fontsize=8)
    axes[-1].set_xlabel('Elapsed decode time (s)');save(fig,'controller_trace')
    print(f'Generated 11 PNG + 11 SVG plots in {out}')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('directory')
    make_figures(parser.parse_args().directory)
