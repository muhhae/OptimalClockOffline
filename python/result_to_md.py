import glob
import os
import re
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass
class OutputLog:
    trace_path: str
    cache_size: int
    miss_ratio: float
    n_req: int
    n_promoted: int


result_dir = "../result/log"
output_dir = "../result/graph"

urls = [
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/twitter/cluster50.oracleGeneral.zst",
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/metaCDN/meta_rnha.oracleGeneral.zst",
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/alibabaBlock/v2/7.oracleGeneral.zst",
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/wiki/wiki_2019t.oracleGeneral.zst",
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/cloudphysics/w01.oracleGeneral.bin.zst",
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/fiu/fiu_cheetah.cs.fiu.edu-110108-113008.oracleGeneral.zst",
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/metaKV/meta_kvcache_traces_1.oracleGeneral.bin.zst",
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/metaStorage/block_traces_5.oracleGeneral.bin.zst",
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/msr/msr_prxy_1.oracleGeneral.zst",
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/systor/2016_LUN1.oracleGeneral.zst",
    "https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/tencentBlock/v2/traces/1351.oracleGeneral.zst",
]


def extract_desc(filename):
    prefix = filename[: filename.rfind("[")]
    desc = filename[filename.rfind("[") + 1 : filename.rfind("]")]
    return (prefix, desc)


files = sorted(glob.glob(os.path.join(result_dir, "*.csv")), key=extract_desc)
readme = open("../result/README.md", "w")
readme.write("# RESULT\n")

"""
### Cluster 50 Twitter (139.655.585 req)
---
![128mib](./graph/cluster50[128MiB].png)
![256mib](./graph/cluster50[256MiB].png)
![512mib](./graph/cluster50[512MiB].png)
![1024mib](./graph/cluster50[1024MiB].png)
![2048mib](./graph/cluster50[2048MiB].png)
![0.001](./graph/cluster50[0.001].png)
![0.01](./graph/cluster50[0.01].png)
![0.1](./graph/cluster50[0.1].png)
![0.2](./graph/cluster50[0.2].png)
![0.4](./graph/cluster50[0.4].png)
"""

current_prefix = ""

for file in files:
    if Path(file).stat().st_size == 0:
        continue

    df = pd.read_csv(file)
    if df.empty:
        continue

    df = df.rename(columns={"cache_size(MiB)": "cache_size"})
    logs = [OutputLog(**row) for row in df.to_dict(orient="records")]
    trace_path = logs[0].trace_path
    cache_size = logs[0].cache_size
    promotion_reduced = logs[0].n_promoted - logs[-1].n_promoted
    n_req = logs[0].n_req

    prefix, desc = extract_desc(file)
    if current_prefix != prefix:
        readme.write(f"## {prefix[prefix.rfind('/') + 1 :]}")
        url = ""
        for u in urls:
            if u.find(prefix[prefix.rfind("/") + 1 :] + ".oracleGeneral") != -1:
                url = u
                break
        readme.write(f" {url}\n")
        current_prefix = prefix

    readme.write(
        f"> ![graph](./graph/{prefix[prefix.rfind('/') + 1 :]}[{desc}].png)  \n"
    )
    readme.write(f"> **Trace Path**: {trace_path}  \n")
    readme.write(f"> **Desc**: {desc}  \n")
    readme.write(f"> **Cache Size**: {cache_size}MiB  \n")
    readme.write(f"> **Total Request**: {n_req:,}  \n")
    readme.write(f"> **First Promotion**: {logs[0].n_promoted:,}  \n")
    readme.write(f"> **Last Promotion**: {logs[-1].n_promoted:,}  \n")
    readme.write(f"> **Promotion Reduced**: {promotion_reduced:,}  \n\n")
