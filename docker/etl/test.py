import os
import pandas as pd
from sqlalchemy import create_engine

db_name = os.getenv("DB_NAME", "data_bank")
db_user = os.getenv("DB_USER", "postgres")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")

engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

df = pd.read_sql("SELECT COUNT(*) as row_count FROM pokemon", engine)
print(df)
