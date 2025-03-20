import pickle

# Serialización y almacenamiento de una función (lo mismo para las clases)
def saludar ():
    print ('Hola')
    
with open ('funcion.pickle', 'wb') as fichero:
    pickle.dump (saludar, fichero) # Solo almacena la referencia a la función, no a su comportamiento



with open ('funcion.pickle', 'rb') as fichero:
    mi_funcion = pickle.load (fichero) # Sólo recupera la referencia a la función
    
print (type(mi_funcion))

mi_funcion() # Funciona porque la función 'saludar' está en memoria