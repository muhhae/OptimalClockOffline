#!/bin/bash

PYSCRIPT=../../libCacheSim/scripts/data_gen.py

echo "0 0.3 0.7 1 1.3 1.7 2" | xargs -n 1 -P "$(nproc --ignore=2)" bash -c '
    alpha="$1"
    ../python/.venv/bin/python "'"$PYSCRIPT"'" -m 1000000 -n 100000000 --alpha "$alpha" --bin-output "zipf_${alpha}_10_100.oracleGeneral" &&
    echo "alpha $alpha generated!"
' _
