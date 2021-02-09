from flask import request
from flask_restx import Resource, marshal
from flask_pydantic import validate

from . import ns_cm, ns_am

from app.conocimiento.views import \
    update_concept

# Schemas and models
from .schemas import response_404_structure, \
    concept_list_response, concept_name, concept_response, \
    relation_list_response, relation_response, estructure, \
    answer_list, answer_response, answer_evaluation_request, answer_list_response
# Input models
from .models import ConceptRegister
from app.conocimiento.models import AnswerList, Concept, Relation, Structure

# Funcionalidades heredadas
# Conceptos
@ns_cm.route("/conceptos", endpoint='concept_list')
class ConceptList(Resource):
    @ns_cm.marshal_with(concept_list_response)
    def get(self):
        """Obtiene un listado con todos los conceptos de la base de datos"""
        concept_list, data = Concept.all()
        return data

@ns_cm.route("/concepto")
class ConceptCreate(Resource):
    # Valida la estructura del json
    @validate(body=ConceptRegister)
    # Valida el contenido del json
    @ns_cm.expect(concept_name)
    @ns_cm.marshal_with(concept_response)
    @ns_cm.response(400, 'Validation error: Estructura del json incorrecta', response_404_structure)
    def post(self):
        """Inserta un nuevo concepto en la base de conocimiento"""
        request_data = request.get_json()
        concept, response_data = Concept.save(request_data['nombre'])
        return response_data

@ns_cm.route("/concepto/<nombre>")
class ConceptManager(Resource):
    @ns_cm.marshal_with(concept_response)
    def get(self, nombre):
        """Busca un concepto dentro de la base de conocimiento y muestra los datos si existe"""
        concept, data = Concept.get(nombre)
        return data

    @validate(body=ConceptRegister)
    @ns_cm.expect(concept_name)
    @ns_cm.marshal_with(concept_response)
    @ns_cm.response(400, 'Validation error', response_404_structure)
    def put(self, nombre):
        """Actualiza un concepto buscandolo por nombre"""
        data = request.get_json()
        return update_concept(nombre, data)

    @ns_cm.marshal_with(concept_response)
    def delete(self, nombre):
        """Borra un concepto de la base de conocimiento buscandolo por nombre"""
        return Concept.delete(nombre)


# Relaciones
@ns_cm.route("/relaciones")
class RelationList(Resource):
    @ns_cm.marshal_with(relation_list_response)
    def get(self):
        """Devuelve todas las relaciones que contiene la base de conocimiento"""
        relation_list, data = Relation.all()
        return data


@ns_cm.route("/relacion/<nombre>")
class RelationGet(Resource):
    @ns_cm.marshal_with(relation_response)
    def get(self, nombre):
        """Busca una relación dentro de la base de conocimiento y muestra los datos si existe"""
        relation, data = Relation.get(nombre)
        return data


# Estructura
@ns_cm.route("/estructura")
class StructureCreate(Resource):
    @validate(body=Structure)
    @ns_cm.expect(estructure)
    @ns_cm.marshal_with(answer_response)
    @ns_cm.response(400, 'Validation error', response_404_structure)
    def post(self):
        """Inserta una nueva estructura en la base de conocimiento"""
        data = request.get_json()
        structure = Structure(**data)
        return structure.save()


# Respuesta
@ns_am.route("/respuesta/evaluar")
class ResponseEvaluate(Resource):
    @ns_am.expect(answer_evaluation_request)
    def post(self):
        """Evalúa a respuesta de un estudiante y devuelve la calificación"""
        pass


@ns_am.route("/respuesta/corregir")
class ResponseCorrect(Resource):
    def post(self):
        """Corrige ortograficamente una respuesta, separa los términos y los clasifica en conceptos y relaciones"""
        pass


# Nuevas funcionalidades
@ns_am.route("/respuesta/grabar")
class AnswersSave(Resource):
    @validate(body=AnswerList)
    @ns_am.expect(answer_list)
    @ns_am.marshal_with(answer_list_response)
    def post(self):
        """Inserta una lista de respuestas en forma de concepto-relacion-concepto en la base de datos
        devolviendo el resultado de cada operacion"""
        data = request.get_json()
        answer_list_object = AnswerList(**data)
        answer_list_response_object = answer_list_object.save()
        return answer_list_response_object
