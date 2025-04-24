relative_cache_sizes=(0.001 0.01 0.1 0.2 0.4)
max_iteration=1
basedir="/mnt/v0"

traces_txt="$1"
if [[ -z $traces_txt ]]; then
  echo "Usage: bash test.sh [traces_txt] [out_dir=$basedir/OptimalClockOffline/result] [model=~/OptimalClockOffline/python/ML/v4/model/logistic_regression]"
  exit 1
fi

out_dir="$2"
if [[ -z $out_dir ]]; then
  out_dir="$basedir/OptimalClockOffline/result"
fi

model="$3"
if [[ -z $model ]]; then
  model="logistic_regression"
fi
model="~/OptimalClockOffline/python/ML/v4/model/$model"
echo Model: $model

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
        log_file="$out_dir/log/${basename}[${cache_size},ignore_obj_size,logistic_regression_$cache_size].csv"
        if ! [ -s $log_file ]; then
            echo "shell:1:$min_dram:2:~/OptimalClockOffline/build/cacheSimulator $file -o $out_dir -r $cache_size -i 1 --ignore-obj-size -d ignore_obj_size,logistic_regression_$cache_size -a ML -m $model[$cache_size,ignore_obj_size].onnx" >> ~/task
        else
            echo "Skipping processing: (corresponding result exists and not empty: $log_file)"
        fi
        # log_file="$out_dir/log/${basename}[${cache_size},ignore_obj_size,logistic_regression_All].csv"
        # if ! [ -s $log_file ]; then
        #     echo "shell:1:$min_dram:2:~/OptimalClockOffline/build/cacheSimulator $file -o $out_dir -r $cache_size -i 1 --ignore-obj-size -d ignore_obj_size,logistic_regression_All -a ML -m $model[All,ignore_obj_size].onnx" >> ~/task
        # else
        #     echo "Skipping processing: (corresponding result exists and not empty: $log_file)"
        # fi
        log_file="$out_dir/log/${basename}[${cache_size},logistic_regression_$cache_size].csv"
        if ! [ -s $log_file ]; then
            echo "shell:1:$min_dram:2:~/OptimalClockOffline/build/cacheSimulator $file -o $out_dir -r $cache_size -i 1 -d logistic_regression_$cache_size -a ML -m $model[$cache_size].onnx" >> ~/task
        else
            echo "Skipping processing: (corresponding result exists and not empty: $log_file)"
        fi
        # log_file="$out_dir/log/${basename}[${cache_size},logistic_regression_All].csv"
        # if ! [ -s $log_file ]; then
        #     echo "shell:1:$min_dram:2:~/OptimalClockOffline/build/cacheSimulator $file -o $out_dir -r $cache_size -i 1 -d logistic_regression_All -a ML -m $model[All].onnx" >> ~/task
        # else
        #     echo "Skipping processing: (corresponding result exists and not empty: $log_file)"
        # fi
    done
done < "$traces_txt"
