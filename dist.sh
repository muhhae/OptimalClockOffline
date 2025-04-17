relative_cache_sizes=(0.001 0.01 0.1 0.2 0.4)
max_iteration=20

MIN_SIZE=$(( 1024*1024*512 )) # 512 MB
MAX_SIZE=$(( 1024*1024*1024*32 )) # 32 GB

traces_txt="$1"
if [[ -z $traces_txt ]]; then
  echo "[arg] traces_txt required"
  exit 1
fi

rm ~/task

while IFS= read -r link; do
    if [ -z "$link" ] || [[ "$link" == \#* ]]; then
        continue
    fi
    filename=$(basename $link)
    file="/mnt/gv0/traces/$filename"

    basename="${filename%%.oracleGeneral*}"
    size=$(stat --format="%s" "$file")
    if [ $size -lt $MIN_SIZE ] || [ $size -gt $MAX_SIZE ]; then
        echo "Skipping processing: $filename (filesize outside allowed range, $(( size/1024/1024/1024 )))"
        continue
    fi

    gb=$(( (size + 1024*1024*1024 - 1) / (1024*1024*1024) ))
    min_dram=$(( gb+1 ))

    for cache_size in "${relative_cache_sizes[@]}"; do
        log_file="/mnt/gv0/OptimalClockOffline/result/log/${basename}[${cache_size},ignore_obj_size].csv"
        if ! [ -s $log_file ]; then
            echo "shell:1:$min_dram:2:~/OptimalClockOffline/build/cacheSimulator $file -o /mnt/gv0/OptimalClockOffline/result -r $cache_size -i $max_iteration --ignore-obj-size -d ignore_obj_size" >> ~/task
        else
            echo "Skipping processing: $filename $cache_size (corresponding result exists and not empty: $log_file)"
        fi
    done
    for cache_size in "${relative_cache_sizes[@]}"; do
        log_file="/mnt/gv0/OptimalClockOffline/result/log/${basename}[${cache_size}].csv"
        if ! [ -s $log_file ]; then
            echo "shell:1:$min_dram:2:~/OptimalClockOffline/build/cacheSimulator $file -o /mnt/gv0/OptimalClockOffline/result -r $cache_size -i $max_iteration" >> ~/task
        else
            echo "Skipping processing: $filename $cache_size (corresponding result exists and not empty: $log_file)"
        fi
    done
done < "$traces_txt"
