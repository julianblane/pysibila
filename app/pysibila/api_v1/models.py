from pydantic import BaseModel


class ConceptRegister(BaseModel):
    nombre: str


class EstructureRegister(BaseModel):
    conceptoOrigen: str
    conceptoDestino: str
    relacion: str