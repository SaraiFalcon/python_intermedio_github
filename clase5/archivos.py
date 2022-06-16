# practica de manipulación de archivos con python
# open ()

archivo = open("texto.txt", "w")

archivo.write("Hola \n")
archivo.write("mundo")

archivo.close()

xlsx = open("libro.xlsx", 'w')
xlsx.close

print ("Terminó la manipulación de archivos")

