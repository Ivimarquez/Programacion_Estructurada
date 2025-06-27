"""
crear un proyecto que permita gestionar (administrar) peliculas colocar un menu de opciones
para agregar, borrar, modificar, mostrar, buscar, limpiar una lista de peliculas

notas:
1-utilizar funciones y llamar desde otro archivo (modulo)
2.-utilizar diccionarios para almacenar los atributos (nombre,categoria,clasificación, genero,idioma) de peliculas
"""


import peliculas

opcion=True

while opcion:
 peliculas.borrarPantalla()
 print("GESTION DE PELICULAS")
 print("1. Agregar")
 print("2. Borrar")
 print("3. Modificar")
 print("4. Mostrar")
 print("5. Buscar")
 print("6. Limpiar")
 print("7. Salir")
 opcion = input("Seleccione una opcion: ")

 match opcion:
  case"1":
    peliculas.agregarPeliculas()
    peliculas.espereTecla()
  case"2":
    peliculas.borrarPeliculas()
    peliculas.espereTecla()
  case"3":
    peliculas.modificarPeliculas()
    peliculas.espereTecla()
  case"4":
    peliculas.mostrarPeliculas()
    peliculas.espereTecla()
  case"5":
    peliculas.buscarPeliculas()
    peliculas.espereTecla()
  case"6":
    peliculas.limpiarPeliculas()
    peliculas.espereTecla()
  case"7":
    opcion=False
    peliculas.borrarPantalla()
    print("Terminaste la ejecucion del sistema.....Gracias")
  case _:
    opcion=True
    peliculas.espereTecla()
    print("Opcion no valida vuelve a intentarlo")
