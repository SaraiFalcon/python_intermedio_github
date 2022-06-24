from auth.login import is_authenticated
import os
os.system('cls')

#user = shudleston5
#password = XeL8MY

#print(is_authenticated("usuari", "contrase"))
#print(is_authenticated("shudleston5", "XeL8MY"))

if is_authenticated("shudleston5", "XeL8MY"):
    print("Bienvenido usuario")
else:
    print("credenciales incorrectas")

if  not is_authenticated("shudleston5", "XeL8MYx"):
    print("credenciales invalidas")
    