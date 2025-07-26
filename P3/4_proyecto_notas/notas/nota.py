from conexionBD import * 
import conexionBD

def crear(usuario_id, titulo, descripcion):
    try:
        conexion = conexionBD.obtener_conexion()
        if conexion is None:
            return False
        cursor = conexion.cursor()
        sql = "INSERT INTO notas (usuario_id, titulo, descripcion, fecha) VALUES (%s, %s, %s, NOW())"
        datos = (usuario_id, titulo, descripcion)
        cursor.execute(sql, datos)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print("❌ Error al crear nota:", e)
        return False

def mostrar(usuario_id):
    try:
        conexion = conexionBD.obtener_conexion()
        if conexion is None:
            return []
        cursor = conexion.cursor()
        sql = "SELECT * FROM notas WHERE usuario_id = %s"
        cursor.execute(sql, (usuario_id,))
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados
    except Exception as e:
        print("❌ Error al mostrar notas:", e)
        return []

def actualizar(id_nota, titulo, descripcion):
    try:
        conexion = conexionBD.obtener_conexion()
        if conexion is None:
            return False
        cursor = conexion.cursor()
        sql = "UPDATE notas SET titulo = %s, descripcion = %s WHERE id = %s"
        datos = (titulo, descripcion, id_nota)
        cursor.execute(sql, datos)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print("❌ Error al actualizar nota:", e)
        return False

def eliminar(id_nota):
    try:
        conexion = conexionBD.obtener_conexion()
        if conexion is None:
            return False
        cursor = conexion.cursor()
        sql = "DELETE FROM notas WHERE id = %s"
        cursor.execute(sql, (id_nota,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print("❌ Error al eliminar nota:", e)
        return False

def buscar_nota(usuario_id, id_nota):
    try:
        conexion = conexionBD.obtener_conexion()
        if conexion is None:
            return None
        cursor = conexion.cursor()
        sql = "SELECT * FROM notas WHERE usuario_id = %s AND id = %s"
        cursor.execute(sql, (usuario_id, id_nota))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado
    except Exception as e:
        print("❌ Error al buscar nota:", e)
        return None