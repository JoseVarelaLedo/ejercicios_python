# Crear una película y agregarla al archivo xml correspondiente al ejercicio
# Título
# Director
# Genero
# Guardar a fichero para comprobar el resultado

import xml.etree.ElementTree as ET
import xml.dom.minidom

FILE = './ejercicio_012_xml.xml'

# Cargar el archivo XML existente
tree = ET.parse(FILE)
peliculas = tree.getroot()  # Obtener el nodo raíz <peliculas>

# Crear un nuevo elemento de película
nueva_pelicula = ET.Element('pelicula')
ET.SubElement(nueva_pelicula, 'titulo').text = 'El Padrino'
ET.SubElement(nueva_pelicula, 'director').text = 'Francis Ford Coppola'
ET.SubElement(nueva_pelicula, 'genero').text = 'Crimen, Drama'

# Insertar la nueva película dentro del nodo <peliculas>
peliculas.append(nueva_pelicula)

# Convertir el árbol en una cadena con formato bonito
xml_bytes = ET.tostring(peliculas, encoding='utf-8')
xml_string = xml_bytes.decode('utf-8')

# Usar minidom para formatear correctamente
xml_pretty = xml.dom.minidom.parseString(f'<?xml version="1.0" encoding="utf-8"?>\n{xml_string}').toprettyxml(indent="  ")

# Guardar el archivo con formato correcto
with open(FILE, 'w', encoding='utf-8') as f:
    f.write(xml_pretty)

print("Película añadida correctamente al archivo XML.")
