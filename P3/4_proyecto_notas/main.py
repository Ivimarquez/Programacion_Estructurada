import conexionBD
import funciones
from notas import notas
from usuarios import usuario
import getpass

def main():
    opcion = True
    while opcion:
        funciones.borrarPantalla()
        opcion = funciones.menu_usuario()

        if opcion == "1" or opcion == "REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: 📝 Registro en el Sistema ::..")
            nombre = input("\t 🙋 ¿Cuál es tu nombre?: ").upper().strip()
            apellidos = input("\t 🧑‍🤝‍🧑 ¿Cuáles son tus apellidos?: ").upper().strip()
            email = input("\t 📧 Ingresa tu email: ").lower().strip()
            password = getpass.getpass("\t 🔒 Ingresa tu contraseña: ").strip()
            resultado = usuario.registrar(nombre, apellidos, email, password)
            if resultado:
                print(f"\n\t✅ Se registró el usuario {nombre} {apellidos} correctamente")
            else:
                print(f"\n\t❌ No fue posible registrar el usuario en este momento, inténtalo más tarde ...")    
            funciones.esperarTecla()

        elif opcion == "2" or opcion == "LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: 🔐 Inicio de Sesión ::.. ")     
            email = input("\t 📧 Ingresa tu E-mail: ").lower().strip()
            password = getpass.getpass("\t 🔑 Ingresa tu contraseña: ").strip()
            lista_usuarios = usuario.inicio_sesion(email, password)
            if not lista_usuarios:
                print(f"\n\t⚠️ E-mail y/o contraseña incorrectas, por favor verifique ....")
                funciones.esperarTecla()
                continue
            print(f"\n\t👋 Bienvenido {lista_usuarios[1]} {lista_usuarios[2]}, has iniciado sesión ...")
            if len(lista_usuarios) > 0:
                menu_notas(lista_usuarios[0], lista_usuarios[1], lista_usuarios[2])
            else:
                print(f"\n\t⚠️ E-mail y/o contraseña incorrectas, por favor verifique ....")
            funciones.esperarTecla()

        elif opcion == "3" or opcion == "SALIR": 
            print("👋 Terminó la ejecución del sistema.")
            opcion = False
            funciones.esperarTecla()  

        else:
            print("❌ Opción no válida")
            opcion = True
            funciones.esperarTecla() 


def menu_notas(usuario_id, nombre, apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t 👋 Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion = funciones.menu_notas()

        if opcion == '1' or opcion == "CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: 🆕 Crear Nota ::. ")
            titulo = input("\t📝 Título: ")
            descripcion = input("\t🗒️ Descripción: ")
            respuesta = notas.crear(usuario_id, titulo, descripcion)
            if respuesta:
                print("\n\t✅ Nota creada correctamente.")
            else:
                print("\n\t❌ Error al crear la nota, por favor intente de nuevo.")
            funciones.esperarTecla()

        elif opcion == '2' or opcion == "MOSTRAR":
            funciones.borrarPantalla()
            lista_notas = notas.mostrar(usuario_id)
            if not lista_notas:
                print("\n\t📭 No hay notas para mostrar.")
            else:
                print(f"\n\t📋 {'ID':<10} {'Título':<15} {'Descripción':<15} {'Fecha':<15}")
                print("-" * 60)
                for n in lista_notas:
                    print(f"\n\t{n[0]:<10} {n[2]:<15} {n[3]:<15} {n[4]}")
                    print("-" * 60)
            funciones.esperarTecla()

        elif opcion == '3' or opcion == "CAMBIAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: ✏️ {nombre} {apellidos}, vamos a modificar una Nota ::. \n")
            id_nota = input("\t \t 🆔 ID de la nota a actualizar: ").strip()
            nota = notas.buscar_nota(usuario_id, id_nota)
            if not nota:
                print("\n\t❌ No existe ninguna nota con ese ID.")
                funciones.esperarTecla()
                continue
            titulo = input("\t📝 Nuevo título: ")
            descripcion = input("\t🗒️ Nueva descripción: ")
            respuesta = notas.actualizar(id_nota, titulo, descripcion)
            if respuesta:
                print("\n\t✅ Nota actualizada correctamente.")
            else:
                print("\n\t❌ Error al actualizar la nota, por favor intente de nuevo.")
            funciones.esperarTecla()

        elif opcion == '4' or opcion == "ELIMINAR":
            funciones.borrarPantalla()
            print(f"\n\t ..:: 🗑️ Borrar Nota ::..\n")
            lista_notas = notas.mostrar(usuario_id)
            if not lista_notas:
                print("\n\t📭 No hay notas para mostrar.")
                funciones.esperarTecla()
                continue
            else:
                print(f"\n\t📋 {'ID':<10} {'Título':<15} {'Descripción':<15} {'Fecha':<15}")
                print("-" * 60)
                for n in lista_notas:
                    print(f"\n\t{n[0]:<10} {n[2]:<15} {n[3]:<15} {n[4]}")
                    print("-" * 60)
            id_nota = input("\t \t 🆔 ID de la nota a eliminar: ").strip()
            nota = notas.buscar_nota(usuario_id, id_nota)
            if not nota:
                print("\n\t❌ No existe ninguna nota con ese ID.")
                funciones.esperarTecla()
                continue
            respuesta = notas.eliminar(id_nota)
            if respuesta:
                print("\n\t✅ Nota eliminada correctamente.")
            else:
                print("\n\t❌ Error al eliminar la nota, por favor intente de nuevo.")
            funciones.esperarTecla()

        elif opcion == '5' or opcion == "BUSCAR":
            funciones.borrarPantalla()
            id_nota = input("\t \t 🕵️ ID de la nota a buscar: ").strip()
            nota = notas.buscar_nota(usuario_id, id_nota)
            if nota:
                print("\n\t🔍 Nota encontrada:")
                print(f"\t🆔 ID: {nota[0]}")
                print(f"\t👤 Usuario ID: {nota[1]}")
                print(f"\t📝 Título: {nota[2]}")
                print(f"\t🗒️ Descripción: {nota[3]}")
                print(f"\t📅 Fecha: {nota[4]}")
            else:
                print("\n\t❌ No se encontró ninguna nota con ese ID.")
            funciones.esperarTecla()

        elif opcion == '6' or opcion == "SALIR":
            break

        else:
            print("\n \t \t ❌ Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()


if __name__ == "__main__":
    main()
