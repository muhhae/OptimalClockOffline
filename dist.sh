relative_cache_sizes=(0.001 0.01 0.1 0.2 0.4)
max_iteration=2
basedir="/mnt/v0"

traces_txt="$1"
if [[ -z $traces_txt ]]; then
  echo "[arg1] traces_txt required"
  exit 1
fi

out_dir="$2"
if [[ -z $out_dir ]]; then
  out_dir="./result"
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
        datasets="$out_dir/datasets/${basename}[${cache_size},ignore_obj_size,TEST].csv"
            echo "shell:1:$min_dram:1:~/OptimalClockOffline/build/cacheSimulator $file -o $out_dir -r $cache_size -i $max_iteration --ignore-obj-size -d ignore_obj_size,TEST" >> ~/task
        datasets="$out_dir/datasets/${basename}[${cache_size},TEST].csv"
            echo "shell:1:$min_dram:1:~/OptimalClockOffline/build/cacheSimulator $file -o $out_dir -r $cache_size -i $max_iteration -d TEST" >> ~/task
    done
done < "$traces_txt"
