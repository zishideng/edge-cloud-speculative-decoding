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
