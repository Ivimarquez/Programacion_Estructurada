from ConexionDB import *
import datetime
Fecha=datetime.datetime.now()

def AgregarVenta(Id_empleado,Id_producto,nombre,cantidad_productos,precio,subtotal,iva,total):
    try:
        Fecha=datetime.datetime.now()
        cursor.execute("insert into ventas (Id_empleado,Id_producto,Nombre,Cantidad,Fecha,Precio,Subtotal,Iva,Total) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Id_empleado,Id_producto,nombre,cantidad_productos,Fecha,precio,subtotal,iva,total))
        conexion.commit()
        return True
    except:
        return False
    
def MostrarVentas():
    try:
        cursor.execute("select * from ventas")
        Lista=cursor.fetchall()
        return Lista
    except:
        return []
    
def BuscarVenta(folio):
    try:
        cursor.execute("select * from ventas where Folio=%s",(folio,))
        Lista=cursor.fetchone()
        return Lista
    except:
        return []
    
def ProductoInVenta(codigo):
    try:
        cursor.execute("select * from ventas where Id_producto=%s",(codigo,))
        Lista=cursor.fetchall()
        if len(Lista)>0:
            return True
        else:
            return False
    except:
        return False

def ModificarVenta(cantidad,fecha,subtotal,iva,total,folio):
    try:
        cursor.execute("update ventas set Cantidad=%s,Fecha=%s,Subtotal=%s,Iva=%s,Total=%s where Folio=%s",(cantidad,fecha,subtotal,iva,total,folio))
        conexion.commit()
        return True
    except:
        return False
    
def BorrarVenta(folio):
    try:
        cursor.execute("delete from ventas where Folio=%s",(folio,))
        conexion.commit()
        return True
    except:
        return False