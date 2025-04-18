import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from dataclasses import dataclass
import os
import glob
from pathlib import Path
from collections import defaultdict


def extract_desc(filename: str) -> (str, list):
    prefix = filename[: filename.rfind("[")]
    desc = filename[filename.rfind("[") + 1 : filename.rfind("]")]
    desc = desc.split(",")
    desc = [
        {x[: x.find("=")]: x[x.find("=") + 1 :]} if x.find("=") != -1 else x
        for x in desc
    ]
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

files = glob.glob(os.path.join(result_dir, "*.csv"))

overall_missratio = defaultdict(lambda: defaultdict(list))
overall_percent_missratio = defaultdict(lambda: defaultdict(list))
overall_promotions = defaultdict(lambda: defaultdict(list))
overall_percent_promotions = defaultdict(lambda: defaultdict(list))
overall_d_missratio = defaultdict(lambda: defaultdict(list))
overall_d_percent_missratio = defaultdict(lambda: defaultdict(list))
overall_d_promotions = defaultdict(lambda: defaultdict(list))
overall_d_percent_promotions = defaultdict(lambda: defaultdict(list))

ignore_obj_size_overall_missratio = defaultdict(lambda: defaultdict(list))
ignore_obj_size_overall_percent_missratio = defaultdict(lambda: defaultdict(list))
ignore_obj_size_overall_promotions = defaultdict(lambda: defaultdict(list))
ignore_obj_size_overall_percent_promotions = defaultdict(lambda: defaultdict(list))
ignore_obj_size_overall_d_missratio = defaultdict(lambda: defaultdict(list))
ignore_obj_size_overall_d_percent_missratio = defaultdict(lambda: defaultdict(list))
ignore_obj_size_overall_d_promotions = defaultdict(lambda: defaultdict(list))
ignore_obj_size_overall_d_percent_promotions = defaultdict(lambda: defaultdict(list))

overall_max_iteration = defaultdict(list)
ignore_obj_size_overall_max_iteration = defaultdict(list)

# DEBUG_SAMPLE = 4
# DEBUG_COUNT = 0

my_algo = {}

for file in files:
    if Path(file).stat().st_size == 0:
        continue
    df = pd.read_csv(file)
    if df.empty:
        continue
    logs = [OutputLog(**row) for row in df.to_dict(orient="records")]
    prefix, desc = extract_desc(file)
    size = float(desc[0])
    if desc.count("my_algo"):
        my_algo[prefix, size, desc.count("ignore_obj_size")] = logs[0]
        continue


for file in files:
    # if DEBUG_COUNT == DEBUG_SAMPLE:
    #     exit(1)
    # DEBUG_COUNT += 1
    if Path(file).stat().st_size == 0:
        continue

    output_path = os.path.join(output_dir, Path(file).stem + ".png")

    df = pd.read_csv(file)
    if df.empty:
        continue

    logs = [OutputLog(**row) for row in df.to_dict(orient="records")]

    iter = [i for i in range(1, 21)]
    iter_2 = [i for i in range(2, 21)]

    prefix, desc = extract_desc(file)
    size = float(desc[0])

    if desc.count("my_algo"):
        continue

    if desc.count("ignore_obj_size"):
        miss_ratio = [d.miss_ratio for d in logs]
        for i, e in zip(iter, miss_ratio):
            ignore_obj_size_overall_missratio[size][i].append(e)
            ignore_obj_size_overall_missratio[0][i].append(e)

        d_miss_ratio = [
            miss_ratio[0] - miss_ratio[1] for i in range(1, len(miss_ratio))
        ]
        for i, e in zip(iter_2, d_miss_ratio):
            ignore_obj_size_overall_d_missratio[size][i].append(e)
            ignore_obj_size_overall_d_missratio[0][i].append(e)

        percent_missratio = [d.miss_ratio / logs[0].miss_ratio for d in logs]
        for i, e in zip(iter, percent_missratio):
            ignore_obj_size_overall_percent_missratio[size][i].append(e)
            ignore_obj_size_overall_percent_missratio[0][i].append(e)

        d_percent_missratio = [
            percent_missratio[0] - percent_missratio[i]
            for i in range(1, len(percent_missratio))
        ]
        for i, e in zip(iter_2, d_percent_missratio):
            ignore_obj_size_overall_d_percent_missratio[size][i].append(e)
            ignore_obj_size_overall_d_percent_missratio[0][i].append(e)

        n_promotion = [d.n_promoted for d in logs]
        for i, e in zip(iter, n_promotion):
            ignore_obj_size_overall_promotions[size][i].append(e)
            ignore_obj_size_overall_promotions[0][i].append(e)

        d_n_promotion = [
            n_promotion[0] - n_promotion[i] for i in range(1, len(n_promotion))
        ]
        for i, e in zip(iter_2, d_n_promotion):
            ignore_obj_size_overall_d_promotions[size][i].append(e)
            ignore_obj_size_overall_d_promotions[0][i].append(e)

        n_percent_promotion = [d.n_promoted / logs[0].n_promoted for d in logs]
        for i, e in zip(iter, n_percent_promotion):
            ignore_obj_size_overall_percent_promotions[size][i].append(e)
            ignore_obj_size_overall_percent_promotions[0][i].append(e)

        d_n_percent_promotion = [
            n_percent_promotion[0] - n_percent_promotion[i]
            for i in range(1, len(n_percent_promotion))
        ]
        for i, e in zip(iter_2, d_n_percent_promotion):
            ignore_obj_size_overall_d_percent_promotions[size][i].append(e)
            ignore_obj_size_overall_d_percent_promotions[0][i].append(e)
    else:
        miss_ratio = [d.miss_ratio for d in logs]
        for i, e in zip(iter, miss_ratio):
            overall_missratio[size][i].append(e)
            overall_missratio[0][i].append(e)

        d_miss_ratio = [
            miss_ratio[0] - miss_ratio[1] for i in range(1, len(miss_ratio))
        ]
        for i, e in zip(iter_2, d_miss_ratio):
            overall_d_missratio[size][i].append(e)
            overall_d_missratio[0][i].append(e)

        percent_missratio = [d.miss_ratio / logs[0].miss_ratio for d in logs]
        for i, e in zip(iter, percent_missratio):
            overall_percent_missratio[size][i].append(e)
            overall_percent_missratio[0][i].append(e)

        d_percent_missratio = [
            percent_missratio[0] - percent_missratio[i]
            for i in range(1, len(percent_missratio))
        ]
        for i, e in zip(iter_2, d_percent_missratio):
            overall_d_percent_missratio[size][i].append(e)
            overall_d_percent_missratio[0][i].append(e)

        n_promotion = [d.n_promoted for d in logs]
        for i, e in zip(iter, n_promotion):
            overall_promotions[size][i].append(e)
            overall_promotions[0][i].append(e)

        d_n_promotion = [
            n_promotion[0] - n_promotion[i] for i in range(1, len(n_promotion))
        ]
        for i, e in zip(iter_2, d_n_promotion):
            overall_d_promotions[size][i].append(e)
            overall_d_promotions[0][i].append(e)

        n_percent_promotion = [d.n_promoted / logs[0].n_promoted for d in logs]
        for i, e in zip(iter, n_percent_promotion):
            overall_percent_promotions[size][i].append(e)
            overall_percent_promotions[0][i].append(e)

        d_n_percent_promotion = [
            n_percent_promotion[0] - n_percent_promotion[i]
            for i in range(1, len(n_percent_promotion))
        ]
        for i, e in zip(iter_2, d_n_percent_promotion):
            overall_d_percent_promotions[size][i].append(e)
            overall_d_percent_promotions[0][i].append(e)

    # if Path(output_path).exists():
    #     continue

    max_iteration = 19
    # MIN_PROMOTION_DIFF = 1e-8
    MIN_PROMOTION_DIFF = 0

    diffs = abs(np.diff(n_percent_promotion))
    cond = np.where(diffs > MIN_PROMOTION_DIFF)[0]
    # print("diffs", diffs, "\n")
    # print("cond", cond, "\n")
    max_iteration = np.max(cond) + 1

    if max_iteration > 19:
        max_iteration = 19

    # print("Max Iteration", max_iteration, "\n")

    if desc.count("ignore_obj_size"):
        ignore_obj_size_overall_max_iteration[size].append(max_iteration)
    else:
        overall_max_iteration[size].append(max_iteration)

    iter = [i for i in range(1, max_iteration + 2)]
    iter_2 = [i for i in range(2, max_iteration + 2)]

    n_promotion = n_promotion[: max_iteration + 1]
    # print(n_promotion, "\n")
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

    if (prefix, size, desc.count("ignore_obj_size")) in my_algo:
        y1 = my_algo[(prefix, size, desc.count("ignore_obj_size"))].n_promoted
        y2 = my_algo[(prefix, size, desc.count("ignore_obj_size"))].miss_ratio
        axs[0].axhline(
            y=y1,
            color="purple",
            linestyle="--",
            label="My Clock Promotion",
        )
        ax2.axhline(
            y=y2,
            color="green",
            linestyle=":",
            label="My Clock Miss Ratio",
        )

        ymin, ymax = axs[0].get_ylim()
        axs[0].set_ylim(min(ymin, y1), max(ymax, y1))

        ymin2, ymax2 = ax2.get_ylim()
        ax2.set_ylim(min(ymin2, y2), max(ymax2, y2))

    lines1, labels1 = axs[0].get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    axs[0].legend(lines1 + lines2, labels1 + labels2, loc="upper right")

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

    if (prefix, size, desc.count("ignore_obj_size")) in my_algo:
        y1 = (
            n_promotion[0]
            - my_algo[(prefix, size, desc.count("ignore_obj_size"))].n_promoted
        )
        y2 = (
            miss_ratio[0]
            - my_algo[(prefix, size, desc.count("ignore_obj_size"))].miss_ratio
        )
        axs[1].axhline(
            y=y1,
            color="purple",
            linestyle="--",
            label="My Clock Promotion",
        )
        ax3.axhline(
            y=y2,
            color="green",
            linestyle=":",
            label="My Clock Miss Ratio",
        )

        ymin, ymax = axs[1].get_ylim()
        axs[1].set_ylim(min(ymin, y1), max(ymax, y1))
        ymin2, ymax2 = ax3.get_ylim()
        ax3.set_ylim(min(ymin2, y2), max(ymax2, y2))

    lines1, labels1 = axs[1].get_legend_handles_labels()
    lines2, labels2 = ax3.get_legend_handles_labels()
    axs[1].legend(lines1 + lines2, labels1 + labels2, loc="upper right")

    plt.title("Relative")

    # axs[2].set_xlabel("Iteration")
    # axs[2].set_ylabel("Promotion", color="blue")
    # axs[2].plot(iter, n_promotion, marker="o", linestyle="-", color="blue")
    # axs[2].tick_params(axis="y", labelcolor="blue")
    # axs[2].yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))
    # axs[2].xaxis.set_major_locator(ticker.MaxNLocator(nbins=20))
    #
    # ax4 = axs[2].twinx()
    # ax4.set_ylabel("Miss Ratio", color="red")
    # ax4.plot(iter, miss_ratio, marker="s", linestyle="--", color="red")
    # ax4.tick_params(axis="y", labelcolor="red")
    # ax4.yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))
    # ax4.set_ylim(0, 1)

    # plt.title("Fixed Scale")

    fig.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path)
    plt.close()


def max_iteration_boxplot(d: dict, title, y_label, prefix):
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


max_iteration_boxplot(
    ignore_obj_size_overall_max_iteration, "Max Iteration", "Max Iteration", ""
)
max_iteration_boxplot(overall_max_iteration, "Max Iteration", "Max Iteration", "osi_")


def box_plot(d, title, y_label, prefix):
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


box_plot(overall_missratio, "Miss Ratio", "Miss Ratio", "miss_ratio")
box_plot(
    overall_percent_missratio,
    "Miss Ratio (relative)",
    "Miss Ratio (relative)",
    "miss_ratio_percent",
)
box_plot(overall_promotions, "Promotions", "Promotions", "promotions")
box_plot(
    overall_percent_promotions,
    "Promotions (relative)",
    "Promotions (relative)",
    "promotions_percent",
)
box_plot(
    overall_d_missratio,
    "Miss Ratio reduced",
    "First Miss Ratio - Current Miss Ratio",
    "d_miss_ratio",
)
box_plot(
    overall_d_percent_missratio,
    "Miss Ratio (relative) reduced",
    "First Miss Ratio - Current Miss Ratio (relative)",
    "d_miss_ratio_percent",
)
box_plot(
    overall_d_promotions,
    "Promotions reduced",
    "First Promotions - Current Promotions",
    "d_promotions",
)
box_plot(
    overall_d_percent_promotions,
    "Promotions (relative) reduced",
    "First Promotions - Current Promotions (relative)",
    "d_promotions_percent",
)

box_plot(
    ignore_obj_size_overall_missratio, "Miss Ratio", "Miss Ratio", "osi_miss_ratio"
)
box_plot(
    ignore_obj_size_overall_percent_missratio,
    "Miss Ratio (relative)",
    "Miss Ratio (relative)",
    "osi_miss_ratio_percent",
)
box_plot(overall_promotions, "Promotions", "Promotions", "osi_promotions")
box_plot(
    ignore_obj_size_overall_percent_promotions,
    "Promotions (relative)",
    "Promotions (relative)",
    "osi_promotions_percent",
)
box_plot(
    ignore_obj_size_overall_d_missratio,
    "Miss Ratio reduced",
    "First Miss Ratio - Current Miss Ratio",
    "osi_d_miss_ratio",
)
box_plot(
    ignore_obj_size_overall_d_percent_missratio,
    "Miss Ratio (relative) reduced",
    "First Miss Ratio - Current Miss Ratio (relative)",
    "osi_d_miss_ratio_percent",
)
box_plot(
    ignore_obj_size_overall_d_promotions,
    "Promotions reduced",
    "First Promotions - Current Promotions",
    "osi_d_promotions",
)
box_plot(
    ignore_obj_size_overall_d_percent_promotions,
    "Promotions (relative) reduced",
    "First Promotions - Current Promotions (relative)",
    "osi_d_promotions_percent",
)
