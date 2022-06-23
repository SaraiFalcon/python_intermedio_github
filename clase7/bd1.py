#ejemplo de conexión a base de datos postgres utilizando psycopg2

import psycopg2

conn = psycopg2.connect("dbname=python_intermedio_db user=postgres password=root")

cur = conn.cursor()

cur.execute("SELECT * FROM usuarios;")

print(cur.fetchone())

#Cierre de conexiones de BD
cur.close()
conn.close()