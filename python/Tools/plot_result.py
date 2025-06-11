import multiprocessing
import plotly.express as px
import plotly.io as pio
import plotly.graph_objs as go
import typing as T
import glob
import os
import re
from pathlib import Path
from common import extract_desc, OutputLog, ordinal, sort_key
from docs_writer import Write, WriteFig, WriteHTML
import tabulate as tb
from collections import defaultdict


import pandas as pd

pd.set_option("display.max_rows", None)

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


result_dir = "../../result/log"

urls = []
with open("../../trace/reasonable_traces.txt") as f:
    urls = [line.strip() for line in f if line.strip()]


def ParseClassificationReport(report_string):
    overall = {}
    avg_specific = []
    class_specific = []
    report_start_index = report_string.find("Classification Report:")
    report_text = report_string[report_start_index:]
    lines = report_text.strip().split("\n")
    for line in lines:
        line = line.strip()
        if not line:
            continue
        match_overall_accuracy = re.match(r"^Accuracy:\s*([\d.]+)$", line)
        if match_overall_accuracy:
            overall["overall_accuracy"] = float(match_overall_accuracy.group(1))
            continue

        match_class = re.match(
            r"^(?P<label>(?!\baccuracy\b|\bmacro\b|\bweighted\b)\S+)\s+(?P<precision>[\d.]+)\s+(?P<recall>[\d.]+)\s+(?P<f1_score>[\d.]+)\s+(?P<support>[\d]+)$",
            line,
        )
        if match_class:
            data = match_class.groupdict()
            label = data["label"]
            class_specific.append(
                {
                    "class": label,
                    "precision": float(data["precision"]),
                    "recall": float(data["recall"]),
                    "f1-score": float(data["f1_score"]),
                    "support": int(data["support"]),
                }
            )
            continue

        match_table_accuracy = re.match(
            r"^accuracy\s+(?P<score>[\d.]+)\s+(?P<support>[\d]+)$", line
        )
        if match_table_accuracy:
            data = match_table_accuracy.groupdict()
            overall["accuracy_score"] = float(data["score"])
            overall["accuracy_support"] = int(data["support"])
            continue

        match_avg = re.match(
            r"^(?P<avg_type>macro avg|weighted avg)\s+(?P<precision>[\d.]+)\s+(?P<recall>[\d.]+)\s+(?P<f1_score>[\d.]+)\s+(?P<support>[\d]+)$",
            line,
        )
        if match_avg:
            data = match_avg.groupdict()
            avg_type_key = data["avg_type"].replace("avg", "").strip()
            avg_specific.append(
                {
                    "type": avg_type_key,
                    "precision": float(data["precision"]),
                    "recall": float(data["recall"]),
                    "f1-score": float(data["f1_score"]),
                    "support": int(data["support"]),
                }
            )
            continue
    return (
        pd.DataFrame([overall]),
        pd.DataFrame(avg_specific),
        pd.DataFrame(class_specific),
    )


def GetModelMetrics(paths: T.List[str], included_sizes: T.List[str]):
    tmp = []
    for p in paths:
        f = open(p, "r")
        content = f.read()
        report = content[
            content.find("Classification Report")
            + len("Classification Report:\n") : content.find("Confusion Matrix") - 1
        ]
        overall, avg, class_specific = ParseClassificationReport(content)
        kw = "Confusion Matrix"

        content = content[content.find(kw) + len(kw) :]
        content = content[: content.find(kw)]
        content = content.replace(":", "").strip()
        model = p.replace(".md", "").replace(".txt", "")
        model = Path(p).stem
        model, desc = extract_desc(model)
        size = desc[0]
        if size not in included_sizes:
            continue
        top_dist = 1
        if "top" in desc[-1]:
            top_dist = float(desc[-1]["top"])
        # model = f"{model}_{'spec' if size != 'All' else size}"
        model = f"{model}_{size}"

        tmp.append(
            {
                "Model": model,
                "Cache Size": size,
                "Report": report,
                "Top (%)": top_dist * 100,
            }
        )
    return pd.DataFrame(tmp)


def GetBaseResult(paths: T.List[str]):
    tmp = []
    for file in paths:
        if Path(file).stat().st_size == 0:
            continue
        prefix, desc = extract_desc(file)
        df = pd.read_csv(file)
        if df.empty:
            continue
        logs = [OutputLog(**row) for row in df.to_dict(orient="records")]
        for i, log in enumerate(logs):
            if i > 1:
                break
            tmp.append(
                {
                    "Model": f"Offline Clock {ordinal(i + 1)} iteration",
                    "Promotion": log.n_promoted,
                    "Miss Ratio": log.miss_ratio,
                    "Trace": prefix,
                    "Cache Size": float(desc[0]),
                    "Ignore Obj Size": desc.count("ignore_obj_size"),
                }
            )
    return pd.DataFrame(tmp)


def GetOtherResult(paths: T.List[str], name: str):
    tmp = []
    for file in paths:
        if Path(file).stat().st_size == 0:
            continue
        prefix, desc = extract_desc(file)
        df = pd.read_csv(file)
        if df.empty:
            continue
        logs = [OutputLog(**row) for row in df.to_dict(orient="records")]
        tmp.append(
            {
                "Model": name,
                "Promotion": logs[0].n_promoted,
                "Miss Ratio": logs[0].miss_ratio,
                "Trace": prefix,
                "Cache Size": float(desc[0]),
                "Ignore Obj Size": desc.count("ignore_obj_size"),
            }
        )
    return pd.DataFrame(tmp)


def GetModelResult(paths: T.List[str], included_sizes: T.List[str]):
    tmp = []
    for file in paths:
        if Path(file).stat().st_size == 0:
            continue
        prefix, desc = extract_desc(file)
        model = desc[-1]["model"]
        treshold = 0.5
        if "treshold" in desc[-1]:
            treshold = desc[-1]["treshold"]
        size = model.split("_")[-1]
        if size not in included_sizes:
            continue
        size_pos = model.rfind("_")
        model = model[:size_pos]
        # model = f"{model}_{'spec' if size != 'All' else size}"
        model = f"{model}[cache_size={size},treshold={treshold}]"
        df = pd.read_csv(file)
        if df.empty:
            continue
        logs = [OutputLog(**row) for row in df.to_dict(orient="records")]
        tmp.append(
            {
                "Model": f"{model}",
                "Promotion": logs[0].n_promoted,
                "Miss Ratio": logs[0].miss_ratio,
                "Trace": prefix,
                "Cache Size": float(desc[0]),
                "Ignore Obj Size": desc.count("ignore_obj_size"),
            }
        )
    return pd.DataFrame(tmp)


def WriteModelSummaries(md, html, base_result, models_result, included_sizes):
    tmp = []
    for model in models_result["Model"].unique():
        current = models_result.query("Model == @model")
        for i, x in current.iterrows():
            base_log = base_result.query(
                "Trace == @x['Trace'] and `Cache Size` == @x['Cache Size'] and Model == 'Offline Clock 1st iteration' and `Ignore Obj Size` == @x['Ignore Obj Size']"
            )
            tmp.append(
                {
                    "Model": model,
                    "Trace": x["Trace"],
                    "Cache Size": x["Cache Size"],
                    "Miss Ratio Reduced (%)": (
                        base_log["Miss Ratio"].item() - x["Miss Ratio"]
                    )
                    / base_log["Miss Ratio"].item()
                    * 100,
                    "Promotion Reduced (%)": (
                        base_log["Promotion"].item() - x["Promotion"]
                    )
                    / base_log["Promotion"].item()
                    * 100,
                    "Better Than Base": x["Miss Ratio"] < base_log["Miss Ratio"].item(),
                }
            )
    bt_data = defaultdict(list)
    mr_data = defaultdict(list)
    p_data = defaultdict(list)
    data = pd.DataFrame(tmp)
    for model in data["Model"].unique():
        current = data.query("Model == @model")
        bt_data["Model"].append(model)
        bt_data["Better than base % of the times"].append(
            current["Better Than Base"].value_counts(normalize=True).get(True, 0) * 100
        )

        mr_data["Model"].append(model)
        mr_data["Max"].append(current["Miss Ratio Reduced (%)"].max())
        mr_data["Min"].append(current["Miss Ratio Reduced (%)"].min())
        mr_data["Avg"].append(current["Miss Ratio Reduced (%)"].mean())
        mr_data["Mdn"].append(current["Miss Ratio Reduced (%)"].median())

        p_data["Model"].append(model)
        p_data["Max"].append(current["Promotion Reduced (%)"].max())
        p_data["Min"].append(current["Promotion Reduced (%)"].min())
        p_data["Avg"].append(current["Promotion Reduced (%)"].mean())
        p_data["Mdn"].append(current["Promotion Reduced (%)"].median())

    Write(md, html, "# Model Summaries  \n")
    Write(md, html, tb.tabulate(bt_data, headers="keys", tablefmt="html") + "  \n\n")
    Write(md, html, "## Promotion Reduced (%)  \n")
    Write(md, html, tb.tabulate(p_data, headers="keys", tablefmt="html") + "  \n\n")
    Write(md, html, "## Miss Ratio Reduced (%)  \n")
    Write(md, html, tb.tabulate(mr_data, headers="keys", tablefmt="html") + "  \n\n")
    Write(md, html, "# Model Summaries Plot  \n")

    for title in ["Miss Ratio Reduced (%)", "Promotion Reduced (%)"]:
        fig = px.box(
            data,
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
            height=30 * len(data["Model"].unique()),
            width=1000,
            showlegend=False,
        )
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(showgrid=True)

        Write(md, html, f"## {title}\n")
        WriteFig(md, html, fig)

    symbol_map = {
        "Offline Clock 1st iteration": "square-dot",
        "Offline Clock 2nd iteration": "diamond-dot",
        "Zipf Optimal Distribution": "x-dot",
    }
    for model in data["Model"].unique():
        if model not in symbol_map:
            symbol_map[model] = "circle"

    Write(md, html, "# Mean Promotion vs Miss Ratio  \n")
    Write(md, html, "## Cache Size All  \n")
    df = (
        data.groupby("Model")[["Promotion Reduced (%)", "Miss Ratio Reduced (%)"]]
        .mean()
        .reset_index()
        .sort_values(by="Miss Ratio Reduced (%)", ascending=False)
    )

    fig = px.scatter(
        df,
        symbol="Model",
        symbol_map=symbol_map,
        x="Promotion Reduced (%)",
        y="Miss Ratio Reduced (%)",
        color="Model",
    )
    fig.update_traces(
        marker_size=12,
        marker_line=dict(width=2),
        selector=dict(mode="markers"),
    )
    fig.update_xaxes(dtick=10)
    fig.update_layout(
        xaxis_title="Promotion Reduced (%)",
        yaxis_title="Miss Ratio Reduced (%)",
        font=dict(size=14),
        height=800,
        width=1000,
        yaxis_tickformat=".6f",
    )
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    WriteFig(md, html, fig)
    headers = df.columns.tolist()
    table_data = df.values.tolist()
    Write(
        md,
        html,
        f"{tb.tabulate(table_data, headers=headers, tablefmt='html')}  \n\n",
    )
    for size in data["Cache Size"].unique():
        if str(size) not in included_sizes:
            continue
        tmp = data[data["Cache Size"] == size]
        df = (
            tmp.groupby("Model")[["Promotion Reduced (%)", "Miss Ratio Reduced (%)"]]
            .mean()
            .reset_index()
            .sort_values(by="Miss Ratio Reduced (%)", ascending=False)
        )
        Write(md, html, f"## Cache Size {size}  \n")
        fig = px.scatter(
            df,
            symbol="Model",
            symbol_map=symbol_map,
            x="Promotion Reduced (%)",
            y="Miss Ratio Reduced (%)",
            color="Model",
        )
        fig.update_traces(
            marker_size=12,
            marker_line=dict(width=2),
            selector=dict(mode="markers"),
        )
        fig.update_xaxes(dtick=10)
        fig.update_layout(
            xaxis_title="Promotion Reduced (%)",
            yaxis_title="Miss Ratio Reduced (%)",
            font=dict(size=14),
            height=800,
            width=1000,
            yaxis_tickformat=".6f",
        )
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(showgrid=True)
        WriteFig(md, html, fig)

        headers = df.columns.tolist()
        table_data = df.values.tolist()

        Write(
            md,
            html,
            f"{tb.tabulate(table_data, headers=headers, tablefmt='html')}  \n\n",
        )

    Write(md, html, "# Median Promotion vs Miss Ratio  \n")
    Write(md, html, "## Cache Size All  \n")
    df = (
        data.groupby("Model")[["Promotion Reduced (%)", "Miss Ratio Reduced (%)"]]
        .median()
        .reset_index()
        .sort_values(by="Miss Ratio Reduced (%)", ascending=False)
    )
    fig = px.scatter(
        df,
        symbol="Model",
        symbol_map=symbol_map,
        x="Promotion Reduced (%)",
        y="Miss Ratio Reduced (%)",
        color="Model",
    )
    fig.update_traces(
        marker_size=12,
        marker_line=dict(width=2),
        selector=dict(mode="markers"),
    )
    fig.update_xaxes(dtick=10)
    fig.update_layout(
        xaxis_title="Promotion Reduced (%)",
        yaxis_title="Miss Ratio Reduced (%)",
        font=dict(size=14),
        height=800,
        width=1000,
        yaxis_tickformat=".6f",
    )
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    WriteFig(md, html, fig)

    headers = df.columns.tolist()
    table_data = df.values.tolist()

    Write(
        md,
        html,
        f"{tb.tabulate(table_data, headers=headers, tablefmt='html')}  \n\n",
    )

    for size in data["Cache Size"].unique():
        if str(size) not in included_sizes:
            continue
        tmp = data[data["Cache Size"] == size]
        df = (
            tmp.groupby("Model")[["Promotion Reduced (%)", "Miss Ratio Reduced (%)"]]
            .median()
            .reset_index()
            .sort_values(by="Miss Ratio Reduced (%)", ascending=False)
        )
        Write(md, html, f"## Cache Size {size}  \n")
        fig = px.scatter(
            df,
            symbol="Model",
            symbol_map=symbol_map,
            x="Promotion Reduced (%)",
            y="Miss Ratio Reduced (%)",
            color="Model",
        )
        fig.update_traces(
            marker_size=12,
            marker_line=dict(width=2),
            selector=dict(mode="markers"),
        )
        fig.update_xaxes(dtick=10)
        fig.update_layout(
            xaxis_title="Promotion Reduced (%)",
            yaxis_title="Miss Ratio Reduced (%)",
            font=dict(size=14),
            height=800,
            width=1000,
            yaxis_tickformat=".6f",
        )
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(showgrid=True)
        WriteFig(md, html, fig)
        headers = df.columns.tolist()
        table_data = df.values.tolist()

        Write(
            md,
            html,
            f"\n{tb.tabulate(table_data, headers=headers, tablefmt='html')}  \n\n",
        )


def WriteModelMetrics(md, html, model_metrics: pd.DataFrame):
    Write(md, html, "# Model Classification Report  \n")
    for m in model_metrics["Model"].unique():
        Write(md, html, f"## {m}  \n")
        for top in model_metrics["Top (%)"].unique():
            Write(md, html, f"### Top {top}%  \n")
            report = model_metrics.query(
                "Model == @m and `Top (%)` == @top",
            )["Report"].tolist()
            for r in report:
                Write(md, html, f"```\n{r}\n```  \n")


def WriteIndividualResult(md, html, results, included_sizes):
    Write(md, html, "# Individual Workload Result  \n")
    df = pd.concat(results, ignore_index=True)

    ignores = sorted(df["Ignore Obj Size"].unique())
    traces = df["Trace"].unique()
    sizes = df["Cache Size"].unique()

    for trace in traces:
        df_trace = df[df["Trace"] == trace]
        Write(md, html, f"## {Path(trace).stem}  \n")
        for ignore in ignores:
            df_ignore = df_trace[df_trace["Ignore Obj Size"] == ignore]
            if ignore:
                Write(md, html, "## Ignore Obj Size  \n")
            for size in sizes:
                if str(size) not in included_sizes:
                    continue
                df_size = df_ignore[df_ignore["Cache Size"] == size]
                Write(md, html, f"### {size}  \n")
                fig = px.scatter(
                    df_size,
                    x="Promotion",
                    y="Miss Ratio",
                    color="Model",
                )
                fig.update_layout(
                    xaxis_title="Promotion",
                    yaxis_title="Miss Ratio",
                    font=dict(size=14),
                    height=800,
                    width=1000,
                )
                fig.update_xaxes(showgrid=True)
                fig.update_yaxes(showgrid=True)
                WriteFig(md, html, fig)
                Write(
                    md,
                    html,
                    f"```\n{df_size.sort_values(by='Miss Ratio', ascending=False)}\n```  \n",
                )


def Analyze(
    paths: T.List[str],
    output_path: str,
    html_path: str,
    Title: str,
    models_metrics_paths: T.List[str],
    included_models: T.List[str],
    included_treshold: T.List[float],
    included_sizes: T.List[str],
):
    print(f"Analyzing for {Title}")

    model_paths = [f for f in paths if "ML" in f]
    lru_paths = [f for f in paths if "lru" in f]
    dist_optimal_paths = [f for f in paths if "dist_optimal" in f]
    base_paths = [
        f
        for f in paths
        if f not in set(model_paths) | set(lru_paths) | set(dist_optimal_paths)
    ]

    model_paths = [
        f
        for f in model_paths
        if (
            (model := extract_desc(f)[1][-1]["model"])[: model.rfind("_")]
            in included_models
            and (
                "treshold" not in extract_desc(f)[1][-1]
                or float(extract_desc(f)[1][-1]["treshold"]) in included_treshold
            )
        )
    ]
    models_metrics_paths = [
        f
        for f in models_metrics_paths
        if (p := Path(f).stem)[: p.rfind("[")] in included_models
    ]
    if len(model_paths) == 0 or len(models_metrics_paths) == 0:
        print(model_paths)
        print(models_metrics_paths)
        print(f"Empty data for {Title}")
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    os.makedirs(os.path.dirname(html_path), exist_ok=True)

    md = open(output_path, "w")
    html = open(Path(html_path), "w")
    Write(md, html, f"# {Title}  \n# Result  \n")

    model_metrics = GetModelMetrics(models_metrics_paths, included_sizes)
    base_result = GetBaseResult(base_paths)
    model_result = GetModelResult(model_paths, included_sizes)
    lru_result = GetOtherResult(lru_paths, "LRU")
    dist_optimal_result = GetOtherResult(
        dist_optimal_paths, "Zipf Optimal Distribution"
    )

    WriteModelSummaries(
        md,
        html,
        base_result,
        pd.concat(
            [model_result, base_result, dist_optimal_result],
        ),
        included_sizes,
    )
    WriteModelMetrics(md, html, model_metrics)
    WriteIndividualResult(
        md,
        html,
        [base_result, model_result, dist_optimal_result],
        included_sizes,
    )
    WriteHTML(html)
    print(f"Finished analyzing for {Title}")


def Summarize(
    additional_desc: str,
    title: str,
    included_models: T.List[str],
    included_treshold: T.List[float],
    included_sizes: T.List[str],
):
    files = sorted(glob.glob(os.path.join(result_dir, "*.csv")), key=sort_key)
    files = [f for f in files if f.count(additional_desc)]

    models_metric_files = glob.glob("../ML/model/*.md") + glob.glob("../ML/model/*.txt")
    models_metric_files = [m for m in models_metric_files if m.count(additional_desc)]
    models_metric_files = sorted(models_metric_files, key=sort_key)

    model_metrics: T.Dict[bool, T.List[str]] = {}
    model_metrics[True] = [f for f in models_metric_files if f.count("ignore_obj_size")]
    model_metrics[False] = [
        f for f in models_metric_files if not f.count("ignore_obj_size")
    ]

    test_prefix = [extract_desc(f)[0] for f in files if "test" in f]
    files = [f for f in files if extract_desc(f)[0] in test_prefix]

    # [ignore_obj_size] -> paths
    paths: T.Dict[bool, T.List[str]] = {
        False: [f for f in files if "ignore_obj_size" not in f],
        True: [f for f in files if "ignore_obj_size" in f],
    }

    # Analyze(
    #     paths[0],
    #     f"../../result/{title}_obj_size_not_ignored.md",
    #     f"../../docs/{title}_obj_size_not_ignored.html",
    #     f"{title} Test Data Result Obj Size Not Ignored",
    #     model_metrics[0],
    #     included_models,
    #     included_treshold,
    #     included_sizes,
    # )
    Analyze(
        paths[1],
        f"../../result/{title}_obj_size_ignored.md",
        f"../../docs/{title}_obj_size_ignored.html",
        f"{title} Test Data Result Obj Size Ignored",
        model_metrics[1],
        included_models,
        included_treshold,
        included_sizes,
    )
    # Analyze(
    #     files,
    #     f"../../result/{title}.md",
    #     f"../../docs/{title}.html",
    #     f"{title} Test Data Result Combined",
    #     model_metrics[0] + model_metrics[1],
    #     included_models,
    #     included_treshold,
    #     included_sizes,
    # )


ALL_MODELS = [
    "little_random_forest",
    "logistic_regression",
    "logistic_regression_v2",
    "logistic_regression_v3",
    "logistic_regression_v4",
    "LR_1",
    "LR_1_std_scaler",
    "LR_1_robust_scaler",
    "LR_1_log",
    "LR_1_mean",
    "LR_2",
    "LR_2_log",
    "LR_2_mean",
    "LR_3",
    "LR_3_log",
    "LR_3_mean",
    "LR_4",
    "LR_4_std_scaler",
    "LR_4_robust_scaler",
    "LR_4_log",
    "LR_4_mean",
    "LR_5",
    "LR_5_imba",
    "LR_6",
    "LR_6_imba",
    "LR_7",
    "LR_8",
    "LR_9",
    "LR_7_decay_rtime",
    "LR_7_decay_vtime",
    "LR_8_decay_rtime",
    "LR_8_decay_vtime",
    "LR_9_decay_rtime",
    "LR_9_decay_vtime",
    "LR_decay_rtime",
    "LR_decay_vtime",
    "LR_7_w_0_5",
    "LR_7_decay_rtime_w_0_5",
    "LR_7_decay_vtime_w_0_5",
    "LR_8_decay_rtime_w_0_5",
    "LR_8_decay_vtime_w_0_5",
    "LR_9_decay_rtime_w_0_5",
    "LR_9_decay_vtime_w_0_5",
    "LR_decay_vtime_w_0_5",
    "LR_decay_rtime_w_0_5",
    "LR_7_w_0_75",
    "LR_7_decay_rtime_w_0_75",
    "LR_7_decay_vtime_w_0_75",
    "LR_8_decay_rtime_w_0_75",
    "LR_8_decay_vtime_w_0_75",
    "LR_9_decay_rtime_w_0_75",
    "LR_9_decay_vtime_w_0_75",
    "LR_decay_vtime_w_0_75",
    "LR_decay_rtime_w_0_75",
    "LR_id",
    "LR_7_id",
    "LR_8_id",
    "LR_9_id",
]
BASE_MODELS = [
    "LR_1",
    "LR_2",
    "LR_3",
    "LR_4",
    "LR_5",
    "LR_6",
    "LR_7",
    "LR_8",
    "LR_9",
]
ALL_TRESHOLD = [
    0.3,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
]


def main():
    summarize_calls_args = []
    for trace, title in [("zipf1", "Zipf1"), ("cloudphysics", "CloudPhysics")]:
        summarize_calls_args += [
            (
                trace,
                f"{title} Models that use ObjID",
                [
                    "LR_id",
                    "LR_7_id",
                    "LR_8_id",
                    "LR_9_id",
                ],
                ALL_TRESHOLD,
                [
                    "0.01",
                    "0.1",
                    "0.2",
                    "0.4",
                ],
            ),
            (
                trace,
                f"{title} Models that use ObjID vs Model that does not",
                [
                    "LR_id",
                    "LR_7_id",
                    "LR_8_id",
                    "LR_9_id",
                    "LR_7",
                    "LR_8",
                    "LR_9",
                ],
                ALL_TRESHOLD,
                [
                    "0.01",
                    "0.1",
                    "0.2",
                    "0.4",
                ],
            ),
            (
                trace,
                title,
                ["LR_1", "LR_5_imba"],
                ALL_TRESHOLD,
                [
                    "0.01",
                    "0.1",
                    "0.2",
                    "0.4",
                ],
            ),
            (
                trace,
                f"{title} All Model with base treshold",
                ALL_MODELS,
                [0.5],
                [
                    "0.01",
                    "0.1",
                    "0.2",
                    "0.4",
                ],
            ),
            (
                trace,
                f"{title} All Model with all treshold",
                ALL_MODELS,
                ALL_TRESHOLD,
                [
                    "0.01",
                    "0.1",
                    "0.2",
                    "0.4",
                ],
            ),
            (
                trace,
                f"{title} New Model",
                ["LR_7", "LR_8", "LR_9"],
                ALL_TRESHOLD,
                [
                    "0.01",
                    "0.1",
                    "0.2",
                    "0.4",
                ],
            ),
            (
                trace,
                f"{title} New Model With Selected Treshold",
                ["LR_7", "LR_8", "LR_9"],
                [0.8, 0.9],
                [
                    "0.01",
                    "0.1",
                    "0.2",
                    "0.4",
                ],
            ),
            (
                trace,
                f"{title} Base Model",
                BASE_MODELS,
                [0.5],
                [
                    "0.01",
                    "0.1",
                    "0.2",
                    "0.4",
                ],
            ),
            (
                trace,
                f"{title} Decay Model with All Treshold ",
                [
                    "LR_7_decay_rtime",
                    "LR_7_decay_vtime",
                    "LR_8_decay_rtime",
                    "LR_8_decay_vtime",
                    "LR_9_decay_rtime",
                    "LR_9_decay_vtime",
                    "LR_decay_rtime",
                    "LR_decay_vtime",
                ],
                ALL_TRESHOLD,
                [
                    "0.01",
                    "0.1",
                    "0.2",
                    "0.4",
                ],
            ),
            (
                trace,
                f"{title} Selected Non-Decay vs Decay Model with All Treshold",
                [
                    "LR_7",
                    "LR_7_decay_rtime",
                    "LR_7_decay_vtime",
                ],
                ALL_TRESHOLD,
                [
                    "0.01",
                    "0.1",
                    "0.2",
                    "0.4",
                ],
            ),
            (
                trace,
                f"{title} Weighted Models with All Treshold",
                [
                    "LR_7",
                    "LR_8",
                    "LR_9",
                    "LR_7_decay_rtime",
                    "LR_7_decay_vtime",
                    "LR_8_decay_rtime",
                    "LR_8_decay_vtime",
                    "LR_9_decay_rtime",
                    "LR_9_decay_vtime",
                    "LR_decay_rtime",
                    "LR_decay_vtime",
                    "LR_7_w_0_5",
                    "LR_7_decay_rtime_w_0_5",
                    "LR_7_decay_vtime_w_0_5",
                    "LR_8_decay_rtime_w_0_5",
                    "LR_8_decay_vtime_w_0_5",
                    "LR_9_decay_rtime_w_0_5",
                    "LR_9_decay_vtime_w_0_5",
                    "LR_decay_vtime_w_0_5",
                    "LR_decay_rtime_w_0_5",
                    "LR_7_w_0_75",
                    "LR_7_decay_rtime_w_0_75",
                    "LR_7_decay_vtime_w_0_75",
                    "LR_8_decay_rtime_w_0_75",
                    "LR_8_decay_vtime_w_0_75",
                    "LR_9_decay_rtime_w_0_75",
                    "LR_9_decay_vtime_w_0_75",
                    "LR_decay_vtime_w_0_75",
                    "LR_decay_rtime_w_0_75",
                ],
                ALL_TRESHOLD,
                [
                    "0.01",
                    "0.1",
                    "0.2",
                    "0.4",
                ],
            ),
        ]
        for treshold in ALL_TRESHOLD:
            summarize_calls_args += [
                (
                    trace,
                    f"{title} Decay Model with Treshold {treshold}",
                    [
                        "LR_7_decay_rtime",
                        "LR_7_decay_vtime",
                        "LR_8_decay_rtime",
                        "LR_8_decay_vtime",
                        "LR_9_decay_rtime",
                        "LR_9_decay_vtime",
                        "LR_decay_rtime",
                        "LR_decay_vtime",
                        "LR_7_decay_rtime_w_0_5",
                        "LR_7_decay_vtime_w_0_5",
                        "LR_8_decay_rtime_w_0_5",
                        "LR_8_decay_vtime_w_0_5",
                        "LR_9_decay_rtime_w_0_5",
                        "LR_9_decay_vtime_w_0_5",
                        "LR_decay_vtime_w_0_5",
                        "LR_decay_rtime_w_0_5",
                        "LR_7_decay_rtime_w_0_75",
                        "LR_7_decay_vtime_w_0_75",
                        "LR_8_decay_rtime_w_0_75",
                        "LR_8_decay_vtime_w_0_75",
                        "LR_9_decay_rtime_w_0_75",
                        "LR_9_decay_vtime_w_0_75",
                        "LR_decay_vtime_w_0_75",
                        "LR_decay_rtime_w_0_75",
                    ],
                    [treshold],
                    [
                        "0.01",
                        "0.1",
                        "0.2",
                        "0.4",
                    ],
                ),
                (
                    trace,
                    f"{title} Selected Non-Decay vs Decay Model with Treshold {treshold}",
                    [
                        "LR_7",
                        "LR_7_decay_rtime",
                        "LR_7_decay_vtime",
                        "LR_decay_vtime",
                        "LR_decay_rtime",
                    ],
                    [treshold],
                    [
                        "0.01",
                        "0.1",
                        "0.2",
                        "0.4",
                    ],
                ),
                (
                    trace,
                    f"{title} Weighted Models with Treshold {treshold}",
                    [
                        "LR_7",
                        "LR_8",
                        "LR_9",
                        "LR_7_decay_rtime",
                        "LR_7_decay_vtime",
                        "LR_8_decay_rtime",
                        "LR_8_decay_vtime",
                        "LR_9_decay_rtime",
                        "LR_9_decay_vtime",
                        "LR_decay_rtime",
                        "LR_decay_vtime",
                        "LR_7_w_0_5",
                        "LR_7_decay_rtime_w_0_5",
                        "LR_7_decay_vtime_w_0_5",
                        "LR_8_decay_rtime_w_0_5",
                        "LR_8_decay_vtime_w_0_5",
                        "LR_9_decay_rtime_w_0_5",
                        "LR_9_decay_vtime_w_0_5",
                        "LR_decay_vtime_w_0_5",
                        "LR_decay_rtime_w_0_5",
                        "LR_7_w_0_75",
                        "LR_7_decay_rtime_w_0_75",
                        "LR_7_decay_vtime_w_0_75",
                        "LR_8_decay_rtime_w_0_75",
                        "LR_8_decay_vtime_w_0_75",
                        "LR_9_decay_rtime_w_0_75",
                        "LR_9_decay_vtime_w_0_75",
                        "LR_decay_vtime_w_0_75",
                        "LR_decay_rtime_w_0_75",
                    ],
                    [treshold],
                    [
                        "0.01",
                        "0.1",
                        "0.2",
                        "0.4",
                    ],
                ),
            ]
    with multiprocessing.Pool(processes=10) as pool:
        pool.starmap(Summarize, summarize_calls_args)


if __name__ == "__main__":
    main()
