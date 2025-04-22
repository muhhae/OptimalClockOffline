import pandas as pd
import sys


def describe_csv(file_path):
    df = pd.read_csv(file_path)

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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python describe_csv.py <your_file.csv>")
    else:
        describe_csv(sys.argv[1])
