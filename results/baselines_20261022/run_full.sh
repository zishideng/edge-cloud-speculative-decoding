#!/usr/bin/env bash
# Run one frozen final plan with auto-resume. Usage: run_full.sh <phase> <expected target model substring>
# Before every resume, wait until both services are healthy AND the cloud serves the expected model.
cd "$(dirname "$0")/../.."
PH=$1; MODEL=$2; D=results/baselines_20261022; C=http://172.23.123.195:9090
P=$D/${PH}_plan.json; S=$D/$PH/report/status.json; L=$D/${PH}_maintenance.log
for i in $(seq 0 30); do
  if [ "$i" -eq 0 ]; then flag=""; else flag="--resume"; fi
  # A run that failed before any timed request (e.g. while building references) cannot resume: start it afresh.
  if [ -n "$flag" ] && [ "$(python3 -c "import json;print(json.load(open('$S'))['completed'])" 2>/dev/null)" = 0 ]; then
    mv "$D/$PH" "$D/${PH}_failed_init_$(date +%H%M%S)"; flag=""
  fi
  echo "$(date -Is) run attempt $i ${flag}" >> "$L"
  python3 -u -m experiments.progress_probe --plan "$P" $flag >> $D/${PH}_console_$i.log 2>&1
  state=$(python3 -c "import json;print(json.load(open('$S'))['state'])" 2>/dev/null)
  [ "$state" = "complete" ] && { echo "$(date -Is) complete" >> "$L"; exit 0; }
  echo "$(date -Is) stopped (state=$state); waiting for cloud ($MODEL) and draft" >> "$L"
  until curl -s -m 5 $C/info | grep -q "$MODEL" && curl -s -m 5 http://127.0.0.1:8080/health | grep -q ok; do sleep 30; done
  echo "$(date -Is) services healthy (cloud uptime $(curl -s -m 5 $C/info | python3 -c 'import json,sys;print(round(json.load(sys.stdin)["uptime_s"]))'))" >> "$L"
done
echo "$(date -Is) gave up after 30 resumes" >> "$L"; exit 1
