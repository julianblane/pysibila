# pysibila

# Ejecucion 

- Crear un entorno virtual con virtualenv para python3

- Instalar las librerias: 

        pip install -r requirements.txt

- Setear las vareables de entorno (para linux):

    -  Por consola:

            export FLASK_APP="entrypoint:app"
            export FLASK_ENV="development"
            export APP_SETTINGS_MODULE="config.default"

    - De forma permanente: 

         Agregar las lineas anteriores al archivo 'activate' en la carpeta 'venv/bin'

- Correr el proyecto

        flask run


# Documentacion
Se puede acceder a la documentación de la api con la url_ /docs

Para que la documentacion este disponible, se debe configurar el entorno
como testing cambiando la flag app.testing=false en el archivo:

    app/__init__.py
