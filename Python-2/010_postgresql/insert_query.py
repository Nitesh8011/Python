import psycopg2

DB_NAME = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_USER = 'postgres'
DB_PASS = 'postgres'


conn = psycopg2.connect(database=DB_NAME,
                        host=DB_HOST,
                        port=DB_PORT,
                        user=DB_USER,
                        password=DB_PASS)

print("connected with database")

try:
    cur = conn.cursor()

    insert_query = """
        INSERT INTO employee (id, name, email) VALUES (%s, %s, %s)
    """
    data = ('1', 'Nitesh Kumar', 'abc@example.com')
    
    cur.execute(insert_query, data)
    conn.commit()

    print("Query inserted successfully")

except Exception as e:
    print("Failed to insert query ",{e})

finally:
    cur.close()
    conn.close()