'''
Crear un proyecto que permita gestionar (administrar) peliculas. Colocar un menu de opciones: Agregar, Borrar, Modificar, Mostrar, Buscar peliculas.

Notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar dict para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma) de peliculas
3.- Implementar y utlizar una BD Relacional en MySQL

'''

import peliculas

opcion = True

while opcion:
    peliculas.borrarPantalla()
    print("🎬 GESTIÓN DE PELÍCULAS 🎬")
    print("1️⃣  Crear")
    print("2️⃣  Borrar")
    print("3️⃣  Mostrar")
    print("4️⃣  Buscar")
    print("5️⃣  Modificar")
    print("6️⃣  Salir")
    opcion = input("\n🟢 Elige una opción: ").upper()

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
            opcion = False
            peliculas.borrarPantalla()
            print("\n👋 Terminaste la ejecución del sistema... ¡Gracias por usarlo!")
        case _:
            print("\n❌ Opción inválida. Vuelve a intentarlo.")
            peliculas.esperarTecla()



