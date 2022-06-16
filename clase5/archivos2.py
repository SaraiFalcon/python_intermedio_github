#open con with
#variable de contexto

with open("texto2.txt", "w") as archivo:
    archivo.write("Escribiendo archivo utilizando with") #esto es que mientras se corra esta línea va a existir archivo y solito al finalizar python lo cierra, por eso no lleva close
    