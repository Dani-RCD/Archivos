import csv

# Escribir en un archivo CSV
with open("archivo.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nombre", "Edad"])
    writer.writerow(["Luis", 29])

# Leer un archivo CSV
with open("archivo.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
