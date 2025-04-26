datasets_dir=$1
out_dir=$2
model=$3
task_out=$4

if [[ -z $task_out ]]; then
    task_out="~/test-$model.taskfile"
fi

if [ -z "$datasets_dir" ] || [ -z "$out_dir" ] || [ -z "$model" ]; then
    echo "Usage: bash dist.sh [datasets_dir] [out_dir] [model] [task_out]"
    exit 1
fi

shopt -s nullglob
echo "" > $task_out

train() {
    desc="$1"
    ram_usage=128
    datasets=""
    for file in $datasets_dir/*\["$desc"\].csv; do
        datasets+="'$file',"
    done
    if [ -z "$datasets" ]; then
        continue
    fi
    datasets=${datasets%?}
    echo "shell:1:$ram_usage:20:cd ~/OptimalClockOffline/python/ML && \
python -c \"import common as c;\
import $model as m;\
c.AddDatasets($datasets);\
c.SetupData();\
m.SetupModel();\
m.Train();\
c.SaveModel('$out_dir/$model[$desc].pkl');\
c.ExportONNX('$out_dir/$model[$desc].onnx');\
c.PlotSave('$out_dir/$model[$desc].png');\
c.Test()\" > $out_dir/$model[$desc].desc" >> $task_out
}

relative_size=(0.001 0.01 0.1 0.2 0.4)
for size in ${relative_size[@]}; do
    train "$size"
    train "$size,ignore_obj_size"
done
train "All"
train "All,ignore_obj_size"
