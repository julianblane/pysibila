import unittest
from entrypoint import app
app.validate = True
from app.pysibila.api_v1.schemas import concept_name
from app.utils.dict_format_compare import compare


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.tester = app.test_client(self)


    def test_concept_create_200(self):
        # Respuesta correcta
        response = self.tester.post('/concepto',
                                    headers={"Content-Type": "application/json"},
                                    json={"nombre": "juan"})
        self.assertEqual(200, response.status_code)
        response_format = {
            "estado": "ok",
            "mensaje": "string",
            "datos": {
                "conceptos": [
                    {
                        "id": "string",
                        "nombre": "string",
                        "equivalencias": [
                            {
                                "peso": 0,
                                "nombre": "string"
                            }
                        ]
                    }
                ]
            }
        }
        self.assertTrue(compare(response_format, response.json))


    def test_concept_create_400(self):
        # Respuesta incorrecta
        response = self.tester.post('/concepto',
                                    headers={"Content-Type": "application/json"},
                                    json={"incorrecto": "juan"})
        response_format = {
            "validation_error": {
                "body_params": [
                    {
                        "loc": [
                            "string"
                        ],
                        "msg": "string",
                        "type": "string"
                    }
                ]
            }
        }
        self.assertEqual(400, response.status_code)
        self.assertTrue(compare(response_format, response.json))

        response = self.tester.post('/concepto',
                                      headers={"Content-Type": "application/json"},
                                      json={"incorrecto": 2})
        self.assertEqual(400, response.status_code)
        self.assertTrue(compare(response_format, response.json))
