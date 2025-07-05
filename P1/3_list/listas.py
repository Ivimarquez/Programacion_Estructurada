#ejemmplo1: crear una lista de numeros e imprimir el contenido

import os
os.system("cls")

numeros=(23,24)
print(numeros)

lista=""
for i in numeros:
    lista+=f"(i),"
    print(f"{lista}")

lista="("
i=0
while i<len(numeros):
    lista+=f"{numeros[i]},"
    i+=1
print(f"{lista})")


#ejemplo2: crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
palabras=["Hola","2023","Lebroncito","UTD","True"]

palabra_buscar=input("dame la palabra a buscar: ")

#1er forma
if palabra_buscar in palabras:

    print("SI se encontro la palabra en la lista")
else:
    print("NO se encontro la palabra en la lista")

#2da forma
encontro=False
for i in palabras:
    if i==palabra_buscar:
        encontro=True
        #cuantas+=1
        #palabras.index(i)
        #posiciones=palabras.append(palabras.index(i))
if encontro:        
        print("SI se encontro la palabra en la lista")
else:
        print("NO se encontro la palabra en la lista")
    

#3ra forma
encontro=False
for i in range(0,len(palabras)):
    if palabras[i]==palabra_buscar:
        encontro=True
        #cuantas+=1
        #palabras.index(i)
        posiciones=palabras.append (i)
if encontro:        
        print("SI se encontro la palabra en la lista")
else:
        print("NO se encontro la palabra en la lista")


#ejemplo3: añadir elementos a una lista
numero=[]

opc="si"
while opc=="si":
    numero.append(float(int(input("Dame un numero entero o decimal: "))))
    opc=input("Desea agregar otro numero a la lista? (si/no): ").lower()
print(numeros)

#ejemplo 4: crear una lista multidimensional wue permita almacenar el nombre

agenda=[
        ["Carlos","6181234567"],
        ["Alberto","6671234567"],
        ["Martin","6785678923"]
       ]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])    

cadena=""
for r in range(0,3):
    for c in range(0,2):
      cadena+=f"{agenda[r][c]}, "
    cadena+="\n"     
print(cadena) 