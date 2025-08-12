import mysql.connector

try:
    conexion=mysql.connector.connect(
        user="root",
        host="localhost",
        password="",
        database="bd_dulceria"
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("⚠️ No es posible conectarse al sistema por ahora.Por favor intente mas tarde.")