from flask_restx import Namespace

ns_cm = Namespace('ConceptManagement', description="Manejo de conceptos", path="/")
ns_am = Namespace('AnswerManagement', description="Manejo de respuestas", path="/")