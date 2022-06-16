#Manejo de excepciones con python

#ValueError

try:
    respuesta = int(input("Please enter a number: "))
except ValueError as ex:
    print("Hubo un error de valor:", ex)
except Exception as ex:
    print("Hubo una excepción:", ex)

#Solicitar un número, si no es número manejar excepciones
while True:
     try:
         x = int(input("Please enter a number: "))
         break
     except ValueError:
         print("Oops!  That was no valid number.  Try again...")