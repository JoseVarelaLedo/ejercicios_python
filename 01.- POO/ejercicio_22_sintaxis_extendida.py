def calcular():
    print ('Sin argumentos')

def calcular(argumento):
    print ('Con argumento', argumento)
    
def calcular(argumento = 10):
    print ('Con argumento opcional', argumento)
    
def calcular (argumento1, argumento2, *args):
    print(type(args)) # tupla
    print(args)     
  
calcular(10, 20, 30, 40, 50)
  
    
def calcular (argumento1, argumento2, **kwargs):
    print(type(kwargs)) # tupla
    print(kwargs) 
calcular(10, 20, extra1=30, extra2=40)
    
def calcular (*args, **kwargs):
    print (args)
    print (kwargs)

calcular(1, 2, 3, x=10, y=20)


def calcular(argumento_posicional_1, argumento_posicional_2, /, argumento_posicional_o_no_1,  argumento_posicional_o_no_2, *, argumento_solo_keyword_1, argumento_solo_keyword_2):
   # argumentos 1 y 2 deben ser posicionales obligatoriamente
   # argumentos después de la barra pueden ser posicionales o kewyword
   # argumentos después del asterisco keyword obligatoriamente
   print (argumento_posicional_1, argumento_posicional_2, argumento_posicional_o_no_1, argumento_posicional_o_no_2, argumento_solo_keyword_1, argumento_solo_keyword_2)
 
calcular(1, 2, 3, 4, argumento_solo_keyword_1=5, argumento_solo_keyword_2=6)
    
