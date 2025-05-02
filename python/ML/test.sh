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

task_out="$4"
if [[ -z $task_out ]]; then
    task_out="$HOME/test-$model.taskfile"
fi

features=""
case "$model" in
    "little_random_forest")
        features="-F clock_time clock_time_between cache_size obj_size clock_freq lifetime_freq"
        ;;
    "logistic_regression")
        features="-F clock_time clock_time_between cache_size obj_size clock_freq lifetime_freq"
        ;;
    "logistic_regression_v2")
        features="-F clock_time_between clock_freq lifetime_freq time_since obj_size_relative"
        ;;
    "logistic_regression_v3")
        features="-F clock_time_between clock_freq lifetime_freq obj_size_relative"
        ;;
    "logistic_regression_v4")
        features="-F clock_time_between clock_freq lifetime_freq obj_size_relative"
        ;;
    "LR_v5")
        features="-I F32 -F clock_time_between_normalized clock_freq_normalized"
        ;;
    "LR_v6")
        features="-I F32 -F clock_time_between_normalized clock_freq_normalized lifetime_freq_normalized"
        ;;
    "LR_v7")
        features="-F clock_time_between_normalized clock_freq_normalized lifetime_freq_normalized"
        ;;
    "LR_v8")
        features="-F clock_time_between_normalized clock_freq_normalized"
        ;;
    *)
        echo "Unknown model using default features"
        ;;
esac

model_dir="$HOME/OptimalClockOffline/python/ML/model/$model"

echo "" > $task_out


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
        log_file="$out_dir/log/${basename}[${cache_size},ignore_obj_size,ML,model=${model}_${cache_size}].csv"
        if [ -e "$model_dir[$cache_size,ignore_obj_size].onnx" ]; then
          if ! [ -s $log_file ]; then
              echo "shell:1:$min_dram:1:~/OptimalClockOffline/build/cacheSimulator $file $features -o $out_dir -r $cache_size -i 1 --ignore-obj-size -d ignore_obj_size,ML,model=${model}_$cache_size -a ML -m $model_dir[$cache_size,ignore_obj_size].onnx" >> $task_out
          else
              echo "Skipping processing: (corresponding result exists and not empty: $log_file)"
          fi
        else
            echo "Skipping processing: (model doesn't exists: $model[$cache_size,ignore_obj_size])"
        fi
        if [ -e "$model_dir[All,ignore_obj_size].onnx" ]; then
          log_file="$out_dir/log/${basename}[${cache_size},ignore_obj_size,ML,model=${model}_All].csv"
          if ! [ -s $log_file ]; then
              echo "shell:1:$min_dram:1:~/OptimalClockOffline/build/cacheSimulator $file $features -o $out_dir -r $cache_size -i 1 --ignore-obj-size -d ignore_obj_size,ML,model=${model}_All -a ML -m $model_dir[All,ignore_obj_size].onnx" >> $task_out
          else
              echo "Skipping processing: (corresponding result exists and not empty: $log_file)"
          fi
        else
            echo "Skipping processing: (model doesn't exists: $model[All,ignore_obj_size])"
        fi
        if [ -e "$model_dir[$cache_size].onnx" ]; then
          log_file="$out_dir/log/${basename}[${cache_size},ML,model=${model}_${cache_size}'].csv"
          if ! [ -s $log_file ]; then
              echo "shell:1:$min_dram:1:~/OptimalClockOffline/build/cacheSimulator $file $features -o $out_dir -r $cache_size -i 1 -d ML,model=${model}_$cache_size -a ML -m $model_dir[$cache_size].onnx" >> $task_out
          else
              echo "Skipping processing: (corresponding result exists and not empty: $log_file)"
          fi
        else
            echo "Skipping processing: (model doesn't exists: $model[$cache_size])"
        fi
        if [ -e "$model_dir[All].onnx" ]; then
          log_file="$out_dir/log/${basename}[${cache_size},ML,model=${model}_All].csv"
          if ! [ -s $log_file ]; then
              echo "shell:1:$min_dram:1:~/OptimalClockOffline/build/cacheSimulator $file $features -o $out_dir -r $cache_size -i 1 -d ML,model=${model}_All -a ML -m $model_dir[All].onnx" >> $task_out
          else
              echo "Skipping processing: (corresponding result exists and not empty: $log_file)"
          fi
        else
            echo "Skipping processing: (model doesn't exists: $model[All])"
        fi
    done
done < "$traces_txt"
echo "Task Generated: $task_out"
echo "Example: $(tail -n 4 $task_out)"
