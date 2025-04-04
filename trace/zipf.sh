#!/bin/bash

PYSCRIPT=../../libCacheSim/scripts/data_gen.py

echo "0 0.3 0.7 1 1.3 1.7 2" | xargs -n 1 -P "$(nproc --ignore=2)" bash -c '
    alpha="$1"
    echo "working on alpha $alpha!"
    ../python/.venv/bin/python "'"$PYSCRIPT"'" -m 1000000 -n 100000000 --alpha "$alpha" --bin-output "../trace/zipf_${alpha}_10_100.oracleGeneral" &&
    echo "alpha $alpha generated!"
    ../build/cacheSimulator ../result "../trace/zipf_${alpha}_10_100.oracleGeneral" &&
    echo "alpha $alpha processed!"
    ../python/.venv/bin/python ../python/csv_to_plot.py &&
    echo "alpha $alpha plotted!"
    git add ../result/**/* &&
    git commit -m "Added zipf_${alpha}_10_100.oracleGeneral result (automated)" &&
    git push &&
    echo "alpha $alpha pushed!"
' _
