relative_cache_sizes=(0.001 0.01 0.1 0.2 0.4)
max_iteration=20
basedir="/mnt/v0"

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
    file="$basedir/traces/$filename"
    basename="${filename%%.oracleGeneral*}"
    size=$(stat --format="%s" "$file")

    gb=$(( (size + 1024*1024*1024 - 1) / (1024*1024*1024) ))
    min_dram=$(( gb+1 ))

    for cache_size in "${relative_cache_sizes[@]}"; do
        datasets="$basedir/OptimalClockOffline/result/datasets/${basename}[${cache_size},ignore_obj_size].csv"
        if ! [ -s $datasets ]; then
            echo "shell:1:$min_dram:1:~/OptimalClockOffline/build/cacheSimulator $file -o $basedir/OptimalClockOffline/result -r $cache_size -i $max_iteration --generate-datasets --ignore-obj-size -d ignore_obj_size && python ~/OptimalClockOffline/python/describe_csv.py $datasets > $datasets.desc" >> ~/task
        else
            echo "Skipping processing: $filename $cache_size (corresponding result exists and not empty: $datasets)"
        fi
        datasets="$basedir/OptimalClockOffline/result/datasets/${basename}[${cache_size}].csv"
        if ! [ -s $datasets ]; then
            echo "shell:1:$min_dram:1:~/OptimalClockOffline/build/cacheSimulator $file -o $basedir/OptimalClockOffline/result -r $cache_size -i $max_iteration --generate-datasets && python ~/OptimalClockOffline/python/describe_csv.py $datasets > $datasets.desc" >> ~/task
        else
            echo "Skipping processing: $filename $cache_size (corresponding result exists and not empty: $datasets)"
        fi
    done
done < "$traces_txt"
