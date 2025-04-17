#!/bin/bash

input_file="$1"
if [[ -z $input_file ]]; then
  echo "[arg] input_file required"
  exit 1
fi

while IFS= read -r link; do
    if [ -z "$link" ] || [[ "$link" == \#* ]]; then
        continue
    fi
    filename=$(basename $link)
    if [ -f /mnt/gv0/traces/$filename]; then
        echo "Skipping downloading trace, $filename exist"
        continue
    fi
    wget -O /mnt/gv0/traces/$filename $link"
    echo "Finished downloading trace $filename"
done < "$input_file"

echo "Finished downloading trace"
