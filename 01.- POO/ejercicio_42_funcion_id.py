class Videojuego:
    def __init__(self, titulo, plataforma):
        self.titulo     = titulo
        self.plataforma = plataforma
    
    def __eq__ (self, value):
        return (self.titulo == value.titulo  and self.plataforma == value.plataforma)
        
v1 = Videojuego('Super Mario', 'Switch')

v2 = Videojuego('Super Mario', 'Super Famicom')

print ("Antes de asignación")
print (v1 == v2)
print (id(v1))
print (id(v2))

v1 = v2
print ("Después de asignación")
print (v1 is v2)
print (id(v1))
print (id(v2))

