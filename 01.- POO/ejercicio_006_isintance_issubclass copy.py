# función isinstace()  --> Determina si un OBJETO es una instancia de una clase
# función issubclass() --> Determina si una clase es subclase de otra

class Deportista:
    pass

class DeportistaOlimpico (Deportista):
    pass

class SaltadorAltura (DeportistaOlimpico):
    pass


ramon = SaltadorAltura()

print (isinstance(ramon, SaltadorAltura))

print (isinstance(ramon, DeportistaOlimpico))

print (isinstance(ramon, Deportista))

print (issubclass (SaltadorAltura, DeportistaOlimpico))

print (issubclass (DeportistaOlimpico, Deportista))