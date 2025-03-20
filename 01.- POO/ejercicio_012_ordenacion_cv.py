class Candidato:
    PUNTOS_EXPERIENCIA = 1
    PUNTOS_INGLES = 3
    PUNTOS_JAPONES = 5   
    
    def __init__ (self, nombre, experiencia: int, ingles: bool, japones: bool):
        self.nombre = nombre
        self.experiencia = experiencia
        self.ingles = ingles
        self.japones = japones
        
    def __repr__(self):
        return self.nombre
    
    @classmethod
    def valorar_candidato (cls, candidato):      
        puntuacion = candidato.experiencia * cls.PUNTOS_EXPERIENCIA
        if (candidato.ingles):  puntuacion +=cls.PUNTOS_INGLES
        # operador ternario
        puntuacion +=cls.PUNTOS_JAPONES if (candidato.japones) else 0
        return puntuacion
    
        
        
c1 = Candidato ('Juan', 5, True, False)
c2 = Candidato ('Rosa', 4, True, True)
c3 = Candidato ('Ana', 10, False, False)
c4 = Candidato ('Ricardo', 2, False, True)

# Ordenar por:
# año de experiencia = 1 punto
# Inglés: 3 puntos
# Japonés: 5 puntos

candidatos = [c1, c2, c3, c4]

# Tradicional
# def valorar_candidato (candidato: Candidato):
#     PUNTOS_INGLES = 3
#     PUNTOS_JAPONES = 5
#     puntuacion = candidato.experiencia
#     if (candidato.ingles):  puntuacion +=PUNTOS_INGLES
#     if (candidato.japones): puntuacion +=PUNTOS_JAPONES
#     return puntuacion
    
    
# Lambda
candidatos.sort(key=lambda c: c.experiencia + (3 if c.ingles else 0) + (5 if c.japones else 0), reverse=True) 
    

# candidatos.sort(key = valorar_candidato, reverse = True)

print (candidatos)


# Comportamiento adicional incorporando funcionalidades en tiempo de ejecución

def restar (self, operando1, operando2):
    return operando1 - operando2


Candidato.sumar = lambda self, operando1, operando2: operando1 + operando2

Candidato.restar = restar

print (c1.sumar(66,135))

print (c1.restar(99,66))