#!/bin/bash

bash ./download_trace.sh
shopt -s nullglob

offline_clock() {
    file=$1

    filename="$(basename "$file")"
    basename="${filename%%.oracleGeneral*}"
    graph_file="../result/graph/${filename%%.oracleGeneral*}_128MiB.png"

    if [ -f "$graph_file" ]; then
        echo "Skipping processing: $filename (corresponding graph exists: $graph_file)"
    else
        echo "Processing: $filename"
        ../build/cacheSimulator ../result $filename
        ../python/.venv/bin/python ../python/csv_to_plot.py
        ../python/.venv/bin/python ../python/result_to_md.py
        git add ../result/**/* && git commit -m "Added $basename result (automated)" && git push
    fi
}

export -f offline_clock

echo ./*.oracleGeneral* | xargs -n 1 -P "$(nproc --ignore=2)" bash -c 'offline_clock $0'

../python/.venv/bin/python ../python/result_to_md.py

echo "All experiments done!"
