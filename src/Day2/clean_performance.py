import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data" / "raw" / "07_scheme_performance.csv"
output_file = BASE_DIR / "data" / "processed" / "clean_performance.csv"

df = pd.read_csv(input_file)

print("Original Shape:", df.shape)

# Convert numeric columns
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Flag negative Sharpe ratios
if "sharpe_ratio" in df.columns:
    negative_sharpe = df[df["sharpe_ratio"] < 0]

    print("\nFunds with Negative Sharpe Ratio:")
    print(negative_sharpe[["amfi_code", "sharpe_ratio"]])

# Validate expense ratio
if "expense_ratio_pct" in df.columns:
    invalid_expense = df[
        (df["expense_ratio_pct"] < 0.1) |
        (df["expense_ratio_pct"] > 2.5)
    ]

    print("\nInvalid Expense Ratios:")
    print(invalid_expense)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.fillna(0)

output_file.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_file, index=False)

print("\nCleaned Shape:", df.shape)
print(f"Saved: {output_file}")