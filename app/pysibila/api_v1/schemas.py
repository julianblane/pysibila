from flask_restx import fields

from . import ns_cm, ns_am

ESTADO_ENUM = ['ok', 'error', 'no encontrado']
TERM_TIPO_ABV_ENUM = ['C', 'R', '']

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
    "estado": fields.String(description="Estado", enum=ESTADO_ENUM),
    "mensaje": fields.String,
    "datos": fields.Nested(data_concepts)
})

# Single concept
data_concept = ns_cm.model("DataConcept", {
    "concepto": fields.Nested(concept)
})

concept_response = ns_cm.model('ConceptResponse', {
    "estado": fields.String(description="Estado", enum=ESTADO_ENUM),
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
    "estado": fields.String(description="Estado", enum=ESTADO_ENUM),
    "mensaje": fields.String,
    "datos": fields.Nested(data_relations)
})

data_relation = ns_cm.model("DataRelation", {
    "relacion": fields.Nested(relation)
})

relation_response = ns_cm.model("RelationResponse", {
    "estado": fields.String(description="Estado", enum=ESTADO_ENUM),
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
    "estado": fields.String(description="Estado", enum=ESTADO_ENUM),
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

calification_dict = ns_am.model("CalificationDict", {
    "calificacion": fields.Float(description="Calificacion")
})

answer_evaluation_response = ns_am.model("AnswerEvaluateResponse", {
    "estado": fields.String(description="Estado", enum=ESTADO_ENUM),
    "mensaje": fields.String,
    "datos": fields.Nested(calification_dict)
})

answer_correction_request = ns_am.model('AnswerCorrectRequest', {
    'respuesta': fields.String(description="Respuesta")
})

answer_correction_error = ns_am.model("AnswerCorrectError", {
    "error": fields.Boolean(description="Es un termino ortograficacmente incorrecto"),
    "sugerencias": fields.List(fields.String, description="Sugerencias de correcciones")
})

answer_correction_term = ns_am.model('AnswerCorrectTerm', {
    "error": fields.Nested(answer_correction_error),
    "tipo": fields.String(description="Tipo de termino", enum=TERM_TIPO_ABV_ENUM),
    "sugerenciaTipo": fields.String(description="Tipo de termino", enum=TERM_TIPO_ABV_ENUM),
    "nombre": fields.String(description="Termino")
})

answer_correction_response = ns_am.model('AnswerCorrectResponse', {
    "estado": fields.String(description="Estado", enum=ESTADO_ENUM),
    "mensaje": fields.String,
    "datos": fields.List(fields.Nested(answer_correction_term))
})
