import os
# Actividad excepciones
# Replicar el comportamiento de creacion de carpetas con Windows

# al crear un directorio si ya existe agregarle entre parentesis el consecutivo
# carpeta
# carpeta(1)
# carpeta(2)

#Esto es una lista que se puede recorrer
#contenido = os.listdir('C:\\Users\\subex\\Desktop\\python_intermedio_github') #me lista todo lo que hay en el directorio

#print(contenido)

nueva_carpeta = input("Ingresa el nombre de la carpeta: ")

Lista1=os.listdir('C:\\Users\\subex\\Desktop\\python_intermedio_github')
Lista2=[]
for Cont in range(len(Lista1)):
    if str(Lista1[Cont]).find(nueva_carpeta)==0:
       Lista2.append(int(str(Lista1[Cont])[len(nueva_carpeta):len(str(Lista1[Cont]))])) # Determina el ultimo
if Lista2==[]:
   os.makedirs('C:\\Users\\subex\\Desktop\\python_intermedio_github\\'+nueva_carpeta+"1") # Crea el primero si no existe
else:
   os.makedirs('C:\\Users\\subex\\Desktop\\python_intermedio_github\\'+nueva_carpeta+str(int(max(Lista2))+1)) # Crea el siguiente

