from flask import Blueprint
from flask_restx import Api

pysibila_v1_bp = Blueprint('pysibila_v1', __name__)
api = Api(pysibila_v1_bp, title="Pysibila",
          description="Pysibila es una api desarrollada en flask con el objetivo de permitir agregar nuevas funcionalidades a la api getaway en java, incorporar sus funcionalidades y eventualmente reemplazarla.",
          default="Metodos",
          default_label="")