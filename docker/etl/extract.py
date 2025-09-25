def extract():
    import requests
    import pandas as pd

    try:
        url = "https://pokeapi.co/api/v2/pokemon?limit=20"
        response = requests.get(url)
        response.raise_for_status()  # check for HTTP errors
        data = response.json()
        df = pd.json_normalize(data, 'results')
        print(f"Extracted rows: {len(df)}")
        return df
    except Exception as e:
        print(f"ETL pipeline failed during extraction: {e}")
        return pd.DataFrame()
