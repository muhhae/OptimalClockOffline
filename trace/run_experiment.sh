#!/bin/bash

bash ./download_trace.sh
shopt -s nullglob

BATCH_SIZE=4
batch=()

for file in ./*.oracleGeneral*; do
    filename="$(basename "$file")"
    graph_file="../result/graph/${filename%%.oracleGeneral*}_128MiB.png"
    echo $graph_file

    if [ -f "$graph_file" ]; then
        echo "Skipping processing: $filename (corresponding graph exists: $graph_file)"
    else
        batch+=(filename)
    fi

    if ((${#batch[@]} == $batch)); then
        echo "Processing: ${batch[@]}"
        ../build/cacheSimulator ../result ${batch[@]}
        ../python/.venv/bin/python ../python/csv_to_plot.py
        git add ../result/**/* && git commit -m "Added ${batch[@]} result (automated)" && git push
    fi
done

if ((${#batch[@]} > 0)); then
    echo "Processing: ${batch[@]}"
    ../build/cacheSimulator ../result ${batch[@]}
    ../python/.venv/bin/python ../python/csv_to_plot.py
    git add ../result/**/* && git commit -m "Added ${batch[@]} result (automated)" && git push
fi

echo "All experiments done!"
