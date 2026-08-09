"""model_config.py — load model-pair config + validate draft/target vocab.

Usage in a bench script:
    from common.model_config import load_model_config, validate_pair

    cfg = load_model_config(args.model_config)      # dict from models.yaml
    eos_id = cfg["eos_id"]
    # after creating client + verifier:
    validate_pair(client, verifier, cfg)            # raises on mismatch

Config resolution order for the yaml path:
    1. --models-yaml arg if the caller passes one
    2. $SPECDECODE_MODELS_YAML
    3. ./models.yaml, ../models.yaml (repo root from src/)
"""
from __future__ import annotations
import os
import sys
from typing import Dict, Any, Optional

try:
    import yaml
except ImportError:
    yaml = None


def _find_yaml(explicit: Optional[str] = None) -> str:
    cands = []
    if explicit:
        cands.append(explicit)
    if os.environ.get("SPECDECODE_MODELS_YAML"):
        cands.append(os.environ["SPECDECODE_MODELS_YAML"])
    cands += ["configs/models.yaml", "../configs/models.yaml",
              os.path.join(os.path.dirname(__file__), "..", "configs", "models.yaml"),
              "models.yaml", "../models.yaml"]
    for c in cands:
        if c and os.path.exists(c):
            return c
    raise FileNotFoundError(
        "models.yaml not found. Looked in: " + ", ".join(str(c) for c in cands)
        + "\nPass --models-yaml or set SPECDECODE_MODELS_YAML."
    )


def load_model_config(name: str, models_yaml: Optional[str] = None) -> Dict[str, Any]:
    """Return the config dict for the named model pair."""
    if yaml is None:
        raise ImportError("pyyaml not installed. `pip install pyyaml`")
    path = _find_yaml(models_yaml)
    with open(path) as f:
        reg = yaml.safe_load(f)
    if name not in reg:
        raise KeyError(
            f"Model config '{name}' not in {path}. "
            f"Available: {', '.join(reg.keys())}"
        )
    cfg = reg[name]
    # required fields
    for k in ("target", "draft_gguf", "eos_id", "vocab_size"):
        if k not in cfg:
            raise KeyError(f"Model config '{name}' missing required field '{k}'")
    cfg["_name"] = name
    cfg["_yaml_path"] = path
    return cfg


def get_draft_vocab(client) -> Optional[int]:
    """Read the draft model's vocab size from llama.cpp /props, if exposed."""
    try:
        props = client.props()
    except Exception:
        return None
    # llama.cpp exposes vocab under a few possible keys depending on version
    for path in (
        ("default_generation_settings", "n_vocab"),
        ("n_vocab",),
        ("model", "n_vocab"),
    ):
        d = props
        ok = True
        for k in path:
            if isinstance(d, dict) and k in d:
                d = d[k]
            else:
                ok = False
                break
        if ok and isinstance(d, int):
            return d
    return None


def get_target_vocab(verifier) -> Optional[int]:
    """Read target vocab via the verify_server /info endpoint."""
    try:
        import requests
        r = requests.get(f"{verifier.base}/info", timeout=10)
        r.raise_for_status()
        return r.json().get("vocab_size")
    except Exception:
        return None


def validate_pair(client, verifier, cfg: Dict[str, Any],
                  strict: bool = True) -> bool:
    """Check draft vocab == target vocab == cfg expected. 

    strict=True (default): raise RuntimeError on a confirmed mismatch.
    Returns True if validated OK, False if it could not be confirmed
    (e.g. endpoints didn't expose vocab) — in that case we warn but proceed.
    """
    expected = cfg.get("vocab_size")
    dv = get_draft_vocab(client)
    tv = get_target_vocab(verifier)

    msgs = []
    msgs.append(f"[model_config] pair '{cfg.get('_name','?')}': "
                f"expected vocab={expected}, draft={dv}, target={tv}")

    # Confirmed mismatch between draft and target → fatal
    if dv is not None and tv is not None and dv != tv:
        err = (f"VOCAB MISMATCH: draft={dv} target={tv}. "
               f"Speculative decoding requires identical tokenizers. "
               f"Aborting to avoid producing garbage.")
        print("\n".join(msgs), file=sys.stderr)
        if strict:
            raise RuntimeError(err)
        print("[model_config] WARNING: " + err, file=sys.stderr)
        return False

    # Mismatch against the declared expected value → warn (config drift)
    for label, v in (("draft", dv), ("target", tv)):
        if v is not None and expected is not None and v != expected:
            msgs.append(f"[model_config] WARNING: {label} vocab {v} != "
                        f"declared {expected} in models.yaml (update the config?)")

    # Couldn't read either side → can't confirm; warn but proceed
    if dv is None or tv is None:
        msgs.append("[model_config] NOTE: could not read "
                    + ("draft " if dv is None else "")
                    + ("target " if tv is None else "")
                    + "vocab from endpoints; skipping hard validation.")
        print("\n".join(msgs))
        return False

    msgs.append("[model_config] vocab OK (draft == target).")
    print("\n".join(msgs))
    return True
