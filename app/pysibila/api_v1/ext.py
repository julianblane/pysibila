from flask import Blueprint
from flask_restx import Api

pysibila_v1_bp = Blueprint('pysibila_v1', __name__)
api = Api(pysibila_v1_bp)