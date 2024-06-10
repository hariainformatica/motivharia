import sqlite3
import csv
import os

# Conexión a la base de datos
conn = sqlite3.connect(os.path.realpath('../../data/database.db'))
cursor = conn.cursor()

# Crear tabla autor
cursor.execute('''
    CREATE TABLE IF NOT EXISTS autor (
        id INTEGER PRIMARY KEY,
        nombre TEXT
    )
''')

# Leer archivo autores.csv y insertar datos en la tabla autor
with open('../../data/autores.csv', 'r') as file:
    reader = csv.reader(file, delimiter='|')
    for row in reader:
        cursor.execute('INSERT INTO autor (id, nombre) VALUES (?, ?)', row)

# Crear tabla frase
cursor.execute('''
    CREATE TABLE IF NOT EXISTS frase (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        frase TEXT,
        autor_id INTEGER,
        FOREIGN KEY (autor_id) REFERENCES autor (id)
    )
''')

# Leer archivo frases.csv y insertar datos en la tabla frase
with open('../../data/frases.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='|')
    for row in reader:
        cursor.execute('INSERT INTO frase (frase, autor_id) VALUES (?, ?)', row)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()