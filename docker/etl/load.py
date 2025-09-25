import os
from sqlalchemy import create_engine

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

if not db_password:
    raise ValueError("DB_PASSWORD is not set. Please provide it as an environment variable.")

def load(df, table_name="pokemon"):
    conn = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(conn)
    df.to_sql(table_name, engine, schema="public", if_exists="append", index=False)
    print(f"Loaded {len(df)} rows into '{table_name}' in DB '{db_name}'")
