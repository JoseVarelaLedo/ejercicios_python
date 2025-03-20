# Definición de clase
class Ordenador (object):
    
    # Método constructor (llamado inicializador en Python)
    def __init__(self, marca, modelo, precio_unitario): 
        self.marca = marca  # Declaración de atributo (de instancia) y asignación de valor
        self.modelo = modelo
        self.precio = precio_unitario
        self.calcular_velocidad = 200
     
    # Método de instancia
    def mostrar_informacion (self):
        print ('Marca: ', self.marca)
        print ('Modelo: ', self.modelo)
        print('Precio: ', self.precio)
    
class OrdenadorPortatil(Ordenador):
    def __init__(self, marca, modelo, precio_unitario, pulgadas_pantalla):
        super().__init__(marca, modelo, precio_unitario)
        self.pulgadas_pantalla = pulgadas_pantalla
    
# Creación del objeto o de la instancia
mi_ordenador = Ordenador ('Hp', 'Pavilion', 550)  # instanciación

# Creación de objeto de la clase derivada
mi_ordenador_portatil = OrdenadorPortatil('Hp', 'Pavilion', 550, 15)

# mi_ordenador_portatil.mostrar_informacion()

# print (mi_ordenador.velocidad_procesador)

# mi_ordenador.calcula_velocidad()

# velocidad = getattr (mi_ordenador, 'velocidad_procesador', 1000)
# print ('Velocidad: ', velocidad)

setattr (mi_ordenador, 'velocidad_procesador', 2000)

if hasattr (mi_ordenador, 'calcular_velocidad'):
    if (callable (mi_ordenador.calcular_velocidad)):
        mi_ordenador.calcular_velocidad()
    else:
        print ('Tengo de eso, pero no es ejecutable')
else:
    print ('No tengo eso')
    
print (mi_ordenador.__dict__)

print (Ordenador.__dict__)