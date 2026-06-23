import os
import pandas as pd

DATA_PATH = "data/raw"

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

print("="*60)
print("DATASET SUMMARY")
print("="*60)

datasets = {}

for file in csv_files:

    path = os.path.join(DATA_PATH,file)

    df = pd.read_csv(path)

    datasets[file]=df

    print(f"\nDataset : {file}")

    print("-"*60)

    print("Shape")
    print(df.shape)

    print("\nData Types")

    print(df.dtypes)

    print("\nFirst Five Rows")

    print(df.head())

    print("\nMissing Values")

    print(df.isnull().sum())

    print("\nDuplicate Rows")

    print(df.duplicated().sum())

print("\nCompleted.")