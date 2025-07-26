import mysql.connector
from mysql.connector import Error
import os

def borrarPantalla():    
    os.system("cls")

def esperarTecla():
    input("🔸 Presione una tecla para continuar...")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            database="bd_agenda"
        )
        return conexion
    except Error as e:
        print(f"❌ Error de conexión: {e}")
        return None

def agregar_contactos(agenda):
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("📥 Agregar Contacto")
        nombre = input("📝 Nombre: ").upper().strip()
        if nombre in agenda:
            print("⚠️ Este contacto ya existe")
        else:
            tel = input("📞 Teléfono: ").strip()
            email = input("📧 E-mail: ").strip().lower()
            agenda[nombre] = [tel, email]

            cursor = conexionBD.cursor()
            sql = "INSERT INTO contactos (nombre, telefono, email) VALUES (%s, %s, %s)"
            val = (nombre, tel, email)
            cursor.execute(sql, val)
            conexionBD.commit()
            print("✅ Contacto agregado")
    else:
        print("❌ No se pudo conectar a la base de datos.")

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
    print("🔍 Buscar Contacto")
    if not agenda:
        print("⚠️ No hay contactos registrados")
    else:
        nombre = input("📝 Ingrese el nombre que desea buscar: ").upper().strip()
        if nombre in agenda:
            print(f"👤 Nombre: {nombre}\n📞 Teléfono: {agenda[nombre][0]}\n📧 E-mail: {agenda[nombre][1]}")
            print("-" * 60)
            print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<10}")
            print("_" * 60)
        else:
            print("❌ El contacto no se encuentra en la agenda")

def modificar_contacto(agenda):
    borrarPantalla()
    print("✏️ Modificar Contacto")
    if not agenda:
        print("⚠️ No hay contactos en la agenda")
    else:
        nombre = input("📝 Ingrese el nombre del contacto a modificar: ").upper().strip()
        if nombre in agenda:
            print("📄 Valores actuales")
            print(f"👤 Nombre: {nombre}\n📞 Teléfono: {agenda[nombre][0]}\n📧 E-mail: {agenda[nombre][1]}")
            resp = input("❓ ¿Deseas cambiar los valores? (Si/No): ").upper().strip()
            if resp == "SI":
                tel = input("📞 Teléfono nuevo: ").strip()
                email = input("📧 Email nuevo: ").strip().lower()
                agenda[nombre] = [tel, email]

                conexionBD = conectar()
                if conexionBD is not None:
                    cursor = conexionBD.cursor()
                    sql = "UPDATE contactos SET telefono = %s, email = %s WHERE nombre = %s"
                    val = (tel, email, nombre)
                    cursor.execute(sql, val)
                    conexionBD.commit()
                    print("✅ Contacto modificado con éxito")
                else:
                    print("❌ No se pudo conectar a la base de datos.")
            else:
                print("🚫 Modificación cancelada")
        else:
            print("❌ Este contacto no existe")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("🗑️ Eliminar Contacto")
    if not agenda:
        print("⚠️ No hay contactos en la agenda")
    else:
        nombre = input("📝 Ingrese el nombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda:
            print("📄 Valores actuales")
            print(f"👤 Nombre: {nombre}\n📞 Teléfono: {agenda[nombre][0]} \n📧 E-mail: {agenda[nombre][1]}")
            resp = input("❓ ¿Deseas eliminar el contacto? (Si/No): ").upper().strip()
            if resp == "SI":
                agenda.pop(nombre)
                conexionBD = conectar()
                if conexionBD is not None:
                    cursor = conexionBD.cursor()
                    sql = "DELETE FROM contactos WHERE nombre = %s"
                    val = (nombre,)
                    cursor.execute(sql, val)
                    conexionBD.commit()
                    print("✅ Contacto eliminado con éxito")
                else:
                    print("❌ No se pudo conectar a la base de datos.")
            else:
                print("🚫 Eliminación cancelada")
        else:
            print("❌ Este contacto no existe")
