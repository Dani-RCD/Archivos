import json

# Escribir en un archivo JSON
data = {"nombre": "Maria", "edad": 25}
with open("archivo.json", "w") as file:
    json.dump(data, file, indent=4)  # El parámetro indent=4 mejora la legibilidad

print("Datos escritos en archivo.json")

# Leer el archivo JSON
with open("archivo.json", "r") as file:
    data = json.load(file)
    print("Datos leídos del archivo:", data)
