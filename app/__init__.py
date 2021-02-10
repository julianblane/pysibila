from flask import Flask
from flask_restx import Api
from app.pysibila.api_v1.resources import ns_cm, ns_am


def create_app(settings_module):
    app = Flask(__name__, static_url_path='')
    app.config.from_object(settings_module)
    # TODO: poner en archivo de configuracion
    app.config['RESTX_MASK_SWAGGER'] = False
    app.testing = True

    api = Api(title="Pysibila",
              description="Pysibila es una api desarrollada en flask con el objetivo de permitir agregar nuevas funcionalidades a la api getaway en java, incorporar sus funcionalidades y eventualmente reemplazarla.",
              default="Metodos",
              default_label="",
              validate=False)

    api.add_namespace(ns_cm)
    api.add_namespace(ns_am)

    api.init_app(app)

    return app
