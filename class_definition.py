'''
Definición de clase productiva solicitud, la cual tendra como uno de sus métodos la calificación de la misma
'''
#Definiciones globales
import extraction_cleaning #Código para extracción de datos
import transformation #Código para tranformación de datos
import inference #Código para calificación con moedlo

class solicitud(): #Clase declarada para manejar al cliente
    def __init__(self, id):
        self.id=id #id del cliente 
        self.calif=-1 #Calificación arrojada por el modelo
        self.rejection=False #Decreto dado por el modelo
        self.group=-1 #Grupo asignado por el modelo 
        self.version='ND' #Versión del modelo por la cual se califico
        
    def califica_cliente(self):
        '''
        Método que servira para calificar al cliente
        '''
        try:
            # Extracción de datos
            bbdd=extraction_cleaning.main(self.id) 
            # Tranformación de datos
            bdd_t=transformation.main(self.id,bbdd)
            # calificación por modelo
            self.version,self.calif,self.group,self.rejection =inference.main (self.id,bdd_t)
            
            return {'id':self.id,
                    'version':self.version,
                    'prob':self.calif,
                    'group':self.group,
                    'rejection':self.rejection
                    } #Regresamos un diccionario con los datos de la calificación
        except:
            print('Error en calificación')
