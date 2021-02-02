import requests

# Testing
testing = True

if testing: url = "http://localhost:8080"
else: url = "http://sibila.website:8080"

def get_concepts():
    """Devuelve una lista de conceptos consultando la bd de grafos"""
    # Temporario: consulta a la api en java
    request = requests.get(f'{url}/conceptos')
    return request.json()

def create_concept(post_data):
    """Crea un concepto en la BD"""
    # Temporario: pedido a la api en java
    request = requests.post(f'{url}/concepto', data=post_data)

    return request.json()

def delete_concept(name):
    """Elimina un concepto de la BD"""
    # Temporario: pedido a la api en java
    request = requests.delete(f'{url}/concepto/{name}')
    return request.json()
