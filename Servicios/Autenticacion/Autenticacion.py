from Datos.Modelos import UsuarioComun as modelos_usuario


def login_usuario(nombre, password):
    return len(modelos_usuario.login_usuario(nombre, password)) > 0


def crear_usuario(nombre, apellido, fecha_de_nacimiento, password, email):
    modelos_usuario.crear_usuario(nombre, apellido, fecha_de_nacimiento, password, email)
