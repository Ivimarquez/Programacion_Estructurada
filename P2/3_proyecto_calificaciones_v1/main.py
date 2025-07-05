
import calificaciones

def main():
 datos = []
 opcion=True
 while opcion:
     calificaciones.borrarPantalla()
     opcion=calificaciones.menu_principal()
     calificaciones.borrarPantalla()
     match opcion:
         case "1":
          calificaciones.agregar_calificaciones(datos)
          calificaciones.espereTecla()
         case "2":
          calificaciones.mostrar_calificaciones(datos)
          calificaciones.espereTecla()
         case "3":
          calificaciones.calcular_promedios(datos)
          calificaciones.espereTecla()
         case "4":
          opcion=False
          calificaciones.borrarPantalla()
          print("Terminaste la ejecucion del sistema")
         case _:
          opcion=True
          print("Opcion invalida, por favor intente de nuevo.")
          calificaciones.borrarPantalla()


if __name__ == "__main__":
 main()

