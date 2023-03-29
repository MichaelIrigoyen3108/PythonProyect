from flask import Flask, request, redirect, url_for, session
from flask import render_template
from web.servicios import autenticacion, juegos

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autenticacion.validar_credenciales(request.form['nombre'], request.form['password']):
            return redirect(url_for('registro'))

        else:
            return redirect(url_for('navegacion'))
    return render_template('login.html', error=error)


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_usuario(request.form['nombre'],
                                           request.form['apellido'],
                                           request.form['fecha_de_nacimiento'],
                                           request.form['password'],
                                           request.form['email']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('login'))
    return render_template('pagina2.html', error=error)


@app.route('/pagina3', methods=['GET'])
def navegacion():
    return render_template('pagina3.html')


@app.route('/juego', methods=['POST', 'GET'])
def crear_juego():
    if request.method == 'POST':

        if juegos.crear_juego2(request.form['url'],
                               request.form['nombre'],
                               request.form['tematica'],
                               request.form['descripcion'],
                               request.form['rangoDeEdad']):
            return redirect(url_for('login'))

    return render_template('crearjuego2.html')


@app.route('/juegos', methods=['GET'])
def listar_juegos():
    lista_juegos = juegos.listar_juegos(request.form['tematica'])
    return render_template('pagina3.html', lista_juegos=lista_juegos)


@app.route('/buscarjuegos', methods=['POST', 'GET'])
def buscar_juegos():
    mensaje = ''
    buscar_juegos = []
    if request.method == 'POST':
        buscar_juegos = juegos.listar_juegos(request.form['tematica'])

    return render_template('buscarjuegos.html', buscar_juegos=buscar_juegos, mensaje=mensaje)


@app.route('/borrar/<id>', methods=['POST'])
def borrar_juego(id):
    juegos.borrar_juego(id)
    return redirect(url_for('buscar_juegos'))


@app.route('/modificar/<id>', methods=['GET', 'POST'])
def modificar_juego(id):
    modificar_juego = juegos.obtener_juego(id)
    mensaje = ''
    if request.method == 'POST':
        if juegos.modificar_juego(id, request.form['url'], request.form['descripcion']):
            mensaje = 'Juego modificado'
        else:
            mensaje = 'No se pudo modificar el juego'

    return render_template('modificarjuego.html', modificar_juego=modificar_juego, mensaje=mensaje)


if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
    