
import mysql.connector
from mysql.connector import Error

pelicula = {}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t ... ⏳ Oprima cualquier tecla para continuar ...")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"❌ El error que se presenta es: {e}")
        return None

def crearPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\n\t 🎬 .:: Agregar Películas ::.\n")
        pelicula.update({"nombre": input("🎞️ Ingresa el nombre: ").upper().strip()})
        pelicula.update({"categoria": input("📂 Ingresa la categoría: ").upper().strip()})
        pelicula.update({"clasificacion": input("📋 Ingresa la clasificación: ").upper().strip()})
        pelicula.update({"genero": input("🎭 Ingresa el género: ").upper().strip()})
        pelicula.update({"idioma": input("🗣️ Ingresa el idioma: ").upper().strip()})

        cursor = conexionBD.cursor()
        sql = "INSERT INTO peliculas (nombre, categoria, clasificacion, genero, idioma) VALUES (%s, %s, %s, %s, %s)"
        val = (pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"])
        cursor.execute(sql, val)
        conexionBD.commit()
        print("\n\t\t ✅ :::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def mostrarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD != None:
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM peliculas"
        cursor.execute(sql)
        registros = cursor.fetchall()
        print("\n\t 🎬 .:: Mostrar Películas ::.\n")
        if registros:
            print(f"\n\t📋 Mostrar las Películas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-" * 80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-" * 80)
        else:
            print("\n\t ⚠️ .:: No hay películas en el Sistema ::.")

def buscarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD != None:
        nombre = input("🔍 Dame el nombre de la película a buscar: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM peliculas WHERE nombre=%s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        if registros:
            print(f"\n\t📋 Mostrar las Películas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-" * 80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-" * 80)
        else:
            print("\n\t ⚠️ .:: No hay películas en el sistema con ese nombre ::.")

def borrarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD != None:
        nombre = input("🗑️ Dame el nombre de la película a borrar: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM peliculas WHERE nombre=%s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        if registros:
            print(f"\n\t📋 Mostrar las Películas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-" * 80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-" * 80)
            resp = input(f"❓ ¿Deseas borrar la película '{nombre}'? (Si/No): ").lower().strip()
            if resp == "si":
                sql = "DELETE FROM peliculas WHERE nombre=%s"
                val = (nombre,)
                cursor.execute(sql, val)
                conexionBD.commit()
                print("\n\t\t ✅ :::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
        else:
            print("\n\t ⚠️ .:: No hay películas en el sistema con ese nombre ::.")

def modificarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        nombre = input("✏️ Dame el nombre de la película a modificar: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM peliculas WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()

        if registros:
            print(f"\n\t🎞️ Películas encontradas con el nombre '{nombre}':")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoría':<15}{'Clasificación':<15}{'Género':<15}{'Idioma':<15}")
            print(f"-" * 80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-" * 80)

            try:
                id_pelicula = int(input("\n🔢 Ingresa el ID de la película que deseas modificar: "))
                sql = "SELECT * FROM peliculas WHERE id = %s"
                cursor.execute(sql, (id_pelicula,))
                pelicula = cursor.fetchone()

                if pelicula:
                    print(f"\n🎬 Película seleccionada:")
                    print(f"{'ID':<10}{'Nombre':<15}{'Categoría':<15}{'Clasificación':<15}{'Género':<15}{'Idioma':<15}")
                    print(f"{pelicula[0]:<10}{pelicula[1]:<15}{pelicula[2]:<15}{pelicula[3]:<15}{pelicula[4]:<15}{pelicula[5]:<15}")

                    resp = input("\n❓ ¿Deseas modificar esta película? (Si/No): ").lower().strip()
                    if resp == "si":
                        nuevo_nombre = input("Nuevo nombre: ").upper().strip()
                        nueva_categoria = input("Nueva categoría: ").upper().strip()
                        nueva_clasificacion = input("Nueva clasificación: ").upper().strip()
                        nuevo_genero = input("Nuevo género: ").upper().strip()
                        nuevo_idioma = input("Nuevo idioma: ").upper().strip()

                        sql = """
                        UPDATE peliculas
                        SET nombre = %s, categoria = %s, clasificacion = %s, genero = %s, idioma = %s
                        WHERE id = %s
                        """
                        val = (nuevo_nombre, nueva_categoria, nueva_clasificacion, nuevo_genero, nuevo_idioma, id_pelicula)
                        cursor.execute(sql, val)
                        conexionBD.commit()
                        print("\n\t\t ✅ :::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
                    else:
                        print("\n\t 🔕 ::: Operación cancelada :::")
                else:
                    print("\n\t ⚠️ ::: No se encontró ninguna película con ese ID :::")
            except ValueError:
                print("\n\t ❌ ::: ID inválido :::")
        else:
            print("\n\t ⚠️ .:: No hay películas en el sistema con ese nombre ::.")
