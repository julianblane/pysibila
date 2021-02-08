import requests
from config.urls import URL
from .models import Relation, Concept
# conceptos


def update_concept(name, data):
    """Actualiza un concepto de la BD"""
    # Temporario: pedido a la api en java
    # Actualmente la api elimina el concepto en lugar de actualizarlo
    # La documentacion de la api es incorrecta
    request = requests.put(f'{URL}/concepto/{name}?nuevoNombre={data["nombre"]}', json=data)
    return request.json()


def save_response(respuesta):
    """Guarda una respuesta completa en base de datos"""
    # Sera necesario implementar un sistema de rollback
    # para el grabado de la respuesta
    pass


def save_responses(data):
    """Guarda una lista de respuestas en base de datos y devuelve
     un dict con el resultado de cada operacion"""
    pass
