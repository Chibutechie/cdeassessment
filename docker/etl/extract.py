import requests
import pandas as pd
import os

def extract():
        url = os.getenv("URL")
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        df = pd.json_normalize(data.get("results", []))
        return df
    except Exception as e:
        print(f"Error while extracting: {e}")
        return None

if __name__ == "__main__":
    df = extract()
    if df is not None:
        print(df)