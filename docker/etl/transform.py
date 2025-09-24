def transform(df):
    df = df.copy()
    df.columns = [c.lower().replace(".", "_") for c in df.columns]

    def extract_id(url):
        try:
            return int(url.rstrip("/").split("/")[-1])
        except:
            return None

    if "url" in df.columns:
        df["pokemon_id"] = df["url"].apply(extract_id)

    cols = [c for c in ["pokemon_id", "name", "url"] if c in df.columns]
    print("transformation complete")
    return df[cols]