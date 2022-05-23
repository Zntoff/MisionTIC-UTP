'''
Programa que le pregunte al usuario (profesor) el nombre del alumno, el numero de notas que
desea ingresar y los porcentajes correspondientes a cada una de ellas
Posteriormente, de acuerdo con el numero de notas deseado, el pregroma debe preguntar al usuario
el valor de cada una de esas notas para finalmente desplegar en pantalla el informe completo
de notas del estudiante, así (teniendo en cuenta que aprueba el curso con una nota mayor o igual
a 3.0):
Nombre del estudiante
Nota No. n: X.X
#.
#.
#.
#Nota Final: X.X
#Aprueba: Sí/No
Ej. Si son 2 notas: {'nombre': 'Juanito', 0:3.5, 'porcentaje_0':50, 1:4.0, 'porcentaje_1':50}
'''


estudiante = {}

#Se pide el nombre del estudiante
estudiante["nombre"] = input("Ingrese el nombre del alumno: ")

#Se pide la cantidad de notas a ingresar
cantidad_notas = int(input("Ingrese la cantidad de notas: "))
contador_notas = 0
nota_final = 0

while contador_notas < cantidad_notas:
    
    #Se toma la nota
    estudiante[contador_notas] = float(input("Ingrese la nota: "))
    
    #Se toma el porcentaje
    etiqueta_porcentaje = "porcentaje_" + str(contador_notas)
    estudiante[etiqueta_porcentaje] = float(input("Ingrese el porcentaje de la nota: "))
    
    #Se calcula la nota actual
    nota_parcial = estudiante[contador_notas] * estudiante[etiqueta_porcentaje] / 100
    
    #Se añade al valor final
    nota_final = nota_final + nota_parcial
    estudiante["nota_final"] = nota_final
    contador_notas = contador_notas + 1
    
#Se comprueba si se aprueba   
if nota_final >= 3:
    estudiante["aprueba"] = "Si"
else:
    estudiante["aprueba"] = "No"
    
#Se imprime el nombre del estudiante
print(f'------------------------------------------------')
print(f'El estudiante {estudiante["nombre"]} con notas')

#Se imprimen las notas
for i in range(0, cantidad_notas):
    print(f"Nota número {i + 1 } : {estudiante[i]}")
    
#Se imprime la nota final y si se aprueba
print(f'Nota final: {estudiante["nota_final"]}, aprobado: {estudiante["aprueba"]}')