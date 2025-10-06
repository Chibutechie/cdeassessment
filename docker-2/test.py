import psycopg2
from connection import connect

# required_vars = {
#     "host": "localhost",
#     "dbname": "elt_db",
#     "user": "postgres",
#     "password": "024899",
#     "port": 5432
# }

try:
    conn = psycopg2.connect(**connect)
    print(f"Connection status: {conn.status}") 
    print(f"Database: {conn.info.dbname}")
    print(f"User: {conn.info.user}")
    print(f"Host: {conn.info.host}")
    conn.close()
except psycopg2.Error as e:
    print(f"Connection failed: {e}")