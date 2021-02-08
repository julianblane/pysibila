# Pysibila

Pysibila es una api desarrollada en flask con el objetivo de permitir agregar nuevas funcionalidades a la api getaway en java, incorporar sus funcionalidades y eventualmente reemplazarla.

# Entorno de pysibila (Sistema sibila)
![alt text](/documentacion/estructura_sibila.png)
# Estructura de pysibila
![alt text](/documentacion/estructura_pysibila.png)

# Modulos
## Conocimiento
Realiza la gestion de conceptos y relaciones y las
operaciones en la base de datos de OrientDB
### Models
Objetos del dominio definidos en app/conocimiento/models.py
![alt text](/documentacion/conocimiento/models_uml.png)

Para crear el diagrama ejecutar en consola:

        cd documentacion/conocimiento
        pyreverse ../../app/conocimiento/models.py
        dot -Tpng classes.dot > models_uml.png
        rm classes.dot
    
# Intalación y ejecución 

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

- Setear las vareables de entorno (para windows):

    -  Por consola:

            set FLASK_APP="entrypoint:app"
            set FLASK_ENV="development"
            set APP_SETTINGS_MODULE="config.default"

    - De forma permanente: 

         Agregar las lineas anteriores al archivo 'activate.bat' en la carpeta 'venv/Scripts'

- Activar el entorno virtual

- Correr el proyecto

        flask run


# Documentación
Se puede acceder a la documentación de la api en swagger en la url raiz

Documentacion de la api de java:
https://app.swaggerhub.com/apis/UTN-SIBILA/UTN-SIBILA/1.0.0#/

# Testing
La aplicación se puede probar desde la interfaz de swagger o ejecutando
los test unitarios en app/pysibila/api_v1/test/test.py. 
Esto permite realizar pruebas de extremo a extremo

Se debe verificar que se utilice la base local de prueba, esto se define cambiando 
la variable testing en el archivo: config/urls.py

Las pruebas de cada modulo se encuentran en el archivo test.py del 
respectivo modulo