"""bench_smart.py — Ablation benchmark for bootstrap + fallback.

Configs (via flags):
  --bootstrap M       round-0 bootstrap with M cloud tokens (0=off)
  --fallback-k K      check acceptance after K rounds (0=off)
  --fallback-thresh T fall back to cloud-only if acceptance < T

Run the same dataset under several configs to build the ablation table:
  base     : --bootstrap 0 --fallback-k 0      (= fixed edge-cloud SD)
  +boot    : --bootstrap 2 --fallback-k 0
  +fb      : --bootstrap 0 --fallback-k 3 --fallback-thresh 0.65
  full     : --bootstrap 2 --fallback-k 3 --fallback-thresh 0.65
"""
import argparse, json, pathlib, re, time
from tqdm import tqdm

from edge.edge_client_smart import SmartEdgeClient
from edge.verifier import RemoteVerifier
import edge.verifier_ext as verifier_ext  # noqa
from edge.energy_profiler import EnergyProfiler

SYS = {
    "gsm8k": ("You are a math tutor. Solve the problem step by step. "
              "End your answer with exactly: 'Final answer: <number>'."),
    "humaneval": ("You are a Python expert. Provide a complete function "
                  "implementation. Output only the function code."),
    "mtbench": "You are a helpful assistant. Provide a clear, concise answer.",
}
ANSWER_RE = re.compile(r"final answer\s*[:\-]?\s*\$?(-?[\d,]+(?:\.\d+)?)", re.I)

def num(t):
    m = ANSWER_RE.search(t or "")
    if m: return m.group(1).replace(",", "").rstrip(".")
    z = re.findall(r"-?\d+(?:\.\d+)?", t or ""); return z[-1] if z else None
def norm(x):
    if x is None: return None
    x = x.replace(",", "").strip()
    try:
        f=float(x); return str(int(f)) if f.is_integer() else str(f)
    except: return x

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bootstrap", type=int, default=0)
    ap.add_argument("--fallback-k", type=int, default=0)
    ap.add_argument("--fallback-thresh", type=float, default=0.65)
    ap.add_argument("--gamma", type=int, default=2)
    ap.add_argument("--task", choices=["gsm8k","humaneval","mtbench"], default="gsm8k")
    ap.add_argument("--remote-url", default="http://localhost:9090")
    ap.add_argument("--draft-url", default="http://localhost:8080")
    ap.add_argument("--data", required=True)
    ap.add_argument("--n", type=int, default=30)
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--profile-energy", action="store_true")
    ap.add_argument("--out", required=True)
    ap.add_argument("--tag", default=None)
    ap.add_argument("--model-config", default=None,
                    help="name of a pair in models.yaml (e.g. llama3, qwen25). "
                         "If set, supplies eos_id and enables vocab validation.")
    ap.add_argument("--models-yaml", default=None,
                    help="path to models.yaml (default: auto-discover)")
    ap.add_argument("--no-think", action="store_true",
                    help="append /no_think to the user turn to disable Qwen3 thinking")
    args = ap.parse_args()

    # Optional model-pair config: provides eos_id + vocab validation.
    mcfg = None
    eos_id = None
    if args.model_config:
        from model_config import load_model_config
        mcfg = load_model_config(args.model_config, args.models_yaml)
        eos_id = mcfg["eos_id"]
        print(f"[model_config] using '{mcfg['_name']}': target={mcfg['target']}, "
              f"eos_id={eos_id}, vocab={mcfg['vocab_size']}")

    tag = args.tag or f"S_b{args.bootstrap}_fk{args.fallback_k}_{args.task}"
    client = SmartEdgeClient(
        draft_url=args.draft_url,
        bootstrap_m=args.bootstrap,
        fallback_k=args.fallback_k,
        fallback_thresh=args.fallback_thresh,
    )
    verifier = RemoteVerifier(url=args.remote_url)
    print(f"[{tag}] verify: {verifier.health()}")
    # Validate draft/target tokenizer match (only if a model-config was given)
    if mcfg is not None:
        from model_config import validate_pair
        # strict_vocab:false (models.yaml) downgrades a vocab-size mismatch to a
        # warning — needed when the tokenizer is identical but the embedding
        # vocab_size is padded differently (e.g. DeepSeek distill 1.5B vs 32B).
        validate_pair(client, verifier, mcfg,
                      strict=mcfg.get("strict_vocab", True))
    # Confirm /generate exists
    try:
        tids, _, _ = verifier.generate(prompt_ids=[128000], max_tokens=1)
        print(f"[{tag}] /generate OK (test returned {len(tids)} tok)")
    except Exception as e:
        raise SystemExit(f"/generate not available — apply patch_verify_server.py and restart server. {e}")

    samples = []
    with open(args.data) as f:
        for line in f: samples.append(json.loads(line))
    samples = samples[:args.n]
    sysp = SYS[args.task]

    client.generate(messages=[{"role":"user","content":"Hi"}],
                    verifier=verifier, gamma=args.gamma, max_tokens=16,
                    temperature=args.temperature, eos_id=eos_id,
                    no_think=args.no_think)

    def loop():
        recs=[]; t0=time.perf_counter()
        for ex in tqdm(samples, desc=tag):
            q = ex.get("question") or ex.get("prompt") or ex.get("turns",[""])[0]
            text, m = client.generate(
                messages=[{"role":"system","content":sysp},{"role":"user","content":q}],
                verifier=verifier, gamma=args.gamma,
                max_tokens=args.max_tokens, temperature=args.temperature, eos_id=eos_id,
                no_think=args.no_think)
            correct = norm(num(text))==norm(ex.get("gold_answer","")) if args.task=="gsm8k" else None
            recs.append({
                "id": ex.get("id"), "wall_time_s": m.wall_time_s,
                "output_tokens": m.total_output_tokens,
                "n_accepted": m.n_accepted, "n_proposed": m.n_draft_proposed,
                "bootstrap_tokens": m.bootstrap_tokens,
                "fell_back": m.fell_back, "cloud_tokens": m.cloud_tokens,
                "acceptance_at_fallback": m.acceptance_at_fallback,
                "correct": correct,
            })
        return recs, time.perf_counter()-t0

    if args.profile_energy:
        with EnergyProfiler(label=tag) as ep: recs, wall = loop()
        es = ep.summary()
    else:
        recs, wall = loop(); es={"joules":0,"avg_watts":0}

    n=len(recs)
    so=sum(r["output_tokens"] for r in recs); sw=sum(r["wall_time_s"] for r in recs)
    sa=sum(r["n_accepted"] for r in recs); sp=sum(r["n_proposed"] for r in recs)
    nfb=sum(1 for r in recs if r["fell_back"])
    acc = sum(r["correct"] for r in recs if r["correct"] is not None)/n if args.task=="gsm8k" else None

    summary={
        "tag":tag,"bootstrap":args.bootstrap,"fallback_k":args.fallback_k,
        "fallback_thresh":args.fallback_thresh,"gamma":args.gamma,"task":args.task,
        "n_samples":n,"accuracy":acc,
        "agg_tok_s": so/sw if sw else 0,
        "acceptance": sa/max(1,sp),
        "avg_latency_s": sw/n,
        "avg_output_tokens": so/n,
        "n_fell_back": nfb,
        "fallback_rate": nfb/n,
        "joules":es["joules"],"avg_watts":es["avg_watts"],
        "joules_per_token": (es["joules"]/so) if so and es["joules"] else 0,
        "total_wall_s": wall,
    }
    out=pathlib.Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)
    with out.open("w") as f: json.dump({"summary":summary,"records":recs},f,indent=2)
    print(f"\n[{tag}] Summary:")
    for k,v in summary.items(): print(f"  {k}: {v}")
    print(f"  → {out}")

if __name__ == "__main__":
    main()
