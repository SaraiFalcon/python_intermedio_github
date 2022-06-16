#ejemplo de lectura de archivos

with open("texto2.txt") as archivo:
    print(archivo.read())

with open("texto.txt") as archivo:
    print(archivo.read())

with open("texto.txt") as archivo:
    print(archivo.readline()) #lee una sola línea

print("=" * 50)

with open("carpetas.txt") as archivo:
    for linea in archivo.readlines(): #con este lee líneas en plural, si le pongo readline lee carpeta1 y cada caracter lo pone en una linea
        print(linea)