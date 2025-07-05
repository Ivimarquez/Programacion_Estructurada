import agenda

def main():
    agenda_contactos = {}
    
    while True:
        opcion = agenda.menu_principal()

        if opcion == "1":
            agenda.agregar_contacto(agenda_contactos)
        elif opcion == "2":
            agenda.mostrar_contacto(agenda_contactos)
        elif opcion == "3":
            agenda.buscar_contacto(agenda_contactos)
        elif opcion == "4":
            agenda.modificar_contacto(agenda_contactos)
        elif opcion == "5":
            agenda.eliminar_contacto(agenda_contactos)
        elif opcion == "6":
            agenda.borrarPantalla()
            print("👋 Programa Finalizado")
            break
        else:
            print("❌ Opción no válida, intente de nuevo")

        agenda.esperarTecla()

if __name__ == "__main__":
    main()
