'''
Código productivo para transformación  de datos para calificación de modelo

Notas:
- Se crean las variables necesarias para calificar el modelo realizado para este ejercicio.
- Las funciones de transformación son particulares por tipo de dato
'''

#Declaraciones globales
import pandas as pd 
import numpy as np

def transforma_ip(bdd):
    '''
    Función para transformar variables de bdd Internal Payments
    '''
    if len(bdd)==0:
        return pd.DataFrame()
    else:
        #Creamos variables a nivel cliente
        #Trabajo previo con BDD internal_payments
        bdd['dias_atraso']=(bdd['completed_date']-bdd['payment_date']).dt.days #Variable de diferencia de dias entre fecha a pagar y fecha pago
        bdd['tipo_pago']= np.where((bdd['dias_atraso']<0) , 'Adelantado', 'No adelantado') #Variable de clasificación de pago en adelantado o no adelantado
        bdd['tipo_pago_atr']= np.where((bdd['dias_atraso']>0) , 'Atrasado', 'No atrasado') #Variable de clasificación de pago en atrasado o no atrasado

        #Creación de variables
        bdd_agg=bdd[['application_id']].drop_duplicates() 
        bdd_agg['IP_CREDS_PREVIOS']=bdd[bdd['current_loan']!=1]['prev_loan_id'].nunique()
        bdd_agg['IP_MAX_ATRASO']=bdd['dias_atraso'].max()
        bdd_agg['IP_NUM_PAGOS']=len(bdd)
        bdd_agg['IP_NUM_PAGOS_ATRASADOS']=len(bdd[bdd['tipo_pago_atr']=='Atrasado'])

        #Ajustes a variables
        bdd_agg['IP_CREDS_PREVIOS']=bdd_agg['IP_CREDS_PREVIOS'].fillna(0) #Si es vacio significa que su crédito actual es el unico que esta en la BDD de internal Payment
        bdd_agg['IP_NUM_PAGOS_ATRASADOS']=bdd_agg['IP_NUM_PAGOS_ATRASADOS'].fillna(0) #Si es vacio significa que no tiene pagos atrasados
        bdd_agg['IP_MAX_ATRASO']=np.where((bdd_agg['IP_MAX_ATRASO']<0), 0, bdd_agg['IP_MAX_ATRASO'])#Si es negativo lo forzamos a que sea 0, ya que la variable representa atraso
        bdd_agg['IP_PCT_PAGO_PUNTUAL']=(bdd_agg['IP_NUM_PAGOS']-bdd_agg['IP_NUM_PAGOS_ATRASADOS'])/bdd_agg['IP_NUM_PAGOS'] #Si es negativo lo forzamos a que sea 0, ya que la variable representa atraso  (bdd_agg['IP_NUM_PAGOS']-bdd_agg['IP_NUM_PAGOS_ATRASADOS'])/bdd_agg['IP_NUM_PAGOS']

        return bdd_agg
        
def transforma_ef(bdd):
    '''
    Función para transformar variables de bdd external_features
    '''
    if len(bdd)==0:
        return pd.DataFrame()
    else:
        #Creamos variables a nivel cliente
        bdd['FLAG_DEFAULTED_ACCOUNTS_3M']= np.where((bdd['DEFAULTED_ACCOUNTS_3M_OVER_12M_INCLUSIVE']>0) | (bdd['DEFAULTED_ACCOUNTS_3M_OVER_12M_EXCLUSIVE']>0) , 1, 0) 
        return bdd
        
def transforma_cr(bdd):
    '''
    Función para transformar variables de bdd bdd
    '''
    if len(bdd)==0:
        return pd.DataFrame()
    else: 
        #Creamos variables a nivel cliente
        bdd_agg=bdd[['application_id']].drop_duplicates()
        bdd_agg['CR_NUM_CUENTAS']=len(bdd)
        bdd_agg['CR_NUM_CUENTAS_A']=len(bdd[bdd['account_closing_date'].isna()==True])
        bdd_agg['CR_NUM_CUENTAS_C']=len(bdd[bdd['account_closing_date'].isna()==False])
        bdd_agg['CR_SUM_MONTO_A_PAGAR']=bdd['amount_to_pay_next_payment'].sum()
        bdd_agg['CR_MAX_MONTO_MOROSO']=bdd['worst_delinquency_past_due_balance'].max() #Creamos las variables para el modelo

        #Ajustes a variables
        bdd_agg['CR_NUM_CUENTAS_A']=bdd_agg['CR_NUM_CUENTAS_A'].fillna(0) #Si es vacio significa que no tiene cuentas activas
        bdd_agg['CR_NUM_CUENTAS_C']=bdd_agg['CR_NUM_CUENTAS_C'].fillna(0) #Si es vacio significa que no tiene cuentas cerradas
        
        return bdd_agg
        
def main(id,lista_df):
    '''
    Función de llamada principal
    '''
    #print("[Transformation] Start")
    
    vars_ip=transforma_ip(lista_df[0]) #Transformación de BDD internal_payments
    vars_ef=transforma_ef(lista_df[1]) #Tranformación de BDD external features
    vars_cr=transforma_cr(lista_df[2]) #Transformación de BDD credit report
    
    #Creamos df con información de variables 
    vars=pd.DataFrame([id],columns=['application_id'])
    vars=vars.merge(vars_ip,how='left',on='application_id')
    vars=vars.merge(vars_ef,how='left',on='application_id')
    vars=vars.merge(vars_cr,how='left',on='application_id')
    vars.drop('application_id',axis=1)
    if len(vars)==1:
        #print('Transformación completa. -' )
        return vars
    elif len(vars)>1:
        print('Multiples registros con el mismo application_id. - ',id)
        return pd.DataFrame()
    else:
        print('Información no localizada. No es posible construir variables. -',id)
        return pd.DataFrame()
    