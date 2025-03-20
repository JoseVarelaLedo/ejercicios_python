# Excepciones encadenadas

# lista = ['item1', 'item2']

# try:
#     print (lista[2])
# except IndexError as ie:
#     try:
#         resultado = 10 / 0
#     except ZeroDivisionError as zde:
#         print ('Exception interna (zde)', zde)
#         print ('Exception externa (ie)', ie)
#         print ('Información de contexto: ', zde.__context__) # Context contiene la excepción "de fuera"
#         print ('¿Es ie el mismo objeto que zde.__context__?', zde.__context__ is ie)
        
        

# Chained Exceptions Implícito

# class MiException (Exception):
#     pass


# def dividir (n1, n2):
#     try:
#         resultado = n1 / n2
#     except ZeroDivisionError as zde:
#         # OJO AL FROM, que es lo que da la información al __cause__
#         raise MiException ('Ha pasado algo', zde) from zde 
#     return resultado
       
        
# try:
#     resultado = dividir (8,0)
# except MiException as me:
#     print (me)
#     print ('__context__', me.__context__)
#     print ('__cause__', me.__cause__)


# Chained Exceptions Explícito

import traceback

class MiException (Exception):
    pass


def dividir (n1, n2):
    try:
        resultado = n1 / n2
    except ZeroDivisionError as zde:
        # OJO AL FROM, que es lo que da la información al __cause__
        raise MiException ('Ha pasado algo', zde) from zde 
    return resultado
        
try:
    resultado = dividir (8,0)
except MiException as me:
    print (me)
    print (traceback.format_tb(me.__traceback__))
   
