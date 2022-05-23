# Tipos de declaraciones y metodos para cada una element
# Ambos tipos de datos se indexan a partir del 0

# Listas 
# Las listas se caracterizan por ser declaradas en corchetes []
# Cuenta con diversos metodos para modificar, añadir y eliminar datos

#---------------------------------------------------------
# 0. Creación de listas 
# Las listas pueden poseer todo tipo de datos como veremos a continuación:

# lista = [int, int, int, int, str, bool, float]
lista = [1, 2, 3, 4, 'Felipe', True, 1.23]

# Para llamar algún elemento de esta lista partimos del indice 0 
print(lista[4])
# Esto nos imprime por consola 'Felipe', ya que este se encuentra en dicha poscicion

#Otra forma de llamar por ejemplo al ultimo valor sin conocer el tamaño de la lista es usar lista[-1]
print(lista[-1])
#Esto nos imprime via consola 1.23, ya que este es el ultimo valor de la lista 

# Como ya se habia mencionado, estas listas pueden ser modificadas mediante ciertos parametros

#---------------------------------------------------
# 1. Crear una nueva lista desde una existente 

# a. Obtener un dato y guararlo en otra
# Tomaremos el dato Felipe, pero como ya conocemos su posicion en la lista crearemos una nueva con este dato asignandola directamente

casa = []
casa = [lista[5]]
print(casa)
# Resultado por consola: 

#Si imprimimos casa podremos notar que el unico elemento presente es Felipe 

# b. Si necesitamos obtener los ultimos datos de una lista podemos usar el parametro lista[-i:] Donde i representa el dato a partir el cual se va a obtener los valores y : representa que a partir de i se va a tomar hasta el ultimo dato o se puede añadir un valor para que este finalice 

# Ejemplo, casa = lista[-3:] Tomará el valor desde Felipe hasta el ultimo 
casa = lista[-3:]
print(casa)
#Resultado por consola: ['Felipe', True, 1.23]

# c. Tomar todos los datos de una lsita y llevarlos a otra
# El siguiente caso nos lleva a asignar todos los valores de una lista a otra mediante el llamado lista[:]
casa2 = lista[:]
print(casa2) 
# Resultado por consola: [1, 2, 3, 4, 'Felipe', True, 1.23]

#------------------------------------------------------
# 2. Modificar listas 
# La forma de modificar el valor de una lista es llamar a esa casilla y asignarle un nuevo valor.

# EJEMPLO, Te dan una lista de los cuadrados de cada número
cuadrados = [0, 1, 4, 9, 16, 26, 36, 48]
# Notas que el cuadrado del numero 5 esta mal, ya que el cuadrado deberia ser 25, entonces decides modificarlo
# Para modificar un dato se utiliza el siguiente codigo 
# cuadrados[i] = nuevo valor
cuadrados[5] = 25
print(cuadrados)
# Resultado por consola: [0, 1, 4, 9, 16, 25, 36, 48]

#-----------------------------------------------------
# 3. Concatenar listas


