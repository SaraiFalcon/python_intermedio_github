#ejemplo de uso de paquete python 
#psutil
#https://psutil.readthedocs.io/en/latest/

import psutil
import os

#nucleos del cpu
cpu_nucleos = psutil.cpu_count()
cpu_frecuencia = psutil.cpu_freq()

#memoria
memoria_virtual = psutil.virtual_memory()

#disco
disco_uso = psutil.disk_usage ('/')

os.system('clear') #ejecuta comandos como si estuvieramos en la consola
print("=" * 50)
print("Información del sistema")
print("Núcleos del CPU: ", cpu_nucleos)
print("frecuencia del CPU: ", cpu_frecuencia)
print("Memoria virtual: ", memoria_virtual)
print("Uso de disco: ", disco_uso)
print("=" * 50)