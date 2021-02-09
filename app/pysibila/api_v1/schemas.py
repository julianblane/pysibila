from flask_restx import fields, Model

from . import ns_cm, ns_am

# Response 404
body_param = ns_cm.model('body_param', {
    "loc": fields.List(fields.String),
    "msg": fields.String,
    "type": fields.String,
})

body_params = ns_cm.model('body_params', {
    'body_params': fields.List(fields.Nested(body_param))
})

response_404_structure = ns_cm.model('Response404Structure', {
    'validation_error': fields.Nested(body_params)
})
response_404_content_errors = ns_cm.model('Response404ContentErrors', {
    "field": fields.String
})

response_404_content = ns_cm.model('Response404Content', {
    "errors": fields.Nested(response_404_content_errors),
    "message": fields.String
})


# Concepto
# ConceptList
equivalence = ns_cm.model('Equivalence', {
    "peso": fields.Float,
    "nombre": fields.String
})

concept = ns_cm.model("Concept", {
    'id': fields.String,
    'nombre': fields.String,
    'equivalencias': fields.List(fields.Nested(equivalence))
})

data_concepts = ns_cm.model("DataConcepts", {
    "conceptos": fields.List(fields.Nested(concept))
})

concept_list_response = ns_cm.model('ConceptListResponse', {
    "estado": fields.String(description="Estado", enum=['ok', 'error', 'no encontrado']),
    "mensaje": fields.String,
    "datos": fields.Nested(data_concepts)
})

# Single concept
data_concept = ns_cm.model("DataConcept", {
    "concepto": fields.Nested(concept)
})

concept_response = ns_cm.model('ConceptResponse', {
    "estado": fields.String(description="Estado", enum=['ok', 'error', 'no encontrado']),
    "mensaje": fields.String,
    "datos": fields.Nested(data_concept)
})

# ConceptCreate
concept_name = ns_cm.model("ConceptName", {
    "nombre": fields.String()
})


# Relaciones
relation = ns_cm.model('Relation', {
    "id": fields.String,
    "nombre": fields.String,
    "tipo": fields.String
})

data_relations = ns_cm.model("DataRelations", {
    "relaciones": fields.List(fields.Nested(relation))
})

relation_list_response = ns_cm.model("RelationListResponse", {
    "estado": fields.String(description="Estado", enum=['ok', 'error', 'no encontrado']),
    "mensaje": fields.String,
    "datos": fields.Nested(data_relations)
})

data_relation = ns_cm.model("DataRelation", {
    "relacion": fields.Nested(relation)
})

relation_response = ns_cm.model("RelationResponse", {
    "estado": fields.String(description="Estado", enum=['ok', 'error', 'no encontrado']),
    "mensaje": fields.String,
    "datos": fields.Nested(data_relation)
})


# Estructura
estructure = ns_cm.model("Structure", {
    "conceptoOrigen": fields.String,
    "conceptoDestino": fields.String,
    "relacion": fields.String
})


# Guardar respuesta
# Entrada
# Termino
term = ns_am.model("Term", {
    'nombre': fields.String(example='pysibila_concepto_prueba'),
    'tipo_termino': fields.String(enum=['concepto', 'relacion']),
})

answer = ns_am.model("Answer", {
    'terminos': fields.List(fields.Nested(term)),
})

answer_list = ns_am.model("AnswerList", {
    'respuestas': fields.List(fields.Nested(answer),
                              example=[
                                  {
                                      "terminos": [
                                          {
                                              "nombre": "pysibila_concepto_prueba",
                                              "tipo_termino": "concepto"
                                          },
                                          {
                                              "nombre": "pysibila_concepto_prueba",
                                              "tipo_termino": "relacion"
                                          },
                                          {
                                              "nombre": "pysibila_concepto_prueba",
                                              "tipo_termino": "concepto"
                                          },
                                      ]
                                  }
                              ]
                              ),
})

# Salida
answer_response = ns_am.model('AnswerResponse', {
    "estado": fields.String(description="Estado", enum=['ok', 'error', 'no encontrado']),
    "mensaje": fields.String,
    "datos": fields.List(fields.Nested(term))
})

answer_list_response = ns_am.model('AnswerListResponse', {
    'respuestas': fields.List(fields.Nested(answer_response))
})

# answers
answer_evaluation_request = ns_am.model("AnswerEvaluateRequest", {
    "respuestaBase": fields.String(description="Respuesta profesor"),
    "respuestaAlumno": fields.String(description="Respuesta alumno")
})