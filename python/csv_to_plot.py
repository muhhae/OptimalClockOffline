import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from dataclasses import dataclass
import os
import glob
from pathlib import Path


@dataclass
class OutputLog:
    trace_path: str
    cache_size: int
    miss_ratio: float
    n_req: int
    n_promoted: int


result_dir = "../result/log"
output_dir = "../result/graph"

files = glob.glob(os.path.join(result_dir, "*.csv"))

for file in files:
    if Path(file).stat().st_size == 0:
        continue

    output_path = os.path.join(output_dir, Path(file).stem + "_py.png")

    if Path(output_path).exists():
        continue

    df = pd.read_csv(file)
    if df.empty:
        continue

    df = df.rename(columns={"cache_size(MiB)": "cache_size"})
    logs = [OutputLog(**row) for row in df.to_dict(orient="records")]

    iter = [i for i in range(1, 21)]
    miss_ratio = [d.miss_ratio for d in logs]
    n_promotion = [d.n_promoted for d in logs]

    fig, ax1 = plt.subplots(figsize=(10, 5))
    ax1.set_xlabel("Iteration")
    ax1.set_ylabel("Promotion", color="blue")
    ax1.plot(iter, n_promotion, marker="o", linestyle="-", color="blue")
    ax1.tick_params(axis="y", labelcolor="blue")
    ax1.yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))

    ax2 = ax1.twinx()
    ax2.set_ylabel("Miss Ratio", color="red")
    ax2.plot(iter, miss_ratio, marker="s", linestyle="--", color="red")
    ax2.tick_params(axis="y", labelcolor="red")
    ax2.yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))

    plt.title(Path(file).stem)
    fig.tight_layout()
    fig.savefig(output_path)
