from flask import Flask
# from app.pysibila.api_v1 import pysibila_v1_bp
from app.pysibila.api_v1.ext import pysibila_v1_bp 

def create_app(settings_module):
    app = Flask(__name__, static_url_path='')
    app.config.from_object(settings_module)
    app.testing = True

    app.register_blueprint(pysibila_v1_bp)

    return app