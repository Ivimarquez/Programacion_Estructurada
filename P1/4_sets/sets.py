"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("cls")

"""
paises={"México", "Brasil", "España", "Canada", "Canada"}
print(paises)

varios={True, "UTD", 33,3,14}
print(varios)

#funciones u operaciones 
paises.add("Mexico") #Agrega un elemento seleccionado 
print(paises)

paises.pop() #Elimina un elemento que sea seleccionado/ si no hay nada puede borrar cualquiera 
print(paises)


paises.remove("México") #Elimina un elemento seleccionado
print(paises)


#ejemplo crear un programa que solicite el email de los alumnos de la UTD almacenar una lista y posteriormente mostrar
#  en pantalla los correos ingresados sin duplicados.


#solucion 1

resp="si"
emails={""}
while resp=="si":
 email = input("Ingrese su correo electrónico: ")
 emails.add(email)
 resp = input("¿Desea ingresar otro correo? (si/no): ")
print("Correos ingresados:", emails)
"""

#"solucion 2"
resp = "si"
emails=[]
while resp == "si":
    emails.append(input("Ingrese su correo electrónico: "))
    resp = input("¿Desea ingresar otro correo?")
print(emails)
emails_set=set(emails)
print(emails_set)
emails=list(emails_set)