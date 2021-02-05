from flask_restx import fields

from .ext import api

# Response 404
body_param = api.model('body_param', {
    "loc": fields.List(fields.String),
    "msg": fields.String,
    "type": fields.String,
})

body_params = api.model('body_params', {
    'body_params': fields.List(fields.Nested(body_param))
})

response_404 = api.model('Response404', {
    'validation_error': fields.Nested(body_params)
})

# Termino
term = api.model("Term", {
    'id': fields.String,
    'nombre': fields.String,
})

# Concepto
# ConceptList
equivalence = api.model('Equivalence', {
    "peso": fields.Float,
    "nombre": fields.String
})

concept = api.model("Concept", {
    'id': fields.String,
    'nombre': fields.String,
    'equivalencias': fields.List(fields.Nested(equivalence))
})

data_concepts = api.model("DataConcepts", {
    "conceptos": fields.List(fields.Nested(concept))
})

concept_list_response = api.model('ConceptListResponse', {
    "estado": fields.String(description="Estado", enum=['ok', 'error', 'no encontrado']),
    "mensaje": fields.String,
    "datos": fields.Nested(data_concepts)
})

# Single concept
data_concept = api.model("DataConcept", {
    "concepto": fields.Nested(concept)
})

concept_response = api.model('ConceptResponse', {
    "estado": fields.String(description="Estado", enum=['ok', 'error', 'no encontrado']),
    "mensaje": fields.String,
    "datos": fields.Nested(data_concept)
})

# ConceptCreate
concept_name = api.model("ConceptName", {
    "nombre": fields.String()
})


# Relaciones
relation = api.model('Relation', {
    "id": fields.String,
    "nombre": fields.String,
    "tipo": fields.String
})

data_relations = api.model("DataRelations", {
    "relaciones": fields.List(fields.Nested(relation))
})

relation_list_response = api.model("RelationListResponse", {
    "estado": fields.String(description="Estado", enum=['ok', 'error', 'no encontrado']),
    "mensaje": fields.String,
    "datos": fields.Nested(data_relations)
})

data_relation = api.model("DataRelation", {
    "relacion": fields.Nested(relation)
})

relation_response = api.model("RelationResponse", {
    "estado": fields.String(description="Estado", enum=['ok', 'error', 'no encontrado']),
    "mensaje": fields.String,
    "datos": fields.Nested(data_relation)
})


# Estructura
estructure = api.model("Structure", {
    "conceptoOrigen": fields.String,
    "conceptoDestino": fields.String,
    "relacion": fields.String
})


# Guardar respuesta
