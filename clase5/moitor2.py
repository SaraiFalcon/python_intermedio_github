#Hecho por mi
#pasar todo lo del monitor 1 a un archivo de texco
#Crear una carpeta donde se almacenarán los logs
#Crear un archivo con X nombre
#Insertar la informacion recabada en el archivo

#open con with
#variable de contexto

import psutil
import os

cpu_nucleos = psutil.cpu_count()
cpu_frecuencia = psutil.cpu_freq()
memoria_virtual = psutil.virtual_memory()
disco_uso = psutil.disk_usage ('/')

os.system('clear') #ejecuta comandos como si estuvieramos en la consola
os.mkdir("Carpeta_logs")

with open("Carpeta_logs\monitor2.txt", "w") as archivo:
    archivo.write(f"Nucleos del CPU: {cpu_nucleos}\n")
    archivo.write(f"frecuencia del CPU: {cpu_frecuencia}\n")
    archivo.write(f"Memoria virtual: {memoria_virtual}\n")
    archivo.write(f"Uso de disco: {disco_uso}\n")