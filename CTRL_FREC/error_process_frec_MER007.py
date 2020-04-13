#!/drbd/www/cgi-bin/spx/aut_env/bin/python3.6

'''
Created on 8 mar. 2020

@author: Yosniel Cabrera
'''

## LIBRERIAS
import os                                                   

## CONEXIONES
from mypython import lst2str
from time import time 

  
gen_start_time = time()  
                                             

LIST_CONFIG = [
                #VARIABLES DE EJECUCION
                'print_log',        True,                           # VER LOS LOGS EN CONSOLA [ True | False ]
                'DLGID',            'MER007',                       # ID DATALOGGER QUE EJECUTA LAS ACCIONES DE CONTROL
                'TYPE',             'FREC',                         # CUANDO TIENE LE VALOR CHARGE SE CARGA LA CONFIGURACION DE LA db
                
                
                #VARIABLES DE CONFIGURACION
                'SWITCH_OUTPUTS',   False,                          # ALTERNA LAS SALIDAS Y TESTEA QUE LAS ENTRADAS LAS SIGAN [ True | False]
                'EVENT_DETECTION',  False,                          # FORMA EN QUE EL VARIADOR DE VELOCIDAD DETECTA LAS ENTRADAS [ NPN (not_in)| PNP] 
               
            ]






# CONVIERTO A STRIG
STR_CONFIG = lst2str(LIST_CONFIG)
#
# OBTENER LA CARPETA ANTERIOR A LA DE LA RUTA DEL ARCHIVO
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# LLAMADO DEL PROGRAMA 
os.system('{0}/serv_error_APP_selection.py {1}'.format(file_path,STR_CONFIG)) 
#os.system('{0}/serv_APP_selection.py'.format(file_path)) 
#
# CALCULO TIEMPO DE DEMORA
#print(f'control_process_frec_{LIST_CONFIG[3]} TERMINADO A {time()-gen_start_time} s')



###