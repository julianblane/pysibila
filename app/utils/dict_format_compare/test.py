import unittest
from .dict_format_compare import compare as compare


class TestDictFormatCompare(unittest.TestCase):
    def test_dict_format_compare(self):
        dict_1 = {
            'id': "id",
            'nombre': "nombre",
            'equivalencias': {
                'id': "id",
                'nombre': "nombre",
            }
        }

        dict_2 = {
            'id': "id",
            'nombre': "nombre",
            'equivalencias': {
                'id': "id",
                'nombre': "nombre",
            }
        }

        dict_3 = {
            'id': "other",
            'nombre': "nombre",
            'equivalencias': {
                'id': "id",
                'nombre': "nombre",
            }
        }

        dict_4 = {
            'id': "other",
            'nombre': "nombre",
            'equivalencias': {
                'id': "other",
                'nombre': "nombre",
            }
        }

        dict_5 = {
            'id': "other",
            'nombre': "nombre",
            'equivalencias': "string"
        }

        dict_6 = {
            'id': dict(),
            'nombre': "nombre",
            'equivalencias': {
                'id': "other",
                'nombre': "nombre",
            }
        }

        # Mismo diccionario
        self.assertTrue(compare(dict_1, dict_1))
        # Diccionarios iguales
        self.assertTrue(compare(dict_1, dict_2))
        # Valores diferentes
        self.assertTrue(compare(dict_1, dict_3))
        # Valores diferentes en subdiccionario
        self.assertTrue(compare(dict_1, dict_4))
        # Diferentes subdiccionarios
        self.assertFalse(compare(dict_1, dict_5))
        # Diferentes subdiccionarios
        self.assertFalse(compare(dict_1, dict_6))
