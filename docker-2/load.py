import psycopg2

hostname = 'localhost'
database = 'elt_db'
username = 'postgres'
pwd = '024899'
port_id = 5432

conn = psycopg2.connect( 
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)

conn.close()

print("Load successful")