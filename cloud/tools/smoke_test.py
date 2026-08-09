"""Local smoke test for verify_server. Run from H200 login node.

Tests three things:
1. /health  responds
2. /info    returns model details
3. /verify  produces sensible accept/reject on a hand-crafted case

For (3), we ask the target to verify a draft that is *almost certainly
correct* (continuing "The capital of France is" with " Paris"). We expect
≥1 accepted token. Then we test a *probably wrong* draft (continuing the
same prompt with " banana"). We expect 0 accepted tokens and a correction.
"""
import argparse
import json
import sys
import time

import requests
from transformers import AutoTokenizer


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", required=True, help="compute node hostname or IP")
    ap.add_argument("--port", type=int, default=9090)
    ap.add_argument("--target", default="meta-llama/Llama-3.1-8B-Instruct",
                    help="model id (for tokenizer)")
    args = ap.parse_args()

    base = f"http://{args.host}:{args.port}"
    print(f"==> Testing {base}")

    # 1. health
    r = requests.get(f"{base}/health", timeout=5)
    r.raise_for_status()
    print(f"  /health  → {r.json()}")

    # 2. info
    r = requests.get(f"{base}/info", timeout=5)
    r.raise_for_status()
    info = r.json()
    print(f"  /info    → model={info['target_model']}, vocab={info['vocab_size']}")

    # 3. verify — happy path
    tok = AutoTokenizer.from_pretrained(args.target)

    prompt_text = "The capital of France is"
    prompt_ids = tok(prompt_text, add_special_tokens=True)["input_ids"]

    # A draft that the 8B model should largely agree with
    good_draft_text = " Paris"
    good_draft_ids = tok(good_draft_text, add_special_tokens=False)["input_ids"]
    print(f"\n--- happy-path verify ---")
    print(f"  prompt:      '{prompt_text}'  ({len(prompt_ids)} tokens)")
    print(f"  draft:       '{good_draft_text}'  ({len(good_draft_ids)} tokens)")

    t0 = time.perf_counter()
    r = requests.post(f"{base}/verify", json={
        "prompt_ids": prompt_ids,
        "draft_ids": good_draft_ids,
        "temperature": 0.0,
    }, timeout=30)
    dt = (time.perf_counter() - t0) * 1000
    r.raise_for_status()
    resp = r.json()
    print(f"  → n_accepted={resp['n_accepted']}/{len(good_draft_ids)}, "
          f"bonus={resp['bonus_id']} ({tok.decode([resp['bonus_id']]) if resp['bonus_id'] is not None else ''}), "
          f"server={resp['verify_time_ms']:.1f}ms, RTT={dt:.1f}ms")
    assert resp["n_accepted"] >= 1, "expected at least 1 accept for 'Paris' continuation"

    # 4. verify — adversarial draft
    bad_draft_text = " banana muffin recipe"
    bad_draft_ids = tok(bad_draft_text, add_special_tokens=False)["input_ids"]
    print(f"\n--- adversarial verify ---")
    print(f"  draft:       '{bad_draft_text}'  ({len(bad_draft_ids)} tokens)")
    r = requests.post(f"{base}/verify", json={
        "prompt_ids": prompt_ids,
        "draft_ids": bad_draft_ids,
        "temperature": 0.0,
    }, timeout=30)
    r.raise_for_status()
    resp = r.json()
    print(f"  → n_accepted={resp['n_accepted']}/{len(bad_draft_ids)}, "
          f"correction_id={resp['bonus_id']} ({tok.decode([resp['bonus_id']]) if resp['bonus_id'] is not None else ''})")
    assert resp["n_accepted"] < len(bad_draft_ids), \
        "expected at least one rejection for nonsense draft"

    print("\n==> All smoke tests passed.")


if __name__ == "__main__":
    main()
