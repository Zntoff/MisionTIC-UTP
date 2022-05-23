"""
Crear un programa que crea una agenda de contactos
y que permite al usuario: 
- Agregar un contacto 
- Buscar un contacto
- Eliminar un contacto
- Listar todos los contactos
"""

# Posible primera solución 
# Crear el diccionario base 
# {"Juan" : 123, "Pedro" : 345, "Diana": 678}

# Posible segunda solución
# Crear doble diccionario 
# 1: {"Nombre" : Juan, "Telefono": 123}, 2: {"Nombre" : Pedro, "Telefono": 345}, 3: {"Nombre" : Diana, "Telefono": 678}

# 0. Crear la agenda

agenda = {}

# 1. Crear listado de opciones

opcion = 1

while opcion != 5:
    opcion = int(input("""Elija una opción
                    1. Agregar un contacto
                    2. Buscar un contacto
                    3. Eliminar un contactos
                    4. Ver todos los contactos guardados
                    5. Salir
                    
                    """))

    if opcion == 1: #EL usuario quiere agregar un contacto
        nombre= input("Ingrese el nombre del contacto: ")
        agenda[nombre] = input("Ingrese el telefono del contacto: ")
        print("---------------------------")
        print("Su contacto fue creado con exito")
    elif opcion == 2: # El usuario quiere buscar un contacto
        nombre= input("Ingrese el usuario a buscar: ")
        print("---------------------------")
        if agenda[nombre] != None:
            print(f"{nombre} : {agenda[nombre]}")
        else:
            print("El contacto no existe")
    elif opcion == 3: # El usuario quiere eliminar un contacto
        nombre= input("Ingrese el usuario a eliminar: ")
        print("---------------------------")
        if agenda[nombre] != None:
            del agenda[nombre]
            print("---------------------------")
            print("El usuario fue eliminado con exito")
        else:
            print("El contacto no existe")
    elif opcion == 4: #El usuario quiere ver todos sus contactos
        for key in agenda:
            print(f"{key} : {agenda[key]}")
            
    elif opcion == 5: 
        print("Gracias por usar este servicio, tenga buen día")
