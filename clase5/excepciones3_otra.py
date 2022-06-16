import os
# Actividad excepciones
# Replicar el comportamiento de creacion de carpetas con Windows

# al crear un directorio si ya existe agregarle entre parentesis el consecutivo
# carpeta
# carpeta(1)
# carpeta(2)

#Esto es una lista que se puede recorrer
#contenido = os.listdir('C:\\Users\\subex\\Desktop\\python_intermedio_github') #me lista todo lo que hay en el directorio

#print(contenido)
def crear_carpetas(nueva_carpeta, consecutivo=0):
    try:
        if consecutivo < 1:
            os.mkdir(nueva_carpeta)
        else:
            os.mkdir(nueva_carpeta + f'({consecutivo})')
    except FileExistsError as ex:
        crear_carpetas(nueva_carpeta, consecutivo + 1)

crear_carpetas("probando")