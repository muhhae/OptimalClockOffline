#!/bin/bash

bash ./download_trace.sh
shopt -s nullglob

for file in ./*.oracleGeneral*; do
    filename="$(basename "$file")"
    graph_file="../result/graph/${filename%%.oracleGeneral*}_128MiB.png"
    echo $graph_file

    if [ -f "$graph_file" ]; then
        echo "Skipping processing: $filename (corresponding graph exists: $graph_file)"
    else
        echo "Processing: $filename"
        ../build/cacheSimulator ../result $filename
        ../python/.venv/bin/python ../python/csv_to_plot.py
        git add ../result/**/${filename%%.*}* && git commit -m "Added ${filename%%.*} result (automated)" && git push
    fi
done

echo "All experiments done!"
