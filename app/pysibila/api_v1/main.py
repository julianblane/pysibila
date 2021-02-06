from flask_restx import fields, Model
from app.utils.dict_format_compare.dict_format_compare import compare

# concept_name = Model("ConceptName", {
#     "nombre": fields.String()
# })
# concept_example_2 = {
#     'nombre1': "nombre",
# }
# print(concept_name._schema['properties'])
# print(compare(concept_name._schema['properties'], concept_example_2))
#
# print(type(concept_name))
#
#
v = [1,2,3,4,5,6,7,8,9]
print(v[::2])