class Motor:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def arrancar (self):
        pass
    
motor = Motor ('V8')

print (dir(Motor))
print (dir(motor))
print (dir(Motor.arrancar))