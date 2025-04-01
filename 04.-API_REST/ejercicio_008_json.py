import json

# Función dumps: convertir un objeto a json (no siempre)
# Función dump: convierte un objeto a son (no siempre) y lo almacena en un fichero
texto_normal = "Este texto es normal"
print (json.dumps(texto_normal)) # Salida: "Este texto es normal"


texto_raro = "Este texto no es \"normal\""
print (json.dumps(texto_raro)) # Salida: "Este texto no es \"normal\""

numero = 1_900
print (json.dumps(numero))  # Salida: 1900

diccionario = {'nombre': 'Python', 'tipo': 'Multiparadigma'}
print (json.dumps(diccionario)) 
# Salida: {"nombre": "Python", "tipo": "Multiparadigma"} OJO AL CAMBIO DE LAS COMILLAS, DE SIMPLES A DOBLES

tupla = ('Primavera', 'Verano', 'Otoño', 'Invierno')
print(json.dumps(tupla)) 
# Salida: ["Primavera", "Verano", "Oto\u00f1o", "Invierno"] OJO -> Convierte tupla a array, que es el tipo que existe en JSON

precio_justo = True
print (json.dumps(precio_justo)) # Salida: true OJO -> lo pasa a minúscula

valor = None
print (json.dumps(valor)) # Salida: null OJO-> convierte a null

# Si queremos pasar a json una clase propia hay que hacerla serializable, o usar el __dict__ (opción menos recomendable)

# Opción 1: A través de una función o método estático
class EquipoSegundo:
    def __init__(self, nombre, sede):
        self.nombre = nombre
        self.sede = sede
    
    # con este método hacemos las instancias serializables
    @staticmethod
    def encoder(equipo):
        if isinstance (equipo, EquipoSegundo):
            return equipo.__dict__
        else:
            raise TypeError ('No es serializable')
        
# Función equivalente al método anterior
# def encoder(equipo):
#     if isinstance (equipo, EquipoSegundo):
#         return equipo.__dict__
#     else:
#         raise TypeError ('No es serializable')
             
compos = EquipoSegundo ('Compostela', 'San Lázaro')

# OJO A LA LLAMADA, utilizando el método codificaxor que creamos a través del atributo default
print(json.dumps(compos, default=EquipoSegundo.encoder))

###########################################################

# Opción 2: Utilizar una clase como encoder, que hereda de JSONEncoder
class EquipoSegundo:
    def __init__(self, nombre, sede):
        self.nombre = nombre
        self.sede = sede
    
class Encoder(json.JSONEncoder):
    def default (self, object):
        if isinstance (object, EquipoSegundo):
            return object.__dict__
        else:
            return super().default(self)        
             
celta = EquipoSegundo ('Celta', 'Balaídos')

# OJO -> Aquí usamos cls, la clase codificadora
print(json.dumps(celta, cls=Encoder))