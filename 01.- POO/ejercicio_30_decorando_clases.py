def decorador_validador (clase_a_decorar):
    print ("En validador", clase_a_decorar)
    # Obtenemos una referencia al método de obtención de valores de atributos
    clase_a_decorar.atributos = clase_a_decorar.__getattribute__    # acceso a todos los atributos de la clase
    
    def internal_wrapper (self, nombre_atributo):
        print ('Entramos en wrapper con', nombre_atributo)
        if (nombre_atributo == 'importe'):
            print ('Está leyendo el importe')
            if clase_a_decorar.atributos (self, nombre_atributo) > 1_500:
                raise ValueError ("No se pueden leer cantidades mayores a 1500")
            
        return clase_a_decorar.atributos (self, nombre_atributo)
    # Redefinimos el comportamiento de obtención de valores de atributos
    clase_a_decorar.__getattribute__ = internal_wrapper
    return clase_a_decorar

@decorador_validador
class Factura:
    def __init__(self, numero, importe):
        self.numero = numero
        self.importe = importe
        
factura_1 = Factura('69', 1_500)
factura_2 = Factura('70', 1_850)

print (factura_1.numero)    # No ejecuta el if del decorador, porque estamos invocando el número
print (factura_1.importe)   # Ejecuta el if del decorador, porque hemos invocado el importe


factura_1.importe = 2_000

# print (factura_1.importe)    # Hace que salte el error