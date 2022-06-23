import psycopg2

#abrimos la conexión
conn = psycopg2.connect("dbname=python_intermedio_db user=postgres password=root")
#abrimos un cursos a la BD
cur = conn.cursor()

#user= shudleston5
#password=XeL8MY
#fetchone() metodo que obtiene un registro de la base de datos
#fetchall() metodo que obtiene todos los registros
#rowcount contamos registros
#rownumber contamos número de filas 

usuario = input("Usuario: ")
password = input("Contraseña: ")

#buscar al usuario en la BD con query
consulta = f"SELECT username, password FROM usuarios where username = \'{usuario}\' AND password = \'{password}\'" 

#Para ejecutar el codigo SQL
cur.execute(consulta)

#Mostrar el resultado de la consulta
usuario_valido = cur.fetchall()
print(usuario_valido)

#Si se encuentra un usuario con esos datos enviar un mensaje de bienvenida

#Si el

cur.close()
conn.close()