relative_cache_sizes=(0.001 0.01 0.1 0.2 0.4)
max_iteration=20

for file in /mnt/gv0/traces/*; do
    filename="$(basename "$file")"
    basename="${filename%%.oracleGeneral*}"

    for cache_size in "${relative_cache_sizes[@]}"; do
        log_file="/mnt/gv0/OptimalClockOffline/result/log/${basename}[${cache_size}].csv"
        if ! [ -s $log_file ]; then
            echo "shell:1:1:1:~/OptimalClockOffline/build/cacheSimulator $file -o /mnt/gv0/OptimalClockOffline/result -r $cache_size -i $max_iteration" >> ~/task
        else
            echo "Skipping processing: $filename $cache_size (corresponding result exists and not empty: $log_file)"
        fi
    done
done
