# Pysibila

Pysibila es una api desarrollada en flask con el objetivo de permitir agregar nuevas funcionalidades a la api getaway en java, incorporar sus funcionalidades y eventualmente reemplazarla.

# Entorno de pysibila (Sistema sibila)
![alt text](/documentacion/estructura_sibila.png)
# Estructura de pysibila
![alt text](/documentacion/estructura_pysibila.png)
# Ejecución 

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


# Documentación
Se puede acceder a la documentación de la api con la url raiz

Documentacion de la api de java:
https://app.swaggerhub.com/apis/UTN-SIBILA/UTN-SIBILA/1.0.0#/