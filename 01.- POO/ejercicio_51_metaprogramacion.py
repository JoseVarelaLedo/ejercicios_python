# # Metaclase

# # a = 3

# # print (type(a))

# # print (type(int))

# class Autor:
#     pass

# autor = Autor()

# # print (type(autor))
# # print (type(Autor))

# # Atributos especiales:

# print (Autor.__name__) # nombre de la clase
# # print (autor.__name__) # error
# print (Autor.__class__) 
# print (autor.__class__)

# print (Autor.__bases__) # clases de las que hereda


# # Función (constructor) type que permite crear clases

# # Con un argumento, nos dice de qué tipos es lo que le pasamos
# print (type(Autor))

# # Con 3 argumentos construye una clase
# # x -> Nombre de la clase (atributo __name__)
# # y -> Tupla con las clases de la que hereda la nueva clase (atributo __bases__)
# # z -> Diccionario con los métodos y atributos de la clase (atributo __dict__)


# def saludar (self):
#     print ('Saludando...')
    
# # se pone coma en el segundo parámetro para que se sepa que es una tupla
# MiNuevaClase = type('MiNuevaClase', (object,), {'idioma': 'Español', 'saludar': saludar})

# instancia = MiNuevaClase()

# print (instancia.idioma)

# instancia.saludar()


# Crear una clase Videojuego, que tenga constructor con título y plataforma, y método para mostrar datos

def constructor(self, titulo, plataforma):
    self.titulo = titulo
    self.plataforma = plataforma
    
def to_string(self):
    return f'Título: {self.titulo}, Plataforma: {self.plataforma}'

def mostrar_datos (self):
    print( f'{self.titulo}, juego perteneciente a al plataforma {self.plataforma}')
    print ('-------------------------------------------------------------------\n')
    print ('La instancia que hemos creado para representarla tiene estos datos:')
    print ('-------------------------------------------------------------------\n')
    print ('Clase de la instancia', self.__class__)    
    print ('Diccionario de la instancia:', self.__dict__)
    clase = self.__class__
    print ('La clase a su vez es de tipo:', clase.__class__)
    print ('y hereda de:', clase.__bases__)
    print ('La clase además tiene este diccionario:', clase.__dict__)
    

Videojuego = type ('Videojuego', (object,), {'__init__': constructor, '__repr__': to_string, 'mostrar_datos':mostrar_datos})

videojuego = Videojuego('The Legend of Zelda', 'Nintendo Switch')

print (videojuego)

print (videojuego.titulo)

print (videojuego.plataforma)

videojuego.mostrar_datos()