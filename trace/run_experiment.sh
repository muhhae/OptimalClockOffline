#!/bin/bash

bash ./download_trace.sh

for file in "./*"; do
    filename="$(basename "$file")"
    graph_file="../result/graph/${filename%%.*}_128MiB.png"

    if [ -f "$graph_file" ]; then
        echo "Skipping processing: $filename (corresponding graph exists: $graph_file)"
    else
        echo "Processing: $filename"
        ../build/cacheSimulator . $filename
    fi
done

echo "All experiments done!"
git add -A && git commit -m "Added some result (automatic)" && git push
