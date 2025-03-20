class Ordenador:
    def __init__ (self, nombre, ghz, ram, disco):
        self.nombre = nombre
        self.ghz = ghz
        self.ram = ram
        self.disco = disco
        
# crear métodos mágicos para sumar ordenadores, multiplicar, restar y calcular la longitud

    def __len__ (self):
        return self.ghz
    
    def __mul__(self, otro):
        return self.ghz * otro.ghz
    
    def __truediv__ (self, otro):
        return self.ram / otro.ram
    
    def __sub__ (self, otro):
        return self.disco - otro.disco
    
    def __add__ (self, otro):
         return self.ghz + otro.ghz
    
    
    
ordenador1 = Ordenador ("Hp", 3, 8, 2000)

ordenador2 = Ordenador ("Asus", 4, 16, 500)

print (ordenador1 / ordenador2 )