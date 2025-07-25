import funciones
import conexionBD
from notas import nota
from usuarios import usuario
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usuario()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado :
                print(f"Se registro el usuario {nombre} {apellidos} correctamente")
            else:
                print("No fue posible registrar el usuario en este momento, intentalo mas tarde")
            funciones.esperarTecla()


        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            lista_usuarios=usuario.inicio_sesion(email,password)
            if len(lista_usuarios)>0:
                menu_notas()
            else:
                print(f"El email y/o contraseña incorrectas por favor verifique...")
            funciones.esperarTecla()

        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            respuesta = nota.crear(usuario_id, titulo, descripcion)
            if respuesta:
                print(f"\n \tSe creo la nota {titulo} con exito")
            else:
                print("\n \tNo fue posible crear la nota en este momento, intentalo mas tarde")
            funciones.esperarTecla()  

        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            lista_notas= nota.mostrar(usuario_id)
            if len(lista_notas) == 0:
                print(f"\n\t Mostrar las notas)
                for fila in lista_notas:
                    print(f"{fila[0]} {fila[1]} - {fila[2]} - {fila[3]} - {fila[4]}")
                    print(f"({fi"
            else:
                print("\n \t No hay notas para este usuario.")
            funciones.esperarTecla()

        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")
            #Agregar codigo
            resultado = nota.cambiar(id, titulo, descripcion)
            if resultado:
                print(f"\n \t Se actualizó la nota {titulo} con éxito")
            else:
                print("\n \t No fue posible actualizar la nota en este momento, intentalo mas tarde")
            funciones.esperarTecla()      

        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            id = input("\t \t ID de la nota a eliminar: ")
            #Agregar codigo
            respuesta = nota.borrar(id)
            if respuesta:
                print(f"\n \t Se eliminó la nota  {id} con éxito")
            else:
                print("\n \t No fue posible eliminar la nota en este momento, intentalo mas tarde")
            funciones.esperarTecla()
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
   main()