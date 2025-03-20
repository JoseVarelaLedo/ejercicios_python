def decorador_1(funcion):
    def wrapper (*args, **kwargs):
        print ('Decorador 1', args)
        return funcion (*args, **kwargs)
    return wrapper


def decorador_2(funcion):
    def wrapper (*args, **kwargs):
        print ('Decorador 2', args)
        return funcion (*args, **kwargs)
    return wrapper

@decorador_1
@decorador_2
def saludar (nombre):
    print ('Hola', nombre)

saludar('Juan')