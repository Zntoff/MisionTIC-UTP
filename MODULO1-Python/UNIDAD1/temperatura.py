# Realizar una calculadora de grados celsius a farenheit
# Y viceversa 

option = 1 
cel = 0 
far = 0 

while option != 3:
    option = int(input("""
                       Bienvenido a la calculadora de grados celsius a farenheit
                       --------------------------------------
                       Seleccione la opción: 
                       1. Pasar de Celcius a Farenheit
                       2. Pasar de Farenheit a Celsius
                       3. Salir
                       """))
    
    if option == 1:
        cel = input("Ingrese la temperatura en Celsius: ")
        
        try:
            far_float = float(cel)
            far = ((far_float ) * 9 / 5) + 32
            print(f"{far_float} grados Celsius equivalen a {far} grados Farenheit")
        
        except:
            print("Ingrese un número valido")
    elif option == 2:
        far = input("Ingrese la temperatura en Farenheit: ")
        
        try:
            cel_float = float(far)
            cel = ((cel_float - 32) * 5 /9)
            print(f"{cel_float} grados Farenheit equivalen a {cel} grados Celsius")
        
        except:
            print("Ingrese un número valido")
    elif option == 3:
        print("Gracias por usar este servicio, tenga buen día")