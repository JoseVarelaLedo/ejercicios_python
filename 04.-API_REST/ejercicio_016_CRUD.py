import requests
import json
# Por ahorrar tiempo y espacio no se gestionan los errores (habría que hacerlo)

API_KEY = 'e2b8dff4'
BASE_URL = f'https://omdbapi.com/?apikey={API_KEY}'

def show_movies(movies, count):
    print('Se mostrarán los 10 primeros resultados tan sólo')
    for movie in movies:
        show_movie(movie)
    print (f'Total:{count}')

def show_movie(movie):
    print(movie['Title'])
    #print(movie['Title'], movie['Year'], movie['Director'])
    #print(movie)

def read(movie_name):
    reply = requests.get(f'{BASE_URL}&t={movie_name}', timeout=5)
    if (reply.status_code==requests.codes.OK):
        movie_name = reply.json()
        show_movie(movie_name)
    else:
        print('Ha pasado algo:', reply.status_code)

def read_all(movie_name):
    reply = requests.get(f'{BASE_URL}&s={movie_name}', timeout=5)
    if (reply.status_code==requests.codes.OK):
        # tuve que usar el get() de los diccionarios, porque desde POSTMAN la respuesta que se obtiene es ésta:
#         {
#            "Search": [
#               {"Title": "Batman Begins", "Year": "2005"},
#               {"Title": "The Dark Knight", "Year": "2008"},
#               {"Title": "The Dark Knight Rises", "Year": "2012"}
#              ],
#     "totalResults": "3",
#     "Response": "True"
# }
        movies = reply.json().get("Search", [])
        count = reply.json().get("totalResults")
        show_movies(movies, count)
    else:
        print('Ha pasado algo:', reply.status_code)

if __name__=='__main__':
    opcion = input('Elige, película [i]ndividual o [l]istado\n')
    if opcion == 'i':        
        read(input('Título de la película:\n'))
    else:        
        read_all(input('Título de la película:\n'))