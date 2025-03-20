import time

import json
# PASO PREVIO

# def decorador_simple (funcion):
#     print ('Soy la decoracion')
#     return funcion

# def saludador ():
#     print ('Hola, soy un saludador')
    
# funcion_decorada = decorador_simple (saludador)
# funcion_decorada()


# DECORADOR SIMPLE
# def asteriscador(funcion_a_decorar):
#     #función interna -> no se llama de forma explícita -> tiene que ser de uso universal, de ahí el uso de argumentos genéricos
#     def funcion_interna (*args, **kwargs):
#         print ('*'*len(args[0]))
#         funcion_a_decorar(*args, **kwargs)
#         print ('*'*len(args[0]))
#     return funcion_interna

# @asteriscador
# def mostrar_en_mayusculas (texto: str):
#     print (texto.upper())
#     return len(texto)>10
    

# mayor_10 = mostrar_en_mayusculas ('hola mundo')
# print (mayor_10)
    
    
    
# Crear un decorador que deje un log con el timestamp de la ejecución de la función y el nombre de la función que se esté ejecutando

class FactoryPersistencia:
    @staticmethod
    def get_persistence_manager():
        return GestorPersistencia()

class GestorPersistencia:
    def save(self, nombre_fichero, objeto):
        with open(nombre_fichero, mode='wt', encoding='utf-8') as fichero:
            json.dump(objeto, fichero, indent=4)

def logger(archivo):
    def decorador(func):
        def funcion_interna(*args, **kwargs):
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            log_entry = {"timestamp": timestamp, "function": func.__name__}
            
            # Guardar en JSON usando GestorPersistencia
            gestor = FactoryPersistencia.get_persistence_manager()
            gestor.save(archivo, log_entry)

            return func(*args, **kwargs)
        return funcion_interna
    return decorador
    
@logger ('log.json')
def funcion_a_llamar ():
    print ('Función vacía')
    
funcion_a_llamar()