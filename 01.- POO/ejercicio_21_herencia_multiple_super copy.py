class Vehiculo ():
    def __init__ (self, nombre):        
        print ('__init__ de vehículo')
        self.nombre = nombre
        
    def arrancar(self):          
        print ('Estoy arrancando...')  

class Automovil (Vehiculo):   
    def __init__(self, nombre, velocidad):
        print ('__init__ de automóvil')
        Vehiculo.__init__(self, nombre)
        self.velocidad = velocidad
        
    def atacar (self):
        print (f'Soy {self.nombre} y estoy atacando como automóvil...') 

class Avion (Vehiculo):    
     def __init__(self, nombre, altitud):
        print ('__init__ de avión')
        Vehiculo.__init__(self, nombre)
        self.altitud = altitud
     def atacar (self):
        print (f'Soy {self.nombre} y estoy atacando como avión...')   

class BatMovil (Automovil, Avion):
    def __init__ (self, nombre, velocidad, altitud):
        Automovil.__init__ (self, nombre, velocidad)
        Avion.__init__ (self, nombre, altitud)
       
    def atacar(self):
        Automovil.atacar(self)
        Avion.atacar(self)
        print (f'Soy {self.nombre} y tengo ataques múltiples...')   
   

batmovil = BatMovil('Batmovil', 290, 400)

batmovil.atacar()