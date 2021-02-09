import unittest
from .models import AnswerList


class TestAnswer(unittest.TestCase):
    def setUp(self) -> None:
        self.request_correct = {
            "respuestas": [
                {
                    "respuesta": [
                        {
                            "nombre": "pysibila_concepto_prueba",
                            "tipo_termino": "concepto"
                        },
                        {
                            "nombre": "pysibila_concepto_prueba",
                            "tipo_termino": "relacion"
                        },
                        {
                            "nombre": "pysibila_concepto_prueba",
                            "tipo_termino": "concepto"
                        },
                    ]
                }
            ]
        }

        self.request_incorrect_format = {
            "respuestas": [
                {
                    "respuesta": [
                        {
                            "nombre": "pysibila_concepto_prueba",
                            "tipo_termino": "concepto"
                        },
                        {
                            "nombre": "pysibila_concepto_prueba",
                            "tipo_termino": "concepto"
                        },
                        {
                            "nombre": "pysibila_concepto_prueba",
                            "tipo_termino": "concepto"
                        },
                    ]
                }
            ]
        }

        self.request_incorrect_format_2 = {
            "respuestas": [
                {
                    "respuesta": [
                        {
                            "nombre": "pysibila_concepto_prueba",
                            "tipo_termino": "concepto"
                        },
                    ]
                }
            ]
        }

        self.request_incorrect_format_3 = {
            "respuestas": [
                {
                    "respuesta": [
                        {
                            "nombre": "pysibila_concepto_prueba",
                            "tipo_termino": "relacion"
                        },
                        {
                            "nombre": "pysibila_concepto_prueba",
                            "tipo_termino": "concepto"
                        },
                        {
                            "nombre": "pysibila_concepto_prueba",
                            "tipo_termino": "relacion"
                        },
                    ]
                }
            ]
        }


    def test_create(self):
        # Caso correcto
        answer_list = AnswerList(**self.request_correct)
        self.assertTrue(answer_list is not None)
        self.assertTrue(answer_list.respuestas is not None)

        # Formato incorrecto
        answer_list = AnswerList(**self.request_correct)

    def test_validate_format(self):
        answer_list = AnswerList(**self.request_correct)
        # Obtiene la primera respuesta de la lista
        answer = answer_list.respuestas[0]

        self.assertTrue(answer.is_valid_format())

        # Respuesta no sigue el patron concepto relacion concepto
        answer_list = AnswerList(**self.request_incorrect_format)
        self.assertFalse(answer_list.respuestas[0].is_valid_format())

        # Respuesta demasiado corta
        answer_list = AnswerList(**self.request_incorrect_format_2)
        self.assertFalse(answer_list.respuestas[0].is_valid_format())

        # Respuesta que empieza por relacion
        answer_list = AnswerList(**self.request_incorrect_format_3)
        self.assertFalse(answer_list.respuestas[0].is_valid_format())
