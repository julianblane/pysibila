from flask import Flask

def create_app(settings_module):
    app = Flask(__name__, static_url_path='')
    app.config.from_object(settings_module)
    app.testing = True

    return app
