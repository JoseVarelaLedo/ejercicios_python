# Decorador basado en un clase que deje un registro de log en:
# - Archivo
# - BD
# - WebService
from enum import Enum

class TipoPersistencia(Enum):
    FICHERO = 1
    BASE_DE_DATOS = 2
    WEB_SERVICE = 3

class GestorPersistenciaFichero:
    def write_log(self, mensaje):
        print('Escribiendo en fichero:', mensaje)

class GestorPersistenciaBD:
    def write_log(self, mensaje):
        print('Escribiendo en Base de Datos:', mensaje)

class GestorPersistenciaWebService:
    def write_log(self, mensaje):
        print('Escribiendo en Web Service:', mensaje)

class FactoryGestoresPersistencia:
    @staticmethod
    def get_gestor_persistencia(tipo_persistencia: TipoPersistencia):
        match tipo_persistencia:
            case TipoPersistencia.FICHERO:
                return GestorPersistenciaFichero()
            case TipoPersistencia.BASE_DE_DATOS:
                return GestorPersistenciaBD()
            case TipoPersistencia.WEB_SERVICE:
                return GestorPersistenciaWebService()
        raise ValueError("Tipo de persistencia no válido")

class GestorPersistencia:
    def __init__(self, tipo_de_persistencia: TipoPersistencia):
        self.tipo_de_persistencia = tipo_de_persistencia
        
    def __call__(self, funcion_a_decorar):
        def funcion_interna(*args, **kwargs):
            gestor_persistencia_elegido = FactoryGestoresPersistencia.get_gestor_persistencia(self.tipo_de_persistencia)
            if gestor_persistencia_elegido:
                gestor_persistencia_elegido.write_log(f"Llamando a la función {funcion_a_decorar.__name__} con args={args}, kwargs={kwargs}")
            return funcion_a_decorar(*args, **kwargs)
        return funcion_interna

@GestorPersistencia(TipoPersistencia.BASE_DE_DATOS)
def save(texto):
    print("Guardando desde la función a decorar con este argumento:", texto)
    return texto

save('Prueba de guardado con decoración')