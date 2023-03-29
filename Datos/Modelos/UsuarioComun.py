from Datos.BaseDeDatos import BaseDeDatos


def login_usuario(nombre, password):
    login_usuario_sql = f"""
        SELECT ID FROM usuario WHERE NOMBRE= '{nombre}' and PASSWORD='{password}'"""
    bd = BaseDeDatos()
    return bd.ejecutar_sql(login_usuario_sql)


def crear_usuario(nombre, apellido, fecha_de_nacimiento, password, email):
    crear_usuario_sql = f"""
        INSERT INTO usuario (NOMBRE, APELLIDO, FECHA_DE_NACIMIENTO, PASSWORD, EMAIL)
        VALUES ('{nombre}', '{apellido}', '{fecha_de_nacimiento}', '{password}',' {email}')  """

    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)
