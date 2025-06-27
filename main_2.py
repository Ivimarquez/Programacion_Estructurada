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
 print("1. Crear")
 print("2. Borrar")
 print("3. Mostrar")
 print("4. Agregar caracteristica")
 print("5. Modificar Caracteristica")
 print("6. Borrar caracteristica")
 print("7. Salir")
 opcion = input("Seleccione una opcion: ")

 match opcion:
  case"1":
    peliculas.crearPeliculas()
    peliculas.espereTecla()
  case"2":
    peliculas.borrarPeliculas()
    peliculas.espereTecla()
  case"3":
    peliculas.mostrarPeliculas()
    peliculas.espereTecla()
  case"4":
    peliculas.agregarCaracteristicaPeliculas()
    peliculas.espereTecla()
  case"5":
    peliculas.modificarCaracteristicaPeliculas()
    peliculas.espereTecla()
  case"6":
    peliculas.borrarCaracteristicaPeliculas()
    peliculas.espereTecla()
  case"7":
    opcion=False
    peliculas.borrarPantalla()
    print("Terminaste la ejecucion del sistema.....Gracias")
  case _:
    opcion=True
    peliculas.espereTecla()
    print("Opcion no valida vuelve a intentarlo")
