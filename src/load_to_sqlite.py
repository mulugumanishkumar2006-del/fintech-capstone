import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

# Load tables
pd.read_csv("data/raw/01_fund_master.csv").to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv("data/processed/clean_nav_history.csv").to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv("data/processed/clean_transactions.csv").to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv("data/processed/clean_performance.csv").to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv("data/raw/03_aum_by_fund_house.csv").to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv("data/raw/04_monthly_sip_inflows.csv").to_sql(
    "fact_sip_industry",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully!")
print("Location: data/db/bluestock_mf.db")