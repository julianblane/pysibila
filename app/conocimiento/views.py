import requests


def get_concepts():
    """Devuelve una lista de conceptos consultando la bd de grafos"""
    # Temporario: consulta a la api en java
    request = requests.get("http://sibila.website:8080/conceptos")
    return request.json()

def create_concept():
    """Crea un concepto en la BD"""
    pass