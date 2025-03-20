class Coche:
    def __init__ (self, nombre, precio, consumo, velocidad):
        self.nombre = nombre
        self. precio = precio
        self.consumo = consumo
        self.velocidad = velocidad
        
    # Comparación menor que
    def __lt__ (self, other):
        print ('lt')
        return self.precio < other.precio
    
    # Comparación mayor que
    def __gt__ (self, other):
        print ('gt')
        return self.precio > other.precio
    
    # Comparación de igualdad
    def __eq__ (self, other):
        return self.consumo == other.consumo
    
    def __repr__ (self):
        return f'Coche: {self.nombre}'
        
        
coche_1 = Coche ('Mazda', 20_000, 5.5, 200)

coche_2 = Coche ('Polo', 10_000, 5.5, 180)

coche_3 = Coche ('Kia', 11_000, 6.5, 175)


# Lista
lista_coches = [coche_1, coche_2, coche_3]


# Tupla
tupla_coches = (coche_1, coche_2, coche_3)

coches_ordenados = sorted (lista_coches)

print (coches_ordenados)

coches_ordenados_reversed = sorted(lista_coches, reverse = True)

print (coches_ordenados_reversed)

print (coche_1 == coche_2)