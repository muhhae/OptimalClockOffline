#!/bin/bash

shopt -s nullglob

offline_clock() {
    fixed_cache_sizes=(128 256 512 1024 2048)
    relative_cache_sizes=(0.001 0.01 0.1 0.2 0.4)
    max_iteration=20

    file=$1

    do_cache_sizes=()

    filename="$(basename "$file")"
    basename="${filename%%.oracleGeneral*}"

    for cache_size in "${relative_cache_sizes[@]}"; do
        log_file="../result/log/${basename}[${cache_size}].csv"
        if ! [ -s $log_file ]; then
            do_cache_sizes+=($cache_size)
        else
            echo "Skipping processing: $filename $cache_size (corresponding result exists and not empty: $log_file)"
        fi
    done

    for cache_size in "${fixed_cache_sizes[@]}"; do
        log_file="../result/log/${basename}[${cache_size}MiB].csv"
        if ! [ -s $log_file ]; then
            do_cache_sizes+=($cache_size)
        else
            echo "Skipping processing: $filename $cache_size (corresponding result exists and not empty: $log_file)"
        fi
    done

    echo "Processing: $filename"
    echo "Cache Size: ${do_cache_sizes[@]}"

    ../build/cacheSimulator $filename -o ../result -r ${do_cache_sizes[@]} -i $max_iteration &&
    ../python/.venv/bin/python ../python/csv_to_plot.py &&
    ../python/.venv/bin/python ../python/result_to_md.py &&
    git add ../result/**/${basename}* && git commit -m "Added $basename result (automated)" && git push
}

export -f offline_clock

echo ./*.oracleGeneral* | xargs -n 1 -P "$(nproc --ignore=2)" bash -c 'offline_clock $0'

../python/.venv/bin/python ../python/result_to_md.py

echo "All experiments done!"
