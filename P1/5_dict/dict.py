"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener 
  como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 
  Tambien se conoce como un arreglo asosiativo u Objeto JSON
  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("cls")

paises=["México", "Brasil", "Canada", "España"]

pais1={"nombre": "México", "Capital": "CDMX", "Poblacion": 126000000, "Idioma": "Español", "Status": True }
pais2={"nombre": "Brasil", "Capital": "Brasilia", "Poblacion": 213000000, "Idioma": "Portugues", "Status": True }
pais3={"nombre": "Canada", "Capital": "Ottawa", "Poblacion": 38000000, "Idioma": ["Ingles" , "Frances"], "Status": True }

print(pais1)
for i in pais1:
    print(f"{i}={pais1[i]}")

#agregar un atributo mas
pais1["altitud"]=3000
for i in pais1:
    print(f"{i}={pais1[i]}")

#modificarun valor de un item
pais1.update({"altitud":2500})
for i in pais1:
 print(f"{i}={pais1[i]} ")