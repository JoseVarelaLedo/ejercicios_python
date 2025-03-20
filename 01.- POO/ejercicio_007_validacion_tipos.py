# Tarea tiene dos atributos y un método
# ejecutar() que imprime un mensaje. El mensaje puede o no estar
class Tarea:
    def __init__(self, lugar, descripcion):
        self.lugar = lugar
        self.descripcion = descripcion
        
    def ejecutar (self):
        print (f'Ejecutando {self.descripcion} en {self.lugar}')
        
# La función ejecutador recibe una tarea y la ejecuta
# Debe confirmar que se recibe una tarea, y que la tarea se puede ejecutar. Si algo está mal, lanza excepción
        
def ejecutador (tarea: Tarea) -> None:
    if (not isinstance (tarea, Tarea)):
         raise TypeError ('No es una tarea')
    if (not hasattr (tarea, 'ejecutar')):
        raise AttributeError ('No dispone de método ejecutar')    
    if (not callable(getattr (tarea, 'ejecutar'))):
        raise AttributeError ('El ejecutar de la tarea no es callable')
    tarea.ejecutar()      

tarea = Tarea ('Cocina', 'Lavar platos')

ejecutador (tarea)

tarea_fake = 'No soy tarea'
try:
    ejecutador (tarea_fake)
except TypeError as te:
    print (te)
