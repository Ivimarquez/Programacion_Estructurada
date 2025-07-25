import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
   input("\n\t ... Oprima cualquier tecla para continuar ...")

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None
    
