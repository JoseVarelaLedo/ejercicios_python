def decorador (argumento):
    def funcion_externa(funcion_a_decorar):
        def funcion_interna (*args, **kwargs):
            if (argumento == True):
                print ('Decorando...')
            else: 
                print ('No se decora...')
            return funcion_a_decorar(**args, **kwargs)
        return funcion_interna
    return funcion_externa

class ClaseDecoradora:
    def __init__ (self, argumento):
        self.argumento = argumento
        
    def __call__ (self, funcion_a_decorar):
        def funcion_interna (*args, **kwargs):
            if (self.argumento == True):
                print ('Decorando...')
            else: 
                print ('No se decora...')
            return funcion_a_decorar(*args, **kwargs)
        return funcion_interna
    
@ClaseDecoradora(False)
def saludar():
    print ('Hola')
    
saludar()