class Vehiculo ():
    def arrancar(self):          
        print ('Estoy arrancando...') 
   
def circular (self):
    print ('Estoy circulando...') 

def volar (self):
    print ('Estoy volando...')    

class BatMovil (Vehiculo):   
   
   def __init__(self):
     pass

BatMovil.circular = circular
BatMovil.volar = volar

batmovil = BatMovil()

batmovil.arrancar()

batmovil.circular()

batmovil.volar()