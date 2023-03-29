from Datos.BaseDeDatos import BaseDeDatos

def crear_juego(url, nombre, tematica, descripcion, rangoDeEdad):
    crear_juego_sql = f"""
        INSERT INTO juegos (URL, NOMBRE, TEMATICA, DESCRIPCION, RANGODEEDAD)
        VALUES('{url}', '{nombre}','{tematica}','{descripcion}','{rangoDeEdad}')"""
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_juego_sql)
    
def borrar_juego(id):
    borrar_juego_sql = f"""
        DELETE FROM juegos WHERE ID='{id}'"""

    bd = BaseDeDatos()
    bd.ejecutar_sql(borrar_juego_sql)

def listar_juegos(tematica):
    listar_juegos_sql = f"""
        SELECT ID,URL, DESCRIPCION, RANGODEEDAD, NOMBRE, TEMATICA FROM juegos WHERE TEMATICA='{tematica}'"""

    bd = BaseDeDatos()
    return [{"id": registro[0],
             "URL": registro[1],
             "DESCRIPCION": registro[2],
             "RANGO DE EDAD": registro[3],
             "NOMBRE": registro[4],
             "TEMATICA": registro[5]}
            for registro in bd.ejecutar_sql(listar_juegos_sql)]


def modificar_juego(id, url, descripcion):
    modificar_juego_sql = f"""
        UPDATE juegos SET URL='{url}', DESCRIPCION='{descripcion}' WHERE ID='{id}'"""

    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_juego_sql)


def obtener_juego(id):
    listar_juegos_sql = f"""
        SELECT ID,URL, DESCRIPCION, RANGODEEDAD, NOMBRE, TEMATICA FROM juegos WHERE id='{id}'"""

    bd = BaseDeDatos()
    return [{"id": registro[0],
             "URL": registro[1],
             "DESCRIPCION": registro[2],
             "RANGO DE EDAD": registro[3],
             "NOMBRE": registro[4],
             "TEMATICA": registro[5]}
            for registro in bd.ejecutar_sql(listar_juegos_sql)]