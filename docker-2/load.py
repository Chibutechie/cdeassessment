import os
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
from connection import connect

try: 
    conn = psycopg2.connect(**connect)
    print("Connection successful!")
    conn.close()
    print("Load successful")
except Exception as error: 
    print(f"Error: {error}")