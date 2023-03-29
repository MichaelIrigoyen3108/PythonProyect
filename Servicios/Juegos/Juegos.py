from Datos.Modelos import JuegoUsuario as modelos_Juego


def crear_juego(url, nombre, tematica, descripcion, rangoDeEdad):
    modelos_Juego.crear_juego(url, nombre, tematica, descripcion, rangoDeEdad)


def borrar_juego(id_juego):
    modelos_Juego.borrar_juego(id_juego)


def listar_juegos(tematica):
    return modelos_Juego.listar_juegos(tematica)


def modificar_juego(id, url, descripcion):
    modelos_Juego.modificar_juego(id, url, descripcion)


def obtener_juego(id):
    return modelos_Juego.obtener_juego(id)
