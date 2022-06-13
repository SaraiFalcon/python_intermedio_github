import os

def crear_carpetas(sufijo, cantidad):
    """
    Crear N número de carpetas
    """

    for i in range (cantidad):
        os.mkdir (f"{sufijo}{i}")
        print(f"creando carpeta {sufijo}{i}")