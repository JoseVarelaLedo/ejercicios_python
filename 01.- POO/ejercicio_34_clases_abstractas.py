import abc # Módulo referente a las clases abstractas
# class Motor:
#     def __init__ (self, nombre):    # Tiene constructor, aunque no es instanciable, es HEREDABLE
#         self.nombre = nombre
        
#     def arrancar (self):
#         print ('Arrancando el motor', self.nombre)
        
#     @abc.abstractmethod
#     def acelerar (self):
#         pass
    
# #motor_v8 = Motor ('V8') # Esta instanciación no es posible

# class MotorCombustion (Motor):
#     def __init__(self, nombre):
#         super().__init__(nombre)
    
#     def acelerar (self):
#         print ('Soy el motor ', self.nombre, 'y estoy acelerando')
        
# motor_v8 = MotorCombustion ('V8') # Esta instanciación sólo es posible si MotorCombustion implementa el método acelerar

class Notificador (abc.ABC):
    @abc.abstractmethod
    def notificar (self, destinatario, mensaje):
        pass

class NotificadorEmail (Notificador):
    def notificar (self, destinatario, mensaje):
        print (f'Enviando email a {destinatario} con el mensaje {mensaje}')
        
class NotificadorWhatsapp (Notificador):
    def notificar (self, destinatario, mensaje):
        print (f'Enviando whatsapp a {destinatario} con el mensaje {mensaje}')
        
class NotificadorSMS (Notificador):
    def notificar (self, destinatario, mensaje):
        print (f'Enviando sms a {destinatario} con el mensaje {mensaje}')
    
def get_notificador ():
    #return None
    return  NotificadorEmail()

notificaciones = (('Juan', 'Haz la Cama'), ('Jose', 'Ve a la compra'))

notificador = get_notificador()
if (isinstance(notificador, Notificador)):
    for notificacion in notificaciones:
        notificador.notificar (notificacion[0], notificacion[1])