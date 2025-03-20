class Cliente:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        
class ClienteVip(Cliente):
    def __init__ (self, nombre, apellidos, edad, tarjeta_oro):
        super().__init__ (nombre, apellidos, edad)
        self.tarjeta_oro = tarjeta_oro
        
    def saludar (self):
        print ("Hola desde la sala VIP")
        
    def modificar (self):
        # setattr (self, 'saludar', f'Hola, me llamo {self.nombre}')
        self.saludar = 'Hola'
        
   

cliente_vip = ClienteVip ('John', 'Doe', 55, 'Tarjeta Gold')

if hasattr (cliente_vip, 'saludar'):
    if (callable(cliente_vip.saludar)):
        cliente_vip.saludar()
    else:
        print ('Saludar no es un método, y no se puede invocar así')
else:
    print ('No tenemos tal función o atributo')
    
    