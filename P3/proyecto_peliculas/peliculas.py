import mysql.connector
from mysql.connector import Error


#Dict u objeto que permita almacenar los sig atributos:(nombre,categoria,clasificación, genero,idioma) de peliculas
peliculas={
   "nombre":"",
   "categoria":"",
   "clasificacion":"",
   "genero":"",
   "idioma":"",
}

peliculas = [] 
pelicula={}

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("Presione una tecla para continuar...")

def conectar():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user="root",
            password="",
            database='bd_peliculas'
        )
        return conexion
    except Error as e:
        print(f"Error que se presenta es: {e}")
        return None

def crearPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print( "agregar peliculas")
        pelicula.update({"nombre ": input ("ingresa el nombre "). upper().strip()})
        #pelicula["nombre"]=input("ingresa el nombre:") .upper().strip()
        pelicula.update({"categoria ": input ("ingresa la categoria "). upper().strip()})
        pelicula.update({"clasificacion ": input ("ingresa la clasificacion "). upper().strip()})
        pelicula.update({"genero ": input ("ingresa el genero  "). upper().strip()})
        pelicula.update({"idioma ": input ("ingresa el idioma "). upper().strip()})
        #### SQL a BD
        cursor=conexionBD.cursor() 
        sql="insert into peliculas (nombre, categoria, clasificacion, genero, idioma) values ( %s, %s, %s, %s, %s)"
        val=(pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"])
        cursor.execute(sql, val)
        conexionBD.commit()

def mostrarPeliculas():
    borrarPantalla()
    print("MOSTRAR PELICULAS")
    if len(peliculas) > 0:
        for i in range(len(peliculas)):
            print(f"{i + 1}: {peliculas[i]}")
    else:
        print("NO HAY PELICULAS EN ESTE MOMENTO EN EL SISTEMA")

def borrarPeliculas():
  borrarPantalla()
  print("Borrar o Quitar TODAS laS Películas")
  resp=input("¿Deseas quitar o borrar todas las películas del sistema? (Si/No) ")
  if resp=="si":
    pelicula.clear()
    print("LA OPERACION SE REALIZO CON EXÍTO")

def modificarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM peliculas"
        cursor.execute(sql)
        registros = cursor.fetchall()
        print("\n\t .:: Modificar Películas ::.\n")        
        if registros:
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
            print("-" * 80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print("-" * 80)
            try:
                id_modificar = int(input("\nIngrese el ID de la película que desea modificar: "))
                cursor.execute("SELECT * FROM peliculas WHERE id = %s", (id_modificar,))
                pelicula = cursor.fetchone()

                if pelicula:
                    print("\nDeje vacío el campo que no desee modificar.\n")
                    nuevo_nombre = input(f"Nombre ({pelicula[1]}): ") or pelicula[1]
                    nueva_categoria = input(f"Categoría ({pelicula[2]}): ") or pelicula[2]
                    nueva_clasificacion = input(f"Clasificación ({pelicula[3]}): ") or pelicula[3]
                    nuevo_genero = input(f"Género ({pelicula[4]}): ") or pelicula[4]
                    nuevo_idioma = input(f"Idioma ({pelicula[5]}): ") or pelicula[5]

                    sql_update = """
                        UPDATE peliculas 
                        SET nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s 
                        WHERE id=%s
                    """
                    datos = (nuevo_nombre, nueva_categoria, nueva_clasificacion, nuevo_genero, nuevo_idioma, id_modificar)
                    cursor.execute(sql_update, datos)
                    conexionBD.commit()
                    print("\n\tPelícula modificada correctamente.\n")
                else:
                    print("\n\tNo se encontró una película con ese ID.\n")
            except Exception as e:
                print(f"\n\tOcurrió un error: {e}\n")
            finally:
                cursor.close()
                conexionBD.close()
        else:
            print("No hay películas en el Sistema")
