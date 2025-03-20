def funcion_generar_pdf (self):
    print (f'Generando pdf para la factura: {self.numero}')

# en este punto disponemos de una referencia a la clase (clase_a_decorar)
def decorador(clase_a_decorar):   
    ###########################################################
    # En este punto, disponemos de una referencia a la clase,
    # y la podemos añadir comportamiento extra, como
    # atributos y métodos de clase
    ###########################################################
    print ('Definición del decorador')    
    clase_a_decorar.generar_pdf = funcion_generar_pdf
    clase_a_decorar.unidades = 10
   
    def inner_wrapper (*args, **kwargs):
        print ('Entrada al inner_wrapper,', args, kwargs)
        instancia = clase_a_decorar(*args, **kwargs)
        ###########################################################
        # en este punto tenemos una referencia al objeto (instancia)
        ###########################################################
        return instancia
    return inner_wrapper


@decorador
class Factura:
    def __init__(self, numero, importe):
        self.numero = numero
        self.importe = importe
        
    def get_numero(self):
        return self.numero

f1 = Factura (101, 15_000)    

numero_f1 = f1.get_numero()

print (numero_f1)

f2 = Factura(102, 25_000)

f1.generar_pdf()

print (f1.unidades)

print (f2.unidades)

print (Factura.__dict__)





