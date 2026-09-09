"""Central experiment configuration; all times are milliseconds."""
import json
import math
import warnings
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# 这里只声明必填参数名称，不在此处赋值。
# 实际值填写在 configs/my-experiment.json，例如："K_MAX": 4。
# 以下注释中的数值仅为实验示例，不代表最终推荐参数。
REQUIRED = [
    'K_MIN',                   # K 下限；必须为 1。示例："K_MIN": 1
    'K_MAX',                   # K 上限。示例："K_MAX": 4
    'K_INITIAL',               # 初始 K。示例："K_INITIAL": 1
    'QUALITY_BUDGET',          # 单请求累计 regret 预算（nats）。示例：0.5
    'MAX_LOGPROB_REGRET',      # 单 token regret 上限（nats）。示例：0.2
    'MIN_PROBABILITY_RATIO',   # 候选概率 / top-1 概率下限。示例：0.82
    'TARGET_ACCEPTANCE_RATE',  # 目标接受率。示例：0.9
    'QUALITY_EVAL_INTERVAL',   # 质量评估间隔（轮）。示例：4
    'QUALITY_WINDOW_SIZE',     # 质量统计窗口（token 决策数）。示例：32
    'GAMMA_MIN',               # 草稿窗口下限（token）。示例：1
    'GAMMA_MAX',               # 草稿窗口上限（token）。示例：8
    'GAMMA_INITIAL',           # 初始草稿窗口（token）。示例：2
    'ESTIMATION_WINDOW_SIZE',  # 延迟/接受率统计窗口（轮）。示例：32
    'WINDOW_UPDATE_INTERVAL',  # 草稿窗口更新间隔（轮）。示例：2
    'WINDOW_CHANGE_STEP',      # 每次窗口最大变化量（token）。示例：1
    'WINDOW_HYSTERESIS',       # 更新窗口所需的相对吞吐收益。示例：0.05（5%）
]


def validate(c):
    missing = [k for k in REQUIRED if c.get(k) is None]
    if missing:
        raise ValueError('请填写实验配置参数: ' + ', '.join(missing))
    integers = [k for k in REQUIRED if k not in {
        'QUALITY_BUDGET', 'MAX_LOGPROB_REGRET', 'MIN_PROBABILITY_RATIO',
        'TARGET_ACCEPTANCE_RATE', 'WINDOW_HYSTERESIS'}]
    integers += ['SEED', 'MIN_ESTIMATION_SAMPLES', 'K_UPDATE_INTERVAL', 'K_CHANGE_STEP']
    for k in integers:
        if type(c[k]) is not int or c[k] < (0 if k == 'SEED' else 1):
            raise ValueError(f'{k} must be a positive integer (SEED may be zero)')
    for k, v in c.items():
        if isinstance(v, (float, int)) and (not math.isfinite(v) or v < 0):
            raise ValueError(f'{k} must be finite and nonnegative')
    for stem in ('K', 'GAMMA'):
        if not c[stem+'_MIN'] <= c[stem+'_INITIAL'] <= c[stem+'_MAX']:
            raise ValueError(f'{stem}_MIN <= {stem}_INITIAL <= {stem}_MAX required')
    if c['K_MIN'] != 1:
        raise ValueError('K_MIN must be 1 to allow quality-budget tightening')
    for k in ('MIN_PROBABILITY_RATIO', 'TARGET_ACCEPTANCE_RATE', 'WINDOW_HYSTERESIS',
              'MIN_TOP1_CONFIDENCE', 'BUDGET_TIGHTEN_FRACTION', 'RISK_TIGHTEN_THRESHOLD'):
        if not 0 <= c[k] <= 1:
            raise ValueError(f'{k} must be in [0, 1]')
    if c['MIN_ESTIMATION_SAMPLES'] > c['ESTIMATION_WINDOW_SIZE']:
        raise ValueError('MIN_ESTIMATION_SAMPLES exceeds ESTIMATION_WINDOW_SIZE')
    if c['REQUEST_TIMEOUT_S'] <= 0 or c['RTT_HIGH_MS'] <= 0:
        raise ValueError('Timeout and RTT_HIGH_MS must be positive')
    for k in ('N_REQUESTS','MAX_TOKENS','REPEATS','FIXED_K'):
        if type(c[k]) is not int or c[k] < 1:
            raise ValueError(f'{k} must be a positive integer')
    if not c['K_MIN'] <= c['FIXED_K'] <= c['K_MAX']:
        raise ValueError('FIXED_K outside K bounds')
    for key, lo, hi in [('GAMMA_SWEEP',c['GAMMA_MIN'],c['GAMMA_MAX']), ('K_SWEEP',c['K_MIN'],c['K_MAX'])]:
        if not c[key] or any(type(x) is not int or not lo <= x <= hi for x in c[key]):
            raise ValueError(f'{key} contains invalid candidates')
    if not 0 < c['SIM_TOP2_PROBABILITY'] <= c['SIM_TOP1_PROBABILITY'] < 1 or c['SIM_TOP1_PROBABILITY']+c['SIM_TOP2_PROBABILITY'] >= 1:
        raise ValueError('Invalid synthetic model probabilities')
    if not 0 <= c['SIM_DRAFT_ACCURACY'] <= 1:
        raise ValueError('Invalid SIM_DRAFT_ACCURACY')
    if not c['NETWORK_SCENARIOS']:
        raise ValueError('Network scenarios cannot be empty')
    allowed={'rtt_ms','jitter_ms','bandwidth_mbps','burst_at','burst_ms','queue_ms','queue_jitter_ms'}
    for name, scenario in c['NETWORK_SCENARIOS'].items():
        if set(scenario)-allowed or 'rtt_ms' not in scenario or any(type(v) not in (int,float) or not math.isfinite(v) or v<0 for v in scenario.values()):
            raise ValueError(f'Invalid network scenario: {name}')
        if 'bandwidth_mbps' in scenario and scenario['bandwidth_mbps'] <= 0:
            raise ValueError(f'Bandwidth must be positive: {name}')
    return c


def load_config(path=None):
    base = json.loads((ROOT / 'configs/experiment.defaults.json').read_text(encoding='utf-8'))
    if path:
        overrides = json.loads(Path(path).read_text(encoding='utf-8'))
        unknown = set(overrides) - set(base)
        if unknown:
            raise ValueError('Unknown configuration keys: ' + ', '.join(sorted(unknown)))
        base.update(overrides)
    if base['EXPERIMENT_DEFAULTS']:
        warnings.warn('使用保守的实验默认值；这些值不是最终推荐参数。', UserWarning)
    return validate(base)
