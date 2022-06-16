#ejemplo de lectura de archivos

with open("texto2.txt") as archivo:
    print(archivo.read())

with open("texto.txt") as archivo:
    print(archivo.read())

with open("texto.txt") as archivo:
    print(archivo.readline()) #lee una sola línea

print("=" * 50)

with open("carpetas.txt") as archivo:
    for linea in archivo.readlines():
        print(linea)