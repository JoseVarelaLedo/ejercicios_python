class Jugador:
    # Variable de clase. No pertenece al objeto, sino a la clase (como algo estático en Java)
    limite_salarial = 10_000
    
    def __init__(self, nombre, salario):
        self.nombre = nombre
        if salario > Jugador.limite_salarial:
            raise ValueError('Salario demasiado alto')
    
 
    
try:
    jugador = Jugador ('Ronaldo', 20_000)
   
except ValueError as ve:
    print (ve)
    
Jugador.limite_salarial = 21_000


try:
    jugador = Jugador ('Ronaldo', 20_000)
    print ('Jugador fichado')
except ValueError as ve:
    print (ve)
    
jugador.limite_salarial = 30_000

print (Jugador.limite_salarial)

print (jugador.limite_salarial)

print (Jugador.__dict__)

print (jugador.__dict__)

