#!/usr/bin/env bash
# Switch Jetson Orin Nano power mode.
#
# JetPack 6 Orin Nano modes:
#   0 = 15W (default, single core boost OK)
#   1 = 7W  (lowest power, throttled CPU/GPU)
#   2 = MAXN (uncapped, ~25W peak — needs good cooling)
#
# On Orin Nano Super there is also "MAXN_SUPER" but that's only the dev kit.
# Use `sudo nvpmodel -q --verbose` to see what your unit supports.
set -e

MODE="${1:-show}"

case "$MODE" in
    show|list)
        echo "==> Current mode:"
        sudo nvpmodel -q
        echo
        echo "==> Available modes:"
        sudo nvpmodel -p --verbose 2>/dev/null | head -40 || \
            cat /etc/nvpmodel.conf | grep -E "^< POWER_MODEL" || true
        ;;
    7w|7W|1)
        sudo nvpmodel -m 1
        echo "==> Set to 7W"
        ;;
    15w|15W|0)
        sudo nvpmodel -m 0
        echo "==> Set to 15W"
        ;;
    maxn|MAXN|2)
        sudo nvpmodel -m 2 2>/dev/null || sudo nvpmodel -m 0
        echo "==> Set to MAXN (or 15W if MAXN unavailable)"
        sudo jetson_clocks
        echo "==> Locked clocks to max"
        ;;
    *)
        echo "Usage: $0 [show|7w|15w|maxn]"
        exit 1
        ;;
esac

echo
echo "==> Now:"
sudo nvpmodel -q | head -3
