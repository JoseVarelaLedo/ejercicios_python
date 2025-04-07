import sqlite3

class Movie:
    def __init__(self, id, title, director, year):
        self.id = id
        self.title = title
        self.director = director
        self.year = year


class BaseDatosPeliculas:
    def __init__(self):
        self.conn = sqlite3.connect('movies.db')
        self.__create_table()
    
    def __create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS movies  (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            director TEXT NOT NULL,
                            year INTEGER NOT NULL)
            """)
        self.conn.commit()

    # CRUD
    # 1.- CREATE
    def insert_movie(self, movie : Movie):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO movies (title, director, year) VALUES (?,?,?)',
                       (movie.title, movie.director, movie.year))
        self.conn.commit()
        print (f'{movie.title} añadida correctamente')
        
    # 2_a.- READ
    def read_movie(self, id):
        cursor = self.conn.cursor()
        movie = cursor.execute (f'SELECT * FROM movies WHERE id ={id}').fetchone()
        if movie:
            print(f'Título: {movie[1]}, Director: {movie[2]}, Año: {movie[3]}')
        else:
            print(f'No se encontró la película con ID {id}')
    
    # 2_b.- READ ALL
    def read_all(self):
        cursor = self.conn.cursor()
        movies = cursor.execute('SELECT * FROM movies');
        movies = list(movies)
        print (type(movies))
        return movies
        # for movie in movies:
        #     print(f'Título: {movie[1]}, Director: {movie[2]}, Año: {movie[3]}')
    
    # 3.- UPDATE (usamos kwargs pA)
    #def update_movie(self, id, **kwargs): # llamada original con **kwargs
    # cambiamos la llamada para que admita una tupla, que después desestructuramos
    def update_movie (self, update_data):       
        if not update_data:
            print ('No se han recibido argumentos')
            return None
        else:
            id_movie, arguments = update_data        
            cursor = self.conn.cursor()
            campos = ', '.join(f'{campo} = ?' for campo in arguments.keys())
            # print (type(kwargs.values()))

        # EXPLICACIÓN LÍNEA QUE VIENE A CONTINUACIÓN:        
        # kwargs.values() devuelve un diccionario, por tanto pares de clave-valor
        # list(kwargs.values()) convierte el diccionario iterable en una lista.
        # como queremos prevenir operaciones matemáticas accidentales, pasamos id como una lista de un solo 
        # elemento a añadir a la lista de values

            valores = list(arguments.values()) + [id_movie]  

            sql = f'UPDATE movies SET {campos} WHERE id = ?'
            
            cursor.execute(sql, valores)
            self.conn.commit()
            
            print(f'Película con ID {id_movie} actualizada correctamente.')
        
    # 4.- DELETE
    def delete_movie (self, id):
        cursor = self.conn.cursor()
        cursor.execute(f'DELETE FROM movies WHERE id={id}')
        self.conn.commit()
        
        print (f'Se ha borrado correctamente la película con id: {id}')
        
    @classmethod
    def menu_insert(cls) -> Movie:
        id_movie = 0
        title = input ('Título:\n') .strip()  
        director = input ('Director:\n').strip()
        year = input ('Fecha de estreno:\n').strip()
        return Movie(id_movie, title, director, year )
    
    @classmethod
    def menu_read(cls)->int:
        id_movie=input('Introduce id de la película a leer:\n').strip()
        if not id_movie.isdigit():
            print('No has introducido un dato numérico')
            BaseDatosPeliculas.menu_read()
        else:
            id_movie=int(id_movie)
        return id_movie
    
    @staticmethod
    def show_movies(movies):
        for movie in movies:
             print(f'Título: {movie[1]}, Director: {movie[2]}, Año: {movie[3]}')
    
    @classmethod
    def menu_update(cls):       
        id_movie = input('Id: ').strip()
        
        if not id_movie.isdigit():
            print('El ID debe ser un número válido.')
            return None  # salir si no se introduce un dato numérico
        
        id_movie = int(id_movie)

        title = input('Título:\n ').strip()
        director = input('Director:\n ').strip()
        year = input('Fecha de estreno:\n ').strip()

        # Diccionario con solo los valores no vacíos
        update_data = {k: v for k, v in {
            'title': title,
            'director': director,
            'year': int(year) if year.isdigit() else None
        }.items() if v}

        if update_data:
            return id_movie, update_data  
        else:
            print('No se han introducido datos para actualizar')
            return None
        
    @classmethod
    def menu_delete(cls)-> int:
        id_movie=input('Introduce id de la película a eliminar:\n').strip()
        if not id_movie.isdigit():
            print('No has introducido un dato numérico')
            BaseDatosPeliculas.menu_delete()
        else:
            id_movie=int(id_movie)
        return id_movie

    @staticmethod
    def menu_general(movies_db):        
        opcion = input('Introduce opción: \n\t[C]rear Película \n\t[L]eer Película \n\tLeer [T]odas \n\t[A]ctualizar Película \n\t[B]orrar Película\n')
        match opcion.lower():
            case 'c':
                movies_db.insert_movie(BaseDatosPeliculas.menu_insert())
            case 'l':
                movies_db.read_movie(BaseDatosPeliculas.menu_read())        
            case 'a':
                movies_db.update_movie(BaseDatosPeliculas.menu_update())    
            case 'b':
                movies_db.delete_movie(BaseDatosPeliculas.menu_delete())    
            case 't':
                BaseDatosPeliculas.show_movies(movies_db.read_all())
        
        again = input ('Alguna otra consulta?\n\t[S]í\t[N]o\n')
        if again.lower() == 's':
            BaseDatosPeliculas.menu_general(movies_db)
        
                
if __name__ == '__main__':
    movies_db = BaseDatosPeliculas()

    #movies_db.insert_movie(BaseDatosPeliculas.menu_insert())

    #tiburon = Movie(0, 'Tiburón', 'Steven Spielberg', 1977)
    # tiburon_2 = Movie(0, 'Tiburón II', 'Steven Spielberg', 1979)
    # movies_db.insert_movie(tiburon_2)

    #movies_db.read_movie(BaseDatosPeliculas.menu_read()) 
    #movies_db.update_movie(BaseDatosPeliculas.menu_update())
   
    #movies_db.delete_movie(BaseDatosPeliculas.menu_delete())
    BaseDatosPeliculas.menu_general(movies_db)