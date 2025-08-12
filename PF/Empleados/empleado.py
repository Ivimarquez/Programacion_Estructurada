from ConexionDB import *
from mysql.connector import Error
import datetime
import hashlib

def hash_password(Password):
    return hashlib.sha256(Password.encode()).hexdigest()

def AgregarEmpleado(Nombre,Apellidos,Correo,Password):
    try:
        Fecha=datetime.datetime.now()
        Password=hash_password(Password)
        cursor.execute("insert into empleados (Nombre,Apellidos,Correo,Password,fecha) values (%s,%s,%s,%s,%s)",(Nombre,Apellidos,Correo,Password,Fecha))
        conexion.commit()
        respuesta="Correct"
        return respuesta
    except mysql.connector.errors.IntegrityError:
        respuesta="key duplicada"
        return respuesta
    except:
        respuesta=None
        return respuesta
    
def Inicio_sesion2(Correo,Password):
    try:
        contrasenia=hash_password(Password)
        cursor.execute("select * from empleados where Correo=%s and Password=%s",(Correo,contrasenia))
        Lista=cursor.fetchone()
        return Lista
    except:
        return []
    
def Inicio_sesion(Correo,Password):
    try:
        contrasenia=hash_password(Password)
        cursor.execute("select * from empleados where Correo=%s and Password=%s",(Correo,contrasenia))
        Lista=cursor.fetchone()
        return Lista
    except:
        return []
  




