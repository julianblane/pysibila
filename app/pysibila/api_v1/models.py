from pydantic import BaseModel


class ConceptRegister(BaseModel):
    nombre: str