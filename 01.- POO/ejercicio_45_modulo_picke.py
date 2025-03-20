import pickle

class Pelicula:
    def __init__(self, titulo: str, year: int):
        self.titulo = titulo
        self.year = year
        
    def get_titulo(self)        :
        return self.titulo

    def __repr__(self):
        return f'{self.titulo} ({self.year})'    
    
alien = Pelicula ('Alien', 1978)

# Escritura
with open ('pelicula.pickle', mode = 'wb') as fichero_peliculas:    # wb para que sea binario "escriturable"
    pickle.dump(obj = alien, file = fichero_peliculas)
    
# Lectura
pelicula2: Pelicula
with open ('pelicula.pickle', mode = 'rb') as fichero_peliculas:   #rb para lectura binaria
    pelicula2 = pickle.load(file = fichero_peliculas)
    
print (pelicula2)
