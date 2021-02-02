from .ext import api
from flask_restx import fields

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
