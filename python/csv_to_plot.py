import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from dataclasses import dataclass
import os
import glob
from pathlib import Path
from collections import defaultdict


def extract_desc(filename):
    prefix = filename[: filename.rfind("[")]
    desc = filename[filename.rfind("[") + 1 : filename.rfind("]")]
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
overall_promotions = defaultdict(lambda: defaultdict(list))
overall_d_missratio = defaultdict(lambda: defaultdict(list))
overall_d_promotions = defaultdict(lambda: defaultdict(list))

for file in files:
    if Path(file).stat().st_size == 0:
        continue

    output_path = os.path.join(output_dir, Path(file).stem + ".png")

    df = pd.read_csv(file)
    if df.empty:
        continue

    df = df.rename(columns={"cache_size(MiB)": "cache_size"})
    logs = [OutputLog(**row) for row in df.to_dict(orient="records")]

    iter = [i for i in range(1, 21)]
    miss_ratio = [d.miss_ratio for d in logs]
    n_promotion = [d.n_promoted for d in logs]

    iter_2 = [i for i in range(2, 21)]
    d_miss_ratio = [miss_ratio[i] - miss_ratio[0] for i in range(1, len(miss_ratio))]
    d_n_promotion = [
        n_promotion[0] - n_promotion[i] for i in range(1, len(n_promotion))
    ]

    _, desc = extract_desc(file)
    size = float(desc)
    for i, e in zip(iter, miss_ratio):
        overall_missratio[size][i].append(e)
        overall_missratio[0][i].append(e)
    for i, e in zip(iter, n_promotion):
        overall_promotions[size][i].append(e)
        overall_promotions[0][i].append(e)
    for i, e in zip(iter_2, d_miss_ratio):
        overall_d_missratio[size][i].append(e)
        overall_d_missratio[0][i].append(e)
    for i, e in zip(iter_2, d_n_promotion):
        overall_d_promotions[size][i].append(e)
        overall_d_promotions[0][i].append(e)

    # if Path(output_path).exists():
    #     continue

    fig, axs = plt.subplots(3, 1, figsize=(10, 5 * 3))
    axs[0].set_xlabel("Iteration")
    axs[0].set_ylabel("Promotion", color="blue")
    axs[0].plot(iter, n_promotion, marker="o", linestyle="-", color="blue")
    axs[0].tick_params(axis="y", labelcolor="blue")
    axs[0].yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))
    axs[0].xaxis.set_major_locator(ticker.MaxNLocator(nbins=21))

    ax2 = axs[0].twinx()
    ax2.set_ylabel("Miss Ratio", color="red")
    ax2.plot(iter, miss_ratio, marker="s", linestyle="--", color="red")
    ax2.tick_params(axis="y", labelcolor="red")
    ax2.yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))

    plt.title(Path(file).stem)

    axs[1].set_xlabel("Iteration")
    axs[1].set_ylabel("$\\Delta$ Promotion", color="blue")
    axs[1].plot(iter_2, d_n_promotion, marker="o", linestyle="-", color="blue")
    axs[1].tick_params(axis="y", labelcolor="blue")
    axs[1].yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))
    axs[1].xaxis.set_major_locator(ticker.MaxNLocator(nbins=20))

    ax3 = axs[1].twinx()
    ax3.set_ylabel("$\\Delta$ Miss Ratio", color="red")
    ax3.plot(iter_2, d_miss_ratio, marker="s", linestyle="--", color="red")
    ax3.tick_params(axis="y", labelcolor="red")
    ax3.yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))

    plt.title("Relative")

    axs[2].set_xlabel("Iteration")
    axs[2].set_ylabel("Promotion", color="blue")
    axs[2].plot(iter, n_promotion, marker="o", linestyle="-", color="blue")
    axs[2].tick_params(axis="y", labelcolor="blue")
    axs[2].yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))
    axs[2].xaxis.set_major_locator(ticker.MaxNLocator(nbins=20))

    ax4 = axs[2].twinx()
    ax4.set_ylabel("Miss Ratio", color="red")
    ax4.plot(iter, miss_ratio, marker="s", linestyle="--", color="red")
    ax4.tick_params(axis="y", labelcolor="red")
    ax4.yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))
    ax4.set_ylim(0, 1)

    plt.title("Fixed Scale")

    fig.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path)
    plt.close()

overal_path = "../result/overall"

overall_missratio = dict(sorted(overall_missratio.items()))
overall_promotions = dict(sorted(overall_promotions.items()))

all_i = sorted({i for desc in overall_missratio.values() for i in desc})
os.makedirs(os.path.dirname(overal_path), exist_ok=True)

for i in all_i:
    data = []
    labels = []
    for desc in overall_missratio:
        if i in overall_missratio[desc]:
            data.append(overall_missratio[desc][i])
            labels.append(desc)

    plt.figure()
    plt.boxplot(data, tick_labels=labels)
    plt.title(f"Miss ratio across cache size (i = {i})")
    plt.xlabel("cache size")
    plt.ylabel("Miss Ratio")
    plt.savefig(overal_path + "/mr_i_" + str(i) + ".png")
    plt.close()

for desc in overall_missratio:
    data = []
    labels = []
    for i in sorted(overall_missratio[desc]):
        data.append(overall_missratio[desc][i])
        labels.append(str(i))

    if desc == 0:
        desc = "All"

    plt.figure()
    plt.boxplot(data, tick_labels=labels)
    plt.title(f"Miss ratio across i (cache size = {desc})")
    plt.xlabel("Iteration")
    plt.ylabel("Miss Ratio")
    plt.savefig(overal_path + "/mr_s_" + str(desc) + ".png")
    plt.close()

all_i = sorted({i for desc in overall_promotions.values() for i in desc})

for i in all_i:
    data = []
    labels = []
    for desc in overall_promotions:
        if i in overall_promotions[desc]:
            data.append(overall_promotions[desc][i])
            labels.append(desc)

    plt.figure()
    plt.boxplot(data, tick_labels=labels)
    plt.title(f"Promotions across cache size (i = {i})")
    plt.xlabel("Cache Size")
    plt.ylabel("Promotions")
    plt.savefig(overal_path + "/p_i_" + str(i) + ".png")
    plt.close()

for desc in overall_promotions:
    data = []
    labels = []
    for i in sorted(overall_promotions[desc]):
        data.append(overall_promotions[desc][i])
        labels.append(str(i))

    if desc == 0:
        desc = "All"

    plt.figure()
    plt.boxplot(data, tick_labels=labels)
    plt.title(f"Promotions across i (cache size = {desc})")
    plt.xlabel("Iteration")
    plt.ylabel("Promotions")
    plt.savefig(overal_path + "/p_s_" + str(desc) + ".png")
    plt.close()

overall_d_missratio = dict(sorted(overall_d_missratio.items()))
overall_d_promotions = dict(sorted(overall_d_promotions.items()))

all_i = sorted({i for desc in overall_d_missratio.values() for i in desc})

for i in all_i:
    data = []
    labels = []
    for desc in overall_d_missratio:
        if i in overall_d_missratio[desc]:
            data.append(overall_d_missratio[desc][i])
            labels.append(desc)

    plt.figure()
    plt.boxplot(data, tick_labels=labels)
    plt.title(f"Miss ratio increased across cache size (i = {i})")
    plt.xlabel("cache size")
    plt.ylabel("current_missratio - first_missratio")
    plt.savefig(overal_path + "/dmr_i_" + str(i) + ".png")
    plt.close()

for desc in overall_d_missratio:
    data = []
    labels = []
    for i in sorted(overall_d_missratio[desc]):
        data.append(overall_d_missratio[desc][i])
        labels.append(str(i))

    if desc == 0:
        desc = "All"

    plt.figure()
    plt.boxplot(data, tick_labels=labels)
    plt.title(f"Miss ratio increased across i (cache size = {desc})")
    plt.xlabel("Iteration")
    plt.ylabel("current_missratio - first_missratio")
    plt.savefig(overal_path + "/dmr_s_" + str(desc) + ".png")
    plt.close()

all_i = sorted({i for desc in overall_d_promotions.values() for i in desc})

for i in all_i:
    data = []
    labels = []
    for desc in overall_d_promotions:
        if i in overall_d_promotions[desc]:
            data.append(overall_d_promotions[desc][i])
            labels.append(desc)

    plt.figure()
    plt.boxplot(data, tick_labels=labels)
    plt.title(f"Promotions reduced across cache size (i = {i})")
    plt.xlabel("Cache Size")
    plt.ylabel("first_promotion - current_promotions")
    plt.savefig(overal_path + "/dp_i_" + str(i) + ".png")
    plt.close()

for desc in overall_d_promotions:
    data = []
    labels = []
    for i in sorted(overall_d_promotions[desc]):
        data.append(overall_d_promotions[desc][i])
        labels.append(str(i))

    if desc == 0:
        desc = "All"

    plt.figure()
    plt.boxplot(data, tick_labels=labels)
    plt.title(f"Promotions reduced across i (cache size = {desc})")
    plt.xlabel("Iteration")
    plt.ylabel("first_promotion - current_promotions")
    plt.savefig(overal_path + "/dp_s_" + str(desc) + ".png")
    plt.close()
