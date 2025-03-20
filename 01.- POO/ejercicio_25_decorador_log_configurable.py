# Crear un decorador que deje registro de log que permita indicar en dónde:
# - Fichero
# - Base de datos
# - WebService

# LOG_FILE_NAME = 'log.json'

# def escribir_log(*textos:str):
#     with open(LOG_FILE_NAME, mode='at') as fichero:
#         for texto in textos[:-1]:
#             fichero.write(texto + ',')
#         fichero.write(textos[-1])
#         fichero.write('\n')

# def logger(opcion: str):                                                         # primer nivel de anidamiento, para recibir el parámetro
#     def external_wrapper (funcion):                                              # segundo nivel, recibe la función a decorar
#         def internal_wrapper (*args, **kwargs):                                  # tercer nivel, recibe los argumentos de la función a decorar
#             #print (f'Se va a guardar usando la opción de {opcion}')    
#             # Se haría con if, la línea anterior es de prueba:
#             if ( opcion == ' Fichero'):
#                 print ('Salvando a fichero')
#                 escribir_log ('Salvando a fichero')
#             elif (opcion == 'Base de Datos'):
#                 print ("Salvando a Base de Datos")
#                 escribir_log ('Salvando a Base de Datos')
#             else:
#                 print ('Salvando a WebService')
#                 escribir_log ('Salvando a Web Service')

#             resultado = funcion (*args, **kwargs)
#             return resultado                                                    # los return van siguiendo el orden inverso de anidamiento
#         return internal_wrapper                                                 # se devuelve la función, si hacemos esto return internal_wrapper(), devolvería el resultado
#     return external_wrapper

# @logger('Base de Datos')
# def save():
#     print('Llamando a función')

# save()



# SOLUCIÓN PROFESOR

from enum import Enum

class TipoPersistencia (Enum):
    FICHERO         = 1
    BASE_DE_DATOS   = 2
    WEB_SERVICE     = 3

class GestorPersistenciaFichero:
    def write_log(self, mensaje):
        print ('Escribiendo en fichero', mensaje)
        
class GestorPersistenciaBD:
    def write_log(self, mensaje):
        print ('Escribiendo en Base de Datos', mensaje)
        
class GestorPersistenciaWebService:
    def write_log(self, mensaje):
        print ('Escribiendo en Web Service', mensaje)
    
    
class FactoryGestoresPersistencia:
    @staticmethod
    def get_gestor_persistencia (tipo_persistencia):
        match tipo_persistencia:
            case TipoPersistencia.FICHERO:
                return GestorPersistenciaFichero()
            case TipoPersistencia.BASE_DE_DATOS:
                return GestorPersistenciaBD()
            case TipoPersistencia.WEB_SERVICE:
                return GestorPersistenciaWebService()

class GestorPersistencia:
    def write_log (self, tipo_persistencia: TipoPersistencia, mensaje):
        FactoryGestoresPersistencia.get_gestor_persistencia (tipo_persistencia).write_log (mensaje)
        


def superlogger (tipo_persistencia: TipoPersistencia):
    def external_wrapper (funcion_a_decorar):
        def internal_wrapper (*args, **kwargs):
            GestorPersistencia().write_log(tipo_persistencia, ' texto a escribir en el log')                
            return funcion_a_decorar(*args, **kwargs)
        return internal_wrapper
    return external_wrapper

@superlogger(tipo_persistencia = TipoPersistencia.WEB_SERVICE)
def sumar (s1, s2):
    return s1 +s2

print (sumar(6,7))
    
                
        