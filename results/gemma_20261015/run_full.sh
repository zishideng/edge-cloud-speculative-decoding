#!/usr/bin/env bash
# Run the frozen Gemma full_110 plan; after a lost cloud connection wait for the
# server and resume with the same plan (at most 30 times). Every event is logged.
cd "$(dirname "$0")/../.."
P=results/gemma_20261015/full_110_plan.json
S=results/gemma_20261015/full_110/report/status.json
L=results/gemma_20261015/full_110_maintenance.log
for i in $(seq 0 30); do
  if [ "$i" -eq 0 ]; then flag=""; else flag="--resume"; fi
  echo "$(date -Is) run attempt $i ${flag}" >> "$L"
  python3 -u -m experiments.progress_probe --plan "$P" $flag >> results/gemma_20261015/full_110_console_$i.log 2>&1
  state=$(python3 -c "import json;print(json.load(open('$S'))['state'])" 2>/dev/null)
  [ "$state" = "complete" ] && { echo "$(date -Is) complete" >> "$L"; exit 0; }
  echo "$(date -Is) stopped (state=$state); waiting for cloud" >> "$L"
  until curl -s -m 5 http://172.23.123.195:9090/health | grep -q ok && curl -s -m 5 http://127.0.0.1:8080/health | grep -q ok; do sleep 30; done
  echo "$(date -Is) services healthy (cloud uptime $(curl -s -m 5 http://172.23.123.195:9090/info | python3 -c 'import json,sys;print(round(json.load(sys.stdin)["uptime_s"]))'))" >> "$L"
done
echo "$(date -Is) gave up after 30 resumes" >> "$L"; exit 1
