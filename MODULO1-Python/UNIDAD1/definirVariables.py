# Primer vistazo a las definiciones de los diferentes tipos de datos en variables

texto = "Hola a todos, soy un String y almaceno textos"
num = 12345
binario = True 

# Existen varios tipos de datos numericos, entre ellos encontramos:
# Enteros int(), decimales flat(), numeros grandes double() entre otros int

# int
num_int = 123

# float
num_float = 123.23

# Además encontraremos los primeros comparadores lógicos usados para dar un resultado 
# Estos son la base de la programación y la creación de algoritmos funcionales
# Para realizar una acción en base a los datos que ingresemos debemos compararlos y para ellos
# usaremos if, elif y else para decodor acciones a realizar 

# < o > 

num_1 = 234
num_2 = 345

if (num_1 < num_2):
    print("Num 1 es mayor a num 2")
else:
    print("Num 2 es mayor o igual a Num 1")
    
#Esto nos dará un resultado por consola pero solamente si ingresamos datos en el codigo
#Por ende siempre dara el mismo resultado, para solucionar esto debemos solicitar datos al
# usuario que utilizará el programa, esto lo haremos con la función input

#Input solo recogera datos en texto plano o strings, para usar datos numericos tenemos que 
# transcribir dicho texto a numeros, esto lo haremos con la funcion int() en caso de ser 
# numeros enteros o float() si son numeros decimales 

nombre = input("Ingrese su nombre: ") #Aqui recibiremos un texto plano 

numeroTelefonico = int(input("Ingrese su numero de telefono: ")) 
# Aqui estaremos recibiendo un texto que pasaremos a numero con la función int() 

numeroDecimal = float(input("Ingrese un numero decimal: "))
# No es oblogatorio el que sea un numero decimal pero podra recibirlo si se presenta la condicion

# Formatear una linea de texto 
# Cuando vamos a formar un texto al cual le daremos resultados de variables es importante formatear dicha
# linea de texto, para ello usaremos la letra f cuando estemos formando el texto a imprimir,
# seguido de ello ingresaremos los datos de variables llamandolas entre corchetes {}

print(f"Hola {nombre}, tu numero de contacto es {numeroTelefonico} y tu numero decimal es {numeroDecimal}")
# imprime(formateada"Hola {Nombre introducido}, tu numero de contacto es {Numero introducido}) y tu numero decimal es {Numero introducido})

"""
Num 1 es mayor a num 2
Ingrese su nombre: Manuelito Perez
Ingrese su numero de telefono: 32132132121
Ingrese un numero decimal: 123.45
Hola Manuelito Perez, tu numero de contacto es 32132132121 y tu numero decimal es 123.45

Este sera el resultado por consola del codigo descrito
"""
