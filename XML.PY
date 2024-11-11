import xml.etree.ElementTree as ET

# Crear un archivo XML
root = ET.Element("libros")
libro = ET.SubElement(root, "libro", titulo="Python 101")
ET.SubElement(libro, "autor").text = "Guido Van Rossum"
ET.SubElement(libro, "precio").text = "39.99"

# Guardar el archivo XML
tree = ET.ElementTree(root)
tree.write("archivo.xml")

# Leer y analizar el archivo XML
tree = ET.parse("archivo.xml")
root = tree.getroot()
for libro in root:
    print(libro.attrib["titulo"])
    for atributo in libro:
        print(atributo.tag, ":", atributo.text)
