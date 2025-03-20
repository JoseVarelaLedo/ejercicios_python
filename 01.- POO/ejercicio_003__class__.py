class Factura:
    def __init__(self, numero):
         self.numero = numero
         
    def calcular (self):
        pass
    
    
    
factura = Factura(1000)

print (Factura.__class__)

print (factura.__class__)

print (factura.numero.__class__)

print (factura.calcular.__class__)