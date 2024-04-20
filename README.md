# EjercicioKonfioAbr24
Código de solución de Ejercicio Konfio realizado por Julio Gaspar

## Contenido:
- class_definition.py: Módulo donde definimos la clase "solicitud" la cual tiene definido un método para calificarlas solicitudes con el modelo desarrollado.
- extraction_cleaning.py: Módulo donde se definen funciones para extraer la información necesaria para la calificación de modelos.
- transformation.py: Módulo donde se definen funciones para crear las variables input para los modelos.
- inference.py: Módulo donde se definen funciones para calificar con el modelo desarrollado.
- ejecucion_productiva.py: Código de ejecución, con el podemos calificar solicitudes (applicadion_id) con el modelo desarrollado.
- pipeline_final_f.konfio: Objeto serializado Pickle que contiene el modelo y la imputación de datos elegido.
- requirements.txt: Archivo texto con información del versionamiento de Python y librerias en el dónde se desarrolló el código.

## Importante:
- En el módulo extraction_cleaning.py debe ser actualizada la variable *path_db* con la dirección de la carpeta donde se guarda la información internal_payments, external_features y credit_reports.
- En el módulo inference.py debe ser actualizada la variable *path* con la dirección de la carpeta donde está el objeto serializado pipeline_final_f.konfio.
