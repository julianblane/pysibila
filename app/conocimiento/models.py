from pydantic import BaseModel
from typing import List
from enum import Enum
from config.urls import URL
import requests


class TermType(str, Enum):
    CONCEPTO = 'concepto'
    RELACION = 'relacion'


class Term(BaseModel):
    nombre: str
    tipo_termino: TermType


class AnswerResponse(BaseModel):
    """Resultado de la accion realizada con la respuesta que será devuelta como respuesta a la llamada"""
    # Atributos a serializar
    estado: str
    mensaje: str
    datos: List[Term]


class Answer(BaseModel):
    """Respuesta formada por un conjunto de conceptos y relaciones en formato concepto - relacion - concepto"""
    terminos: List[Term]

    def get(self):
        """Obtiene una respuesta completa de base de datos"""
        pass

    def save(self):
        """Almacena una respuesta completa en base de datos"""
        pass

    def invalid_format_response(self):
        """Devuelve un objeto de respuesta indicando el error"""
        return AnswerResponse(estado="error",
                              mensaje="Los terminos no siguen el formato concepto, relacion, concepto",
                              datos=self.terminos)

    def is_valid_format(self):
        """Verifica si el formato de la respuesta es de la forma concepto - relacion - concepto"""

        # Cantidad de terminos de la respuesta
        if len(self.terminos) < 3 or len(self.terminos) % 2 == 0:
            return False
        # Verificar que los terminos pares sean conceptos
        if not all(map(lambda term: term.tipo_termino == TermType.CONCEPTO, self.terminos[::2])):
            return False
        # Verificar que los terminos pares sean conceptos
        if not all(map(lambda term: term.tipo_termino == TermType.RELACION, self.terminos[1::2])):
            return False
        return True

    def save(self):
        """Guarda una respuesta completa en base de datos y devuelve el resultado de la operacion"""
        # Nota: a fututro implementar transacciones con commit y rollback

        # Si el formato no es valido devuelve un objeto de respuesta indicando el error
        if not self.is_valid_format():
            return AnswerResponse(estado="error",
                                  mensaje="Los terminos no siguen el formato concepto - relacion - concepto",
                                  datos=self.terminos)

        # Se recorre los conceptos guardando cada estructura
        for term_index in range(0, len(self.terminos) - 2, 2):
            structure = Structure(conceptoOrigen=self.terminos[term_index].nombre,
                                  conceptoDestino=self.terminos[term_index + 2].nombre,
                                  relacion=self.terminos[term_index + 1].nombre)
            data = structure.save()
            # Si surge un error durante el proceso de guardado se deja de guardar y se
            # devuelve un objeto de respuesta indicando error
            # Nota: a fututro implementar transacciones con commit y rollback
            if not data['estado'] == 'ok':
                return AnswerResponse(estado="error",
                                      mensaje="Error en la grabación de la pregunta",
                                      datos=self.terminos)

        # La respuesta se grabo correctamente
        return AnswerResponse(estado="ok",
                              mensaje="Respuesta grabada correctamente",
                              datos=self.terminos)


class AnswerListResponse(BaseModel):
    """Lista de resultados de las acciones realizadas con las respuestas que será
    devuelta como respuesta a la llamada"""
    respuestas: List[AnswerResponse]


class AnswerList(BaseModel):
    """Maneja el proceso que se desea realizar sobre la lista de respuestas"""
    # Atributos para serializacion
    respuestas: List[Answer]

    # Atributos del dominio

    def save(self):
        """Guarda un conjunto de respuestas en base de datos y devuelve la respuesta para cada operacion"""
        # Listado de respuestas al grabado de respuestas en base de datos
        answer_list_response = AnswerListResponse(respuestas=[])
        for answer in self.respuestas:
            # Guarda cada respuesta y agrega el resultado de la operacion a la lista
            # de respuestas de operacion
            answer_list_response.respuestas.append(answer.save())
        return answer_list_response




class Equivalency(BaseModel):
    nombre: str
    peso: float


class Concept(Term):
    id: str
    equivalencias: List[Equivalency]

    # Al definirle un valor al objeto ya no es requerido al crearlo
    tipo_termino = TermType.CONCEPTO

    @classmethod
    def get(cls, name):
        """Busca un concepto en base de datos y lo devuelve se la encuentra"""
        request = requests.get(f'{URL}/concepto/{name}')
        data = request.json()
        if data['estado'] == 'ok':
            # Soluciona problemas en el formato en que la api de java devuelve un concepto
            data_fix = request.json()
            data_fix['datos']['concepto']['equivalencias'] = []
            concept = Concept(**data_fix['datos']['concepto'])
            return concept, data
        return None, data

    @classmethod
    def all(cls):
        """Devuelve una lista de conceptos consultando la bd de grafos"""
        # Temporario: consulta a la api en java
        request = requests.get(f'{URL}/conceptos')
        data = request.json()
        if data['estado'] == 'ok':
            data_fix = request.json()
            concept_list = []
            for data_concept in data_fix['datos']['conceptos']:
                # Soluciona problemas en el formato en que la api de java devuelve un concepto
                data_concept['equivalencias'] = []
                # Crea un concepto y lo agrega a la lista
                concept_list.append(Concept(**data_concept))
            return concept_list, data
        return None, data

    @classmethod
    def save(cls, name):
        """Crea un nuevo concepto en la BD"""
        # Temporario: pedido a la api en java
        request = requests.post(f'{URL}/concepto', data={'nombre': name})
        data = request.json()
        if data['estado'] == 'ok':
            concept, get_data = cls.get(name)
            return concept, data
        return None, data

    @classmethod
    def delete(cls, name):
        """Elimina un concepto de la BD"""
        # Temporario: pedido a la api en java
        request = requests.delete(f'{URL}/concepto/{name}')
        return request.json()

    @classmethod
    def exists(cls, name):
        """Indica si el objeto se encuentra en la base de datos"""
        concept, data = cls.get(name)
        return concept is not None


class Relation(Term):
    # Atributos para serializacion
    id: str
    tipo: str

    # Al definirle un valor al objeto ya no es requerido al crearlo
    tipo_termino = TermType.RELACION

    @classmethod
    def get(cls, name):
        """Busca una relacion en base de datos y la devuelve se la encuentra"""
        # Temporario: consulta a la api en java
        request = requests.get(f'{URL}/relacion/{name}')
        data = request.json()
        if data['estado'] == 'ok':
            relation = Relation(**data['datos']['relacion'])
            return relation, data
        return None, data

    @classmethod
    def all(cls):
        """Devuelve una lista de relaciones consultando la bd de grafos"""
        # Temporario: consulta a la api en java
        request = requests.get(f'{URL}/relaciones')
        data = request.json()
        if data['estado'] == 'ok':
            relation_list = []
            # Crea una nueva relacion y la agrega a la lista
            for relation_data in data['datos']['relaciones']:
                relation_list.append(Relation(**relation_data))
            return relation_list, data
        return None, data

    @classmethod
    def exists(cls, name):
        """Indica si el objeto se encuentra en la base de datos"""
        relation, data = cls.get(name)
        return relation is not None


class Structure(BaseModel):
    """Una estructura es una instancia de una relacion entre 2 conceptos
    Una relacion no puede existir sino conecta 2 concepto
    Un concepto no deberia existir sin ninguna relacion que lo vincule"""
    # Atributos para serializacion
    conceptoOrigen: str
    conceptoDestino: str
    relacion: str

    @classmethod
    def get_relations(cls, origin_concept, destiny_concept):
        """Obtiene todas las estructuras entre 2 conceptos"""
        pass

    def save(self):
        """Crea una estructura de concepto relacion concepto,
        creando cada concepto y la relacion entre ellos solo si no existen"""
        data = {
            'conceptoOrigen': self.conceptoOrigen,
            'conceptoDestino': self.conceptoDestino,
            'relacion': self.relacion
        }
        # Problema: En ocaciones parece duplicar los coneptos en bd
        # Ver que tipo de objeto deberia devolver data (estimo que un par concepto relacion concepto)
        # Temporario: pedido a la api en java
        request = requests.post(f'{URL}/estructura', data=data)
        # A futuro debera obtener los conceptos y la relacion y guardarlos en sus atributos
        return request.json()

    def get(self, relation, origin_concept, destiny_concept):
        """Obtiene una estructura a partir del nombre de sus conceptos y su relacion si existe"""
        pass
