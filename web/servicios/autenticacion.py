import requests

from web.servicios import rest_api


def validar_credenciales(usuario, password):
    body = {"nombre": usuario,
            "password": password}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    return respuesta.status_code == 200


def crear_usuario(nombre, apellido, fecha_de_nacimiento, password, email):
    body = {"nombre": nombre,
            "apellido": apellido,
            "fecha_de_nacimiento": fecha_de_nacimiento,
            "password": password,
            "email": email}
    respuesta = requests.post(f'{rest_api.API_URL}/usuario', json=body)
    return respuesta.status_code == 200


