import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from dataclasses import dataclass
import os
import glob
from pathlib import Path
from collections import defaultdict
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
        if file.find("_v4") == -1 and file.find("forest") == -1:
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
    iter_2 = [i for i in range(2, max_iteration + 2)]

    n_promotion = n_promotion[: max_iteration + 1]
    miss_ratio = miss_ratio[: max_iteration + 1]
    d_n_promotion = d_n_promotion[:max_iteration]
    d_miss_ratio = d_miss_ratio[:max_iteration]

    fig, axs = plt.subplots(2, 1, figsize=(12, 5 * 2))
    axs[0].set_xlabel("Iteration")
    axs[0].set_ylabel("Promotion", color="blue")
    axs[0].plot(iter, n_promotion, marker="o", linestyle="-", color="blue")
    axs[0].tick_params(axis="y", labelcolor="blue")
    axs[0].yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))
    axs[0].xaxis.set_major_locator(
        ticker.MaxNLocator(nbins=len(n_promotion) + 1, integer=True)
    )

    ax2 = axs[0].twinx()
    ax2.set_ylabel("Miss Ratio", color="red")
    ax2.plot(iter, miss_ratio, marker="s", linestyle="--", color="red")
    ax2.tick_params(axis="y", labelcolor="red")
    ax2.yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))

    colors = ["#6A5ACD", "#D2691E", "#228B22"]
    if (prefix, size, desc.count("ignore_obj_size")) in ml_algo:
        current_ml = ml_algo[prefix, size, desc.count("ignore_obj_size")]
        current_ml = dict(sorted(current_ml.items()))
        counter = 0
        for k in current_ml:
            y1 = current_ml[k].n_promoted
            y2 = current_ml[k].miss_ratio
            axs[0].axhline(
                y=y1,
                linestyle="-",
                label=f"{k} Promotion",
                color=colors[counter],
                linewidth=3,
            )
            ax2.axhline(
                y=y2,
                linestyle="--",
                label=f"{k} Miss Ratio",
                color=colors[counter],
                linewidth=3,
            )
            counter += 1

            ymin, ymax = axs[0].get_ylim()
            axs[0].set_ylim(min(ymin, y1), max(ymax, y1))

            ymin2, ymax2 = ax2.get_ylim()
            ax2.set_ylim(min(ymin2, y2), max(ymax2, y2))

    lines1, labels1 = axs[0].get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    lines = []
    labels = []
    for i, j, k, x in zip(lines1, lines2, labels1, labels2):
        lines.append(i)
        lines.append(j)
        labels.append(k)
        labels.append(x)

    axs[0].legend(
        lines,
        labels,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.1),
        ncol=3,
    )

    plt.title(Path(file).stem)

    axs[1].set_xlabel("Iteration")
    axs[1].set_ylabel("$\\Delta$ Promotion", color="blue")
    axs[1].plot(iter_2, d_n_promotion, marker="o", linestyle="-", color="blue")
    axs[1].tick_params(axis="y", labelcolor="blue")
    axs[1].yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))
    axs[1].xaxis.set_major_locator(
        ticker.MaxNLocator(nbins=len(d_n_promotion) + 1, integer=True)
    )

    ax3 = axs[1].twinx()
    ax3.set_ylabel("$\\Delta$ Miss Ratio", color="red")
    ax3.plot(iter_2, d_miss_ratio, marker="s", linestyle="--", color="red")
    ax3.tick_params(axis="y", labelcolor="red")
    ax3.yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))

    if (prefix, size, desc.count("ignore_obj_size")) in ml_algo:
        current_ml = ml_algo[prefix, size, desc.count("ignore_obj_size")]
        current_ml = dict(sorted(current_ml.items()))
        counter = 0
        for k in current_ml:
            y1 = n_promotion[0] - current_ml[k].n_promoted
            y2 = miss_ratio[0] - current_ml[k].miss_ratio
            axs[1].axhline(
                y=y1,
                linestyle="-.",
                label=f"{k} Promotion",
                color=colors[counter],
                linewidth=3,
            )
            ax3.axhline(
                y=y2,
                linestyle=":",
                label=f"{k} Miss Ratio",
                color=colors[counter],
                linewidth=3,
            )
            counter += 1

            ymin, ymax = axs[1].get_ylim()
            axs[1].set_ylim(min(ymin, y1), max(ymax, y1))
            ymin2, ymax2 = ax3.get_ylim()
            ax3.set_ylim(min(ymin2, y2), max(ymax2, y2))

    lines1, labels1 = axs[1].get_legend_handles_labels()
    lines2, labels2 = ax3.get_legend_handles_labels()

    plt.title("Relative")

    fig.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path)
    plt.close()


async def ConcurrentIndividualPlot(files):
    await MLPlot(files)
    task = [IndividualPlot(file) for file in files if Path(file).stat().st_size > 0]
    await asyncio.gather(*task)
    print("Done Plotting Individuals")
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
    print("Done Plotting Overall")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    result_dir = "../result/log"
    output_dir = "../result/graph"

    files = glob.glob(os.path.join(result_dir, "*.csv"))
    asyncio.run(ConcurrentIndividualPlot(files))
