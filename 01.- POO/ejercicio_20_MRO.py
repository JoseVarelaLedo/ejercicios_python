class A:
    def info (self):
        print ('A')
        
class B(A):
    def info (self):
        print ('C')
        
class C(A):
    def info (self):
        print ('C')
# No da problema
# class D (B, A):
#     # def info (self):
#     #     print ('D')
#     pass

# Da problema de consistencia por encontrar el método primero en la clase madre y después en la clase hija
class D (A, B):
   
    pass

d = D()

d.info()
    
    