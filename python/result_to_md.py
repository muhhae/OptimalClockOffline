import numpy as np
import typing as T
import glob
import os
from pathlib import Path
from common import extract_desc, OutputLog
import tabulate as tb
import matplotlib.pyplot as plt


import pandas as pd


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

base_log = [f for f in files if not f.count("ML")]
ML_log = [f for f in files if f.count("ML")]

test_log = [f for f in base_log if f.count("TEST")]
test_prefix = [extract_desc(e)[0] for e in test_log]
ML_test_log = [f for f in ML_log if extract_desc(f)[0] in test_prefix]

# [IgnoreObjSize] -> path
base: T.Dict[bool, T.List[str]] = {}
base[True] = [f for f in base_log if f.count("ignore_obj_size")]
base[False] = [f for f in base_log if not f.count("ignore_obj_size")]

# [IgnoreObjSize] -> path
base_test: T.Dict[bool, T.List[str]] = {}
base_test[True] = [f for f in test_log if f.count("ignore_obj_size")]
base_test[False] = [f for f in test_log if not f.count("ignore_obj_size")]

# [IgnoreObjSize] -> path
ML_test: T.Dict[bool, T.List[str]] = {}
ML_test[True] = [f for f in ML_test_log if f.count("ignore_obj_size")]
ML_test[False] = [f for f in ML_test_log if not f.count("ignore_obj_size")]

included_models = [
    "little_random_forest",
    "logistic_regression",
    "logistic_regression_v2",
    "logistic_regression_v3",
    "logistic_regression_v4",
    "LR_1",
    "LR_1_log",
    "LR_1_mean",
    "LR_2",
    "LR_2_log",
    "LR_2_mean",
    "LR_3",
    "LR_3_log",
    "LR_3_mean",
    "LR_v5",
    "LR_v5_norm",
    "LR_v6",
    "LR_v7",
    "LR_v8",
]


def ModelSummaries(
    base: T.List[str],
    ml: T.List[str],
    output_path: str,
    Title: str,
):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    md = open(output_path, "w")
    md.write(f"# {Title}  \n# Result  \n")

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

    for file in base:
        if Path(file).stat().st_size == 0:
            continue
        prefix, desc = extract_desc(file)
        ignore_size = desc.count("ignore_obj_size")
        df = pd.read_csv(file)
        if df.empty:
            continue
        logs = [OutputLog(**row) for row in df.to_dict(orient="records")]
        base_result[prefix, float(desc[0]), ignore_size] = logs[0].miss_ratio
        base_promotion[prefix, float(desc[0]), ignore_size] = logs[0].n_promoted

    for file in ml:
        if Path(file).stat().st_size == 0:
            continue

        prefix, desc = extract_desc(file)
        ignore_size = desc.count("ignore_obj_size")
        model = desc[-1]["model"]
        size = model.split("_")[-1]
        size_pos = model.rfind("_")
        model = model[:size_pos]
        if model not in included_models:
            print(model)
            continue

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

    md.write("# Model Summaries  \n")
    bt_data = {
        "Model": [],
        "Best Models on Exp.": [],
        "Better than base % of the times": [],
    }
    mr_data = {
        "Model": [],
        "Max": [],
        "Min": [],
        "Avg": [],
        "Mdn": [],
    }
    p_data = {
        "Model": [],
        "Max": [],
        "Min": [],
        "Avg": [],
        "Mdn": [],
    }
    for k in better_than_base:
        v = better_than_base[k]
        p = promotion_reduced[k]
        m = miss_ratio_reduced[k]
        b = 0
        if k in model_best_count:
            b = model_best_count[k]
        bt_data["Model"].append(k)
        bt_data["Best Models on Exp."].append(b)
        bt_data["Better than base % of the times"].append(v.count(True) / len(v) * 100)

        mr_data["Model"].append(k)
        mr_data["Max"].append(np.max(m) * 100)
        mr_data["Min"].append(np.min(m) * 100)
        mr_data["Avg"].append(np.mean(m) * 100)
        mr_data["Mdn"].append(np.median(m) * 100)

        p_data["Model"].append(k)
        p_data["Max"].append(np.max(p) * 100)
        p_data["Min"].append(np.min(p) * 100)
        p_data["Avg"].append(np.mean(p) * 100)
        p_data["Mdn"].append(np.median(p) * 100)

    md.write(tb.tabulate(bt_data, headers="keys", tablefmt="github") + "  \n\n")
    md.write("## Promotion Reduced (%)  \n")
    md.write(tb.tabulate(p_data, headers="keys", tablefmt="github") + "  \n\n")
    md.write("## Miss Ratio Reduced (%)  \n")
    md.write(tb.tabulate(mr_data, headers="keys", tablefmt="github") + "  \n\n")
    md.write("# Model Summaries Plot  \n")

    models = list(better_than_base.keys())
    mr = list(miss_ratio_reduced.values())
    pr = list(promotion_reduced.values())

    for x, title in zip([mr, pr], ["Miss Ratio", "Promotion"]):
        plt.figure(figsize=(12, len(models) / 2), constrained_layout=True)
        plt.boxplot(x, vert=False, patch_artist=True)
        plt.title(f"{title} Reduced", fontsize=14)
        plt.xlabel(title, fontsize=14)
        plt.yticks(range(1, len(models) + 1), models, fontsize=14)
        md.write(f"## {title} Reduced  \n")
        title += "_" + Title
        title = title.replace(" ", "_")
        plt.savefig(f"../result/graph/{title}.png", bbox_inches="tight")
        md.write(f"![graph](./graph/{title}.png)  \n")

    md.write("# Individual Workload Result  \n")

    current_prefix = ""
    current_base_file = ""

    for file in base:
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

        if current_prefix != prefix:
            md.write(f"## {prefix[prefix.rfind('/') + 1 :]}  \n")
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
        md.write(
            f"> **Better Than Base**: {'True' if better_than_base else 'False'}  \n"
        )
        # md.write(f"> **First Promotion**: {logs[0].n_promoted:,}  \n")
        # md.write(f"> **Last Promotion**: {logs[-1].n_promoted:,}  \n")
        # md.write(f"> **Promotion Reduced**: {promotion_reduced:,}  \n\n")

        if current_prefix != prefix:
            current_prefix = prefix


ModelSummaries(
    base_test[0],
    ML_test[0],
    "../result/test_obj_size_not_ignored.md",
    "Test Data Result Obj Size Not Ignored",
)
ModelSummaries(
    base_test[1],
    ML_test[1],
    "../result/test_obj_size_ignored.md",
    "Test Data Result Obj Size Ignored",
)
ModelSummaries(
    base_test[0] + base_test[1],
    ML_test[0] + ML_test[1],
    "../result/test.md",
    "Test Data Result Combined",
)
