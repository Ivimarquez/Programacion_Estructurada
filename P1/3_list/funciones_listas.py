"""
list (array) son collectiones o conjunto de datos/valores 
bajo un mismo nombre, para acceder a los valores se hace un 
indice numerico

nota: sus valores si son modificables

la lista es una coleccion de datos ordenados y modificable. 
Permite mimbros modificados 
"""

#import os
#os.system (cls)

#funciones mas comunes en las listas
paises=("Mexico", "España", "Brasil","Canada")

numeros=(23,45,8,24)
varios=("hola", 3.1416,33,True)

#imprimir 
print(paises)
print(numeros)
print(varios)

#recorrer la lista
#1er forma

for i in paises:
    print(i)

#2do forma
for i in range(0,len(paises)):
    print(paises[i])

#ordenar elementos de una lista
paises.sort()
print(paises)
paises.sort()
print(numeros)

#dar la vuelta auna lista
paises.reverse()
print(varios )

#agregar, insertar,añadir un elemento a una lista
#1er forma
paises.apped("Honduras")
print(paises)

#2da forma
paises.insert(1,"Honduras")
print(paises)

paises.sort()
print(paises)

#eliminar, borrar, suprimir un elemento de una lista
#1er forma
paises.pop(4)
print(paises)

#2da forma
paises.remove("Honduras")
print(paises)

#bucar un elemento dentro de la lista 
print(paises)

print("Brasil" in paises)

#contar el numero de veces que aparece un elemento dentro de una lista

print(numeros)
cuantos=numeros.cout(23)
print(cuantos)

#conocer la posicion o indice en el que se encuentra un elemento de la lista
print(paises)
posicion=paises.index("Canada")
print(f"El vaor de Canada lo encontro en la posicion: {posicion}")

#unir el contenido de una lista dentro de otra lista
print(numeros)
numeros2=[100,200]
print(numeros2)

#crear a partir de las listas de numeros 1 y 2 un resultante y mostrar el contenido ordenado decendentemente

numeros.extend(numeros2)

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

#ejemmplo1: crear una lista de numeros e imprimir el contenido
#ejemplo2: crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
#ejemplo3: añadir elementos a una lista
#ejemplo 4: crear una lista multidimensional wue permita almacenar el nombre
