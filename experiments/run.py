"""One-command experiment pipeline. Explicit synthetic or real-service mode."""
import argparse
import csv
import hashlib
import importlib.metadata
import json
import platform
import random
import subprocess
import sys
import traceback
import uuid
from statistics import mean
from datetime import datetime
from pathlib import Path
from common.experiment_config import ROOT, load_config
from common.metrics import LABELS, summary
from common.quality import difference_rate
from common.simulation import run_simulation


def write_json(path,data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf-8')


def create_output(root):
    # Windows wall clocks can give concurrent runs the same microsecond label.
    out=Path(root)/(datetime.now().strftime('%Y%m%d_%H%M%S_%f')+'_'+uuid.uuid4().hex[:8])
    out.mkdir(parents=True,exist_ok=False)
    for folder in ('config','raw','logs','tables','figures','report'):
        (out/folder).mkdir()
    return out


def write_csv(path,rows):
    if not rows:
        raise ValueError(f'No data for {path}')
    fields=list(dict.fromkeys(k for row in rows for k in row))
    with path.open('w',newline='',encoding='utf-8-sig') as f:
        writer=csv.DictWriter(f,fieldnames=fields); writer.writeheader()
        for row in rows:
            writer.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in row.items()})


def variants(c):
    g=c['GAMMA_INITIAL']; k=c['FIXED_K']
    result=[('baseline','A','strict',False,g,1),('baseline','B','strict',True,g,1),
            ('baseline','C','fixed',False,g,k),('baseline','Proposed','adaptive',True,g,None)]
    result += [('gamma_sweep',f'gamma_{g}','strict',False,g,1) for g in c['GAMMA_SWEEP']]
    result += [('k_sweep',f'k_{k}','fixed',False,g,k) for k in c['K_SWEEP']]
    return result


def enrich(record):
    rows=record['rounds']; examined=sum(r['n_examined'] for r in rows)
    record['strict_acceptance_rate']=sum(r['strict_accepted'] for r in rows)/max(1,examined)
    record['relaxed_acceptance_rate']=sum(r['n_accepted'] for r in rows)/max(1,examined)
    record['relaxed_only_rate']=sum(r['relaxed_only'] for r in rows)/max(1,examined)
    record['accepted_proposed_ratio']=sum(r['n_accepted'] for r in rows)/max(1,sum(r['n_proposed'] for r in rows))
    record['text_difference_rate']=difference_rate(record['reference_text'],record['output_text'])
    record['token_difference_rate']=difference_rate(record['reference_ids'],record['output_ids'])
    record['task_quality_drop']=(record['reference_quality']-record['task_quality']) if record['task_quality'] is not None else None
    record['round_latency']=summary([r['round_total_ms'] for r in rows])
    return record


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config')
    parser.add_argument('--mode',choices=['simulate','real'],default='simulate')
    parser.add_argument('--output-root',default='results')
    parser.add_argument('--verbose-tokens',action='store_true')
    parser.add_argument('--verbose-rounds',action='store_true')
    args=parser.parse_args(argv)
    out=create_output(args.output_root)
    failures=[]; records=[]; checks=[]
    try:
        c=load_config(args.config); c['VERBOSE_TOKENS'] |= args.verbose_tokens
        c['VERBOSE_ROUNDS'] |= args.verbose_rounds
        write_json(out/'config/resolved.json',c)
        environment={'mode':args.mode,'python':sys.version,'platform':platform.platform(),
                     'packages':{p:importlib.metadata.version(p) for p in ('requests','matplotlib','numpy','fastapi','uvicorn','httpx')},
                     'hardware_conditions':'synthetic virtual time' if args.mode=='simulate' else 'externally managed; record device/load with service deployment'}
        for name,cmd in [('git_status',['git','status','--short']),('git_head',['git','rev-parse','HEAD'])]:
            result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace')
            environment[name]=result.stdout
        write_json(out/'config/environment.json',environment)
        for name,cmd in [('static',[sys.executable,'-m','experiments.static_check']),
                         ('unit',[sys.executable,'-m','unittest','discover','-s','tests','-p','test_core.py','-v']),
                         ('integration',[sys.executable,'-m','unittest','discover','-s','tests','-p','test_integration.py','-v'])]:
            p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace')
            (out/'logs'/f'{name}.log').write_text(p.stdout+p.stderr,encoding='utf-8')
            checks.append({'stage':name,'exit_code':p.returncode})
            if p.returncode: failures.append({'stage':name,'error':f'See logs/{name}.log'})
        if failures:
            raise RuntimeError('Required checks failed; experiments not run')
        live=None
        if args.mode=='real':
            from edge.experiment_live import LiveExperiment
            live=LiveExperiment(c)
            write_json(out/'config/service_info.json',live.info)
        dataset_path=ROOT/c['DATASET']
        data=dataset_path.read_bytes()
        samples=[json.loads(line) for line in data.decode('utf-8').splitlines() if line.strip()][:c['N_REQUESTS']]
        if not samples: raise ValueError('Dataset contains no requests')
        write_json(out/'config/requests.json',samples)
        write_json(out/'config/dataset.json',{'path':c['DATASET'],'sha256':hashlib.sha256(data).hexdigest(),
                                            'used_by_model':args.mode=='real',
                                            'note':'Synthetic mode uses request indices, not natural language content'})
        jobs=[]
        for scenario_name,scenario in c['NETWORK_SCENARIOS'].items():
            for repeat in range(c['REPEATS']):
                group=variants(c)
                random.Random(c['SEED']+repeat).shuffle(group)
                for study,method,strategy,adaptive,gamma,k in group:
                    for index,ex in enumerate(samples):
                        jobs.append((scenario_name,scenario,repeat,study,method,strategy,adaptive,gamma,k,index,ex))
        for scenario_name,scenario,repeat,study,method,strategy,adaptive,gamma,k,index,ex in jobs:
            name=f'{scenario_name}_{repeat}_{method}_{index}'
            try:
                record=(live.run(strategy,adaptive,gamma,k,ex,index,scenario) if live else
                        run_simulation(c,strategy,adaptive,gamma,k,index,scenario))
                record.update(id=name,mode=args.mode,study=study,method=method,scenario=scenario_name,
                              configured_rtt_ms=scenario['rtt_ms'],repeat=repeat,request_index=index,
                              configured_gamma=gamma,configured_k=k,adaptive_window=adaptive)
                enrich(record); records.append(record)
                write_json(out/'raw'/f'{name}.json',record)
                if c['VERBOSE_ROUNDS']:
                    for row in record['rounds']:
                        print(f"[{name} round={row['round_index']}] K={row['k']} gamma={row['gamma']} "
                              f"RTT~{row['network_rtt_ms']:.3f}ms queue={row['cloud_queue_ms']:.3f}ms "
                              f"verify={row['cloud_verify_ms']:.3f}ms total={row['round_total_ms']:.3f}ms")
                if c['VERBOSE_TOKENS'] and args.mode=='simulate':
                    for row in record['rounds']: print(json.dumps(row['decisions'],ensure_ascii=False))
            except Exception as exc:
                failures.append({'stage':name,'error':str(exc)})
                (out/'logs'/f'{name}.log').write_text(traceback.format_exc(),encoding='utf-8')
        if not records: raise RuntimeError('No successful experiments; no charts generated')
        table=[{k:v for k,v in r.items() if k not in ('rounds','output_ids','reference_ids','output_text','reference_text')} for r in records]
        write_csv(out/'tables/requests.csv',table)
        rounds=[dict(r,experiment_id=record['id'],method=record['method'],scenario=record['scenario']) for record in records for r in record['rounds']]
        write_csv(out/'tables/rounds.csv',rounds)
        statistics={}
        for metric,label in LABELS.items():
            source=records if metric in ('ttft_ms','tpot_ms','tokens_per_second') else rounds
            values=[r[metric] for r in source if r.get(metric) is not None]
            if values: statistics[metric]=dict(label=label,**summary(values))
        write_json(out/'tables/latency_summary.json',statistics)
        write_csv(out/'tables/latency_summary.csv',[dict(metric=k,**v) for k,v in statistics.items()])
        # Keep comparisons separate by scenario/method/study, never aggregate unlike schemes.
        grouped=[]
        for key in sorted({(r['study'],r['scenario'],r['method']) for r in records}):
            group=[r for r in records if (r['study'],r['scenario'],r['method'])==key]
            for metric in LABELS:
                if metric in ('ttft_ms','tpot_ms','tokens_per_second'):
                    continue
                values=[row[metric] for r in group for row in r['rounds'] if row.get(metric) is not None]
                if values: grouped.append(dict(study=key[0],scenario=key[1],method=key[2],metric=metric,**summary(values)))
            for metric in ('tokens_per_second','ttft_ms','tpot_ms','strict_acceptance_rate','relaxed_acceptance_rate','token_difference_rate','task_quality_drop'):
                values=[r[metric] for r in group if r[metric] is not None]
                if values: grouped.append(dict(study=key[0],scenario=key[1],method=key[2],metric=metric,**summary(values)))
        write_csv(out/'tables/comparison.csv',grouped)
        print(f'Completed {len(records)} requests; {len(failures)} failures. Mode={args.mode}')
        for key,v in statistics.items(): print(f"{v['label']}: mean={v['mean']:.3f}, P95={v['p95']:.3f}, P99={v['p99']:.3f}")
        from analysis.make_figures import make_figures
        make_figures(out)
    except Exception as exc:
        failures.append({'stage':'pipeline','error':str(exc)})
        (out/'logs/pipeline.log').write_text(traceback.format_exc(),encoding='utf-8')
        print(f'ERROR: {exc}',file=sys.stderr)
    finally:
        write_json(out/'report/status.json',{'mode':args.mode,'checks':checks,'successful_requests':len(records),'failures':failures})
        report=['# 云边推测解码实验报告', '', f'模式：**{args.mode}**。'+('本报告全部性能与模型输出来自合成模型和虚拟时间，不是真实 GPU/LLM 实验。' if args.mode=='simulate' else '真实服务，网络条件为应用层延迟注入；不是操作系统流量整形。'),
                '',f'成功请求：{len(records)}；失败项：{len(failures)}。',
                '', '基线 A：严格+固定窗口；B：严格+自适应窗口；C：受质量约束的固定 K+固定窗口；Proposed：联合自适应。',
                '', '质量预算只约束累计 logprob regret，不能保证任务准确率。合成模式 task_quality_drop 为空；使用明确标注的 token 差异率绘图。',
                '', '每轮原始决策见 ../raw/；请求、轮次、各方案分组统计见 ../tables/；PNG/SVG 见 ../figures/。',
                '', 'TTFT 含模板和分词；TPOT 为验证批次对外可见的 token 时间间隔均值，同批 token 的间隔为零。非流式 API 返回文本的时间不同于这里的首批可用时间。',
                '', '模拟各方案使用同一合成模型、种子、请求索引、网络函数；重复运行用于管线验证，不代表独立统计样本。真实运行按固定种子打乱方案顺序，但硬件负载与缓存仍需外部控制。',
                '', '## 检查结果', *[f"- {x['stage']}: exit {x['exit_code']}" for x in checks],
                '', '## 失败项', *([f"- {f['stage']}: {f['error']}" for f in failures] or ['无。'])]
        if records:
            report += ['', '## 基线比较（各请求等权平均）', '',
                       '| 场景 | 方案 | tokens/s | TTFT ms | Token差异率 | 任务质量下降 |',
                       '|---|---|---:|---:|---:|---:|']
            for scenario,method in sorted({(r['scenario'],r['method']) for r in records if r['study']=='baseline'}):
                group=[r for r in records if r['study']=='baseline' and r['scenario']==scenario and r['method']==method]
                qualities=[r['task_quality_drop'] for r in group if r['task_quality_drop'] is not None]
                quality=f'{mean(qualities):.4f}' if qualities else 'N/A'
                report.append(f"| {scenario} | {method} | {mean(r['tokens_per_second'] for r in group):.3f} | {mean(r['ttft_ms'] for r in group):.3f} | {mean(r['token_difference_rate'] for r in group):.4f} | {quality} |")
            report += ['', '模拟中的序列化/反序列化设为零，表示未建模；真实 HTTP 测试与真实服务模式使用 perf_counter 测量。',
                       '', '## 图表', '', *[f'![{p.stem}](../figures/{p.name})' for p in sorted((out/'figures').glob('*.png'))]]
        (out/'report/report.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
        print(f'Artifacts: {out.resolve()}')
    return int(bool(failures))


if __name__=='__main__': sys.exit(main())
