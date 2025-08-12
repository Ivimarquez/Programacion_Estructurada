from ConexionDB import *
from fpdf import FPDF



def AgregarProducto(codigo,Id_empleado,nombre,categoria,precio,unidades,cantidad,caducidad):
    try:
        cursor.execute("insert into inventario (Codigo,Id_empleado,Nombre,Categoria,Precio,Cantidad_unidades,Cantidad_producto,Caducidad) values (%s,%s,%s,%s,%s,%s,%s,%s) ",(codigo,Id_empleado,nombre,categoria,precio,unidades,cantidad,caducidad))
        conexion.commit()
        return True
    except:
        return False
    
def MostrarProductos():
    try:
        cursor.execute("select * from inventario")
        Lista=cursor.fetchall()
        return Lista
    except:
        return []
    
def BuscarProductos(codigo):
    try:
        cursor.execute("select * from inventario where Codigo=%s",(codigo,))
        Lista=cursor.fetchone()
        return Lista
    except:
        return []
    
def ModificarProducto(Id_empleado,nombre,categoria,precio,unidades,cantidad,caducidad,codigo):
    try:
        cursor.execute("update inventario set Id_empleado=%s,Nombre=%s,Categoria=%s,Precio=%s,Cantidad_unidades=%s,Cantidad_producto=%s,Caducidad=%s where Codigo=%s",(Id_empleado,nombre,categoria,precio,unidades,cantidad,caducidad,codigo))
        conexion.commit()
        return True
    except:
        return False

def ProductoInVentas(Codigo):
    try:
        cursor.execute("select productos.Codigo, productos.Nombre,productos.Categoria from productos join inventario on productos.Codigo = inventario.codigo where productos.Codigo=%s ",(Codigo,))
        Lista=cursor.fetchall()
        return Lista
    except:
        return []
    
def VentaProducto(codigo,cantidad_productos):
    Lista=BuscarProductos(codigo)
    newcantidad=Lista[5]-cantidad_productos
    cursor.execute("update inventario set Cantidad_unidades=%s where Codigo=%s",(newcantidad,Lista[0]))
    return "Hecho"
    
def BorrarProducto(Codigo):
    try:
        cursor.execute("delete from inventario where Codigo=%s",(Codigo,))
        conexion.commit()
        return True
    except:
        return False
