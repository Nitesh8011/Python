import psycopg2

DB_NAME = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_USER = 'postgres'
DB_PASS = 'postgres'


try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    print("connected with database")

except Exception as e:
    print("Failed to connect with database: ", {e})

cur = conn.cursor()

cur.execute("""
    CREATE TABLE employee(
            ID INT   PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            EMAIL TEXT NOT NULL)
    """)

conn.commit()
print("Table created successfully")
conn.close()