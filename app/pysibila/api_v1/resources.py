from flask import request
from flask_restx import Resource
from .schemas import concept_list, concept_name, concept_response, \
    relation_list, relation_response

# Se debe importar el blueprint aunque no se utilice para que el codigo
# en este archivo sea leido, no modificar
from .ext import api, pysibila_v1_bp

from app.conocimiento.views import \
    get_concepts, create_concept, get_concept, update_concept, delete_concept,\
    get_relations, get_relation


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
    @api.marshal_with(concept_list)
    def post(self):
        """Inserta un nuevo concepto en la base de conocimiento"""
        data = request.get_json()
        return create_concept(data)


@api.route("/concepto/<nombre>")
class ConceptManager(Resource):
    @api.marshal_with(concept_response)
    def get(self, nombre):
        """Busca un concepto dentro de la base de conocimiento y muestra los datos si existe"""
        return get_concept(nombre)

    @api.expect(concept_name)
    @api.marshal_with(concept_response)
    def put(self, nombre):
        """Actualiza un concepto buscandolo por nombre"""
        data = request.get_json()
        return update_concept(nombre, data)

    @api.marshal_with(concept_response)
    def delete(self, nombre):
        """Borra un concepto de la base de conocimiento buscandolo por nombre"""
        return delete_concept(nombre)


# Relaciones
@api.route("/relaciones")
class RelationList(Resource):
    @api.marshal_with(relation_list)
    def get(self):
        """Devuelve todAs las relaciones que contiene la base de conocimiento"""
        return get_relations()


@api.route("/relacion/<nombre>")
class RelationGet(Resource):
    @api.marshal_with(relation_response)
    def get(self, nombre):
        """Busca una relación dentro de la base de conocimiento y muestra los datos si existe"""
        return get_relation(nombre)


# Estructura
@api.route("/estructura")
class StructureCreate(Resource):
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
