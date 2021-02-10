import requests
from config.urls import URL


def answer_correct(answer):
    request = {
        "respuesta": answer,
    }
    response = requests.POST(f'{URL}/respuesta/corregir', json=request)
    return response.json()