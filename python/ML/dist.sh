datasets_dir=$1
out_dir=$2
if [ -z "$datasets_dir" ] || [ -z "$out_dir" ]; then
    echo "Usage: bash dist.sh [datasets_dir] [out_dir]"
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
    ram_usage=32
    # echo "Ram Usage: $ram_usage"
    echo "shell:1:$ram_usage:2:cd ~/OptimalClockOffline/python/ML && python -c \"import common as c;c.AddDatasets($datasets);c.SetupData();lr.SetupModel(1000);lr.Train();c.SaveModel('$out_dir/model[$size].pkl')\"" >> ~/task
done
