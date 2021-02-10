import requests
from config.urls import URL


def answer_evaluate(base, to_evaluate):
    request = {
        "respuestaBase": base,
        "respuestaAlumno": to_evaluate
    }
    response = requests.POST(f'{URL}/respuesta/evaluar', json=request)
    return response.json()
