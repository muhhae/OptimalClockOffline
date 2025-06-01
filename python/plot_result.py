import plotly.express as px
import plotly.io as pio
import typing as T
import glob
import os
import re
from pathlib import Path
from common import extract_desc, OutputLog, ordinal
import tabulate as tb
import markdown as MD
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


result_dir = "../result/log"

urls = []
with open("../trace/reasonable_traces.txt") as f:
    urls = [line.strip() for line in f if line.strip()]


def sort_key(filename):
    desc = extract_desc(filename)[1]
    if "model" in desc[-1]:
        return (filename, desc[0], desc[-1]["model"])
    return (filename, desc[0])


def printls(ls: T.List):
    for x in ls:
        print(x)


g_html_content = ""


def Write(md: T.TextIO, html: T.TextIO, content: str):
    global g_html_content
    md.write(content)
    g_html_content += content


def WriteFig(md: T.TextIO, html: T.TextIO, fig):
    global g_html_content
    md.write(fig.to_image(format="svg").decode("utf-8") + "  \n")
    g_html_content += fig.to_html(full_html=False, include_plotlyjs=False) + "  \n"


def WriteHTML(html: T.TextIO):
    global g_html_content
    md = MD.Markdown(
        extensions=["extra", "toc", "pymdownx.arithmatex"],
        extension_configs={"pymdownx.arithmatex": {"generic": True}},
    )
    html_body = md.convert(g_html_content)
    toc = md.toc
    html.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src='https://cdn.plot.ly/plotly-3.0.1.min.js' charset='utf-8'></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/core.min.js" integrity="sha512-Vj8DsxZwse5LgmhPlIXhSr/+mwl8OajbZVCr4mX/TcDjwU1ijG6A15cnyRXqZd2mUOQqRk4YbQdc7XhvedWqMg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css" integrity="sha512-BrOPA520KmDMqieeM7XFe6a3u3Sb3F1JBaQnrIAmWg3EYrciJ+Qqe6ZcKCdfPv26rGcgTrJnZ/IdQEct8h3Zhw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
    :root {{
        /* Light mode defaults */
        --bg-color: #fff;
        --sidebar-bg: #f6f8fa;
        --text-color: #222;
        --sidebar-link: #444;
        --sidebar-link-hover: #111;
        --sidebar-heading: #333;
        --sidebar-marker: #444;
    }}
    @media (prefers-color-scheme: dark) {{
        :root {{
            --bg-color: #111;
            --sidebar-bg: #111;
            --text-color: #eee;
            --sidebar-link: #818181;
            --sidebar-link-hover: #f1f1f1;
            --sidebar-heading: #818181;
            --sidebar-marker: #818181;
        }}
    }}
    body {{
        background-color: var(--bg-color);
        color: var(--text-color);
        display: flex;
        margin: 0;
    }}
    .sidenav {{
        height: 100%;
        width: 280px;
        min-width: 200px;
        max-width: 300px;
        position: fixed;
        z-index: 1;
        top: 0;
        left: 0;
        background-color: var(--sidebar-bg);
        overflow-x: hidden;
        padding: 2em 1em 2em 2em;
    }}
    .sidenav.closed {{
        transform: translateX(-100%);
    }}
    .sidenav a {{
        padding: 1px 1px 1px 1px;
        font-size: 16px;
        color: var(--sidebar-link);
        display: block;
        text-decoration: none;
        transition: color 0.2s;
    }}
    .sidenav h2 {{
        padding: 1px 1px 1px 1px;
        font-size: 20px;
        color: var(--sidebar-heading);
        display: block;
    }}
    .sidenav li::marker {{
        color: var(--sidebar-marker);
        display: block;
    }}
    .sidenav a:hover {{
        color: var(--sidebar-link-hover);
    }}
    .sidebar-toggle-btn {{
      position: fixed;
      top: 10px;
      left: 10px;
      z-index: 1002;
      background: var(--sidebar-bg);
      color: var(--sidebar-link);
      border: 1px solid var(--sidebar-link);
      border-radius: 4px;
      padding: 8px 14px;
      cursor: pointer;
      font-size: 18px;
      transition: background 0.2s, color 0.2s;
    }}
    .sidebar-toggle-btn:hover {{
      background: var(--sidebar-link-hover);
      color: var(--bg-color);
    }}
    .sidenav.closed ~ .content {{
      margin-left: 0;
    }}
    .content {{
        margin-left: 300px;
        padding: 2em;
        width: 100%;
    }}
    .markdown-body {{box - sizing: border-box;
        min-width: 200px;
        max-width: 980px;
        margin: 0 auto;
        padding: 45px;
    }}
    @media (max-width: 767px) {{
        .markdown-body {{
            padding: 15px;
        }}
    }}
</style>
</head>
<body>
<button class="sidebar-toggle-btn" id="sidebarToggleBtn" aria-label="Toggle sidebar">&#9776;</button>
<nav class="sidenav" id="sidebar">
    <h2>Table of Contents</h2>
    {toc}
</nav>
<script>
    const sidebar = document.getElementById('sidebar');
    const btn = document.getElementById('sidebarToggleBtn');
    btn.addEventListener('click', function(){{
      sidebar.classList.toggle('closed');
      if (sidebar.classList.contains('closed')) {{
        btn.setAttribute('aria-label', 'Open sidebar');
      }} else {{
        btn.setAttribute('aria-label', 'Close sidebar');
      }}
    }});
    if(window.innerWidth <= 700){{
      sidebar.classList.add('closed');
    }}
</script>
<main class="content">
<article class="markdown-body">
    {html_body}
</article>
</main>
</body>
</html>
""")
    g_html_content = ""


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


def GetModelMetrics(paths: T.List[str]):
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

        py_v = re.sub(r"\s+", " ", content.strip())
        py_v = re.sub(r"(?<=\d) (?=\d)", ", ", py_v)
        py_v = re.sub(r"\] \[", "], [", py_v)

        if py_v == "":
            continue

        model = p.replace(".md", "").replace(".txt", "")
        model = Path(p).stem
        model, desc = extract_desc(model)
        size = desc[0]
        # model = f"{model}_{'spec' if size != 'All' else size}"
        model = f"{model}_{size}"

        (TN, FP), (FN, TP) = eval(py_v)

        tmp.append(
            {
                "Model": model,
                "Cache Size": size,
                "True Negatives": TN / (TN + FN) * 100 if TN != 0 else 0,
                "True Positives": TP / (TP + FP) * 100 if TP != 0 else 0,
                "False Negatives": FN / (TN + FN) * 100 if FN != 0 else 0,
                "False Positives": FP / (TP + FP) * 100 if FP != 0 else 0,
                "Report": report,
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


def GetModelResult(paths: T.List[str]):
    tmp = []
    for file in paths:
        if Path(file).stat().st_size == 0:
            continue
        prefix, desc = extract_desc(file)
        model = desc[-1]["model"]
        size = model.split("_")[-1]
        size_pos = model.rfind("_")
        model = model[:size_pos]
        # model = f"{model}_{'spec' if size != 'All' else size}"
        model = f"{model}_{size}"
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


def WriteModelSummaries(md, html, base_result, models_result):
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
    Write(md, html, tb.tabulate(bt_data, headers="keys", tablefmt="github") + "  \n\n")
    Write(md, html, "## Promotion Reduced (%)  \n")
    Write(md, html, tb.tabulate(p_data, headers="keys", tablefmt="github") + "  \n\n")
    Write(md, html, "## Miss Ratio Reduced (%)  \n")
    Write(md, html, tb.tabulate(mr_data, headers="keys", tablefmt="github") + "  \n\n")
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
            width=800,
            showlegend=False,
        )
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(showgrid=True)

        Write(md, html, f"## {title}\n")
        WriteFig(md, html, fig)

    Write(md, html, "# Promotion vs Miss Ratio  \n")
    fig = px.scatter(
        data.groupby("Model")[["Promotion Reduced (%)", "Miss Ratio Reduced (%)"]]
        .mean()
        .reset_index(),
        x="Promotion Reduced (%)",
        y="Miss Ratio Reduced (%)",
        color="Model",
    )
    fig.update_xaxes(dtick=10)
    fig.update_layout(
        xaxis_title="Promotion Reduced (%)",
        yaxis_title="Miss Ratio Reduced (%)",
        font=dict(size=14),
        height=800,
        width=800,
        yaxis_tickformat=".6f",
    )
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    WriteFig(md, html, fig)


def WriteModelMetrics(md, html, model_metrics: pd.DataFrame):
    Write(md, html, "# Model Classification Report  \n")
    for m in model_metrics["Model"].unique():
        Write(md, html, f"## {m}  \n")
        report = model_metrics.query("Model == @m")["Report"].tolist()
        for r in report:
            Write(md, html, f"```\n{r}\n```  \n")
    Write(md, html, "# Model Metrics  \n")
    for title in [
        "True Positives",
        "True Negatives",
        "False Positives",
        "False Negatives",
    ]:
        fig = px.box(
            model_metrics,
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
            height=30 * len(model_metrics["Model"].unique()),
            width=800,
            showlegend=False,
        )
        fig.update_xaxes(showgrid=True)
        fig.update_yaxes(showgrid=True)

        Write(md, html, f"## {title} \n")
        WriteFig(md, html, fig)


def WriteIndividualResult(md, html, results):
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
                    width=800,
                )
                fig.update_xaxes(showgrid=True)
                fig.update_yaxes(showgrid=True)
                WriteFig(md, html, fig)


def Analyze(
    paths: T.List[str],
    output_path: str,
    html_path: str,
    Title: str,
    models_metrics_paths: T.List[str],
    included_models: T.List[str],
):
    print(f"Analyzing for {Title}")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    os.makedirs(os.path.dirname(html_path), exist_ok=True)

    md = open(output_path, "w")
    html = open(Path(html_path), "w")
    Write(md, html, f"# {Title}  \n# Result  \n")

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
        )
    ]
    models_metrics_paths = [
        f
        for f in models_metrics_paths
        if (p := Path(f).stem)[: p.rfind("[")] in included_models
    ]

    model_metrics = GetModelMetrics(models_metrics_paths)
    base_result = GetBaseResult(base_paths)
    model_result = GetModelResult(model_paths)
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
    )
    WriteModelMetrics(md, html, model_metrics)
    WriteIndividualResult(
        md, html, [base_result, lru_result, model_result, dist_optimal_result]
    )
    WriteHTML(html)


def Summarize(additional_desc: str, title: str, included_models: T.List[str]):
    files = sorted(glob.glob(os.path.join(result_dir, "*.csv")), key=sort_key)
    files = [f for f in files if f.count(additional_desc)]

    models_metric_files = glob.glob("ML/model/*.md") + glob.glob("ML/model/*.txt")
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

    Analyze(
        paths[0],
        f"../result/{title}_obj_size_not_ignored.md",
        f"../docs/{title}_obj_size_not_ignored.html",
        f"{title} Test Data Result Obj Size Not Ignored",
        model_metrics[0],
        included_models,
    )
    Analyze(
        paths[1],
        f"../result/{title}_obj_size_ignored.md",
        f"../docs/{title}_obj_size_ignored.html",
        f"{title} Test Data Result Obj Size Ignored",
        model_metrics[1],
        included_models,
    )
    Analyze(
        files,
        f"../result/{title}.md",
        f"../docs/{title}.html",
        f"{title} Test Data Result Combined",
        model_metrics[0] + model_metrics[1],
        included_models,
    )


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
]

Summarize("zipf1", "Zipf1", ["LR_1", "LR_5_imba"])
Summarize("zipf0", "Zipf0", ["LR_1", "LR_5_imba"])

Summarize("zipf1", "Zipf1 All Model", ALL_MODELS)
Summarize("zipf0", "Zipf0 All Model", ALL_MODELS)
