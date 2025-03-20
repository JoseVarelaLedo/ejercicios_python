class Motor:
    '''
    Soy un motor de combustión
    '''
    def __init__(self, nombre):
        self.nombre = nombre
        
    '''
    Método para arrancar el motor
    '''
    def arrancar (self):
        pass
    
motor = Motor ('V8')

print (help(Motor))
