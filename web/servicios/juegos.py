import json
import requests

from web.servicios import rest_api


def crear_juego2(url, nombre, tematica, descripcion, rangoDeEdad):
    body = {"url": url,
            "nombre": nombre,
            "tematica": tematica,
            "descripcion": descripcion,
            "rangoDeEdad": rangoDeEdad}
    respuesta = requests.post(f'{rest_api.API_URL}/juego', json=body)
    return respuesta.status_code == 200


def listar_juegos(tematica):
    respuesta = requests.get(f'{rest_api.API_URL}/juegos?tematica={tematica}')
    return respuesta.json()


def borrar_juego(id):
    respuesta = requests.delete(f'{rest_api.API_URL}/juegos/{id}')
    return respuesta.status_code == 200


def modificar_juego(id, url, descripcion):
    body = {"url": url,
            "descripcion": descripcion}
    respuesta = requests.put(f'{rest_api.API_URL}/juegos/{id}', json=body)
    return respuesta.status_code == 200

def obtener_juego(id):
    body = {"id":id}
    respuesta = requests.get(f'{rest_api.API_URL}/juegos/{id}', json=body)
    return respuesta.json()
