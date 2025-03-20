
class Vehiculo ():
    def arrancar(self):          
        print ('Estoy arrancando...')    

class VehiculoTerrestre ():
    def circular (self):
        print ('Estoy circulando...')    

class VehiculoAereo ():
    def volar (self):
        print ('Estoy volando...')    

class BatMovil (Vehiculo):   
   
    def __init__(self):
        self.vehiculoTerrestre = VehiculoTerrestre()
        self.vehiculoAereo = VehiculoAereo()
    
# Con Composición

batmovil = BatMovil()

batmovil.arrancar()

batmovil.vehiculoTerrestre.circular()

batmovil.vehiculoAereo.volar()