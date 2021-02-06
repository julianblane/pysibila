from pydantic import BaseModel
from typing import Dict, List
from enum import Enum

# Entradas
class ConceptRegister(BaseModel):
    nombre: str


class EstructureRegister(BaseModel):
    conceptoOrigen: str
    conceptoDestino: str
    relacion: str
