"""Offline quality evaluation; never execute generated code on the host."""
import re
from decimal import Decimal, InvalidOperation
from difflib import SequenceMatcher


def difference_rate(reference, output):
    return 1-SequenceMatcher(None,reference,output,autojunk=False).ratio()


def numeric_answer(text):
    matches=re.findall(r'(?:Final answer\s*:|####)\s*\$?(-?[\d,]+(?:\.\d+)?)',text,re.I)
    if not matches:
        return None
    try:
        return Decimal(matches[-1].replace(',',''))
    except InvalidOperation:
        return None


def task_quality(task, output, example):
    if task != 'gsm8k':
        return None  # HumanEval needs an isolated evaluator; MT-Bench needs a judge.
    predicted=numeric_answer(output)
    gold=example.get('gold_answer')
    if gold is None or predicted is None:
        return 0.0
    return float(predicted == Decimal(str(gold).replace(',','')))


def evaluate_quality(task, output, example, stop_reason):
    """Keep benchmark accuracy separate from completion/extraction diagnostics."""
    extracted = numeric_answer(output) is not None if task == 'gsm8k' else None
    score = task_quality(task, output, example)
    status = ('unsupported' if score is None else
              'correct' if score == 1 else
              'incorrect' if extracted else
              'incomplete' if stop_reason == 'length' else 'answer_not_extracted')
    return dict(task_quality=score, answer_extracted=extracted,
                quality_status=status, stop_reason=stop_reason,
                truncated=stop_reason == 'length')


def first_divergence(reference, output):
    for index, (expected, actual) in enumerate(zip(reference, output)):
        if expected != actual:
            return index
    return min(len(reference), len(output)) if len(reference) != len(output) else None
