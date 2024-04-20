'''
Código ejemplo de calificación productiva.
Aqui llamamos a la clase solicitud , le asignamos un identificador (el id solicitud a calificar)
y nos regresa un diccionario con los siguientes datos:
- id
- version: Versión del modelo que califico 
- calif: Probabilidad de default dado por su evaluación en el modelo
- group: Bin/Grupo al que pertenece la probabilidad de default 
- rejection: True si es rechazado por modelo, False si no es rechazado por modelo
'''

import class_definition

#Calificación de solicitudes
cliente_calificado=class_definition.solicitud(1615) #Actualizar con application_id que queramos calificar
resultado= cliente_calificado.califica_cliente()
print(resultado)

