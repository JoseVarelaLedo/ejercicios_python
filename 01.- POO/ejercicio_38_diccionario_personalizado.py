'''
Queremos disponer de un diccionario de tipos concretos en los que las claves va a ser número enteros y los valores van a ser instancias de la clase Cliente
'''

class Cliente:
    def __init__ (self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        
    def __repr__(self):
        return f"Cliente({self.nombre}, {self.apellidos})"

class DiccionarioClientes (dict):
    __clase_clave = int
    __clase_valor = Cliente
    def __init__(self, *args, **kwargs):
        if args:
            if isinstance(args[0], dict): 
                for clave, valor in args[0].items():
                    self[clave] = valor  
            else:                       # si no se recibe un par de clave - valor (un diccionario)
                raise TypeError('Deben usarse claves de tipo entero y valores Cliente')
        super().__init__(**kwargs)
        
    def __setitem__(self, clave, valor):
        if not isinstance(clave, DiccionarioClientes.__clase_clave):
            raise TypeError('La clave debe ser un número entero')
        if not isinstance(valor, DiccionarioClientes. __clase_valor):
            raise TypeError('El valor debe ser una instancia de Cliente')
        super().__setitem__(clave, valor)

clientes1 = DiccionarioClientes() 
        
clientes = DiccionarioClientes({
    1: Cliente('Pepe', 'Pérez'),
    2: Cliente('Ana', 'López')
})

clientes[3] = Cliente ('Juan', 'Varela')

# cliente2 = DiccionarioClientes ('Nuevo Diccionario') # da error porque no estamos pasando un diccionario para construir

# clientes1[0] = 'cliente magnífico' # falla

print(clientes)

print (clientes1)

# clientes["a"] = Cliente("Carlos", "Gómez")  # genera un TypeError