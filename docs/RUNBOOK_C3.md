# C3 Energy Sweep — Runbook

## Files (deploy to Jetson)
Copy these to `~/Downloads/day4b_jetson/`:
- `energy_profiler.py`
- `bench_c3_energy.py`
- `summarize_c3.py`

## Prereqs
- jtop installed and `sudo systemctl start jetson_stats` (already done in Day 3)
- H200 verify server running, SSH tunnel up on port 9090
- Jetson llama-server running on 8080

## Procedure (3 power modes × 3 γ values = 9 cells, ~75 min total)

### Mode 1: 7W (low-power)
```bash
sudo nvpmodel -m 1
sleep 5
cd ~/Downloads/day4b_jetson
python bench_c3_energy.py \
    --power-mode 7W \
    --remote-url http://localhost:9090 \
    --gammas 2 3 5 \
    --n 30 \
    --data ~/Downloads/day3_jetson/gsm8k_test_50.jsonl \
    --out ~/b3_results/C3_7W.json
```

### Mode 2: 15W (default)
```bash
sudo nvpmodel -m 0
sudo jetson_clocks
sleep 5
python bench_c3_energy.py \
    --power-mode 15W \
    --remote-url http://localhost:9090 \
    --gammas 2 3 5 \
    --n 30 \
    --data ~/Downloads/day3_jetson/gsm8k_test_50.jsonl \
    --out ~/b3_results/C3_15W.json
```

### Mode 3: MAXN (uncapped, what you've been using)
```bash
sudo nvpmodel -m 2
sudo jetson_clocks
sleep 5
python bench_c3_energy.py \
    --power-mode MAXN \
    --remote-url http://localhost:9090 \
    --gammas 2 3 5 \
    --n 30 \
    --data ~/Downloads/day3_jetson/gsm8k_test_50.jsonl \
    --out ~/b3_results/C3_MAXN.json
```

### Aggregate
```bash
python summarize_c3.py \
    ~/b3_results/C3_7W.json \
    ~/b3_results/C3_15W.json \
    ~/b3_results/C3_MAXN.json \
    --md-out ~/b3_results/C3_table.md \
    --lookup-out ~/b3_results/C3_lookup.json
cat ~/b3_results/C3_table.md
```

## Expected results
- **MAXN γ=3**: ~15.6 tok/s, ~15W, J/tok ~0.96 (your current baseline)
- **15W γ=3**: ~12-14 tok/s, ~12W, **lower J/tok**
- **7W γ=3**: ~6-8 tok/s, ~7W, depends — could be best or worst J/tok
- **Pareto frontier**: typically MAXN at low-latency end, 7W at low-energy end

## What to vet
After each cell finishes, sanity-check:
- `n_samples > 0` (didn't crash)
- `energy_samples > 100` (jtop actually reported)
- `avg_watts` matches power mode (7W mode → ~7-9W, 15W → ~12-15W, MAXN → ~15-25W)

If `avg_watts = 0`, jtop integration broken — see fallback below.

## jtop fallback (if profiler reports 0 watts)
```python
# Quick test
python3 -c "from jtop import jtop; j=jtop(); j.start(); import time; time.sleep(1); print(j.power); j.close()"
```
If this prints power info, energy_profiler.py's key extraction is wrong;
paste output to next session and I'll patch.

## Notes
- Each cell ~7-10 minutes (30 samples × 14-20s avg latency)
- Don't move/touch Jetson during runs — vibrations affect cooling/clocks
- If MAXN crashes (thermal), drop to 15W and continue
