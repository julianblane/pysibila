import unittest
from entrypoint import app
app.validate = True
from app.pysibila.api_v1.schemas import concept_name
from app.utils.dict_format_compare import compare


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.tester = app.test_client(self)

        self.concept_name = "pysibila_concepto_prueba"
        self.nombre_relacion = "pysibila_relacion_prueba"

        # Formato de las respuestas esperadas
        self.concept_list_response = {
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
        self.concept_response = {
            "estado": "ok",
            "mensaje": "string",
            "datos": {
                "concepto": {
                    "id": "string",
                    "nombre": "string",
                    "equivalencias": [
                        {
                            "peso": 0,
                            "nombre": "string"
                        }
                    ]
                }
            }
        }
        self.response_404_structure =  {
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
        self.response_404_content = {
            "errors": {
                "nombre": "5 is not of type 'string'"
            },
            "message": "Input payload validation failed"
        }


    def test_concept_list(self):
        response = self.tester.get('/conceptos',
                                   headers={"Content-Type": "application/json"})
        # Codigo de respuesta
        self.assertEqual(200, response.status_code)
        # Cuerpo de respuesta
        self.assertTrue(compare(self.concept_list_response, response.json))


    def test_concept_create(self):
        # Respuesta correcta
        response = self.tester.post('/concepto',
                                    headers={"Content-Type": "application/json"},
                                    json={"nombre": self.concept_name})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.concept_response, response.json))

        # Respuesta incorrecta
        # Estructura incorrecta
        response = self.tester.post('/concepto',
                                    headers={"Content-Type": "application/json"},
                                    json={"incorrecto": self.concept_name})
        self.assertEqual(400, response.status_code)
        self.assertTrue(compare(self.response_404_structure, response.json))

        # Contenido incorrecto
        response = self.tester.post('/concepto',
                                    headers={"Content-Type": "application/json"},
                                    json={"nombre": 2})
        self.assertEqual(400, response.status_code)
        self.assertTrue(compare(self.response_404_content, response.json))


    def test_concept_get(self):
        response = self.tester.get(f'/concepto/{self.concept_name}',
                                   headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.concept_response, response.json))


    def test_concept_update(self):
        # Respuesta correcta
        response = self.tester.put(f'/concepto/{self.concept_name}',
                                   headers={"Content-Type": "application/json"},
                                   json={"nombre": "concepto_prueba"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.concept_response, response.json))

        # Respuesta incorrecta
        # Estructura incorrecta
        response = self.tester.put(f'/concepto/{self.concept_name}',
                                   headers={"Content-Type": "application/json"},
                                   json={"incorrecto": "concepto_prueba"})
        self.assertEqual(400, response.status_code)
        self.assertTrue(compare(self.response_404_structure, response.json))

        response = self.tester.put(f'/concepto/{self.concept_name}',
                                   headers={"Content-Type": "application/json"},
                                   json={"nombre": 2})
        self.assertEqual(400, response.status_code)
        self.assertTrue(compare(self.response_404_content, response.json))


    def test_concept_delete(self):
        response = self.tester.delete(f'/concepto/{self.concept_name}',
                                      headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.concept_response, response.json))