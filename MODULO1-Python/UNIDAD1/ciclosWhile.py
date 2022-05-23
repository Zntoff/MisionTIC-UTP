# Cuando queremos generar un ciclo tenemos que tener claro dos factores importantes
# 1. Se tiene que definir un final para el ciclo, sino este podra ejecutarse hasta
# que colapse la maquina que lo ejecute
#2. Los datos de inicio y lo que se quiere lograr

# Realice la tabla del 2 que tenga como limite el número 20

x = 0 #Definimos el inicio del ciclos 

while x <= 20:  # Mientras que el valor de x sea menor o igual que 20
    print(x)    # Muestra en consola el valor actual de X
    x = x + 2   # Toma el valor actual de x y sumale 2
    
"""
0
2
4
6
8
10
12
14
16
18
20

Este sera el resultado por consola del codigo descrito
"""
