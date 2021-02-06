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


class Answer(BaseModel):
    respuesta: List[Term]

    def get(self):
        """Obtiene una respuesta completa de base de datos"""
        pass

    def save(self):
        """Almacena una respuesta completa en base de datos"""
        pass

    def is_valid_format(self):
        """Verifica si el formato de la respuesta es de la forma concepto - relacion - concepto"""
        # Cantidad de terminos de la respuesta
        if len(self.respuesta) < 3 or len(self.respuesta) % 2 == 0:
            return False
        # Verificar que los terminos pares sean conceptos
        if not all(map(lambda term: term.tipo == TermType.CONCEPTO, self.respuesta[::2])):
            return False
        # Verificar que los terminos pares sean conceptos
        if not all(map(lambda term: term.tipo == TermType.RELACION, self.respuesta[1::2])):
            return False
        return True


class AnswerList(BaseModel):
    respuestas: List[Answer]


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
    def delete(self, name):
        """Elimina un concepto de la BD"""
        # Temporario: pedido a la api en java
        request = requests.delete(f'{URL}/concepto/{name}')
        return request.json()


    # @classmethod
    # def delete(cls):


class Relation(Term):
    # Atributos para serializacion
    id: str
    tipo: str

    # Atributos de comportamiento
    preview_concept = Concept
    next_concept = Concept

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
