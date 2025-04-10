#!/bin/bash

shopt -s nullglob

offline_clock() {
    fixed_cache_sizes=(128 256 512 1024 2048)
    relative_cache_sizes=(0.001 0.01 0.1 0.2 0.4)
    max_iteration=20

    file=$1

    do_relative_cache_sizes=()
    do_fixed_cache_sizes=()

    filename="$(basename "$file")"
    basename="${filename%%.oracleGeneral*}"

    for cache_size in "${relative_cache_sizes[@]}"; do
        log_file="../result/log/${basename}[${cache_size}].csv"
        if ! [ -s $log_file ]; then
            do_relative_cache_sizes+=($cache_size)
        else
            echo "Skipping processing: $filename $cache_size (corresponding result exists and not empty: $log_file)"
        fi
    done

    for cache_size in "${fixed_cache_sizes[@]}"; do
        log_file="../result/log/${basename}[${cache_size}MiB].csv"
        if ! [ -s $log_file ]; then
            do_fixed_cache_sizes+=($cache_size)
        else
            echo "Skipping processing: $filename $cache_size (corresponding result exists and not empty: $log_file)"
        fi
    done

    if [ "${#do_relative_cache_sizes[@]}" -ne 0 ] || [ "${#do_fixed_cache_sizes[@]}" -ne 0 ] ; then
        arg = ""
        if [ "${#do_relative_cache_sizes[@]}" -ne 0 ] ; then
            arg+="-r ${do_relative_cache_sizes[@]}"
        fi
        if [ "${#do_fixed_cache_sizes[@]}" -ne 0 ] ; then
            arg+=" -f ${do_fixed_cache_sizes[@]}"
        fi
        echo "Processing: $filename"
        echo "Cache Size: ${do_relative_cache_sizes[@]}"
        ../build/cacheSimulator $filename -o ../result $arg -i $max_iteration
    fi

    ../python/.venv/bin/python ../python/csv_to_plot.py
    ../python/.venv/bin/python ../python/result_to_md.py
    git pull --rebase && git add ../result/* && git commit -m "Update result (automated)" && git push
}

export -f offline_clock

echo ./*.oracleGeneral* | xargs -n 1 -P "$(nproc --ignore=2)" bash -c 'offline_clock $0'

../python/.venv/bin/python ../python/result_to_md.py

echo "All experiments done!"
