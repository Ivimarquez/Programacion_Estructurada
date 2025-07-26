def borrarPantalla():
    import os  
    os.system("cls") 

def esperarTecla():
    input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def menu_usuario():
    print("📚 .:: Sistema de Gestión de Notas ::. \n1️⃣  Registro  \n2️⃣  Login \n3️⃣  Salir ")
    opcion = input("🔘 Elige una opción: ").upper() 
    return opcion   

def menu_notas():
    print("\n \t📝 .:: Menú de Notas ::. \n\t1️⃣ Crear \n\t2️⃣ Mostrar \n\t3️⃣ Cambiar \n\t4️⃣ Eliminar \n\t5️⃣ Buscar Nota \n\t6️⃣ Salir")
    opcion = input("\t\t🔘 Elige una opción: ").upper().strip()
    return opcion

