import pandas as pd
import sys


def describe_csv(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    print("\n🧾 Basic Info:")
    print("-" * 60)
    print(df.info())

    print("\n📊 Summary Statistics (Numerical Columns):")
    print("-" * 60)
    print(df.describe(include=[float, int]))

    print("\n📌 Missing Values:")
    print("-" * 60)
    print(df.isnull().sum())

    print("\n🆔 Unique Values per Column:")
    print("-" * 60)
    print(df.nunique())

    if "wasted" in df.columns:
        print("\n🚫 Subset: wasted == 0")
        print("-" * 60)
        print(df[df["wasted"] == 0].describe(include=[float, int]))

        print("\n✅ Subset: wasted == 1")
        print("-" * 60)
        print(df[df["wasted"] == 1].describe(include=[float, int]))
    else:
        print("\n⚠️ Column 'wasted' not found in CSV.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python describe_csv.py <your_file.csv>")
    else:
        describe_csv(sys.argv[1])
