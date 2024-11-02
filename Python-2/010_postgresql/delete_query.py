import psycopg2

DB_HOST = 'localhost'
DB_PORT = '5432'
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'postgres'


conn = psycopg2.connect(database=DB_NAME,
                        user=DB_NAME,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)
print("Connected with Database")

cur = conn.cursor()

original_table = input("Enter original table name: ")
backup_table = input("Enter backup table suffix: ")
delete_query = input("Enter query: ")

backup_query = f'select * into {original_table}_{backup_table} from {original_table}'

# backup query execute
cur.execute(backup_query)
conn.commit()

print("Backup query executed")
print("Total row effected "+str(cur.rowcount))


# delete query execute
cur.execute(delete_query)
conn.commit()

print("Delete query executed")
print("Total row effected "+str(cur.rowcount))