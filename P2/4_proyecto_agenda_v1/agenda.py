def borrarPantalla():    
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("Presione una tecla para continuar...")

def menu_principal():
    borrarPantalla()
    print("📖 Sistema de gestión de Agenda de Contactos 📖")
    print(" 1. Agregar contacto")
    print(" 2. Mostrar todos los contactos")
    print(" 3. Buscar contacto por nombre")
    print(" 4. Modificar contacto")
    print(" 5. Eliminar contacto") 
    print(" 6. Salir")
    return input("👉 Seleccione una opción (1-6): ")

def agregar_contacto(agenda):
    borrarPantalla()
    print("📥 Agregar Contacto")
    nombre = input("Nombre: ").upper().strip()
    if nombre in agenda:
        print("⚠️ Este contacto ya existe")
    else:
        tel = input("Teléfono: ").strip()
        email = input("E-mail: ").strip().lower()
        agenda[nombre] = [tel, email]
        print("✅ Contacto agregado con éxito")

def mostrar_contacto(agenda):
    borrarPantalla()
    print("📋 Mostrar Contactos")
    if not agenda:
        print("⚠️ No hay contactos registrados")
    else:
        for nombre, datos in agenda.items():
            print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<25}")
        print("-" * 60)

def buscar_contacto(agenda):
    borrarPantalla()
    print("🔎 Buscar Contacto")
    nombre = input("Ingrese el nombre que desea buscar: ").upper().strip()
    if nombre in agenda:
        tel, email = agenda[nombre]
        print(f"Nombre: {nombre}, Teléfono: {tel}, E-mail: {email}")
        print("-" * 60)
    else:
        print("❌ El contacto no existe en la agenda")

def modificar_contacto(agenda):
    borrarPantalla()
    print("✏️ Modificar Contacto")
    if not agenda:
        print("⚠️ No hay contactos registrados")
    else:
        nombre=input("Ingrese el nombre del contacto a modificar: ").upper().strip()
        if nombre in agenda:
            print("Valores Actuales")
            print(f"Nombre: {nombre}, telefono: {agenda[nombre][0]}, E-mail: {agenda[nombre][1]}")
            resp=input("¿Desea modificar el contacto? (S/N): ").upper().strip()
            if resp == "S":
                tel = input("Nuevo Teléfono: ") .upper() .strip()
                email = input("Nuevo E-mail: ").strip().lower()
                agenda[nombre] = [tel, email]
                print("✅ Contacto modificado con éxito")
            else:
                print("❌ Modificación cancelada")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("🗑️ Eliminar Contacto")
    if not agenda:
        print("⚠️ No hay contactos registrados")
    else:
        nombre=input("Ingrese el nombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda:
            resp=input("¿Desea eliminar el contacto? (S/N): ").upper().strip()
            if resp == "S":
                agenda.pop(nombre)
                print("✅ Contacto eliminado con éxito")
            else:
                print("❌ Este contacto no existe")


#pop = eliminar_contacto

