from flask import request
from flask_restx import Resource
from .schemas import concept_list, concept_name, concept_response

# Se debe importar el blueprint aunque no se utilice para que el codigo
# en este archivo sea leido, no modificar
from .ext import api, pysibila_v1_bp

from app.conocimiento.views import get_concepts, create_concept


# Conceptos
@api.route("/conceptos", endpoint='concept_list')
class ConceptList(Resource):
    @api.marshal_with(concept_list)
    def get(self):
        """Obtiene un listado con todos los conceptos de la base de datos"""
        return get_concepts()


@api.route("/concepto")
class ConceptCreate(Resource):
    @api.expect(concept_name)
    @api.marshal_with(concept_response)
    def post(self):
        """Inserta un nuevo concepto en la base de conocimiento"""
        data = request.get_json()
        return create_concept(data)


@api.route("/concepto/<nombre>")
class ConceptManager(Resource):
    def get(self, nombre):
        """Busca un concepto dentro de la base de conocimiento y muestra los datos si existe"""
        pass

    def put(self, nombre):
        """Actualiza un concepto buscandolo por nombre"""

    def delete(self, nombre):
        """Borra un concepto de la base de conocimiento buscandolo por nombre"""
        pass


# Relaciones
@api.route("/relaciones")
class RelationList(Resource):
    def get(self):
        """Devuelve todAs las relaciones que contiene la base de conocimiento"""
        pass


@api.route("/relacion/{nombre}")
class RelationCreate(Resource):
    def get(self, nombre):
        """Busca una relación dentro de la base de conocimiento y muestra los datos si existe"""
        pass


# Estructura
@api.route("/estructura")
class RelationCreate(Resource):
    def post(self):
        """Inserta una nueva estructura en la base de conocimiento"""
        pass


# Respuesta
@api.route("/respuesta/evaluar")
class ResponseEvaluate(Resource):
    def post(self):
        """Evalúa a respuesta de un estudiante y devuelve la calificación"""
        pass

@api.route("/respuesta/corregir")
class ResponseCorrect(Resource):
    def post(self):
        """Corrige ortograficamente una respuesta, separa los términos y los clasifica en conceptos y relaciones"""
        pass
