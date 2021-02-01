from .ext import api
from flask_restx import fields

equivalence = api.model('Equivalence', {
    "peso": fields.Float,
    "nombre": fields.String
})

concept = api.model("Concept", {
    'id': fields.String,
    'nombre': fields.String,
    'equivalencias': fields.List(fields.Nested(equivalence))
})

data_concepts = api.model("ConceptDict", {
    "conceptos": fields.List(fields.Nested(concept))
})

concept_list = api.model('ConceptList', {
    "estado": fields.String(description="Estado", enum=['ok', 'error', 'no encontrado']),
    "mensaje": fields.String,
    "datos": fields.Nested(data_concepts)
})