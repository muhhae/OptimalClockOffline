#!/bin/bash

input_file="traces.txt"
output_file="$HOME/task"

while IFS= read -r link; do
    if [ -z "$link" ] || [[ "$link" == \#* ]]; then
        continue
    fi
    filename=$(basename $link)
    echo "shell:1:1:1:LC_ALL=C wget -O /mnt/gv1/traces/$filename $link" >> $output_file

done < "$input_file"

echo "Finished adding task to $output_file."
