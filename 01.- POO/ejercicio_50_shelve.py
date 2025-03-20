import shelve
import abc

# # ESCRITURA
# # el flag 'c' es abrir para lectura y escritura, y crear si no existe
# fichero_persistencia = shelve.open('datos.shlv', flag = 'c') 

# fichero_persistencia ['Santiago'] = 'A Coruña'
# fichero_persistencia ['Vigo'] = 'Pontevedra'
# fichero_persistencia ['Sarria'] = 'Lugo'

# fichero_persistencia.close() # al final hay que cerrarlo para que sea legible

# # LECTURA

# fichero_persistencia = shelve.open('datos.shlv', flag = 'c') 
# print (fichero_persistencia['Sarria'])

# fichero_persistencia.close()

# # UPDATE

# fichero_persistencia = shelve.open('datos.shlv', flag = 'c') 
# fichero_persistencia['Sarria'] = 'Asturias'
# print (fichero_persistencia['Sarria'])

# fichero_persistencia.close()

'''
Utilizando shelve crear un sistema de almacenamiento de objetos libro utilizando como clave el ISBN
'''

class Libro:      
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
    
    def __str__(self):
        return f'Título: {self.titulo}. Autor: {self.autor}. ISBN: {self.isbn}'
    
    def __repr__(self):
        return self.__str__()

    def create(self):
        if Libro.gestor_persistencia:
            Libro.gestor_persistencia.create(self.isbn, self)
        else:
            raise ValueError('No se ha definido un gestor de persistencia')

    @classmethod
    def read(cls, isbn):
        if cls.gestor_persistencia:
            return cls.gestor_persistencia.read(isbn)
        else:
            raise ValueError('No se ha definido un gestor de persistencia')

class GestorPersistencia(abc.ABC):
    @abc.abstractmethod
    def create(self, id, obj):
        pass

    @abc.abstractmethod
    def read(self, id):
        pass

class GestorPersistenciaShelve(GestorPersistencia):
    FILE_NAME = 'libros.shlv'
    
    def create(self, id, obj):
        fichero = shelve.open(self.FILE_NAME)
        fichero[id] = obj
        fichero.close()

    def read(self, id):
        fichero = shelve.open(self.FILE_NAME)
        obj = fichero.get(id, None) 
        fichero.close()
        return obj

Libro.gestor_persistencia = GestorPersistenciaShelve()

if __name__ == '__main__':
    
    fichero_libros = shelve.open('libros.shlv', flag = 'c')
    
    libro1 = Libro('El libro de Python', 'VVAA', '979-8305103298')
    libro2 = Libro ('Las fuerzas contrarias', 'Lorenzo Silva', '9788423367177')
    libro3 = Libro ('El albatros negro', 'María Oruña', '9788401034794')
    
    libro1.create()
    libro2.create()
    libro3.create()
    
    libro_recuperado = Libro.read('979-8305103298')
    print(libro_recuperado) 
    
    libro_recuperado = Libro.read('9788423367177')
    print(libro_recuperado) 
    
    libro_recuperado = Libro.read('9788401034794')
    print(libro_recuperado) 
    
    mi_libro : Libro
    
    if '9788401034794' in fichero_libros.keys():
        mi_libro = fichero_libros ['9788401034794']
    else:
        print ('No tenemos ese libro')
        
    print (mi_libro)
    
    # Actualización masiva
    
    fichero_libros.update({'DESCONOCIDO 1':'Libro desconocido', 'DESCONOCIDO 2': 'Otro libro desconocido'})
    
    # Obtención de número de elmentos y recorrido
    
    print(f'Tengo {len(fichero_libros)} libros')
    for isbn in fichero_libros.keys():
        print(isbn)
    
    fichero_libros.close()