import glob
import os
import re
from dataclasses import dataclass
from pathlib import Path
from pathlib import Path

import pandas as pd


def extract_desc(filename: str) -> (str, list):
    prefix = filename[: filename.rfind("[")]
    desc = filename[filename.rfind("[") + 1 : filename.rfind("]")]
    desc = desc.split(",")
    dict_data = {x[: x.find("=")]: x[x.find("=") + 1 :] for x in desc if "=" in x}
    desc = [x for x in desc if "=" not in x]
    desc.append(dict_data)
    return (prefix, desc)


@dataclass
class OutputLog:
    trace_path: str
    cache_size: int
    ignore_obj_size: bool
    miss_ratio: float
    n_req: int
    n_promoted: int


result_dir = "../result/log"
output_dir = "../result/graph"

urls = []
with open("../reasonable_traces.txt") as f:
    urls = [line.strip() for line in f if line.strip()]


def sort_key(filename):
    desc = extract_desc(filename)[1]
    if "model" in desc[-1]:
        return (filename, desc[0], desc[-1]["model"])
    return (filename, desc[0])


files = sorted(glob.glob(os.path.join(result_dir, "*.csv")), key=sort_key)
os.makedirs(os.path.dirname("../result/README.md"), exist_ok=True)
os.makedirs(os.path.dirname("../result/TEST.md"), exist_ok=True)
readme = open("../result/README.md", "w")
test_readme = open("../result/TEST.md", "w")
readme.write("""# RESULT AGAINST TEST DATA
# [Test Data](./result/TEST.md)
# [Box Plot](./overall/README.md)
# [Box Plot (obj_size_ignored)](./overall/README_obj_size_ignored.md)
# Line Plot
""")
test_readme.write("""# RESULT AGAINST TRAIN DATA
# [Train Data](./result/README.md)
# [Box Plot](./overall/README.md)
# [Box Plot (obj_size_ignored)](./overall/README_obj_size_ignored.md)
# Line Plot
""")

current_prefix = ""
current_base_file = ""

test_data = False

for file in files:
    if Path(file).stat().st_size == 0:
        continue

    prefix, desc = extract_desc(file)
    if desc.count("ML"):
        continue

    df = pd.read_csv(file)
    if df.empty:
        continue

    logs = [OutputLog(**row) for row in df.to_dict(orient="records")]
    trace_path = logs[0].trace_path
    cache_size = logs[0].cache_size
    promotion_reduced = logs[0].n_promoted - logs[-1].n_promoted
    n_req = logs[0].n_req

    if not file.count("ML"):
        current_base_file = file[file.rfind("/") + 1 :]
        current_base_file = Path(current_base_file).with_suffix(".png")

    if desc.count("TEST"):
        test_data = True
    md = test_readme if test_data else readme
    if current_prefix != prefix:
        md.write(f"## {prefix[prefix.rfind('/') + 1 :]}")
        url = ""
        for u in urls:
            if u.find(prefix[prefix.rfind("/") + 1 :] + ".oracleGeneral") != -1:
                url = u
                break
        md.write(f" {url}\n")
    md.write(f"> ![graph](./graph/{current_base_file})  \n")
    md.write(f"> **Trace Path**: {trace_path}  \n")
    md.write(f"> **Log Path**: [{file}]({file})  \n")
    md.write(f"> **Desc**: {desc}  \n")
    md.write(f"> **Cache Size**: {cache_size}  \n")
    md.write(f"> **Ignore Obj Size**: {logs[0].ignore_obj_size}  \n")
    md.write(f"> **Total Request**: {n_req:,}  \n")
    md.write(f"> **First Promotion**: {logs[0].n_promoted:,}  \n")
    md.write(f"> **Last Promotion**: {logs[-1].n_promoted:,}  \n")
    md.write(f"> **Promotion Reduced**: {promotion_reduced:,}  \n\n")

    if current_prefix != prefix:
        test_data = False
        current_prefix = prefix
