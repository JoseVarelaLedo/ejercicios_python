import json

# Pregunta si queremos escribir o leer
# Si es escribir guarda el JSON en un fichero
# Si es leer, restaura el objeto a partir del fichero

FILE = 'equipo.json'

class Equipo:
    def __init__(self, nombre, sede):
        self.nombre = nombre
        self.sede = sede

def encoder_equipo(equipo):
    if isinstance(equipo, Equipo):
        return equipo.__dict__
    else:
        raise TypeError('No es serializable')

def decoder_equipo(equipo_json):
    return Equipo(equipo_json['nombre'], equipo_json['sede'])

def mini_menu_cavernicola():
    opcion = input('Introduce opción, [E] para escribir y [L] para leer: ').lower()

    if opcion not in ['l', 'e']:
        print('Lo que has introducido no es correcto')
        return

    if opcion == 'e':  
        equipo = Equipo('S.D. Compostela', 'Santiago de Compostela')
        with open(FILE, 'w') as archivo:
            json.dump(equipo, archivo, default=encoder_equipo, indent=4)
        print("Datos guardados correctamente en 'equipo.json'.")

    elif opcion == 'l': 
        try:
            with open(FILE, 'r') as archivo:
                equipo_json = json.load(archivo)
                equipo_recuperado = decoder_equipo(equipo_json)
            print(f'Equipo restaurado: {equipo_recuperado.nombre}, {equipo_recuperado.sede}')
            print (type(equipo_recuperado))
        except FileNotFoundError:
            print("El archivo 'equipo.json' no existe. Primero escribe los datos.")

mini_menu_cavernicola()
