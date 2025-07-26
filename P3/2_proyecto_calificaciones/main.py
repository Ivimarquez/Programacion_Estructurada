import calificaciones

def main():
    datos = []
    opcion = ""

    while True:
        calificaciones.borrarPantalla()
        print("\n\t\t\t .::: 📚 GESTIÓN DE CALIFICACIONES :::. \n")
        print("\t 1️⃣  Ingresar calificación")
        print("\t 2️⃣  Mostrar calificaciones")
        print("\t 3️⃣  Calcular calificaciones")
        print("\t 4️⃣  Salir")
        
        opcion = input("\n\t✏️  Elige una opción: ").upper()

        match opcion:
            case "1":
                calificaciones.agregarCalificaciones()
                calificaciones.espereTecla()
            case "2":
                calificaciones.mostrarCalificaciones()
                calificaciones.espereTecla()
            case "3":
                calificaciones.calcularCalificaciones()
                calificaciones.espereTecla()
            case "4":
                calificaciones.borrarPantalla()
                print("✅  Terminaste la ejecución del sistema. ¡Hasta luego!")
                break
            case _:
                print("❌  Opción inválida, vuelve a intentarlo")
                calificaciones.espereTecla()

if __name__ == "__main__":
    main()

