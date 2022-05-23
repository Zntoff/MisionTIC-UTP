# Diseñar un algoritmo que permita determinar si un número introducido es primo o
# no. Un número es primo cuando solamente es divisible entre el mismo y la unidad.
# Un número es primo cuando puede dividirse por uno o por su mismo número.
# Ejemplo: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29…

# Instrucciones:
# 1. Pedir un numero y si el valor es igual a 0 terminar el programa 
# 2. Determinar si el valor es primo o no primo 
# 3. Volver a pedir el numero 

numero = 1

def tabla(numero):
    for i in range(1, 11):
        print(i * numero)

while numero != 0:
    numero = int(input("ingrese el numero de la tabla"))
    tabla(numero)