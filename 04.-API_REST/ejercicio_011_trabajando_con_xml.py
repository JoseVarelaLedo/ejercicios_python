# 4 alternativas para trabajar con XML desde Python
# incluidas en el módulo xml
# 1.- dom - Document Object Model
# 2.- parsers -- wrappers
# 3.- sax - Simple Api for XML
# 4.- etree -- la librería XML Element Tree


# Usaremos Element Tree
import xml.etree.ElementTree

# Obtener el elemento raíz a través de getroot
cars_for_sale = xml.etree.ElementTree.parse('cars.xml').getroot()
print(cars_for_sale.tag) # cars_for_sale
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for elemento in car:
        if elemento.tag == 'price':
            print('\t\t', elemento.tag, end='')
            print(elemento.attrib, end='')
            print(' =', elemento.text)
        else:
            print('\t\t', elemento.tag, end='')
            print(' =', elemento.text)
