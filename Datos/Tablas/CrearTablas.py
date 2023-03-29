import sqlite3

sql_tabla_usuario = """
CREATE TABLE usuario(
ID INTEGER NOT NULL PRIMARY KEY,
EMAIL TEXT,
FECHA_DE_NACIMIENTO INTEGER NOT NULL,
APELLIDO TEXT NOT NULL,
NOMBRE TEXT NOT NULL,
PASSWORD INTEGER NOT NULL,
ROL TEXT)"""

sql_tabla_juegos = """
CREATE TABLE juegos(
ID INTEGER NOT NULL  PRIMARY KEY,
URL TEXT NOT NULL ,  
DESCRIPCION TEXT NOT NULL ,
RANGODEEDAD INTEGER NOT NULL , 
NOMBRE TEXT NOT NULL , 
TEMATICA TEXT NOT NULL )"""

sql_tabla_usuario_rol = """
CREATE TABLE usuario_rol(
ID_USUARIO INTEGER, 
ID_ROL INTEGER, 
FOREIGN KEY(ID_ROL) 
REFERENCES ROL(ID), 
FOREIGN KEY(ID_USUARIO)
REFERENCES ROL(ID))"""

sql_tabla_rol_juegos = """
CREATE TABLE rol_juego(
ID_JUEGO INTEGER,
ID_ROL INTEGER,
FOREIGN KEY(ID_JUEGO) 
REFERENCES ROL(ID),
FOREIGN KEY(ID_ROL) 
REFERENCES ID_JUEGOS(ID))"""

if __name__ == '__main__':
    try:
        print('Creando base de datos..')
        conexion = sqlite3.connect('../../unLugarParaAprender.db')

        print('creando tabla..')
        conexion.execute(sql_tabla_usuario)
        conexion.execute(sql_tabla_juegos)
        conexion.execute(sql_tabla_usuario_rol)
        conexion.execute(sql_tabla_rol_juegos)

        conexion.close()
        print('cracion finalizada')
    except Exception as e:
        print(f'Error creando base de datos: {e}', e)
