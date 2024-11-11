import os

# Carpeta llamada "nueva_carpeta"
os.makedirs("nueva_carpeta", exist_ok=True)

# Crear un archivo de texto dentro de "nueva_carpeta"
with open(os.path.join("nueva_carpeta", "archivo.txt"), "w") as file:
    file.write("Contenido dentro de la carpeta.")
    
print("Archivo creado con éxito en 'nueva_carpeta/archivo.txt'")
