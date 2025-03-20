import abc
import csv
import pickle
import json
from enum import Enum

class TipoPersistencia (Enum):
    PICKLE  =   1
    JSON    =   2
    CSV     =   3
    

class GestorPersistencia(abc.ABC):
    @abc.abstractmethod
    def create(self, id, obj):
        pass

    @abc.abstractmethod
    def read(self, id):
        pass

    # @abc.abstractmethod
    # def update(self, id, obj):
    #     pass

    # @abc.abstractmethod
    # def delete(self, obj):
    #     pass


class GestorPersistenciaPickle(GestorPersistencia):
    EXTENSION = '.pickle'

    @classmethod
    def __get_file_name(cls, id):
        return str(id).replace(' ', '_').lower()+cls.EXTENSION

    def create(self, id, obj):
        nombre_fichero = GestorPersistenciaPickle.__get_file_name(id)
        with open(nombre_fichero, mode = 'wb') as archivo:
            pickle.dump(obj, archivo)

    def read(self, id):
        nombre_fichero = GestorPersistenciaPickle.__get_file_name(id)
        with open(nombre_fichero, mode = 'rb') as archivo:
            objeto = pickle.load(archivo)
        return objeto
    

'''
Crear otra implementación de GestorPersistencia:
json, ficheros planos con delimitadores, csv,...
'''
    
class GestorPersistenciaJSON(GestorPersistencia):
    EXTENSION = '.json'

    @classmethod
    def __get_file_name(cls, id):
        return str(id).replace(' ', '_').lower() + cls.EXTENSION

    def create(self, id, obj):
        nombre_fichero = self.__get_file_name(id)
        with open(nombre_fichero, 'w', encoding='utf-8') as archivo:
            json.dump(obj.__dict__, archivo, ensure_ascii=False, indent=4)

    def read(self, id):
        nombre_fichero = self.__get_file_name(id)
        try:
            with open(nombre_fichero, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return None


class GestorPersistenciaCSV(GestorPersistencia):
    EXTENSION = '.csv'

    @classmethod
    def __get_file_name(cls, id):
        return str(id).replace(' ', '_').lower() + cls.EXTENSION

    def create(self, id, obj):
        nombre_fichero = GestorPersistenciaCSV.__get_file_name(id)      
        atributos = vars(obj) if hasattr(obj, '__dict__') else obj
        
        try:           
            with open(nombre_fichero, mode='r', newline='', encoding='utf-8') as archivo:               
                existe_fichero = True
        except FileNotFoundError:         
            existe_fichero = False        
     
        with open(nombre_fichero, mode='a', newline='', encoding='utf-8') as archivo:
            csv_writer = csv.writer(archivo)
            if not existe_fichero:              
                csv_writer.writerow(atributos.keys()) 
            csv_writer.writerow(atributos.values()) 

    def read(self, id):
        nombre_fichero = GestorPersistenciaCSV.__get_file_name(id)        
        try:
            with open(nombre_fichero, mode='r', newline='', encoding='utf-8') as archivo:
                csv_reader = csv.DictReader(archivo)
                for fila in csv_reader:
                    if fila['titulo'].lower() == id.lower():  
                        return fila 
        except FileNotFoundError:           
            return None
        return None



class GestorPersistenciaFactory:
    NOMBRE_FICHERO = 'ejercicio_48_config.json'
    @staticmethod
    def get_gestor_persistencia() -> GestorPersistencia:
        with open (GestorPersistenciaFactory.NOMBRE_FICHERO, 'rt') as archivo:
            configuracion = json.load (archivo)        
            tipo_persistencia = TipoPersistencia(configuracion['TIPO_PERSISTENCIA'])
        
            match  tipo_persistencia:
                case TipoPersistencia.PICKLE:
                    return GestorPersistenciaPickle()
                case TipoPersistencia.JSON:
                    return GestorPersistenciaJSON()
                case TipoPersistencia.CSV:
                    return GestorPersistenciaCSV()
                case _:
                    raise ValueError("Tipo de persistencia no soportado. Hay que usar 'pickle', 'json' o 'csv'.")
   

