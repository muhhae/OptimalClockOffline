#!/bin/bash

PYSCRIPT=../../libCacheSim/scripts/data_gen.py

echo "0 0.5 1 1.5 2" | xargs -P "$(nproc --ignore=2)" -I {} bash -c '
    ../python/.venv/bin/python "$1" -m 1000000 -n 100000000 --alpha {} --bin-output "../trace/zipf_{}_10_100.oracleGeneral" &&
    echo "alpha {} generated!" &&
    ../build/cacheSimulator ../result "../trace/zipf_{}_10_100.oracleGeneral" &&
    echo "alpha {} processed!" &&
    ../python/.venv/bin/python ../python/csv_to_plot.py &&
    echo "alpha {} plotted!" &&
    git add ../result/**/* &&
    git commit -m "Added zipf_{}_10_100.oracleGeneral result (automated)" &&
    git push &&
    echo "alpha {} pushed!"
' _ "$PYSCRIPT"
