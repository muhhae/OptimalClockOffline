datasets_dir=$1
out_dir=$2
model=$3
if [ -z "$datasets_dir" ] || [ -z "$out_dir" ] || [ -z "$model" ]; then
    echo "Usage: bash dist.sh [datasets_dir] [out_dir] [model]"
    exit 1
fi
relative_size=(0.001 0.01 0.1 0.2 0.4)
shopt -s nullglob
rm ~/task
for size in ${relative_size[@]}; do
    datasets=""
    for file in $datasets_dir/*\["$size"\].csv; do
        datasets+="'$file',"
    done
    if [ -z "$datasets" ]; then
        continue
    fi
    datasets=${datasets%?}
    # ram_usage=$(python -c "import common;common.AddDatasets($datasets);import var;print(int(var.df.memory_usage(deep=True).sum()/1024**3))")
    # ram_usage=$((ram_usage+4))
    ram_usage=32
    # echo "Ram Usage: $ram_usage"
    echo "shell:1:$ram_usage:20:cd ~/OptimalClockOffline/python/ML &&\
python -c \"import common as c;\
import $model as m;\
c.AddDatasets($datasets);\
c.SetupData();\
m.SetupModel();\
m.Train();\
c.SaveModel('$out_dir/$model[$size].pkl');\
c.ExportONNX('$out_dir/$model[$size].onnx');\
c.PlotSave('$out_dir/$model[$size].png');\
c.Test()\" > $out_dir/$model[$size].desc" >> ~/task

    datasets=""
    for file in $datasets_dir/*\["$size,ignore_obj_size"\].csv; do
        datasets+="'$file',"
    done
    if [ -z "$datasets" ]; then
        continue
    fi
    datasets=${datasets%?}
    # ram_usage=$(python -c "import common;common.AddDatasets($datasets);import var;print(int(var.df.memory_usage(deep=True).sum()/1024**3))")
    # ram_usage=$((ram_usage+4))
    ram_usage=32
    # echo "Ram Usage: $ram_usage"
    echo "shell:1:$ram_usage:20:cd ~/OptimalClockOffline/python/ML &&\
python -c \"import common as c;\
import $model as m;\
c.AddDatasets($datasets);\
c.SetupData();\
m.SetupModel();\
m.Train();\
c.SaveModel('$out_dir/$model[$size,ignore_obj_size].pkl');\
c.ExportONNX('$out_dir/$model[$size,ignore_obj_size].onnx');\
c.PlotSave('$out_dir/$model[$size,ignore_obj_size].png');\
c.Test()\" > $out_dir/$model[$size,ignore_obj_size].desc" >> ~/task
done
size="All"
datasets=""
F="$(/usr/bin/find "$datasets_dir" -maxdepth 1 -name "*.csv" | grep -v "size].csv$")"
while IF= read -r l; do
    datasets+="'$l',"
done <<< "$F"
datasets=${datasets%?}
# ram_usage=$(python -c "import common;common.AddDatasets($datasets);import var;print(int(var.df.memory_usage(deep=True).sum()/1024**3))")
# ram_usage=$((ram_usage+4))
ram_usage=100
# echo "Ram Usage: $ram_usage"
echo "shell:1:$ram_usage:20:cd ~/OptimalClockOffline/python/ML &&\
python -c \"import common as c;\
import $model as m;\
c.AddDatasets($datasets);\
c.SetupData();\
m.SetupModel();\
m.Train();\
c.SaveModel('$out_dir/$model[$size].pkl');\
c.ExportONNX('$out_dir/$model[$size].onnx');\
c.PlotSave('$out_dir/$model[$size].png');\
c.Test()\" > $out_dir/$model[$size].desc" >> ~/task

datasets=""
for file in $datasets_dir/*,ignore_obj_size\].csv; do
    datasets+="'$file',"
done
datasets=${datasets%?}
# ram_usage=$(python -c "import common;common.AddDatasets($datasets);import var;print(int(var.df.memory_usage(deep=True).sum()/1024**3))")
# ram_usage=$((ram_usage+4))
ram_usage=100
# echo "Ram Usage: $ram_usage"
echo "shell:1:$ram_usage:20:cd ~/OptimalClockOffline/python/ML &&\
python -c \"import common as c;\
import $model as m;\
c.AddDatasets($datasets);\
c.SetupData();\
m.SetupModel();\
m.Train();\
c.SaveModel('$out_dir/$model[$size,ignore_obj_size].pkl');\
c.ExportONNX('$out_dir/$model[$size,ignore_obj_size].onnx');\
c.PlotSave('$out_dir/$model[$size,ignore_obj_size].png');\
c.Test()\" > $out_dir/$model[$size,ignore_obj_size].desc" >> ~/task
