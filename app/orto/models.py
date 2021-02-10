from pydantic import BaseModel


class AnswerCorrection(BaseModel):
    respuesta: str
