"""
crear un proyecto que permita gestionar (administrar) peliculas colocar un menu de opciones
para agregar, borrar, modificar, mostrar, buscar, limpiar una lista de peliculas

notas:
1-utilizar funciones y llamar desde otro archivo (modulo)
2.-utilizar diccionarios para almacenar los atributos (nombre,categoria,clasificación, genero,idioma) de peliculas
"""


import peliculas_1

opcion=True

while opcion:
 peliculas_1.borrarPantalla()
 print("📖 GESTION DE PELICULAS 📖")
 print(" 1️⃣. Agregar")
 print(" 2️⃣. Borrar")
 print(" 3️⃣. Modificar")
 print(" 4️⃣. Mostrar")
 print(" 5️⃣. Buscar")
 print(" 6️⃣. Limpiar")
 print(" 7️⃣. Salir")
 opcion = input( "👉 Seleccione una opcion: ")

 match opcion:
  case"1":
    peliculas_1.agregarPeliculas()
    peliculas_1.espereTecla()
  case"2":
    peliculas_1.borrarPeliculas()
    peliculas_1.espereTecla()
  case"3":
    peliculas_1.modificarPeliculas()
    peliculas_1.espereTecla()
  case"4":
    peliculas_1.mostrarPeliculas()
    peliculas_1.espereTecla()
  case"5":
    peliculas_1.buscarPeliculas()
    peliculas_1.espereTecla()
  case"6":
    peliculas_1.limpiarPeliculas()
    peliculas_1.espereTecla()
  case"7":
    opcion=False
    peliculas_1.borrarPantalla()
    print("✅ Terminaste la ejecucion del sistema.....Gracias ✅")
  case _:
    opcion=True
    peliculas_1.espereTecla()
    print(" ❌ Opcion no valida vuelve a intentarlo ❌")
