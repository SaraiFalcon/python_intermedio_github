#ejemplo de conexión a base de datos postgres utilizando psycopg2

import psycopg2

conn = psycopg2.connect("dbname=python_intermedio_db user=postgres password=root")
cur = conn.cursor()

#Obtener usuario id 50
cur.execute("SELECT * FROM usuarios where id=50;")
print(cur.fetchone())

#Obtener todos los usuarios como una tupla
cur.execute("SELECT * FROM usuarios;")

usuarios_tupla= cur.fetchall()
for usuario in usuarios_tupla:
    print(usuario)

#Cierre de conexiones de BD
cur.close()
conn.close()