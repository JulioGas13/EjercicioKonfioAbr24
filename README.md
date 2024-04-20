# EjercicioKonfioAbr24
Código productivo para Ejercicio Konfio realizado por Julio Gaspar

## Archivos:
- class_definition.py: Módulo donde definimos la clase "solicitud" la cual tiene un método para calificar las solicitudes con el modelo desarrollado.
- extraction_cleaning.py: Módulo donde se definen funciones para extraer la información necesaria para la calificación del modelo.
- transformation.py: Módulo donde se definen funciones para crear las variables input para el modelo.
- inference.py: Módulo donde se definen funciones para calificar la solicitud con el modelo.
- **ejecucion_productiva.py**: Código de ejecución, con el podemos calificar solicitudes (applicadion_id) con el modelo desarrollado.
- pipeline_final_f.konfio: Objeto serializado Pickle que contiene el modelo y la imputación de datos.
- requirements.txt: Archivo texto con información del versionamiento de Python y librerias dónde se desarrolló el código.

## Importante:
- En el módulo extraction_cleaning.py debe ser actualizada la variable **path_db** con la dirección de la carpeta donde se guarda la información internal_payments, external_features y credit_reports.
- En el módulo inference.py debe ser actualizada la variable **path** con la dirección de la carpeta donde está el objeto serializado pipeline_final_f.konfio.
- La solicitud (application_id) que puede ser calificada es aquella de la cual tenemos información (con datos en archivos internal_payments, external_features y credit_reports)
