import plotly.express as px
import plotly.io as pio
import numpy as np
import typing as T
import glob
import os
import re
from pathlib import Path
from common import extract_desc, OutputLog, ordinal
import tabulate as tb


import pandas as pd

# Available templates:
# ggplot2
# seaborn
# simple_white
# plotly
# plotly_white
# plotly_dark
# presentation
# xgridoff
# ygridoff
# gridon
# none
pio.templates.default = "plotly_dark"


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
    models_metrics: T.List[str],
):
    TN_ps = {}
    FN_ps = {}
    TP_ps = {}
    FP_ps = {}

    for p in models_metrics:
        f = open(p, "r")
        content = f.read()
        kw = "Confusion Matrix"
        content = content[content.find(kw) + len(kw) :]
        content = content[: content.find(kw)]
        content = content.replace(":", "").strip()
        py_v = re.sub(r"\s+", " ", content.strip())
        py_v = re.sub(r"(?<=\d) (?=\d)", ", ", py_v)
        py_v = re.sub(r"\] \[", "], [", py_v)

        if py_v == "":
            continue

        x = eval(py_v)

        TN = x[0][0]
        FP = x[0][1]
        FN = x[1][0]
        TP = x[1][1]

        TN_p = 0
        TP_p = 0
        FN_p = 0
        FP_p = 0

        if TN != 0:
            TN_p = TN / (TN + FN) * 100
        if TP != 0:
            TP_p = TP / (TP + FP) * 100
        if FN != 0:
            FN_p = FN / (TN + FN) * 100
        if FP != 0:
            FP_p = FP / (TP + FP) * 100

        model = p.replace(".md", "").replace(".txt", "")
        model = Path(p).stem

        model, desc = extract_desc(model)
        size = desc[0]
        if size != "All":
            size = "spec"
        model += "_" + size
        for d in [TN_ps, TP_ps, FN_ps, FP_ps]:
            if model not in d:
                d[model] = []

        TN_ps[model].append(TN_p)
        TP_ps[model].append(TP_p)
        FN_ps[model].append(FN_p)
        FP_ps[model].append(FP_p)

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
    md.write(
        "$\\dfrac{Base Promotion - Model Promotion}{Base Promotion} \\times 100$  \n"
    )
    md.write(tb.tabulate(p_data, headers="keys", tablefmt="github") + "  \n\n")
    md.write("## Miss Ratio Reduced (%)  \n")
    md.write(
        "$\\dfrac{Base Miss Ratio - Model Miss Ratio}{Base Miss Ratio} \\times 100$  \n"
    )
    md.write(tb.tabulate(mr_data, headers="keys", tablefmt="github") + "  \n\n")
    md.write("# Model Summaries Plot  \n")

    models = list(better_than_base.keys())
    mr = list(miss_ratio_reduced.values())
    mr = [[x * 100 for x in l] for l in mr]
    pr = list(promotion_reduced.values())
    pr = [[x * 100 for x in l] for l in pr]

    for x, title in zip([mr, pr], ["Miss Ratio", "Promotion"]):
        data = []
        for model_name, values in zip(models, x):
            for val in values:
                data.append({"Model": model_name, f"{title} Reduced (%)": val})

        df = pd.DataFrame(data)

        fig = px.box(
            df,
            x=f"{title} Reduced (%)",
            y="Model",
            title=f"{title} Reduced (%)",
            color="Model",
        )
        fig.update_xaxes(dtick=10)
        fig.update_layout(
            xaxis_title=title,
            yaxis_title=None,
            font=dict(size=14),
            height=30 * len(models),
            width=800,
            showlegend=False,
        )
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(showgrid=True)

        md.write(f"## {title} Reduced (%) \n")
        md.write(
            f"$\\dfrac{{Base {title} - Model {title}}}{{Base {title}}} \\times 100$  \n\n"
        )
        svg = fig.to_image(format="svg").decode("utf-8")
        md.write(f"{svg}  \n")

    models = list(TN_ps.keys())
    TN_ps_v = list(TN_ps.values())
    TP_ps_v = list(TP_ps.values())
    FN_ps_v = list(FN_ps.values())
    FP_ps_v = list(FP_ps.values())

    for x, title in zip(
        [TN_ps_v, TP_ps_v, FN_ps_v, FP_ps_v],
        [
            "True Negatives (%)",
            "True Positives (%)",
            "False Negatives (%)",
            "False Positives (%)",
        ],
    ):
        data = []
        for model_name, values in zip(models, x):
            for val in values:
                data.append({"Model": model_name, title: val})

        df = pd.DataFrame(data)

        fig = px.box(
            df,
            x=title,
            y="Model",
            title=title,
            color="Model",
        )
        fig.update_xaxes(dtick=10)
        fig.update_layout(
            xaxis_title=title,
            yaxis_title=None,
            font=dict(size=14),
            height=30 * len(models),  # similar to figsize in matplotlib
            width=800,
            showlegend=False,
        )
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(showgrid=True)

        md.write(f"## {title} \n")
        svg = fig.to_image(format="svg").decode("utf-8")
        md.write(f"{svg}  \n")

    md.write("# Individual Workload Result  \n")

    models_result = []
    for f in ml:
        if Path(f).stat().st_size == 0:
            continue
        prefix, desc = extract_desc(f)
        model = desc[-1]["model"]
        size = model.split("_")[-1]
        size = "spec" if size != "All" else size
        model = model[: model.rfind("_") + 1] + size
        df = pd.read_csv(f)
        log = [OutputLog(**row) for row in df.to_dict(orient="records")][0]
        models_result.append(
            {
                "model": model,
                "trace": log.trace_path[: log.trace_path.rfind(".oracleGeneral")],
                "promotion": log.n_promoted,
                "miss_ratio": log.miss_ratio,
                "cache_size": desc[0],
                "ignore_obj_size": desc.count("ignore_obj_size"),
            }
        )
    models_result = pd.DataFrame(models_result)
    traces = models_result["trace"].unique()
    cache_sizes = models_result["cache_size"].unique()
    for trace in traces:
        md.write(f"## {trace}  \n")
        for ignore_obj_size in range(2):
            if ignore_obj_size:
                md.write("## Object Size Ignored  \n")
            for cache_size in cache_sizes:
                base_result = next(
                    (
                        x
                        for x in base
                        if Path(extract_desc(x)[0]).name == trace
                        and extract_desc(x)[1].count("ignore_obj_size")
                        == ignore_obj_size
                        and extract_desc(x)[1][0] == cache_size
                    ),
                    None,
                )
                if base_result is None:
                    continue
                trace_model_result = models_result.query(
                    "trace == @trace and ignore_obj_size == @ignore_obj_size and cache_size == @cache_size"
                )
                if Path(base_result).stat().st_size == 0:
                    continue
                prefix, desc = extract_desc(base_result)
                df = pd.read_csv(base_result)
                if df.empty:
                    continue
                logs = [OutputLog(**row) for row in df.to_dict(orient="records")]
                base_result = pd.DataFrame(
                    [
                        {
                            "model": f"Offline Clock {ordinal(i + 1)} iteration",
                            "promotion": v.n_promoted,
                            "miss_ratio": v.miss_ratio,
                        }
                        for i, v in enumerate(logs)
                    ]
                )
                trace_result = pd.concat(
                    [
                        base_result,
                        trace_model_result[["model", "promotion", "miss_ratio"]],
                    ],
                    ignore_index=True,
                )
                fig = px.scatter(
                    trace_result,
                    x="promotion",
                    y="miss_ratio",
                    color="model",
                    title=f"trace {trace} with relative cache size={cache_size}",
                )
                fig.update_layout(
                    xaxis_title="Promotion",
                    yaxis_title="Miss Ratio",
                    font=dict(size=14),
                    width=800,
                    showlegend=True,
                )
                fig.update_xaxes(showgrid=True)
                fig.update_yaxes(showgrid=True)
                svg = fig.to_image(format="svg").decode("utf-8")
                md.write(f"### {cache_size}  \n")
                md.write(svg + "  \n")


# Files Variables

files = sorted(glob.glob(os.path.join(result_dir, "*.csv")), key=sort_key)
models_metric_files = glob.glob("ML/model/*.md") + glob.glob("ML/model/*.txt")
models_metric_files = sorted(models_metric_files, key=sort_key)

model_metrics: T.Dict[bool, T.List[str]] = {}
model_metrics[True] = [f for f in models_metric_files if f.count("ignore_obj_size")]
model_metrics[False] = [
    f for f in models_metric_files if not f.count("ignore_obj_size")
]

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

ModelSummaries(
    base_test[0],
    ML_test[0],
    "../result/test_obj_size_not_ignored.md",
    "Test Data Result Obj Size Not Ignored",
    model_metrics[0],
)
ModelSummaries(
    base_test[1],
    ML_test[1],
    "../result/test_obj_size_ignored.md",
    "Test Data Result Obj Size Ignored",
    model_metrics[1],
)
ModelSummaries(
    base_test[0] + base_test[1],
    ML_test[0] + ML_test[1],
    "../result/test.md",
    "Test Data Result Combined",
    model_metrics[0] + model_metrics[1],
)
ModelSummaries(
    base_test[0],
    ML_test[0],
    "../result/test_obj_size_not_ignored.html",
    "Test Data Result Obj Size Not Ignored",
    model_metrics[0],
)
ModelSummaries(
    base_test[1],
    ML_test[1],
    "../result/test_obj_size_ignored.html",
    "Test Data Result Obj Size Ignored",
    model_metrics[1],
)
ModelSummaries(
    base_test[0] + base_test[1],
    ML_test[0] + ML_test[1],
    "../result/test.html",
    "Test Data Result Combined",
    model_metrics[0] + model_metrics[1],
)
