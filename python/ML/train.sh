datasets_dir=$1
out_dir=$2
model=$3
task_out=$4

if [[ -z $task_out ]]; then
    task_out="$HOME/train-$model.taskfile"
fi

if [ -z "$datasets_dir" ] || [ -z "$out_dir" ] || [ -z "$model" ]; then
    echo "Usage: bash train.sh [datasets_dir] [out_dir] [model] [task_out]"
    exit 1
fi

shopt -s nullglob
echo "" > $task_out

train() {
    descs="$1"
    model_desc="$2"
    if [ -z "$model_desc" ]; then
      model_desc=$descs
    fi
    ram_usage=128
    datasets=""
    for desc in $descs; do
      for file in $datasets_dir/*\["$desc"\].csv; do
          datasets+="'$file',"
      done
    done
    if [ -z "$datasets" ]; then
        return
    fi
    datasets=${datasets%?}
    echo "shell:1:$ram_usage:20:cd $HOME/OptimalClockOffline/python/ML && \
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
train "\"${relative_size[@]}\"" "All"

descs=""
for s in ${relative_size[@]}; do
  descs+="$s,ignore_obj_size"
done
train "\"$descs\"" "All,ignore_obj_size"

echo "Task Generated: $task_out"
echo "Example: $(tail -n 1 $task_out)"
echo "Example: $(head -n 1 $task_out)"
