"""
crear un proyecto que permita gestionar (administrar) peliculas colocar un menu de opciones
para agregar, borrar, modificar, mostrar, buscar, limpiar una lista de peliculas

notas:
1-utilizar funciones y llamar desde otro archivo (modulo)
2.-utilizar diccionarios para almacenar los atributos (nombre,categoria,clasificación, genero,idioma) de peliculas
"""


import peliculas_2

opcion=True

while opcion:
 peliculas_2.borrarPantalla()
 print("📖 GESTION DE PELICULAS 📖")
 print("1️⃣. Crear")
 print("2️⃣. Borrar")
 print("3️⃣. Mostrar")
 print("4️⃣. Agregar caracteristica")
 print("5️⃣. Modificar Caracteristica")
 print("6️⃣. Borrar caracteristica")
 print("7️⃣. Salir")
 opcion = input(" 👉 Seleccione una opcion: ")

 match opcion:
  case"1":
    peliculas_2.crearPeliculas()
    peliculas_2.espereTecla()
  case"2":
    peliculas_2.borrarPeliculas()
    peliculas_2.espereTecla()
  case"3":
    peliculas_2.mostrarPeliculas()
    peliculas_2.espereTecla()
  case"4":
    peliculas_2.agregarCaracteristicaPeliculas()
    peliculas_2.espereTecla()
  case"5":
    peliculas_2.modificarCaracteristicaPeliculas()
    peliculas_2.espereTecla()
  case"6":
    peliculas_2.borrarCaracteristicaPeliculas()
    peliculas_2.espereTecla()
  case"7":
    opcion=False
    peliculas_2.borrarPantalla()
    print("Terminaste la ejecucion del sistema.....Gracias")
  case _:
    opcion=True
    peliculas_2.espereTecla()
    print("Opcion no valida vuelve a intentarlo")
