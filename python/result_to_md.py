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
import markdown as MD


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

urls = []
with open("../trace/reasonable_traces.txt") as f:
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


def ModelSummaries(
    base: T.List[str],
    ml: T.List[str],
    output_path: str,
    html_path: str,
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
    html = open(Path(html_path), "w")
    Write(md, html, f"# {Title}  \n# Result  \n")

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

    Write(md, html, "# Model Summaries  \n")
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

    Write(md, html, tb.tabulate(bt_data, headers="keys", tablefmt="github") + "  \n\n")
    Write(md, html, "## Promotion Reduced (%)  \n")
    Write(
        md,
        html,
        "$\\dfrac{Base Promotion - Model Promotion}{Base Promotion} \\times 100$  \n\n",
    )
    Write(md, html, tb.tabulate(p_data, headers="keys", tablefmt="github") + "  \n\n")
    Write(md, html, "## Miss Ratio Reduced (%)  \n")
    Write(
        md,
        html,
        "$\\dfrac{Base Miss Ratio - Model Miss Ratio}{Base Miss Ratio} \\times 100$  \n\n",
    )
    Write(md, html, tb.tabulate(mr_data, headers="keys", tablefmt="github") + "  \n\n")
    Write(md, html, "# Model Summaries Plot  \n")

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

        Write(md, html, f"## {title} Reduced (%) \n")
        Write(
            md,
            html,
            f"$\\dfrac{{Base {title} - Model {title}}}{{Base {title}}} \\times 100$  \n\n",
        )
        WriteFig(md, html, fig)

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

        Write(md, html, f"## {title} \n")
        WriteFig(md, html, fig)

    Write(md, html, "# Individual Workload Result  \n")

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
        Write(md, html, f"## {trace}  \n")
        Write(
            md,
            html,
            f"{next((x for x in urls if x[x.rfind('/') + 1 : x.rfind('.oracleGeneral')] == trace), '')}  \n",
        )
        for ignore_obj_size in range(2):
            if ignore_obj_size:
                Write(md, html, "## Object Size Ignored  \n")
            for cache_size in cache_sizes:
                base_path = next(
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
                if base_path is None:
                    continue
                trace_model_result = models_result.query(
                    "trace == @trace and ignore_obj_size == @ignore_obj_size and cache_size == @cache_size"
                )
                if Path(base_path).stat().st_size == 0:
                    continue
                prefix, desc = extract_desc(base_path)
                df = pd.read_csv(base_path)
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
                Write(md, html, f"### {cache_size}  \n")
                WriteFig(md, html, fig)
                best = best_ml_models[prefix, float(cache_size), ignore_obj_size]
                best_model = best[0]
                best_mr = best[1]
                Write(
                    md,
                    html,
                    f"**Best Models**: {best_model}  \n**Miss Ratio**: {best_mr}  \n",
                )

    WriteHTML(html)


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
    "../docs/test_obj_size_not_ignored.html",
    "Test Data Result Obj Size Not Ignored",
    model_metrics[0],
)
ModelSummaries(
    base_test[1],
    ML_test[1],
    "../result/test_obj_size_ignored.md",
    "../docs/test_obj_size_ignored.html",
    "Test Data Result Obj Size Ignored",
    model_metrics[1],
)
ModelSummaries(
    base_test[0] + base_test[1],
    ML_test[0] + ML_test[1],
    "../result/test.md",
    "../docs/test.html",
    "Test Data Result Combined",
    model_metrics[0] + model_metrics[1],
)
