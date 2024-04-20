'''
Código productivo para extracción de datos para calificación de modelo

Notas:
-Para el ejercicio se extraen los datos desde csv's lo que crea la necesidad de crear direcciones a los folders donde
se encontraran los archivos con la data.
- En producción la dirección puede ser suprimida y las extracciones pueden manejarse como lectura de BDD en SQL.
'''

#Declaraciones globales
path_db=r"C:\Users\Julio\Documents\Aprendizaje\Ciencia de datos\Ejercicio Konfio\konfio_challenge_top_up\datasets" #Dirección general donde estan contenidas las fuentes de datos a utilizar
internal_payments="internal_payments.csv" #Nombre del archivo con información de internal payments
external_features="external_features.csv" #Nombre del archivo con información de external features
credit_reports="credit_reports.csv" #Nombre del archivo con información de credit reports
import pandas as pd

def extrae(id,tipo):
    '''
    Función para extraer la información a nivel ID
    '''
    try:
        bdd=pd.read_csv(path_db+r"/"+tipo)
        bdd=bdd[bdd['application_id']==id] #Filtramos con el id de interés
        #Transformación de variables (en este caso solo debemos convertir las fechas a un formato correcto, pero en dado caso de necesitar mas transformaciones se iran agregando.
        # En caso de necesitar transformaciones particulares, por ej. que se tenga que cambiar el formato de una columna solo en un bdd particular, se ajusta de manera particular.)
        for col in bdd.columns:
            if 'date' in col:
                bdd[col]=pd.to_datetime(bdd[col], format='%Y%m%d %H:%M:%S')   
        return bdd #Regresamos la BDD transformada
    
    except:
        print ('Error al extraer Data')

def main(id=-1):
    '''
    Función de llamada principal
    '''
    #print("[Extract] Start")
    if id>0:
    #Extraemos la información de las distintas fuentes de datos declaradas
        bdd_ip=extrae(id,internal_payments) 
        bdd_ef=extrae(id,external_features)
        bdd_cr=extrae(id,credit_reports)
        #print(f"[Extract] End")
        return [bdd_ip,bdd_ef,bdd_cr] #Regresamos los datos como una lista, donde los indices nos serviran para tomar las bdd requeridas
    else:
        print('Sin id proporcionado o no valido')
    