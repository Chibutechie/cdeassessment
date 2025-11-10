import pandas as pd
from sqlalchemy import create_engine

connect = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "postgres",
    "password": "024899",
    "port": 5432
}

try:  
    engine = create_engine(f"postgresql+psycopg2://{connect['user']}:{connect['password']}@{connect['host']}:{connect['port']}/{connect['dbname']}")
    
    data = pd.read_csv('data.csv', encoding='ISO-8859-1')
    
    data.to_sql('data', engine, schema='public', if_exists='replace', index=False)
    
    print(f"Data loaded successfully! {len(data)} rows inserted.")

except Exception as error: 
    print(f"Error: {error}")