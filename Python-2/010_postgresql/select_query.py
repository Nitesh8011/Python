import psycopg2

DB_NAME = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_USER = 'postgres'
DB_PASS = 'postgres'


conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_NAME,
    password=DB_PASS
)

print("connected with database")

cur = conn.cursor()

cur.execute("select * from employee")
rows = cur.fetchall()

for data in rows:
    print("ID :" + str(data[0]))
    print("NAME :" + data[1])
    print("EMAIL :" + data[2])


print("data fetched successfully")
conn.close()