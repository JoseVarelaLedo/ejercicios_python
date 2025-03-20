class Madre:
    SUPER_CAPACIDAD_MAXIMA = 1000

class GestorGrupo (Madre):
    
    CAPACIDAD_MAXIMA = 50       # Variable o atributo DE CLASE
    
    def __init__(self, nombre, url):
        self.nombre = nombre    # Variable o atributo DE INSTANCIA
        self.url = url
        
    def mostrar_nombre (self):  # Método DE INSTANCIA, recibe self, que es una referencia al propio objeto o instancia
        print (self.nombre)
        
    @classmethod
    def duplicar_capacidad (cls):   # Método DE CLASE, usar cls es una convención, podría ser cualquier otra palabra, lo que importa es que recibe la clase como parámetro
        print ("Heredando en classmethod",cls.SUPER_CAPACIDAD_MAXIMA)
        print ('Capacidad antes de duplicar:', cls.CAPACIDAD_MAXIMA)
        cls.CAPACIDAD_MAXIMA *= 2
        print ('Capacidad después de duplicar:', cls.CAPACIDAD_MAXIMA)
        
    @staticmethod
    def get_informacion():
        print ("Heredando en staticmethod",GestorGrupo.SUPER_CAPACIDAD_MAXIMA)
        print ('Esto es un grupo')

grupo = GestorGrupo ('Python Coruña', 'https://linktr.ee/pythoncoruna')


GestorGrupo.duplicar_capacidad()    # Ambos funcionan, y modifican el valor para todos los objetos
grupo.duplicar_capacidad()          # porque se puede llamar a un método de clase desde una instancia, pero no al revés
                                    # si no fuese @classmethod, y llamásemos a GestorGrupo.duplicar_capacidad() daría error 
GestorGrupo.get_informacion()