import psycopg2

conn = psycopg2.connect("dbname=python_intermedio_db user=postgres password=root")
cur = conn.cursor()

#buscar al usuario en la BD con query
consulta = "SELECT * FROM usuarios;" #Si despues de usuarios le pongo LIMIT 1 sólo trae un resultado 

#Para ejecutar el codigo SQL
cur.execute(consulta)

resultado1 = cur.fetchone() #regresa una tupla con el dato a diferencia de fetchall que regresa una lista con todos los resultados
resultado2 = cur.fetchone() #se va posicionando en el siguiente elemento
resultado3 = cur.fetchone()

print(resultado1)
print(resultado2)
print(resultado3)

cur.close()
conn.close()