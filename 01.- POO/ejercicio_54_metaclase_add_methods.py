'''
Crear un metaclase Comunicador
Las clases que se creen como consecuencia de Comunicador
deberán implementar los métodos:
enviar_email
enviar_sms
enviar_whatsapp

Además, añadir un método que se llame enviar_global
que envíe a través de todos los métodos anteriores
'''

class ComunicadorImplementacion(type):
    def __new__(cls, name, bases, dct):
        required_methods = ['enviar_email', 'enviar_sms', 'enviar_whatsapp']
        
        if bases:  # aplicar comprobación a clases que "implementen" la metaclase
            missing_methods = required_methods - dct.keys()
            if missing_methods:
                raise NotImplementedError(f'La clase {name} debe implementar los métodos: {missing_methods}')
            for method in required_methods:
                if not callable(dct.get(method)):
                    raise TypeError(f"El método {method} en la clase {name} debe ser callable")
            
            def enviar_global(self, mensaje):
                self.enviar_email(mensaje)
                self.enviar_sms(mensaje)
                self.enviar_whatsapp(mensaje)
                
            dct["enviar_global"] = enviar_global
            
        return super().__new__(cls, name, bases, dct)

class BaseComunicador(metaclass=ComunicadorImplementacion):
    pass

class ComunicadorImplementacion(BaseComunicador):
    def enviar_email(self, mensaje):
        print(f'Enviando Email: {mensaje}')
    
    def enviar_sms(self, mensaje):
        print(f'Enviando SMS: {mensaje}')
    
    def enviar_whatsapp(self, mensaje):
        print(f'Enviando WhatsApp: {mensaje}')
    
    # enviar_whatsapp = 10 # Da error porque no es Callable
        
# class ComunicadorMalImplementado(BaseComunicador):
#     def enviar_email(self, mensaje):
#         print(f"Enviando Email: {mensaje}")


com = ComunicadorImplementacion()
com.enviar_global('Hola, este es un mensaje global.')