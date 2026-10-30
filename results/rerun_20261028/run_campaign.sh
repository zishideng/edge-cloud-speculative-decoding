#!/usr/bin/env bash
# Full rerun with interrupt-equipped fixed windows and CAPE (2026-10-28): Gemma-3 (main, sweep, ablation,
# weights), then Llama, Qwen and Gemma-2 (main). Before each pair it waits until the cloud serves that pair's
# target (the switch is requested from the cloud session), then restarts the draft server.
# Writes <pair>.done after each pair and campaign.done at the end.
cd "$(dirname "$0")/../.."
D=results/rerun_20261028; C=http://172.23.123.195:9090; L=$D/campaign.log
pair() {  # <name> <pair key> <cloud model substring> <phases...>
  local name=$1 key=$2 model=$3; shift 3
  [ -f $D/$name.done ] && return 0
  echo "$(date -Is) $name: waiting for cloud model $model" >> $L
  until curl -s -m 5 $C/info | grep -q "$model"; do sleep 60; done
  if [ "$key" != "$(cat $D/.draft 2>/dev/null)" ]; then
    bash $D/switch_draft.sh "$key" >> $L 2>&1 || exit 1
    echo "$key" > $D/.draft
  fi
  for ph in "$@"; do
    echo "$(date -Is) $name: start $ph" >> $L
    bash $D/run_full.sh "$ph" "$model" || { echo "$(date -Is) $ph gave up" >> $L; exit 1; }
    echo "$(date -Is) $name: done $ph" >> $L
  done
  touch $D/$name.done
}
[ -f $D/.draft ] || echo gemma3_270m_4b > $D/.draft   # the Gemma-3 draft server was already running at launch
pair gemma3 gemma3_270m_4b gemma-3-4b-it gemma3_main gemma3_sweep gemma3_ablation gemma3_weights
pair llama  llama3_awq        Meta-Llama-3.1-8B-Instruct-AWQ llama_main
pair qwen   qwen25_05b_7b_awq Qwen2.5-7B-Instruct-AWQ        qwen_main
pair gemma2 gemma2_2b_9b_awq  gemma-2-9b-it-AWQ              gemma2_main
touch $D/campaign.done; echo "$(date -Is) campaign complete" >> $L
