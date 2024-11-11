import zipfile

# Crear un archivo zip
with zipfile.ZipFile("archivo.zip", "w") as zipf:
    zipf.write("archivo.txt")  # Agrega archivo.txt al .zip

# Leer y extraer un archivo zip
with zipfile.ZipFile("archivo.zip", "r") as zipf:
    zipf.extractall("extraido")
