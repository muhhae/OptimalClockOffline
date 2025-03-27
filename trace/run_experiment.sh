#!/bin/bash

bash ./download_trace.sh
shopt -s nullglob

BATCH_SIZE=4
batch=()
batch_name=()

for file in ./*.oracleGeneral*; do
    filename="$(basename "$file")"
    graph_file="../result/graph/${filename%%.oracleGeneral*}_128MiB.png"
    echo $graph_file

    if [ -f "$graph_file" ]; then
        echo "Skipping processing: $filename (corresponding graph exists: $graph_file)"
    else
        batch+=($filename)
        batch_name+=(${filename%%.oracleGeneral*})
    fi

    if ((${#batch[@]} == $batch)); then
        echo "Processing: ${batch[@]}"
        ../build/cacheSimulator ../result ${batch[@]}
        ../python/.venv/bin/python ../python/csv_to_plot.py
        git add ../result/**/* && git commit -m "Added ${batch_name[*]} result (automated)" && git push
        batch=()
        batch_name=()
    fi
done

if ((${#batch[@]} > 0)); then
    echo "Processing: ${batch[@]}"
    ../build/cacheSimulator ../result ${batch[@]}
    ../python/.venv/bin/python ../python/csv_to_plot.py
    git add ../result/**/* && git commit -m "Added ${batch_name[*]} result (automated)" && git push
fi

echo "All experiments done!"
