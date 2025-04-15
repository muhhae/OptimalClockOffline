#!/bin/bash

input_file="traces.txt"
output_file="reasonable_traces.txt"

MIN_SIZE=$((512 * 1024 * 1024))  # 512 MB
MAX_SIZE=$((32 * 1024 * 1024 * 1024))  # 48 GB

get_file_size() {
    url=$1
    size=$(curl -sI "$url" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')
    echo "$size"
}

while IFS= read -r link; do
    if [ -z "$link" ] || [[ "$link" == \#* ]]; then
        continue
    fi

    file_size=$(get_file_size "$link")

    if [ -n "$file_size" ] && [ "$file_size" -ge "$MIN_SIZE" ] && [ "$file_size" -le "$MAX_SIZE" ]; then
        echo "$link" >> "$output_file"
        echo "Added $link with size $file_size bytes."
    fi
done < "$input_file"

echo "Finished checking links. Valid links are in $output_file."
