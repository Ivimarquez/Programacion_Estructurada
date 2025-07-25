'''
Crear un proyecto que permita gestionar (administrar) peliculas. Colocar un menu de opciones: Agregar, Borrar, Modificar, Mostrar, Buscar peliculas.

Notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar dict para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma) de peliculas
3.- Implementar y utlizar una BD Relacional en MySQL

'''

import peliculas

opcion=True

while opcion:
   peliculas.borrarPantalla()
   print("GESTION DE PELICULAS")
   print("1. Crear")
   print("2. Borrar")
   print("3. Mostrar")
   print("4. Buscar")
   print("5. Modificar")
   print("6. Salir")
   opcion=input("Elige una opción: ").upper()

   match opcion:
      case "1":
         peliculas.crearPeliculas()
         peliculas.esperarTecla()
      case "2":
         peliculas.borrarPeliculas()
         peliculas.esperarTecla() 
      case "3":
         peliculas.mostrarPeliculas()
         peliculas.esperarTecla()  
      case "4":
         peliculas.buscarPeliculas()
         peliculas.esperarTecla()
      case "5":
         peliculas.modificarPeliculas()
         peliculas.esperarTecla()
      case "6":
         opcion=False
         peliculas.borrarPantalla()
         print("\n\tTerminaste la ejecución del Sistema ... Gracias ...")
      case _:
         opcion=True
         peliculas.esperarTecla()
         print("\n\tOpción Invalida vuelva a intentarlo")   

                        


