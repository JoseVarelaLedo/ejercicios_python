class Pelicula:
    def __init__(self, titulo, numero_entradas, precio_entrada):
        self.titulo          = titulo
        self.numero_entradas = numero_entradas
        self.precio_entrada  = precio_entrada
        self.__recaudacion   = self.numero_entradas * self.precio_entrada
    
    def cotillear_recaudacion (self, other):
        print ('Cotilleando: ', other.__recaudacion) # se puede acceder desde instancias de una clase a objetos protegidos de la misma clase
  
    @property # hace el getter
    def recaudacion (self):
        return self.__recaudacion
    
    @recaudacion.setter # hace el setter
    def recaudacion (self, nueva_recaudacion):
        self.__recaudacion = nueva_recaudacion
        
    @recaudacion.deleter
    def recaudacion (self):
        raise Exception ('No está permitido borrar este atributo')
    
    # def get_recaudacion (self):
    #     return self.__recaudacion
    
    # def set_recaudacion (self, nueva_recaudacion):
    #     self.__recaudacion = nueva_recaudacion
        
if __name__ == '__main__':
    pelicula_01 = Pelicula ('El Resplandor', 100, 15)
    print (pelicula_01.titulo)
    #print (pelicula.__recaudacion)               # Da error
    print (pelicula_01._Pelicula__recaudacion)    # No da error, forma de acceso externo a propiedad protegida
    
    pelicula_02 = Pelicula ('Tiburón', 80, 2000)
    
    pelicula_02.cotillear_recaudacion (pelicula_01)
    
    print (pelicula_02.recaudacion)
    
    pelicula_02.recaudacion = 200_000
    
    print (pelicula_02.recaudacion)
    
    delattr(pelicula_01, 'recaudacion')
    
    print (pelicula_01.recaudacion)