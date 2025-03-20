# Impedir que la clase Película admita más atributos de los que se crean en el __init__.
class Pelicula:
    def __init__(self, titulo, duracion):    
        self.__bloqueado = False        # si no ponemos esto a false, bloquea de principio la asignación de título
        self.titulo = titulo
        self.duracion = duracion
        self.__bloqueado = True         # tras la instanciación, se pone a True, porque ya está creado, y se bloquea
    
    def __getattribute__(self, name):
        return super().__getattribute__(name)

    def __setattr__(self, name, value):        
        if not hasattr(self, '_Pelicula__bloqueado'):   # la primera vez se añade el atributo bloqueado
            super().__setattr__(name, value)
        elif not self.__bloqueado:                      # la segunda vez, permite asignación
            super().__setattr__(name, value)
        elif hasattr(self, name):                       # la tercera vez, permite cambio de valor
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No se puede añadir el atributo '{name}' a Pelicula")            
       
        super().__setattr__(name, value)

p = Pelicula('El Padrino', 175)

print (p.titulo)

p.titulo = 'La Madrina'
p.duracion = 200

print (p.titulo)

# p.genero = 'Drama'