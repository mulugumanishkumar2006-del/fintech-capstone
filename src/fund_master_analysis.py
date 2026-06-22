import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Unique Fund Houses:")
print(df["fund_house"].unique())

print("\nCategory Counts:")
print(df["category"].value_counts())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].value_counts())