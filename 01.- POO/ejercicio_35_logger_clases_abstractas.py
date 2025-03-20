'''
Crear un sistema de log basado en clases abstractas.
La clase abstracta dispondrá de un método concreto que generará el texto a dejar en el log
Las implementaciones del sistema de log serán: 
    Fichero
    BBDD 
    WebService

La decisión de elegir uno u otro sistema se hará a partir de la lectura de un fichero de configuración

'''
import abc
import datetime
from enum import Enum

class TipoLogger(Enum):
    FICHERO = "0"
    BBDD = "1"
    WEBSERVICE = "2"

class LoggerAbstract(abc.ABC): 
    def _generar_texto_log(self, mensaje):      
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{timestamp} --- {mensaje}"

    @abc.abstractmethod
    def log(self, mensaje):       
        pass

class LoggerFichero(LoggerAbstract):
    def log(self, mensaje):
        texto = self._generar_texto_log(mensaje)
      
        print(f"Log guardado en fichero: {texto}")

class LoggerBBDD(LoggerAbstract):
    def log(self, mensaje):
        texto = self._generar_texto_log(mensaje)
        print(f" · Guardando en la BBDD: {texto}") 

class LoggerWebService(LoggerAbstract):
    def log(self, mensaje):
        texto = self._generar_texto_log(mensaje)
        print(f" · Enviando log al WebService: {texto}") 

def obtener_logger_desde_config():
    try:
        with open("config.txt", "r") as fichero:
            tipo_logger = fichero.read().strip().upper()
            tipo_logger = TipoLogger(tipo_logger)  
    except (FileNotFoundError, ValueError):
        tipo_logger = TipoLogger.FICHERO  # damos un valor por defecto

    loggers = {
        TipoLogger.FICHERO: LoggerFichero,
        TipoLogger.BBDD: LoggerBBDD,
        TipoLogger.WEBSERVICE: LoggerWebService
    }
    
    return loggers[tipo_logger]()  

logger = obtener_logger_desde_config()
logger.log("Mensaje de prueba desde el logger.")