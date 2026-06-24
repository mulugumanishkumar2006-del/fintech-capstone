import pandas as pd
from pathlib import Path

# Paths
input_file = Path("data/raw/02_nav_history.csv")
output_file = Path("data/processed/clean_nav_history.csv")

# Load data
df = pd.read_csv(input_file)

print("Original Shape:", df.shape)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort values
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Remove invalid NAV values
df = df[df["nav"] > 0]

# Reset index
df = df.reset_index(drop=True)

# Save cleaned file
df.to_csv(output_file, index=False)

print("Cleaned Shape:", df.shape)
print("Saved to:", output_file)