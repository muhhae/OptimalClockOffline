#!/bin/bash

urls=(
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/twitter/cluster50.oracleGeneral.zst"
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/metaCDN/meta_rnha.oracleGeneral.zst"
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/alibabaBlock/v2/7.oracleGeneral.zst"
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/wiki/wiki_2019t.oracleGeneral.zst"
)

for url in "${urls[@]}"; do
    filename="$(basename "$url")"
    if [ -f "$filename" ]; then
        echo "Skipping: $filename (already exists)"
    else
        echo "Downloading: $url"
        wget "$url" -O "$filename"
    fi
done

echo "All downloads completed!"
