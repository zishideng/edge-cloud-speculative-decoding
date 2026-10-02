"""One-command compact SD suite with a bilingual final report."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import traceback

from common.experiment_config import ROOT, load_config, validate
from common.model_config import load_model_config
from experiments.run import create_output, write_json
from analysis.suite_report import report


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mode',choices=['real','simulate'],default='simulate')
    ap.add_argument('--profile',choices=['quick','smoke','full'],default='quick')
    ap.add_argument('--config')
    ap.add_argument('--model-pair')
    ap.add_argument('--models-yaml')
    ap.add_argument('--draft-url');ap.add_argument('--cloud-url')
    ap.add_argument('--n',type=int);ap.add_argument('--repeats',type=int)
    ap.add_argument('--max-tokens',type=int);ap.add_argument('--gamma',type=int)
    ap.add_argument('--gamma-lookahead-sweep', nargs='+', type=int, help='Paired fixed gamma and lookahead h=gamma+1 sweep')
    ap.add_argument('--lookahead',type=int,default=5)
    ap.add_argument('--request-offset',type=int,default=0)
    ap.add_argument('--output-root',default='results/suites')
    ap.add_argument('--plan',action='store_true',help='Show resolved plan without running services')
    ap.add_argument('--verbose-tokens',action='store_true');ap.add_argument('--verbose-rounds',action='store_true')
    args=ap.parse_args(argv)
    os.chdir(ROOT)
    c=load_config()
    if args.profile!='full':
        c.update(N_REQUESTS=4,REPEATS=2,GAMMA_INITIAL=4,MAX_TOKENS=512,
                 NETWORK_SCENARIOS={'low':{'rtt_ms':2,'jitter_ms':0},'high':{'rtt_ms':100,'jitter_ms':0}})
    if args.profile=='smoke':
        c.update(N_REQUESTS=1,REPEATS=1,MAX_TOKENS=64,NETWORK_SCENARIOS={'low':{'rtt_ms':2,'jitter_ms':0}})
    if args.config:
        load_config(args.config)  # Reject unknown/invalid config keys.
        c.update(json.loads(Path(args.config).read_text()))
    for name,key in [('n','N_REQUESTS'),('repeats','REPEATS'),('max_tokens','MAX_TOKENS'),('gamma','GAMMA_INITIAL'),
                     ('model_pair','MODEL_PAIR'),('draft_url','DRAFT_URL'),('cloud_url','CLOUD_URL')]:
        value=getattr(args,name)
        if value is not None:c[key]=value
    c['EXPERIMENT_DEFAULTS']=False
    validate(c)
    if args.lookahead<1 or args.request_offset<0:ap.error('lookahead must be positive; request-offset must be nonnegative')
    examples=[x for x in (ROOT/c['DATASET']).read_text().splitlines() if x.strip()]
    if args.request_offset+c['N_REQUESTS']>len(examples):ap.error('Requested prompt range exceeds dataset length')
    methods=['A','B']  # Window/lookahead study: all selected methods use strict K=1.
    if args.profile=='full':
        methods += [f'gamma_{g}' for g in c['GAMMA_SWEEP']]
    if args.mode=='real':methods.append('Lookahead')
    if args.gamma_lookahead_sweep:
        gs=list(dict.fromkeys(args.gamma_lookahead_sweep))
        if any(g < c['GAMMA_MIN'] or g > c['GAMMA_MAX'] for g in gs):
            ap.error('Sweep gamma outside configured bounds')
        c['GAMMA_SWEEP']=gs
        methods=[f'gamma_{g}' for g in gs]
        if args.mode=='real':methods += [f'Lookahead_g{g}' for g in gs]
    model=load_model_config(c['MODEL_PAIR'],args.models_yaml) if args.mode=='real' or args.models_yaml else None
    plan=dict(mode=args.mode,profile=args.profile,model_pair=c['MODEL_PAIR'],methods=methods,
        prompts=c['N_REQUESTS'],repeats=c['REPEATS'],scenarios=c['NETWORK_SCENARIOS'],gamma=c['GAMMA_INITIAL'],
        lookahead=args.lookahead,lookahead_by_method={m:int(m.split('_g')[1])+1 for m in methods if m.startswith('Lookahead_g')},request_offset=args.request_offset,
        expected_requests=len(methods)*c['N_REQUESTS']*c['REPEATS']*len(c['NETWORK_SCENARIOS']),
        note='Simulation excludes asynchronous lookahead: no synthetic overlap speed claim.')
    print(json.dumps(plan,ensure_ascii=False,indent=2),flush=True)
    if args.plan:return 0
    out=create_output(args.output_root)
    write_json(out/'config/plan.json',plan);write_json(out/'config/resolved.json',c)
    # Preserve the exact source tree and registry used, including uncommitted edits.
    for folder in ('common','cloud','edge','experiments','analysis','tests'):
        for path in (ROOT/folder).glob('*.py'):
            dest=out/'config/source'/folder/path.name;dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(path,dest)
    env=os.environ.copy()
    if model:
        registry=out/'config/models.yaml';shutil.copyfile(model['_yaml_path'],registry)
        env['SPECDECODE_MODELS_YAML']=str(registry.resolve())
        write_json(out/'config/model_pair.json',model)
    command=[sys.executable,'-m','experiments.run','--mode',args.mode,'--config',str(out/'config/resolved.json'),
        '--output-root',str(out/'runs'),'--request-offset',str(args.request_offset),'--lookahead',str(args.lookahead),'--methods',*methods]
    for flag in ('verbose_tokens','verbose_rounds'):
        if getattr(args,flag):command.append('--'+flag.replace('_','-'))
    write_json(out/'config/command.json',command)
    code=1
    try:
        print(f'总目录 / Suite: {out.resolve()}',flush=True)
        with (out/'logs/run.log').open('w') as log:
            process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,env=env)
            try:
                for line in process.stdout:
                    print(line,end='',flush=True);log.write(line);log.flush()
                code=process.wait()
            except KeyboardInterrupt:
                import signal
                process.send_signal(signal.SIGINT)
                process.wait(timeout=150)
                code=130
    except Exception:
        (out/'logs/suite_error.log').write_text(traceback.format_exc())
    finally:
        write_json(out/'report/suite_status.json',dict(exit_code=code,plan=plan))
        report(out)
        print(f'最终汇报 / Final report: {(out/"SUMMARY.md").resolve()}',flush=True)
    return code


if __name__=='__main__':
    raise SystemExit(main())
