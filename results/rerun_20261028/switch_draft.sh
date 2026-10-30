#!/usr/bin/env bash
# Restart the single draft server (port 8080) for a model pair. Usage: switch_draft.sh <pair key>
# Settings per pair as in the earlier runs (see each plan's "measurement").
cd "$(dirname "$0")/../.."
PAIR=$1; LOG=results/rerun_20261028/draft_server_$PAIR.log
case $PAIR in
  gemma3_270m_4b)    ENV="LLAMA_ARG_SWA_FULL=1 LLAMA_ARG_MMAP=0 LLAMA_ARG_DIO=1 CTX=2048" ;;
  gemma2_2b_9b_awq)  ENV="LLAMA_ARG_SWA_FULL=1 LLAMA_ARG_MMAP=0 CTX=2048" ;;
  llama3_awq|qwen25_05b_7b_awq) ENV="LLAMA_ARG_MMAP=0 CTX=4096" ;;
  *) echo "unknown pair $PAIR"; exit 2 ;;
esac
# Exact process name only, never a pattern match on command lines (that has killed the caller before).
for pid in $(pgrep -x llama-server); do kill "$pid"; done
until ! pgrep -x llama-server >/dev/null; do sleep 2; done
# NvMap cannot reclaim page cache and there is no sudo: evict it with a transient ~4.2 GB allocation
# (every pair: after a long run the cache leaves too little for even the 1B draft, 2026-10-28).
python3 -c "b=bytearray(4200*2**20); b[::4096]=b'\x01'*len(b[::4096])"
env $ENV HOST=127.0.0.1 PORT=8080 NGL=99 CACHE_RAM=256 setsid nohup bash edge/scripts/start_draft_server.sh "$PAIR" > "$LOG" 2>&1 &
for i in $(seq 1 120); do
  curl -s -m 5 http://127.0.0.1:8080/health | grep -q ok && { echo "$(date -Is) draft $PAIR healthy"; exit 0; }
  sleep 5
done
echo "$(date -Is) draft $PAIR failed to start"; tail -5 "$LOG"; exit 1
