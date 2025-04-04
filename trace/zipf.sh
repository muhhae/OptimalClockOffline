#!/bin/bash

PYSCRIPT=../../libCacheSim/scripts/data_gen.py
# MAX_JOBS=4
# JOB_COUNT=0
#
# for i in 0 0.4 0.8 1 1.4 1.8 2; do
#     (
#         python $PYSCRIPT -m 1000000 -n 100000000\
#             --alpha $i\
#             --bin-output ../trace/zipf_${i}_10_100.oracleGeneral &&
#         echo "alpha $i generated!" &&
#         ../build/cacheSimulator ../result ../trace/zipf_${i}_10_100.oracleGeneral &&
#         echo "alpha $i processed!" &&
#         ../python/.venv/bin/python ../python/csv_to_plot.py &&
#         echo "alpha $i plotted!" &&
#         git add ../result/**/* &&
#         git commit -m "Added zipf_${i}_10_100.oracleGeneral result (automated)" &&
#         git push &&
#         echo "alpha $i pushed!"
#     ) &
#      ((JOB_COUNT++))
#     if ((JOB_COUNT >= MAX_JOBS)); then
#         wait  # Wait for some jobs to finish before starting new ones
#         JOB_COUNT=0
#     fi
# done
#
# wait
# echo "All task done!"

echo "0 0.4 0.8 1 1.4 1.8 2" | xargs -n 1 -P "$(nproc --ignore=2)" -I {} bash -c '
    python "$PYSCRIPT" -m 1000000 -n 100000000 --alpha {} --bin-output "../trace/zipf_{}_10_100.oracleGeneral" &&
    echo "alpha $i generated!" &&
    ../build/cacheSimulator ../result "../trace/zipf_{}_10_100.oracleGeneral" &&
    echo "alpha $i processed!" &&
    ../python/.venv/bin/python ../python/csv_to_plot.py &&
    echo "alpha $i plotted!" &&
    git add ../result/**/* &&
    git commit -m "Added zipf_{}_10_100.oracleGeneral result (automated)" &&
    git push &&
    echo "alpha $i pushed!"
'
