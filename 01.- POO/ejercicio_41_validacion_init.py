'''
Crear una clase Expcepción propia que sea capaz de escribir en un fifhero el log del error que ha ocurrido
Clase Pedido. En el __init__ tiene los siguientes argumentos:
- Número de productos
- Precio unitario

Verificar en el __init__ que el número de productos es un número entero > 0
Verificar en el __init__ que el precio unitario es un número entero > 0
'''
import json
import datetime

class GestorPersistencia:
    def save(self, nombre_fichero, objeto):       
        with open(nombre_fichero, mode='wt', encoding='utf-8') as fichero:         
            json.dump( objeto, fichero)

class PedidoException(Exception):     
    def __init__(self, numero_pedido, mensaje):        
        self.numero_pedido          = numero_pedido
        self.mensaje                = mensaje
        self.__gestor_persistencia  = GestorPersistencia()
        self.save()  
    
    def save(self):      
        self.__gestor_persistencia.save(f'pedido_{self.numero_pedido}.json', self.to_dict())
    
    def to_dict(self):      
        return {
            'numero_pedido':    self.numero_pedido,
            'mensaje':          self.mensaje,
            'timestamp':        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

class Pedido:    
    def __init__(self, numero_pedido, numero_productos, precio_unitario):
        self.numero_pedido      = numero_pedido
        self.validar(numero_pedido,numero_productos, precio_unitario)
        self.numero_productos   = numero_productos
        self.precio_unitario    = precio_unitario

    @staticmethod
    def validar(n_pedido, n_prod, p_unit):       
        if not isinstance(n_prod, int) or n_prod <= 0:
            raise PedidoException(n_pedido, 'El num. de productos debe ser un entero positivo')
        if not isinstance(p_unit, int) or p_unit <= 0:
            raise PedidoException(n_pedido, 'El precio unitario debe ser un entero positivo')
    
    def to_dict(self):        
        return {           
            'numero_pedido': self.numero_pedido,
            'numero_productos': self.numero_productos,
            'precio_unitario': self.precio_unitario            
        }

try:
    pedido_bueno    = Pedido(1, 5, 20)
    
    pedido_erroneo  = Pedido(2, -3, 10)  
except PedidoException as pe:
    print(f'Error en el pedido: {pe.mensaje}')
except Exception as ex:
    print ('Exception', ex)
