import unittest
from entrypoint import app
app.validate = True
from app.utils.dict_format_compare import compare


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.tester = app.test_client(self)

        self.concept_name = "pysibila_concepto_prueba"
        self.relation_name = "pysibila_relacion_prueba"

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
        self.relations_list_response = {
            "estado": "ok",
            "mensaje": "string",
            "datos": {
                "relaciones": [
                    {
                        "id": "string",
                        "nombre": "string",
                        "tipo": "string"
                    }
                ]
            }
        }
        self.relation_response = {
            "estado": "ok",
            "mensaje": "string",
            "datos": {
                "relacion": {
                    "id": "string",
                    "nombre": "string",
                    "tipo": "string"
                }
            }
        }

    # Funciones de soporte
    def create_concept(self, concept=None):
        if concept is None: concept = self.concept_name
        self.tester.post('/concepto',
                         headers={"Content-Type": "application/json"},
                         json={"nombre": concept})

    def delete_concept(self, concept=None):
        if concept is None: concept = self.concept_name
        self.tester.delete(f'/concepto/{concept}',
                           headers={"Content-Type": "application/json"})

    def get_concept(self, concept=None):
        if concept is None: concept = self.concept_name
        return self.tester.get(f'/concepto/{concept}',
                        headers={"Content-Type": "application/json"})

    def concept_exists(self, concept=None):
        if concept is None: concept = self.concept_name
        response = self.get_concept(concept)
        return 'ok' == response.json['estado']

    def get_relation(self, relation=None):
        if relation is None: relation = self.concept_name
        return self.tester.get(f'/relacion/{relation}',
                               headers={"Content-Type": "application/json"})

    def relation_exists(self, relation=None):
        if relation is None: relation = self.relation_name
        response = self.get_relation(relation)
        return 'ok' == response.json['estado']

    # Test
    def test_concept_list(self):
        response = self.tester.get('/conceptos',
                                   headers={"Content-Type": "application/json"})
        # Codigo de respuesta
        self.assertEqual(200, response.status_code)
        # Cuerpo de respuesta
        self.assertTrue(compare(self.concept_list_response, response.json))
        self.assertEqual('ok', response.json['estado'])


    def test_concept_create(self):
        # Eliminar el concepto a crear
        self.delete_concept()

        # Respuesta correcta
        # Concepto insertado exitosamente
        response = self.tester.post('/concepto',
                                    headers={"Content-Type": "application/json"},
                                    json={"nombre": self.concept_name})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.concept_response, response.json))
        self.assertEqual('ok', response.json['estado'])
        self.assertTrue(self.concept_exists())

        # Concepto insertado repetido
        response = self.tester.post('/concepto',
                                    headers={"Content-Type": "application/json"},
                                    json={"nombre": self.concept_name})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.concept_response, response.json))
        self.assertEqual('error', response.json['estado'])
        self.assertTrue(self.concept_exists())

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

        # Eliminar concepto creado
        self.delete_concept()


    def test_concept_get(self):
        # Crear concepto a buscar
        self.create_concept()

        # Concepto encontrado
        response = self.tester.get(f'/concepto/{self.concept_name}',
                                   headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.concept_response, response.json))
        self.assertEqual('ok', response.json['estado'])

        # Eliminar concepto creado
        self.delete_concept()

        # Concepto no encontrado
        response = self.tester.get(f'/concepto/{self.concept_name}',
                                   headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.concept_response, response.json))
        self.assertEqual('no encontrado', response.json['estado'])


    def test_concept_update_success(self):
        # Respuesta correcta
        # Cambio de nombre correcto: No funciona
        # Crear concepto a modificar
        self.create_concept()
        # Eliminar concepto con nombre a cambiar
        self.delete_concept(f"{self.concept_name}_modificado")


        # Resultado
        # {
        #     "estado": "error",
        #     "mensaje": "Cannot index record #11:256: found duplicated key 'pysibila_concepto_prueba_modificado' in index 'Idx_ConceptoNombre' previously assigned to the record #11:255\r\n\tDB name=\"PPR\"\r\n\tDB name=\"PPR\"",
        #     "datos": {
        #         "concepto": {
        #             "id": null,
        #             "nombre": null,
        #             "equivalencias": null
        #         }
        #     }
        # }
        response = self.tester.put(f'/concepto/{self.concept_name}',
                                   headers={"Content-Type": "application/json"},
                                   json={"nombre": f"{self.concept_name}_modificado"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.concept_response, response.json))
        self.assertEqual('ok', response.json['estado'])

        # Verifica si el concepto existe con su nombre cambiado
        self.assertTrue(self.concept_exists('{self.concept_name}_modificado'))
        # Verifica que el concepto no exista con su nombre anterior
        self.assertFalse(self.concept_exists('{self.concept_name}'))

        self.delete_concept()
        self.delete_concept(f"{self.concept_name}_modificado")


    def test_concept_update_not_found(self):
        # Cambio de nombre de concepto inexistente
        # Crear concepto a modificar
        self.delete_concept()
        # Eliminar concepto con nombre a cambiar
        self.delete_concept(f"{self.concept_name}_modificado")

        response = self.tester.put(f'/concepto/{self.concept_name}',
                                   headers={"Content-Type": "application/json"},
                                   json={"nombre": f"{self.concept_name}_modificado"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.concept_response, response.json))
        self.assertEqual('no encontrado', response.json['estado'])

        # Verifica si el concepto existe con su nombre cambiado
        self.assertFalse(self.concept_exists('{self.concept_name}_modificado'))
        # Verifica que el concepto no exista con su nombre anterior
        self.assertFalse(self.concept_exists('{self.concept_name}'))

        self.delete_concept()
        self.delete_concept(f"{self.concept_name}_modificado")


    def test_concept_update_repeated(self):
        # Cambio de nombre de concepto a un nombre repetido
        # Crear concepto a modificar
        self.create_concept()
        # Crear concepto con nombre al que se quiere cambiar
        self.create_concept(f"{self.concept_name}_modificado")

        response = self.tester.put(f'/concepto/{self.concept_name}',
                                   headers={"Content-Type": "application/json"},
                                   json={"nombre": f"{self.concept_name}_modificado"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.concept_response, response.json))
        self.assertEqual('error', response.json['estado'])

        # Verifica si el concepto existe con su nombre cambiado
        self.assertFalse(self.concept_exists('{self.concept_name}_modificado'))
        # Verifica que el concepto no exista con su nombre anterior
        self.assertFalse(self.concept_exists('{self.concept_name}'))

        self.delete_concept()
        self.delete_concept(f"{self.concept_name}_modificado")

    def test_concept_update(self):
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
        # Crear concepto a eliminar
        self.create_concept()

        # Eliminar concepto existente
        response = self.tester.delete(f'/concepto/{self.concept_name}',
                                      headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.concept_response, response.json))
        self.assertEqual('ok', response.json['estado'])
        self.assertFalse(self.concept_exists())

        # Eliminar concepto inexistente
        response = self.tester.delete(f'/concepto/{self.concept_name}',
                                      headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.concept_response, response.json))
        self.assertEqual('no encontrado', response.json['estado'])


    def test_relations_list(self):
        response = self.tester.get('/relaciones',
                                   headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.relations_list_response, response.json))
        self.assertEqual('ok', response.json['estado'])


    def test_relation_get(self):
        # Relacion encontrada
        response = self.tester.get(f'/relacion/{self.relation_name}',
                                   headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.relation_response, response.json))
        self.assertEqual('ok', response.json['estado'])

        # Relacion no encontrada: No se puede eliminar las relaciones ya creadas
        response = self.tester.get(f'/relacion/{self.relation_name}_inexistente',
                                   headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.relation_response, response.json))
        self.assertEqual('no encontrado', response.json['estado'])


    def test_structure_create_all(self):
        # Conceptos
        concept_1 = f'{self.concept_name}_1'
        concept_2 = f'{self.concept_name}_2'
        relation = self.relation_name
        # Se eliminan antes de empezar
        self.delete_concept(concept_1)
        self.delete_concept(concept_2)

        # Crear los nodos y la relacion
        response = self.tester.post(f'/estructura',
                                    headers={"Content-Type": "application/json"},
                                    json={
                                        "conceptoOrigen": concept_1,
                                        "conceptoDestino": concept_2,
                                        "relacion": relation
                                    })
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.relation_response, response.json))
        self.assertEqual('ok', response.json['estado'])
        self.assertTrue(self.concept_exists(concept_1))
        self.assertTrue(self.concept_exists(concept_2))
        self.assertTrue(self.relation_exists(relation))

        # Crear una relacion con nodos ya existentes
        response = self.tester.post(f'/estructura',
                                    headers={"Content-Type": "application/json"},
                                    json={
                                        "conceptoOrigen": concept_1,
                                        "conceptoDestino": concept_2,
                                        "relacion": relation
                                    })
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.relation_response, response.json))
        self.assertEqual('ok', response.json['estado'])
        self.assertTrue(self.concept_exists(concept_1))
        self.assertTrue(self.concept_exists(concept_2))
        self.assertTrue(self.relation_exists(relation))

        # Conceptos y relaciones ya creadas
        response = self.tester.post(f'/estructura',
                                    headers={"Content-Type": "application/json"},
                                    json={
                                        "conceptoOrigen": concept_1,
                                        "conceptoDestino": concept_2,
                                        "relacion": relation
                                    })
        self.assertEqual(200, response.status_code)
        self.assertTrue(compare(self.relation_response, response.json))
        self.assertEqual('ok', response.json['estado'])

        # Se eliminan al terminar
        self.delete_concept(concept_1)
        self.delete_concept(concept_2)

        # La relacion se deberia eliminar al eliminar los nodos
        # self.assertFalse(self.relation_exists(relation))


    def test_structure_errors(self):
        # Conceptos
        concept_1 = f'{self.concept_name}_1'
        concept_2 = f'{self.concept_name}_2'
        relation = self.relation_name
        # Se crean los conceptos antes de empezar

        # Respuesta incorrecta
        # Estructura incorrecta
        response = self.tester.post(f'/estructura',
                                    headers={"Content-Type": "application/json"},
                                    json={
                                        "incorrecto": concept_1,
                                        "conceptoDestino": concept_2,
                                        "relacion": relation
                                    })
        self.assertEqual(400, response.status_code)
        self.assertTrue(compare(self.response_404_structure, response.json))

        # Contenido incorrecto
        esponse = self.tester.post(f'/estructura',
                                   headers={"Content-Type": "application/json"},
                                   json={
                                       "conceptoOrigen": 2,
                                       "conceptoDestino": concept_2,
                                       "relacion": relation
                                   })
        self.assertEqual(400, response.status_code)
        self.assertTrue(compare(self.response_404_structure, response.json))

        # Eliminar concepto creado
        self.delete_concept()