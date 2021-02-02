import requests

# Testing
testing = True

if testing: url = "http://localhost:8080"
else: url = "http://sibila.website:8080"

# conceptos
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


def get_concept(name):
    """Busca un concepto en la BD"""
    # Temporario: pedido a la api en java
    request = requests.get(f'{url}/concepto/{name}')
    return request.json()


def update_concept(name, data):
    """Actualiza un concepto de la BD"""
    # Temporario: pedido a la api en java
    # print(data['nombre'])
    # print(f'{url}/concepto/{name}?nuevoNombre={data["nombre"]}')
    # Actualmente la api elimina el concepto en lugar de actualizarlo
    # La documentacion de la api es incorrecta
    request = requests.put(f'{url}/concepto/{name}?nuevoNombre={data["nombre"]}', json=data)
    return request.json()


def delete_concept(name):
    """Elimina un concepto de la BD"""
    # Temporario: pedido a la api en java
    request = requests.delete(f'{url}/concepto/{name}')
    return request.json()


# Relaciones
def get_relations():
    """Devuelve una lista de relaciones consultando la bd de grafos"""
    # Temporario: consulta a la api en java
    request = requests.get(f'{url}/relaciones')
    return request.json()


def get_relation(name):
    """Busca un concepto en la BD"""
    # Temporario: pedido a la api en java
    request = requests.get(f'{url}/relacion/{name}')
    return request.json()


def create_structure(data):
    """Crea una estructura de concepto relacion concepto,
    creando cada concepto y la relacion entre ellos solo si no existen"""
    # Problema: En ocaciones parece duplicar los coneptos en bd
    # Ver que tipo de objeto deberia devolver data (estimo que un par concepto relacion concepto)
    # Temporario: pedido a la api en java
    request = requests.post(f'{url}/estructura', data=data)
    return request.json()
