class Artefacto:
    pass

class Vehiculo (Artefacto):
    pass

class Automovil (Vehiculo):
    pass

mi_automovil = Automovil() # Herencia Simple: Es instancia de Automovil, de Vehiculo y de Artefacto


class Avion (Vehiculo):
    pass

class BatMovil (Automovil, Avion):   # Herencia múltiple: se lee de izquierda a derecha, primero busca lo que se hereda de Automovil, y después de Avion
    pass