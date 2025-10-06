import pandas as pd
from sqlalchemy import create_engine

connect = {
    "host": "localhost",
    "dbname": "elt_db",
    "user": "postgres",
    "password": "024899",
    "port": 5432
}

try:  
    # Create engine
    engine = create_engine(f"postgresql+psycopg2://{connect['user']}:{connect['password']}@{connect['host']}:{connect['port']}/{connect['dbname']}")
    
    # Read CSV file
    data = pd.read_csv('data.csv', encoding='ISO-8859-1')
    
    # Load data into PostgreSQL
    data.to_sql('data', engine, schema='public', if_exists='append', index=False)
    
    print(f"Data loaded successfully! {len(data)} rows inserted.")

except Exception as error: 
    print(f"Error: {error}")