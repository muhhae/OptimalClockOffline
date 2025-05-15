import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from dataclasses import dataclass
import os
import glob
from pathlib import Path
from collections import defaultdict
from adjustText import adjust_text
from typing import List, Dict
from cycler import cycler
import asyncio

custom_colors = [
    "#1f77b4",  # Blue
    "#ff7f0e",  # Orange
    "#2ca02c",  # Green
    "#d62728",  # Red
    "#9467bd",  # Purple
    "#8c564b",  # Brown
    "#e377c2",  # Pink
    "#7f7f7f",  # Gray
    "#bcbd22",  # Yellow
    "#17becf",  # Cyan
]

# plt.style.use("dark_background")


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


overall_missratio = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
overall_percent_missratio = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
overall_promotions = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
overall_percent_promotions = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
overall_d_missratio = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
overall_d_percent_missratio = defaultdict(
    lambda: defaultdict(lambda: defaultdict(list))
)
overall_d_promotions = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
overall_d_percent_promotions = defaultdict(
    lambda: defaultdict(lambda: defaultdict(list))
)

overall_max_iteration = defaultdict(lambda: defaultdict(list))

# DEBUG_SAMPLE = 4
# DEBUG_COUNT = 0

ml_algo: Dict[tuple, Dict[str, OutputLog]] = defaultdict(lambda: defaultdict(OutputLog))


async def max_iteration_boxplot(d: dict, title, y_label, prefix):
    overal_path = "../result/overall"

    labels = sorted(d.keys())
    data = [d[k] for k in labels]

    plt.figure()
    plt.boxplot(data, tick_labels=labels)
    plt.title(f"{title} across cache size")
    plt.xlabel("Cache Size")
    plt.ylabel(y_label)
    plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
    plt.savefig(f"{overal_path}/{prefix}max_iteration.png")
    plt.close()


async def box_plot(d, title, y_label, prefix):
    overal_path = "../result/overall"
    d = dict(sorted(d.items()))
    all_i = sorted({i for desc in d.values() for i in desc})

    for i in all_i:
        data = []
        labels = []
        for desc in d:
            if i in d[desc]:
                data.append(d[desc][i])
                labels.append(desc)

        plt.figure()
        plt.boxplot(data, tick_labels=labels)
        plt.title(f"{title} across cache size (i = {i})")
        plt.xlabel("Cache Size")
        plt.ylabel(y_label)
        plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
        plt.savefig(f"{overal_path}/{prefix}_i_{str(i)}.png")
        plt.close()

    for desc in d:
        data = []
        labels = []
        for i in sorted(d[desc]):
            data.append(d[desc][i])
            labels.append(str(i))

        if desc == 0:
            desc = "All"

        plt.figure()
        plt.boxplot(data, tick_labels=labels)
        plt.title(f"{title} across i (cache size = {desc})")
        plt.xlabel("Iteration")
        plt.ylabel(y_label)
        plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
        plt.savefig(f"{overal_path}/{prefix}_s_{str(desc)}.png")
        plt.close()


async def MLPlot(files):
    for file in files:
        if Path(file).stat().st_size == 0:
            continue
        if (
            file.find("_v4") == -1
            and file.find("forest") == -1
            and file.find("LR") == -1
        ):
            continue

        df = pd.read_csv(file)
        if df.empty:
            continue
        logs = [OutputLog(**row) for row in df.to_dict(orient="records")]
        prefix, desc = extract_desc(file)
        size = float(desc[0])
        obj_size_ignored = desc.count("ignore_obj_size")
        if desc.count("ML"):
            model = desc[-1]["model"]
            ml_algo[prefix, size, obj_size_ignored][model] = logs[0]
            continue


async def IndividualPlot(file: str):
    output_path = os.path.join(output_dir, Path(file).stem + ".png")

    df = pd.read_csv(file)
    if df.empty:
        return

    logs = [OutputLog(**row) for row in df.to_dict(orient="records")]

    iter = [i for i in range(1, 21)]
    iter_2 = [i for i in range(2, 21)]

    prefix, desc = extract_desc(file)
    size = float(desc[0])

    if len(desc) > (2 + desc.count("ignore_obj_size") + desc.count("TEST")):
        return

    miss_ratio = [d.miss_ratio for d in logs]
    d_miss_ratio = [miss_ratio[0] - miss_ratio[1] for i in range(1, len(miss_ratio))]
    percent_missratio = [d.miss_ratio / logs[0].miss_ratio for d in logs]
    d_percent_missratio = [
        percent_missratio[0] - percent_missratio[i]
        for i in range(1, len(percent_missratio))
    ]
    n_promotion = [d.n_promoted for d in logs]
    d_n_promotion = [
        n_promotion[0] - n_promotion[i] for i in range(1, len(n_promotion))
    ]
    n_percent_promotion = [d.n_promoted / logs[0].n_promoted for d in logs]
    d_n_percent_promotion = [
        n_percent_promotion[0] - n_percent_promotion[i]
        for i in range(1, len(n_percent_promotion))
    ]
    overall = [
        (iter, miss_ratio, overall_missratio),
        (iter, percent_missratio, overall_percent_missratio),
        (iter, n_promotion, overall_promotions),
        (iter, n_percent_promotion, overall_percent_promotions),
        (iter_2, d_miss_ratio, overall_d_missratio),
        (iter_2, d_percent_missratio, overall_d_percent_missratio),
        (iter_2, d_n_promotion, overall_d_promotions),
        (iter_2, d_n_percent_promotion, overall_d_promotions),
    ]
    for it, v, container in overall:
        for i, e in zip(it, v):
            container[desc.count("ignore_obj_size")][size][i].append(e)
            container[desc.count("ignore_obj_size")][0][i].append(e)

    # if Path(output_path).exists():
    #     continue

    max_iteration = 19
    # MIN_PROMOTION_DIFF = 1e-8
    MIN_PROMOTION_DIFF = 0

    diffs = abs(np.diff(n_percent_promotion))
    cond = np.where(diffs > MIN_PROMOTION_DIFF)[0]
    max_iteration = np.max(cond) + 1

    if max_iteration > 19:
        max_iteration = 19

    overall_max_iteration[desc.count("ignore_obj_size")][size].append(max_iteration)

    iter = [i for i in range(1, max_iteration + 2)]

    n_promotion = n_promotion[: max_iteration + 1]
    miss_ratio = miss_ratio[: max_iteration + 1]
    labels = [f"[Offline Clock iteration={i}]" for i in range(1, len(n_promotion) + 1)]

    if (prefix, size, desc.count("ignore_obj_size")) in ml_algo:
        current_ml = ml_algo[prefix, size, desc.count("ignore_obj_size")]
        current_ml = dict(sorted(current_ml.items()))
        for k in current_ml:
            n_promotion.append(current_ml[k].n_promoted)
            miss_ratio.append(current_ml[k].miss_ratio)
            k = k.replace("_", " ")
            labels.append(f"{k}")

    combined = list(zip(n_promotion, miss_ratio, labels))
    combined.sort()

    n_promotion, miss_ratio, labels = zip(*combined)

    fig = plt.figure(figsize=(12, 6), layout="constrained")
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel("Promotion")
    ax.set_ylabel("Miss Ratio")
    ax.scatter(n_promotion, miss_ratio, marker="o")
    ax.tick_params(axis="y", labelcolor="blue")

    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))
    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=20))

    formatter = ticker.ScalarFormatter(useOffset=False, useMathText=False)
    formatter.set_scientific(False)
    ax.yaxis.set_major_formatter(formatter)

    texts = [
        ax.annotate(
            labels[i],
            xy=(n_promotion[i], miss_ratio[i]),
            ha="center",
            va="center",
        )
        for i in range(len(labels))
    ]

    adjust_text(
        texts,
        ax=ax,
        avoid_self=True,
        avoid_points=True,
        only_move={"points": "xy", "text": "xy"},
        expand_text=(2.5, 2.5),
        expand_points=(2.5, 2.5),
        force_text=(1.5, 1.5),
        force_points=(1.5, 1.5),
        min_arrow_len=1,
        lim=2000,
        # save_steps=True,
        # save_prefix="adjustText",
        ensure_inside_axes=True,
        expand_axes=True,
    )

    combined = list(zip(miss_ratio, labels))
    combined.sort()

    print()
    for mr, l in combined:
        print(f"{l} = {mr}")
    print()

    plt.title(Path(file).stem)

    # fig.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path)
    plt.close()


async def ConcurrentIndividualPlot(files):
    await MLPlot(files)
    task = [IndividualPlot(file) for file in files if Path(file).stat().st_size > 0]
    await asyncio.gather(*task)
    print("Done Plotting Individuals")


async def ConcurrentOverallPlot():
    task = [
        max_iteration_boxplot(
            overall_max_iteration[0],
            "Max Iteration",
            "Max Iteration",
            "",
        ),
        max_iteration_boxplot(
            overall_max_iteration[1], "Max Iteration", "Max Iteration", "osi_"
        ),
        box_plot(overall_missratio[0], "Miss Ratio", "Miss Ratio", "miss_ratio"),
        box_plot(
            overall_percent_missratio[0],
            "Miss Ratio (relative)",
            "Miss Ratio (relative)",
            "miss_ratio_percent",
        ),
        box_plot(overall_promotions[0], "Promotions", "Promotions", "promotions"),
        box_plot(
            overall_percent_promotions[0],
            "Promotions (relative)",
            "Promotions (relative)",
            "promotions_percent",
        ),
        box_plot(
            overall_d_missratio[0],
            "Miss Ratio reduced",
            "First Miss Ratio - Current Miss Ratio",
            "d_miss_ratio",
        ),
        box_plot(
            overall_d_percent_missratio[0],
            "Miss Ratio (relative) reduced",
            "First Miss Ratio - Current Miss Ratio (relative)",
            "d_miss_ratio_percent",
        ),
        box_plot(
            overall_d_promotions[0],
            "Promotions reduced",
            "First Promotions - Current Promotions",
            "d_promotions",
        ),
        box_plot(
            overall_d_percent_promotions[0],
            "Promotions (relative) reduced",
            "First Promotions - Current Promotions (relative)",
            "d_promotions_percent",
        ),
        box_plot(overall_missratio[1], "Miss Ratio", "Miss Ratio", "osi_miss_ratio"),
        box_plot(
            overall_percent_missratio[1],
            "Miss Ratio (relative)",
            "Miss Ratio (relative)",
            "osi_miss_ratio_percent",
        ),
        box_plot(overall_promotions[1], "Promotions", "Promotions", "osi_promotions"),
        box_plot(
            overall_percent_promotions[1],
            "Promotions (relative)",
            "Promotions (relative)",
            "osi_promotions_percent",
        ),
        box_plot(
            overall_d_missratio[1],
            "Miss Ratio reduced",
            "First Miss Ratio - Current Miss Ratio",
            "osi_d_miss_ratio",
        ),
        box_plot(
            overall_d_percent_missratio[1],
            "Miss Ratio (relative) reduced",
            "First Miss Ratio - Current Miss Ratio (relative)",
            "osi_d_miss_ratio_percent",
        ),
        box_plot(
            overall_d_promotions[1],
            "Promotions reduced",
            "First Promotions - Current Promotions",
            "osi_d_promotions",
        ),
        box_plot(
            overall_d_percent_promotions[1],
            "Promotions (relative) reduced",
            "First Promotions - Current Promotions (relative)",
            "osi_d_promotions_percent",
        ),
    ]
    await asyncio.gather(*task)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    result_dir = "../result/log"
    output_dir = "../result/graph"

    files = glob.glob(os.path.join(result_dir, "*.csv"))

    asyncio.run(ConcurrentIndividualPlot(files))
    # asyncio.run(ConcurrentOverallPlot())
