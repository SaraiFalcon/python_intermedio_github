"""Hacer un programa que te pida a cuantos grados centigrados estamos
Dependiendo el dato ingresado realizar las siguientes validaciones

si es mas de 35 grados mostrar: "ta juerte la calor"

si esta entre 25 a 30 grados mostrar: "se antoja un pozol"

si la temperatura es menor a 25 grados mostrar: "es hora de sacar el sueter cucarachiento"


utilizar el menor lineas de codigo posible

se evaluara:
legibilidad de codigo


"Simple es mejor que complejo"
"""
temperatura= float (input ('¿Cuál es la temperatura de hoy (en grados centigrados)? '))
if temperatura < 25:
    print ('es hora de sacar el sueter cucarachiento')
elif temperatura > 35:
    print ('ta juerte la calor')
elif temperatura >=25 and temperatura <=30:
    print ('se antoja un pozol')
else:
    print ('no te quejes')




