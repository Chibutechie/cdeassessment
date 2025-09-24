import os
from sqlalchemy import create_engine

def load(df, table_name="pokemon"):
    db_name = os.getenv("DB_NAME", "pokemon")
    db_user = os.getenv("DB_USER", "postgres")    
    db_password = os.getenv("DB_PASSWORD")        
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")

    if not db_password:
        raise ValueError("DB_PASSWORD is not set. Please provide it as an environment variable.")

    if df is None or df.empty:
        print("No data to load (empty DataFrame). Exiting load step.")
        return

    conn_str = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(conn_str)

    df.to_sql(table_name, engine, schema="public", if_exists="append", index=False)
    print(f"Loaded {len(df)} rows into '{table_name}' in DB '{db_name}'")

    engine.dispose()
