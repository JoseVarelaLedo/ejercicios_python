def decorador (funcion):
    def funcion_interna (*args, **kwargs):
        print ('Decorando...')
        return funcion(**args, **kwargs)
    return funcion_interna

class ClaseDecoradora:
    def __init__ (self, funcion_a_decorar):
        self.funcion_a_decorar = funcion_a_decorar
    def __call__ (self, *args, **kwargs):
        print ('Ejecutando clase decoradora')
        self.funcion_a_decorar(**args, **kwargs)
        print ('Fin decoración')      
    
@ClaseDecoradora
def saludar():
    print ('Hola')
    
saludar()

