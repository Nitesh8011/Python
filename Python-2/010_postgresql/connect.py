import psycopg2

DB_HOST = 'localhost'
DB_PORT = '5432'
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'postgres'


try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_NAME,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    print("Connected with Database")

except Exception as e:
    print("failed to connect with database: ",{e})