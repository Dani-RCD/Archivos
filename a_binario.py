# Archivo binario
data = bytes([120, 3, 255, 0, 100])  # Un arreglo de bytes
with open("archivo.bin", "wb") as file:
    file.write(data)

# Leer desde un archivo binario
with open("archivo.bin", "rb") as file:
    contenido = file.read()
    print(contenido)
