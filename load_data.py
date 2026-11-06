"""Load the original AAA workbook and print its structure."""
from pathlib import Path

import pandas as pd


def main():
    path = Path(__file__).resolve().parent / "data_full.xls"
    df = pd.read_excel(path, sheet_name="Sheet1", engine="xlrd")
    X = df.drop(columns="Target")
    y = df["Target"]
    counts = {int(k): int(v) for k, v in y.value_counts().sort_index().items()}
    print(f"Records: {len(df)}")
    print(f"Features: {X.shape[1]}")
    print(f"Blank cells: {int(df.isna().sum().sum())}")
    print(f"Target counts: {counts}")
    print(f"X shape: {X.shape}")
    print(f"y shape: {y.shape}")


if __name__ == "__main__":
    main()
