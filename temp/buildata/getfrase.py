import csv
import os

# Leer autores.csv y almacenar la información en un diccionario
autores = {}
with open(os.path.realpath('../../data/autores.csv'), 'r') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        id, nombre = row
        autores[nombre] = id

# Leer frases.1.csv y almacenar la información en una lista
frases = []
with open(os.path.realpath('../original/frases.clean.csv'), 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        frase, autor = row
        frases.append((frase, autor))

# Crear un nuevo archivo CSV y escribir la frase y el id del autor
with open('../../data/frases.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter='|')
    for frase, autor in frases:
        id = autores.get(autor)
        if id is not None:
            writer.writerow([frase, id])