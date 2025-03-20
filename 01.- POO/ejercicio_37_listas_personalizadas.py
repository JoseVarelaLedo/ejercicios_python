class Pelicula:
    def __init__(self, titulo):
        self.titulo  = titulo
    def __repr__ (self):
        return f'Titulo: {self.titulo}'
      
class ListaPeliculas (list):
    __clase = Pelicula
    def __init__(self, *args, **kwargs):
        print('__init__')
        for object in args[0]:
            if (not isinstance(object, ListaPeliculas.__clase)):
                raise TypeError('No es una película')
        super().__init__(*args, **kwargs)
        
    def append (self, object):
        if (not isinstance(object, ListaPeliculas.__clase)):
            raise TypeError ('No es una película')
        super().append(object)
        
    def __setitem__ (self, index, object):
        if (not isinstance(object, ListaPeliculas.__clase)):
            raise TypeError ('No es una película')
        super().__setitem__ (index, object)
    
    def insert (self, index, object):
        if (not isinstance(object, ListaPeliculas.__clase)):
            raise TypeError ('No es una película')
        super().insert (index, object)
        
# Constructor sin parámetros, no comprueba nada.        
peliculas = ListaPeliculas()

# Constructor de lista a partir de un iterable
# peliculas2 = ((1, 2 , 3))   # Da error
peliculas2 = ListaPeliculas((Pelicula('Spiderman'), Pelicula('Superman')))

# Acceso con método append()

peliculas.append(Pelicula('El Resplandor'))
peliculas.append(Pelicula('Tiburón'))
peliculas.append(Pelicula('Carrie'))

# Acceso por índice
peliculas [0]  = Pelicula ('Los albóndigas en remojo')

# Acceso con insert
peliculas.insert (4, Pelicula ('El ataque de los tomates asesinos'))

for peli in peliculas2:
    print (peli)
    
# peliculas.append ('Melón') # Da error