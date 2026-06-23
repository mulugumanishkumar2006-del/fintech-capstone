import requests
import pandas as pd

scheme_code = "125497"

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

data = response.json()

meta = data["meta"]

history = data["data"]

df = pd.DataFrame(history)

df.to_csv("data/raw/HDFC_Top100_NAV.csv",index=False)

print(meta)

print(df.head())