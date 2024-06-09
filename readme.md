# motivharia
Proyecto de demostración en python para el módulo de programación de DAM del IES Haría

## Organización
Está organizado en varias ramas:
- main : Aplicación principal
- data : Extracción de datos
- ui   : Experimentos con el framework textual

## data

Deberemos construir las tablas para los autores y las frases de motivación resultando dos tablas en sqlite:

| Autor  |
|--------|
| id     |
| nombre |


| Frase      |
|------------|
| id         |
| autor_id   |
| frase      |

Fases:
- Copiar y pegar las frases y sus autores en un archivo frases.txt
- Depurar datos: Extraer todos los autores para corregir posibles nombres
- Construir csv con frases y el id del autor
- Construir tablas en sqlite desde el csv

### 1 Copiar y pegar las frases y sus autores en un archivo frases.txt
Extracción de frases motivadoras de la dirección:
https://www.autognosis.com/estoicismo/frases-estoicas/

### 2 Depurar datos: Extraer todos los autores para corregir posibles nombres

La estructura del archivo frases.txt es:

    cita1 (autorx)

    cita2 (autory)
    
    cita3 (autorx)
    
    ·
    
    ·
    
    ·

Usaremos un script en python con expresiones regulares para extraer los autores
La expresión regular la construimos usando:
https://regex101.com/codegen?language=python

En frases.clean.txt colocamos el texto corregido con autores escritos bien y se construye el listado de autores.csv

### 3 Construir csv con frases y el id del autor
Creamos el archivo de frases.csv desde frases.clean.txt y sustituyendo los autores por el autor_id de autores.csv

### 4 Construir tablas en sqlite desde el csv
Construimos las tablas en una base de datos sqlite

## UI
