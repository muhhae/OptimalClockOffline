relative_cache_sizes=(0.001 0.01 0.1 0.2 0.4)
max_iteration=1
basedir="/mnt/v0"

traces_txt="$1"

usage() {
    echo "Usage: bash $0 -r traces_txt -d traces_dir -o out_dir -m model -a add_desc -t task_out"
    exit 1
}

# Parse options
while getopts "d:o:m:a:t:r:" opt; do
    case $opt in
        d) traces_dir="$OPTARG" ;;
        o) out_dir="$OPTARG" ;;
        m) model="$OPTARG" ;;
        t) task_out="$OPTARG" ;;
        r) traces_txt="$OPTARG" ;;
        a) add_desc="$OPTARG" ;;
        *) usage ;;
    esac
done
if [ -n "$add_desc" ]; then
    add_desc=",$add_desc"
fi
if [ -z "$traces_dir" ] || [ -z "$out_dir" ] || [ -z "$model" ] || [ -z "$traces_txt" ]; then
    usage
fi


features=""
case "$model" in
    "LR_1")
        features="-I F32 -F rtime_since vtime_since clock_freq lifetime_freq"
        ;;
    "LR_1_robust_scaler")
        features="-I F32 -F rtime_since vtime_since clock_freq lifetime_freq"
        ;;
    "LR_1_std_scaler")
        features="-I F32 -F rtime_since vtime_since clock_freq lifetime_freq"
        ;;
    "LR_1_log")
        features="-I F32 -F rtime_since_log vtime_since_log clock_freq_log lifetime_freq_log"
        ;;
    "LR_1_mean")
        features="-I F32 -F rtime_since_log vtime_since_log clock_freq_std lifetime_freq_std"
        ;;
    "LR_2")
        features="-I F32 -F vtime_since clock_freq"
        ;;
    "LR_2_log")
        features="-I F32 -F vtime_since_log clock_freq_log"
        ;;
    "LR_2_mean")
        features="-I F32 -F vtime_since_log clock_freq_std"
        ;;
    "LR_3")
        features="-I F32 -F rtime_since clock_freq"
        ;;
    "LR_3_log")
        features="-I F32 -F rtime_since_log clock_freq_log"
        ;;
    "LR_3_mean")
        features="-I F32 -F rtime_since_log clock_freq_std"
        ;;
    "LR_4")
        features="-I F32 -F rtime_since vtime_since rtime_between clock_freq lifetime_freq"
        ;;
    "LR_4_std_scaler")
        features="-I F32 -F rtime_since vtime_since rtime_between clock_freq lifetime_freq"
        ;;
    "LR_4_robust_scaler")
        features="-I F32 -F rtime_since vtime_since rtime_between clock_freq lifetime_freq"
        ;;
    "LR_4_log")
        features="-I F32 -F rtime_since_log vtime_since_log rtime_between_log clock_freq_log lifetime_freq_log"
        ;;
    "LR_4_mean")
        features="-I F32 -F rtime_since_log vtime_since_log rtime_between_log clock_freq_std lifetime_freq_std"
        ;;
    "LR_5")
        features="-I F32 -F rtime_since rtime_between clock_freq lifetime_freq"
        ;;
    "LR_5_imba")
        features="-I F32 -F rtime_since rtime_between clock_freq lifetime_freq"
        ;;
    "LR_6")
        features="-I F32 -F rtime_since rtime_between clock_freq lifetime_freq"
        ;;
    "LR_6_imba")
        features="-I F32 -F rtime_since rtime_between clock_freq lifetime_freq"
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
    file="$traces_dir/$filename"
    basename="${filename%%.oracleGeneral*}"
    size=$(stat --format="%s" "$file")

    gb=$(( (size + 1024*1024*1024 - 1) / (1024*1024*1024) ))
    min_dram=$(( gb+1 ))

    for cache_size in "${relative_cache_sizes[@]}"; do
        if [ -e "$model_dir[$cache_size,ignore_obj_size$add_desc].onnx" ]; then
            log_file="$out_dir/log/${basename}[${cache_size},ignore_obj_size,ML$add_desc,model=${model}_${cache_size}].csv"
            echo "shell:1:$min_dram:1:~/OptimalClockOffline/build/cacheSimulator $file $features -o $out_dir -r $cache_size -i 1 --ignore-obj-size -d ignore_obj_size,ML$add_desc,model=${model}_$cache_size -a ML -m $model_dir[$cache_size,ignore_obj_size$add_desc].onnx" >> $task_out
        else
            echo "Skipping processing: (model doesn't exists: $model[$cache_size,ignore_obj_size$add_desc])"
        fi
        if [ -e "$model_dir[All,ignore_obj_size$add_desc].onnx" ]; then
            log_file="$out_dir/log/${basename}[${cache_size},ignore_obj_size,ML$add_desc,model=${model}_All].csv"
            echo "shell:1:$min_dram:1:~/OptimalClockOffline/build/cacheSimulator $file $features -o $out_dir -r $cache_size -i 1 --ignore-obj-size -d ignore_obj_size,ML$add_desc,model=${model}_All -a ML -m $model_dir[All,ignore_obj_size$add_desc].onnx" >> $task_out
        else
            echo "Skipping processing: (model doesn't exists: $model[All,ignore_obj_size$add_desc])"
        fi
        if [ -e "$model_dir[$cache_size$add_desc].onnx" ]; then
            log_file="$out_dir/log/${basename}[${cache_size},ML$add_desc,model=${model}_${cache_size}'].csv"
            echo "shell:1:$min_dram:1:~/OptimalClockOffline/build/cacheSimulator $file $features -o $out_dir -r $cache_size -i 1 -d ML$add_desc,model=${model}_$cache_size -a ML -m $model_dir[$cache_size$add_desc].onnx" >> $task_out
        else
            echo "Skipping processing: (model doesn't exists: $model[$cache_size$add_desc])"
        fi
        if [ -e "$model_dir[All$add_desc].onnx" ]; then
            log_file="$out_dir/log/${basename}[${cache_size},ML$add_desc,model=${model}_All].csv"
            echo "shell:1:$min_dram:1:~/OptimalClockOffline/build/cacheSimulator $file $features -o $out_dir -r $cache_size -i 1 -d ML$add_desc,model=${model}_All -a ML -m $model_dir[All$add_desc].onnx" >> $task_out
        else
            echo "Skipping processing: (model doesn't exists: $model[All$add_desc])"
        fi
    done
done < "$traces_txt"
