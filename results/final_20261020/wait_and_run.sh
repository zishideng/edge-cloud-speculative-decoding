#!/usr/bin/env bash
# Wait until the cloud serves the expected model with the prefix-cache verify server, then run the phase.
# Usage: wait_and_run.sh <phase> <target model substring>
cd "$(dirname "$0")/../.."
L=results/final_20261020/${1}_maintenance.log
echo "$(date -Is) waiting for cloud model $2 with prefix_cache_verify" >> "$L"
until curl -s -m 5 http://172.23.123.195:9090/info | python3 -c "import json,sys;d=json.load(sys.stdin);sys.exit(0 if '$2' in d['target_model'] and d['backend_settings'].get('prefix_cache_verify') else 1)" 2>/dev/null; do sleep 60; done
echo "$(date -Is) cloud ready: $(curl -s -m 5 http://172.23.123.195:9090/info | python3 -c 'import json,sys;d=json.load(sys.stdin);print(d["target_model"],d["source_sha256"]["verify_server.py"][:6])')" >> "$L"
sleep 60   # let a freshly started server settle
exec bash results/final_20261020/run_full.sh "$1" "$2"
