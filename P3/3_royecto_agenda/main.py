import agenda

def main():
    agenda_contacto = {}

    while True:
        agenda.borrarPantalla()
        print("\n\t\t\t .::: 📒 SISTEMA DE AGENDA :::. \n\n\t 1️⃣  Agregar contacto  \n\t 2️⃣  Mostrar contactos \n\t 3️⃣  Buscar contactos \n\t 4️⃣  Modificar contacto \n\t 5️⃣  Eliminar contacto \n\t 6️⃣  Salir")
        opcion = input("\n\t\t 🔸 Elige una opción: ").strip()

        if opcion == "1":
            agenda.agregar_contactos(agenda_contacto)
        elif opcion == "2":
            agenda.mostrar_contacto(agenda_contacto)
        elif opcion == "3":
            agenda.buscar_contacto(agenda_contacto)
        elif opcion == "4":
            agenda.modificar_contacto(agenda_contacto)
        elif opcion == "5":
            agenda.eliminar_contacto(agenda_contacto)
        elif opcion == "6":
            agenda.borrarPantalla()
            print("👋 Programa finalizado. ¡Hasta pronto!")
            break
        else:
            print("⚠️ Opción no válida")
        
        agenda.esperarTecla()

if __name__ == "__main__":
    main()
