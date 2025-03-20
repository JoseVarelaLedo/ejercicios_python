'''
- Clase Película con dos atributos
- Creamos una función SIN RETORNO que recibe un objeto Pelicula y modifica alguno de sus atributos
- Creamos una instancia de Pelicula, la pasamos como argumento a la función y la modificamos dentro de ésta.
- ¿Se modifica el objeto fuera de la función?
'''

class Pelicula:
    def __init__(self, titulo: str, year: int):
        self.titulo = titulo
        self.year = year
        
    def __repr__(self):
        return f'{self.titulo} ({self.year})'
        
        
def modifica_pelicula(pelicula: Pelicula, **kwargs):
    if 'titulo' in kwargs and isinstance(kwargs['titulo'], str):
        pelicula.titulo = kwargs['titulo'].upper()
    if 'year' in kwargs and isinstance(kwargs['year'], int):
        pelicula.year = kwargs['year']
        
        
p1 = Pelicula('Tiburón', 1978)

print(p1)  # SALIDA: Tiburón (1978)
    
modifica_pelicula(p1, titulo='La momia', year=2005)

print(p1)  # SALIDA: LA MOMIA (2005) --> Se modifica el objeto original, ya que es un paso por referencia

    