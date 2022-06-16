#Manejo de excepciones cuando creamos un directorio

import os

try:
    os.mkdir("Carpeta_prueba")
    print("Se creo la carpeta")
except FileExistsError as ex:
    os.mkdir("carpeta_prueba1")
    print("Ya existe ese directorio, intenta con otro nombre")
except FileNotFoundError as ex:
    print("No se encontró el directorio proporcionado")
except Exception as ex:
    print("Oops, ocurrio un error")

print("Fin del script")