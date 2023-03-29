from flask import Flask, request, jsonify
from Servicios.Autenticacion import Autenticacion
from Servicios.Juegos import Juegos
from flask import render_template

app = Flask(__name__, template_folder="web/templates")


@app.route("/usuario", methods=['POST'])
def crear_usuario():
    datos_usuario = request.get_json()
    if 'nombre' not in datos_usuario:
        return 'El nombre es requerido'
    if 'apellido' not in datos_usuario:
        return 'El apellido es requerido'
    if 'fecha_de_nacimiento' not in datos_usuario:
        return 'La fecha de nacimiento es requerida'
    if 'password' not in datos_usuario:
        return 'La password es requerida'
    if 'email' not in datos_usuario:
        return 'El mail es requerido'
    Autenticacion.crear_usuario(datos_usuario['nombre'],
                                datos_usuario['apellido'],
                                datos_usuario['fecha_de_nacimiento'],
                                datos_usuario['password'],
                                datos_usuario['email'])
    return 'ok', 200


@app.route("/login", methods=['POST'])
def login_usuario():
    datos_usuario = request.get_json()
    if 'nombre' not in datos_usuario:
        return 'El nombre es requerido'
    if 'password' not in datos_usuario:
        return 'La password es requerida'
    if Autenticacion.login_usuario(datos_usuario['nombre'], datos_usuario['password']):

        return 'ok', 200
    else:
        return 'Usuario no encontrado', 404


@app.route("/juego", methods=['POST'])
def crear_juego():
    datos_juego = request.get_json()
    if 'url' not in datos_juego:
        return 'La url es requerida'
    if 'nombre' not in datos_juego:
        return 'El nombre es requerido'
    if 'tematica' not in datos_juego:
        return 'La tematica es requerida'
    if 'descripcion' not in datos_juego:
        return 'La descripcion es requerida'
    if 'rangoDeEdad' not in datos_juego:
        return 'RangoDeEdad es requerido'

    Juegos.crear_juego(datos_juego['url'],
                       datos_juego['nombre'],
                       datos_juego['tematica'],
                       datos_juego['descripcion'],
                       datos_juego['rangoDeEdad'])
    return 'Juego creado', 200


@app.route("/juegos/<id>", methods=['DELETE'])
def borrar_juego(id):
    Juegos.borrar_juego(id)
    return 'Juego borrado', 200


@app.route("/juegos", methods=['GET'])
def listar_juegos():
    tematica = request.args.get('tematica')

    return jsonify(Juegos.listar_juegos(tematica))


@app.route("/juegos/<id>", methods=['PUT'])
def modificar_juego(id):
    datos_juegos = request.get_json()
    Juegos.modificar_juego(id, datos_juegos['url'], datos_juegos['descripcion'])
    return 'Juego modificado', 200


@app.route("/juegos/<id>")
def obtener_juego(id):
    return jsonify(Juegos.obtener_juego(id))


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
