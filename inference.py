'''
Código productivo para calificar con el modelo serializado.

Notas:
- Se utiliza el modelo serializado pipeline_final_f.konfio oara calificar, este se encuentra en la carpeta definida en path.
- En producción la dirección del path puede ser suprimida si archivos se encuentran en la misma carpeta
'''

#Declaraciones globales
path=r"C:\Users\Julio\Documents\Aprendizaje\Ciencia de datos\Ejercicio Konfio\Produccion" #Dirección general donde estan contenidos los modelos productivos 
test_konfio_model='pipeline_final_f.konfio' #Nombre del modelo productivo
from  pickle import load

def califica_modelo(vars,vars_keep,modelo):
    '''
    Función para calificar con el modelo requerido, estimar su probabilidad y regresar este valor
    '''
    try:
        with open(path+r"/"+modelo, "rb") as m:
            _pipe = load(m)
            prob_pred = _pipe.predict_proba(vars[vars_keep])[:, 1] [0]
        return prob_pred
    except:
        print ('No es posible encontrar el objeto modelo: ',modelo)
        
def retorno_mod_test_konfio_model(prob=-100):
    '''
    Función para crear el diccionario de retorno particularizado según el modelo
    '''
    if prob==-100: #Regresamos valores estandar si no se pudo calificar
        print('No fue posible calificar al cliente')
        version='vRetoKonfio'
        calif=-1
        group= -1
        rejection = False 
        return version,calif,group,rejection
    else: #Regresamos versiones y grupos ajustados por calificación
        version='vRetoKonfio'
        calif=prob
        group=1 if prob<=0.379 else 3 if prob>0.387 else 2 
        rejection = True if prob>0.387 else False 
        return version,calif,group,rejection

def main(id, vars):
    '''
    Función de llamada principal
    '''
    #print("[Inference] Start")
    if len(vars)==1:
        pred_modelo=calif_modelo=califica_modelo(vars,['IP_CREDS_PREVIOS','IP_NUM_PAGOS_ATRASADOS','IP_PCT_PAGO_PUNTUAL','CR_SUM_MONTO_A_PAGAR','CR_MAX_MONTO_MOROSO','DEFAULTED_ACCOUNTS_3M_OVER_12M_EXCLUSIVE'],test_konfio_model) #Calificamos con el modelo
        return retorno_mod_test_konfio_model(pred_modelo) #Regresamos la salida esperada (detalles de  la calificación)
    else:
        print('No es posible calcular la calificación del cliente:' , id)
        
