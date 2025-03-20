import json

class FactoryPersistencia:
    @staticmethod
    def get_persistence_manager():
        return GestorPersistencia()

class GestorPersistencia:
    def save (self, nombre_fichero, objeto):
        fichero = open (nombre_fichero, mode='wt', encoding='utf-8')
        json.dump (objeto.to_dict(), fichero)
        fichero.close()
        
class Factura:
    def __init__ (self, numero, importe):
        self.numero = numero
        self.importe = importe
        self.__gestor_persistencia = FactoryPersistencia.get_persistence_manager()
        
    def save (self):
        self.__gestor_persistencia.save(str(self.numero) + '.txt', self)
    
    def to_dict(self):              # hay que sobreescribir este método para hacer serializable una instancia de la clase
        return {
            'numero': self.numero,
            'importe': self.importe
        }
    
   
        
f = Factura (104, 10_000)

f.save()