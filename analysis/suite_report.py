"""Bilingual, source-derived summary for a complete or failed experiment suite."""
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import random
from statistics import mean

from common.metrics import percentile
from experiments.run import write_csv, write_json


def report(root):
    plan=json.loads((root/'config/plan.json').read_text())
    status=json.loads((root/'report/suite_status.json').read_text())
    records=[];manifest=[]
    for path in sorted((root/'runs').glob('*/raw/*.json')):
        raw=path.read_bytes();r=json.loads(raw)
        if 'method' not in r:continue
        records.append(r);manifest.append(dict(path=str(path.relative_to(root)),sha256=hashlib.sha256(raw).hexdigest()))
    write_json(root/'config/raw_manifest.json',manifest)
    groups=defaultdict(list)
    for r in records:groups[r['scenario'],r['method']].append(r)
    table=[]
    for (scenario,method),rows in sorted(groups.items()):
        scores=[r['task_quality'] for r in rows if r.get('task_quality') is not None]
        table.append(dict(scenario=scenario,method=method,requests=len(rows),
            tps=mean(r['tokens_per_second'] for r in rows),latency_s=mean(r['wall_time_s'] for r in rows),
            quality=mean(scores) if scores else None,truncations=sum(bool(r.get('truncated')) for r in rows)))
    pairs=[]
    for scenario in plan['scenarios']:
        for candidate,control in [('Lookahead','A'),('B','A'),('C','A'),('D','B'),('Proposed','B'),('Proposed','D')]:
            maps={m:{(r['request_index'],r['repeat']):r for r in records if r['method']==m and r['scenario']==scenario} for m in (candidate,control)}
            clustered=defaultdict(list)
            for key in sorted(maps[candidate].keys() & maps[control].keys()):
                a,b=maps[control][key],maps[candidate][key]
                clustered[key[0]].append(b['tokens_per_second']/a['tokens_per_second']-1)
            values=[mean(v) for v in clustered.values()]
            if not values:continue
            rng=random.Random(42)
            boot=[mean(rng.choices(values,k=len(values))) for _ in range(2000)] if plan['mode']=='real' and len(values)>1 else []
            pairs.append(dict(scenario=scenario,candidate=candidate,control=control,gain=mean(values),
                ci95_low=percentile(boot,.025) if boot else None,ci95_high=percentile(boot,.975) if boot else None,
                prompts=len(values),pairs=sum(len(v) for v in clustered.values())))
    if table:write_csv(root/'tables/methods.csv',table)
    if pairs:write_csv(root/'tables/comparisons.csv',pairs)
    complete=status['exit_code']==0 and len(records)==plan['expected_requests']
    if table:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        methods=list(dict.fromkeys(r['method'] for r in table))
        scenarios=list(plan['scenarios']);width=.8/max(1,len(scenarios))
        fig,ax=plt.subplots(figsize=(10,4))
        for j,scenario in enumerate(scenarios):
            values=[next((r['tps'] for r in table if r['method']==m and r['scenario']==scenario),float('nan')) for m in methods]
            ax.bar([i+j*width for i in range(len(methods))],values,width=width,label=scenario)
        ax.set_xticks([i+(len(scenarios)-1)*width/2 for i in range(len(methods))],methods,rotation=20)
        ax.set_ylabel('Tokens/s');ax.set_title(f'{plan["model_pair"]} / {plan["mode"]} / {plan["profile"]}');ax.legend()
        fig.tight_layout()
        fig.savefig(root/'figures/throughput.png',dpi=150);fig.savefig(root/'figures/throughput.svg');plt.close(fig)
    write_json(root/'report/summary.json',dict(complete=complete,completed=len(records),expected=plan['expected_requests'],methods=table,comparisons=pairs))
    lines=[]
    for english in (False,True):
        lines += ['# English summary' if english else '# 中文实验汇报','',
            f'Mode: {plan["mode"]}; model pair: {plan["model_pair"]}; profile: {plan["profile"]}.' if english else
            f'模式：{plan["mode"]}；模型对：{plan["model_pair"]}；实验规模：{plan["profile"]}。',
            f'{"Complete" if complete else "INCOMPLETE"}: {len(records)}/{plan["expected_requests"]} requests.' if english else
            f'{"已完成" if complete else "未完整完成，请检查 logs/run.log"}：{len(records)}/{plan["expected_requests"]} 次请求。','',
            'A: strict/fixed γ; B: strict/adaptive γ; C: fixed K/fixed γ; D: fixed K/adaptive γ; Proposed: adaptive K/γ; Lookahead: A plus fixed h.' if english else
            'A：严格接受＋固定 γ；B：严格接受＋自适应 γ；C：固定 K＋固定 γ；D：固定 K＋自适应 γ；Proposed：联合自适应 K/γ；Lookahead：A 加固定提前草拟 h。','',
            '| Scenario | Method | N | Tokens/s | Latency (s) | Task accuracy | Truncated |' if english else
            '| 场景 | 方案 | 请求数 | token/s | 延迟/秒 | 任务正确率 | 截断数 |',
            '|---|---|---:|---:|---:|---:|---:|']
        for r in table:
            score='N/A' if r['quality'] is None else f'{r["quality"]:.1%}'
            lines.append(f'| {r["scenario"]} | {r["method"]} | {r["requests"]} | {r["tps"]:.3f} | {r["latency_s"]:.3f} | {score} | {r["truncations"]} |')
        lines += ['', 'Paired throughput comparisons:' if english else '配对吞吐比较：','']
        for r in pairs:
            interval='N/A' if r['ci95_low'] is None else f'[{r["ci95_low"]:.2%}, {r["ci95_high"]:.2%}]'
            lines.append(f'- {r["scenario"]}: {r["candidate"]} / {r["control"]}: {r["gain"]:+.2%}; 95% CI {interval}; n={r["prompts"]}.')
        lines += ['', 'Interpretation:' if english else '结论解读：','']
        if not complete or plan['mode']!='real' or plan['profile']=='smoke':
            lines.append('Validation/incomplete run only; no measured speedup conclusion.' if english else '本轮属于流程检查、模拟或不完整运行，不作真实加速结论。')
        else:
            for r in pairs:
                positive=r['ci95_low'] is not None and r['ci95_low']>0 and r['gain']>=.05
                text=('Exploratory speed benefit; check task accuracy before adoption.' if positive else 'A stable ≥5% speed benefit is not established.') if english else ('有探索性的速度收益，采用前仍需检查任务正确率。' if positive else '尚未建立稳定且达到 5% 的速度收益。')
                lines.append(f'- {r["scenario"]} {r["candidate"]}/{r["control"]}: {text}')
        if table:lines += ['', '![Throughput](figures/throughput.png)']
        lines += ['',
            'Intervals cluster repetitions by prompt. Small pilots do not prove generalization or quality noninferiority. No direct-cloud speed comparison.' if english else
            '区间按独立题目聚类计算，重复次数不等于独立样本量。小样本不能证明泛化或质量非劣性；不比较直接云端生成速度。',
            'Simulation validates the pipeline only; lookahead is intentionally excluded. Smoke output may be truncated and is not a performance conclusion.' if english else
            'simulate 仅用于流程验证，不模拟提前草拟加速；smoke 是连通性检查，短输出可能截断，不能据此下性能结论。',
            'Delays are injected on top of the actual network. End-to-end lookahead time includes orphan-work drain.' if english else
            '网络参数是额外注入延迟；提前草拟端到端耗时包含后台任务收尾。',
            'Raw records: runs/*/raw; configuration and source snapshot: config; derived tables: tables.' if english else
            '原始数据：runs/*/raw；配置与代码快照：config；汇总表：tables。','']
    (root/'SUMMARY.md').write_text('\n'.join(lines),encoding='utf-8')
