import requests
import pandas as pd
import os
import re

os.makedirs("data/raw", exist_ok=True)

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "data" in data:
            df = pd.DataFrame(data["data"])
            filename = re.sub(r'[^A-Za-z0-9]+', '_', name)
            df.to_csv(f"data/raw/{filename}.csv", index=False)
            print(f"✅ Downloaded {name}")
        else:
            print(f"❌ No data found for {name}")
    else:
        print(f"❌ Failed to fetch {name}")