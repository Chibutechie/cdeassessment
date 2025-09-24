from extract import extract
from transform import transform
from load import load

def main():
    print("Starting ETL pipeline...")
    df = extract()
    print("Extracted rows:", len(df))
    df = transform(df)
    print("Transformed rows:", len(df))
    load(df, table_name="pokemon")

if __name__ == "__main__":
    main()
