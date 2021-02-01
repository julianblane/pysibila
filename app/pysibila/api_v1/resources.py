from flask_restx import Resource
from .schemas import concept_list
from .ext import api, pysibila_v1_bp

from app.conocimiento.views import get_concepts

@api.route("/conceptos")
class ConceptList(Resource):
    @api.marshal_with(concept_list)
    def get(self):
        return get_concepts()

@api.route("/concepto")
class ConceptCreate(Resource):
    def post(self):
        pass

# @api.route("/concepto/<nombre>")
# class ConceptManager(Resource):
#     def get(self, nombre):
#         pass
#     def put(self, nombre):
#         pass
#     def delete(self, nombre):
#         pass

# POST/concepto
# GET/concepto/{nombre}
# PUT/concepto/{nombre}
# DELETE/concepto/{nombre}
# GET/relaciones
# GET/relacion/{nombre}
# POST/estructura
# POST/respuesta/evaluar
# POST/respuesta/corregir