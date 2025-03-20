class Coche:
    def __init__ (self, nombre, precio, consumo, velocidad):
        self.nombre = nombre
        self. precio = precio
        self.consumo = consumo
        self.velocidad = velocidad

    def __repr__ (self):
        return f'Coche: {self.nombre}'
        
        
coche_1 = Coche ('Mazda', 20_000, 5.5, 200)

coche_2 = Coche ('Polo', 10_000, 5.5, 180)

coche_3 = Coche ('Kia', 11_000, 6.5, 175)

lista_coches = [coche_1, coche_2, coche_3]


# Versión 'tradicional'
def valorar_coche (coche):
    return coche.precio

lista_coches.sort (key = valorar_coche)

# Versión lambda, se establece el criterio con la lambda
#lista_coches.sort(key= lambda coche : coche.precio)

print (lista_coches)
