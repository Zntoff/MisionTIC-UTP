# 1. Escribir un algoritmo que lea cuatro números e indique cual es el mayor

# Primero se introducen los valores a comparar
num_1 = int(input("Inserte el primer número: "))
num_2 = int(input("Inserte el segundo número: "))
num_3 = int(input("Inserte el tercer número: "))
num_4 = int(input("Inserte el cuarto número: "))

#Luego pasamos a realizar las comparaciones
if num_1 == num_2 == num_3 == num_4:                        # Primero comprobamos si son iguales
    print("Los numeros son iguales")
elif num_1 > num_2 and num_1 > num_3 and num_1 > num_4:     # Comprobamos si el primer número es el mayor
    print(f"El numero mayor es {num_1}")
elif num_2 > num_1 and num_2 > num_3 and num_2 > num_4:     # Comprobamos si el segundo número es el mayor
    print(f"El numero mayor es {num_2}")
elif num_3 > num_1 and num_3 > num_2 and num_3 > num_4:     # Comprobamos si el tercer número es el mayor
    print(f"El numero mayor es {num_3}")
elif num_4 > num_1 and num_4 > num_2 and num_4 > num_3:     # Comprobamos si el cuarto número es el mayor
    print(f"El numero mayor es {num_4}")