import psycopg2
import os

os.system('cls')

#abrimos la conexión
conn = psycopg2.connect("dbname=python_intermedio_db user=postgres password=root")
#abrimos un cursos a la BD
cur = conn.cursor()

#user = shudleston5
#password = XeL8MY
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

#Mostrar el resultado de la consulta. Retorna una tupla con un solo resultado
usuario_encontrado = cur.fetchone()
print(usuario_encontrado)

#Si se encuentra un usuario con esos datos enviar un mensaje de bienvenida
#Si encuentra algo en la tupla o sea, que sea mayor que 0 
if len(usuario_encontrado) > 0:
    print(f"Bienvenido {usuario_encontrado[0]}") # [0] Porque sólo quiero que imprima el nombre del usuario
else:
    print("Usuario o password incorrecto, intente de nuevo")

#Si el

cur.close()
conn.close()