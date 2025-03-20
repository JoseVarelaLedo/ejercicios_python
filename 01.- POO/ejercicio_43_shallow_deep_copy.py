numero_1 = 10
numero_2 = numero_1
numero_1 = 20

# print (numero_1)
# print (numero_2)

# lista_1 = [10, 20, 30]
# lista_2 = lista_1
# lista_1.append(40)
# print (lista_1)
# print (lista_2)

# lista_1 = [10, 20, 30]
# lista_2 = lista_1 [:]
# lista_1.append(40)
# print (lista_1)
# print (lista_2)

# lista_3 = [10,20,30, [40,50,60]]
# lista_4 = lista_3[:]

# lista_3[3].append (80)

# print (lista_3)

# print (lista_4)

import copy
lista_3 = [10,20,30, [40,50,60]]
lista_4 = copy.deepcopy(lista_3)

lista_3[3].append (80)

print (lista_3)

print (lista_4)

lista_5 = list (lista_4)

lista_4[0] = 46

print (lista_4)

print (lista_5)
