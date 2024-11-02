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

original_table = input("Enter original table name: ")
backup_table = input("Enter backup table suffix: ")
update_query = input("Enter update query: ")

cur = conn.cursor()
backup_query = f'select * into {original_table}_{backup_table} from {original_table}'

cur.execute(backup_query)
conn.commit()
print("Backup Table Created")
print("Total row affected "+str(cur.rowcount))


cur.execute(update_query)
conn.commit()
print("update query executed")
print("Total row affected "+str(cur.rowcount))