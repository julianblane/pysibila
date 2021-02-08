from flask import request
from flask_restx import Resource, marshal
from flask_pydantic import validate
import json
# Se debe importar el blueprint aunque no se utilice para que el codigo
# en este archivo sea leido, no modificar
from .ext import api, pysibila_v1_bp

from app.conocimiento.views import \
    update_concept

# Schemas and models
from .schemas import response_404_structure, \
    concept_list_response, concept_name, concept_response, \
    relation_list_response, relation_response, estructure, \
    answer_list, answer_list_response, answer_response
# Input models
from .models import ConceptRegister, EstructureRegister
from app.conocimiento.models import AnswerList, Concept, Relation, Structure

# Funcionalidades heredadas
# Conceptos
@api.route("/conceptos", endpoint='concept_list')
class ConceptList(Resource):
    @api.marshal_with(concept_list_response)
    def get(self):
        """Obtiene un listado con todos los conceptos de la base de datos"""
        concept_list, data = Concept.all()
        return data


@api.route("/concepto")
class ConceptCreate(Resource):
    # Valida la estructura del json
    @validate(body=ConceptRegister)
    # Valida el contenido del json
    @api.expect(concept_name)
    @api.marshal_with(concept_response)
    @api.response(400, 'Validation error: Estructura del json incorrecta', response_404_structure)
    def post(self):
        """Inserta un nuevo concepto en la base de conocimiento"""
        request_data = request.get_json()
        concept, response_data = Concept.save(request_data['nombre'])
        return response_data

@api.route("/concepto/<nombre>")
class ConceptManager(Resource):
    @api.marshal_with(concept_response)
    def get(self, nombre):
        """Busca un concepto dentro de la base de conocimiento y muestra los datos si existe"""
        concept, data = Concept.get(nombre)
        return data

    @validate(body=ConceptRegister)
    @api.expect(concept_name)
    @api.marshal_with(concept_response)
    @api.response(400, 'Validation error', response_404_structure)
    def put(self, nombre):
        """Actualiza un concepto buscandolo por nombre"""
        data = request.get_json()
        return update_concept(nombre, data)

    @api.marshal_with(concept_response)
    def delete(self, nombre):
        """Borra un concepto de la base de conocimiento buscandolo por nombre"""
        return Concept.delete(nombre)


# Relaciones
@api.route("/relaciones")
class RelationList(Resource):
    @api.marshal_with(relation_list_response)
    def get(self):
        """Devuelve todas las relaciones que contiene la base de conocimiento"""
        relation_list, data = Relation.all()
        return data


@api.route("/relacion/<nombre>")
class RelationGet(Resource):
    @api.marshal_with(relation_response)
    def get(self, nombre):
        """Busca una relación dentro de la base de conocimiento y muestra los datos si existe"""
        relation, data = Relation.get(nombre)
        return data


# Estructura
@api.route("/estructura")
class StructureCreate(Resource):
    @validate(body=Structure)
    @api.expect(estructure)
    @api.marshal_with(answer_response)
    @api.response(400, 'Validation error', response_404_structure)
    def post(self):
        """Inserta una nueva estructura en la base de conocimiento"""
        data = request.get_json()
        structure = Structure(**data)
        return structure.save()


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


# Nuevas funcionalidades
@api.route("/respuesta/grabar")
class AnswersSave(Resource):
    @validate(body=AnswerList)
    @api.expect(answer_list)
    @api.marshal_with(answer_list)
    def post(self):
        """Inserta una lista de respuestas en forma de concepto-relacion-concepto en la base de datos"""
        data = request.get_json()
        answer = AnswerList(**data)

        return answer
