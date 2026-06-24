import pandas as pd
from pathlib import Path

# Paths
input_file = Path("data/raw/08_investor_transactions.csv")
output_file = Path("data/processed/clean_transactions.csv")

# Load data
df = pd.read_csv(input_file)

print("Original Shape:", df.shape)

# Convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Remove duplicates
df = df.drop_duplicates()

# Validate amount
df = df[df["amount_inr"] > 0]

# Standardize transaction type
df["transaction_type"] = df["transaction_type"].str.strip()

valid_types = ["SIP", "Lumpsum", "Redemption"]
df = df[df["transaction_type"].isin(valid_types)]

# Validate KYC status
valid_kyc = ["Verified", "Pending"]
df = df[df["kyc_status"].isin(valid_kyc)]

# Reset index
df = df.reset_index(drop=True)

# Save cleaned file
df.to_csv(output_file, index=False)

print("Cleaned Shape:", df.shape)
print("\nTransaction Types:")
print(df["transaction_type"].value_counts())

print("\nKYC Status:")
print(df["kyc_status"].value_counts())

print("\nSaved to:", output_file)