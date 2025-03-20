# Hacer un decorador para incorporar a cualquier clase
# y un método que "envíe" la información de los atributos del objeto
# llamado enviar_info

import json

def decorador_enviar_info(clase_a_decorar):    
    # print ('Enviando desde la clase: ', clase_a_decorar, clase_a_decorar.__dict__)
    def enviar_info(self):      
        info = {clave: valor for clave, valor in self.__dict__.items()}
        print(f"Enviando información: {json.dumps(info, indent=4)}")
   
    clase_a_decorar.enviar_info = enviar_info

    return clase_a_decorar  

@decorador_enviar_info
class Persona:
    def __init__(self, nombre, edad):
        self.nombre     = nombre
        self.edad       = edad

p1 = Persona('Juan', 7)
p2 = Persona ('Jose', 35)
p1.enviar_info()
p2.enviar_info()

@decorador_enviar_info
class Factura:
    def __init__(self, numero, importe, cliente):
        self.numero     = numero
        self.importe    = importe
        self.cliente    = cliente        

f1 = Factura(101, 15000, 'Empresa de Juan')
f1.enviar_info()

@decorador_enviar_info
class Cliente:
    def __init__(self, nombre, direccion, telefono, email):
        self.nombre     = nombre
        self.direccion  = direccion
        self.telefono   = telefono     
        self.email      = email  
        
c1 = Cliente ('Juan', 'Casa de Juan', 666666969, 'juan@juan.com')

c1.enviar_info()