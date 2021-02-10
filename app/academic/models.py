from pydantic import BaseModel


class AnswerEvaluation(BaseModel):
    respuestaBase: str
    respuestaAlumno: str
