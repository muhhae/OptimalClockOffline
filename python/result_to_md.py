import numpy as np
import typing as T
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
readme.write("""# RESULT AGAINST TRAIN DATA
# [Test Data](./TEST.md)
# [Box Plot](./overall/README.md)
# [Box Plot (obj_size_ignored)](./overall/README_obj_size_ignored.md)
# Line Plot
""")
test_readme.write("""# RESULT AGAINST TEST DATA
# [Train Data](./README.md)
# [Box Plot](./overall/README.md)
# [Box Plot (obj_size_ignored)](./overall/README_obj_size_ignored.md)
# Line Plot
""")

current_prefix = ""
current_base_file = ""

test_data = False
# [trace, cache_size, ignore_obj_size] -> model, miss_ratio
best_ml_models: T.Dict[tuple[str, float, bool], tuple[str, float]] = {}
# [trace, cache_size, ignore_obj_size] -> miss_ratio
base_result: T.Dict[tuple[str, float, bool], float] = {}
# [trace, cache_size, ignore_obj_size] -> miss_ratio
base_promotion: T.Dict[tuple[str, float, bool], int] = {}
# [model] -> bool
better_than_base: T.Dict[str, T.List[bool]] = {}
# [model] -> float
promotion_reduced: T.Dict[str, T.List[float]] = {}
# [model] -> float
miss_ratio_reduced: T.Dict[str, T.List[float]] = {}

for file in files:
    if Path(file).stat().st_size == 0:
        continue
    prefix, desc = extract_desc(file)
    ignore_size = desc.count("ignore_obj_size")
    if not desc.count("TEST"):
        continue
    if desc.count("ML"):
        continue
    df = pd.read_csv(file)
    if df.empty:
        continue
    logs = [OutputLog(**row) for row in df.to_dict(orient="records")]
    base_result[prefix, float(desc[0]), ignore_size] = logs[0].miss_ratio
    base_promotion[prefix, float(desc[0]), ignore_size] = logs[0].n_promoted

for file in files:
    if Path(file).stat().st_size == 0:
        continue

    prefix, desc = extract_desc(file)
    ignore_size = desc.count("ignore_obj_size")
    if not desc.count("ML"):
        continue

    model = desc[-1]["model"]
    if model.count("v") == 0 and model.count("LR") == 0:
        continue
    size = model.split("_")[-1]
    size_pos = model.rfind("_")
    model = model[:size_pos]
    if size != "All":
        size = "spec"
    model = model + "_" + size
    df = pd.read_csv(file)
    if df.empty:
        continue
    logs = [OutputLog(**row) for row in df.to_dict(orient="records")]
    log = logs[0]

    if model not in better_than_base:
        better_than_base[model] = []
    if model not in promotion_reduced:
        promotion_reduced[model] = []
    if model not in miss_ratio_reduced:
        miss_ratio_reduced[model] = []

    key = prefix, float(desc[0]), ignore_size
    if key not in base_result:
        continue

    better_than_base[model].append(log.miss_ratio < base_result[key])
    miss_ratio_reduced[model].append(
        (base_result[key] - log.miss_ratio) / base_result[key]
    )
    promotion_reduced[model].append(
        (base_promotion[key] - log.n_promoted) / base_promotion[key]
    )

    if (key) not in best_ml_models or best_ml_models[key][1] > log.miss_ratio:
        best_ml_models[key] = (model, log.miss_ratio)
        continue
    if best_ml_models[key][1] == log.miss_ratio:
        prev_model = best_ml_models[key][0]
        new_model = prev_model + "," + model
        best_ml_models[key] = (new_model, log.miss_ratio)

model_best_count = {}
for k in best_ml_models:
    model = best_ml_models[k][0]
    model = model.split(",")
    for e in model:
        if e not in model_best_count:
            model_best_count[e] = 0
        model_best_count[e] += 1

test_readme.write("# Model Summaries  \n")
test_readme.write(
    "|Model|Best Model|Better Than Base (%)|Mean Miss Ratio Reduced (%)|Median Miss Ratio Reduced (%)|Mean Promotion Reduced (%)|Median Promotion Reduced (%)|  \n"
)
test_readme.write("|---|---|---|---|---|---|---|  \n")
for k in better_than_base:
    v = better_than_base[k]
    p = promotion_reduced[k]
    m = miss_ratio_reduced[k]
    b = 0
    if k in model_best_count:
        b = model_best_count[k]
    test_readme.write(
        f"|{k}|{b}|{v.count(True) / len(v) * 100}|{np.mean(m)}|{np.median(m)}|{np.mean(p) * 100}|{np.median(p) * 100}|  \n"
    )


for file in files:
    if Path(file).stat().st_size == 0:
        continue

    prefix, desc = extract_desc(file)
    if desc.count("ML"):
        continue
    if not desc.count("TEST"):
        continue

    df = pd.read_csv(file)
    if df.empty:
        continue

    logs = [OutputLog(**row) for row in df.to_dict(orient="records")]
    trace_path = logs[0].trace_path
    cache_size = logs[0].cache_size
    promotion_reduced = logs[0].n_promoted - logs[-1].n_promoted
    n_req = logs[0].n_req

    current_base_file = file[file.rfind("/") + 1 :]
    current_base_file = Path(current_base_file).with_suffix(".png")

    key = prefix, float(desc[0]), logs[0].ignore_obj_size
    best_model = best_ml_models[key]
    better_than_base = best_model[1] < logs[0].miss_ratio

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
    # md.write(f"> **Log Path**: [{file}]({file})  \n")
    md.write(f"> **Desc**: {desc}  \n")
    md.write(f"> **Cache Size**: {cache_size}  \n")
    # md.write(f"> **Ignore Obj Size**: {logs[0].ignore_obj_size}  \n")
    md.write(f"> **Total Request**: {n_req:,}  \n")
    md.write(f"> **Best Model**: {best_model[0]} => {best_model[1]}  \n")
    md.write(f"> **Better Than Base**: {'True' if better_than_base else 'False'}  \n")
    # md.write(f"> **First Promotion**: {logs[0].n_promoted:,}  \n")
    # md.write(f"> **Last Promotion**: {logs[-1].n_promoted:,}  \n")
    # md.write(f"> **Promotion Reduced**: {promotion_reduced:,}  \n\n")

    if current_prefix != prefix:
        test_data = False
        current_prefix = prefix
