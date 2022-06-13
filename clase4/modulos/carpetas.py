import os
import sys
import shutil


def crear_carpetas(sufijo, cantidad):
    """
    Crear N número de carpetas
    """
    for i in range (cantidad):
        os.mkdir (f"{sufijo}{i}")
        print(f"creando carpeta {sufijo}{i}")


def borrar_carpeta(nombre_archivo, cantidad):
  
    for i in range (cantidad):
        carpeta = nombre_archivo+ str(i)
        if os.path.isdir(carpeta):
            os.rmdir (carpeta)
        print(f"borrando carpeta", carpeta)