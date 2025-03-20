class Producto:
    def __init__(self, nombre, precio, referencia):
        self.nombre = nombre
        self.precio = precio
        self.referencia = referencia
    
    def __len__ (self): # método usado por la función len
        return self.precio
    
    def __str__ (self): # método usado para la función print
        return f"Producto: {self.nombre}, Precio {self.precio}, Referencia: {self.referencia}"
    
    def __repr__ (self):
        return f"Producto: {self.nombre}, Precio {self.precio}, Referencia: {self.referencia}"

pendrive = Producto ("pendrive", 10, "A123")

cd = Producto ("CD", 2, "B456")

print (pendrive)

# Tupla
productos = (pendrive, cd)

print (productos)