#build a csv from frases.1.txt using regular expressions
#every line is a frase with autor in parentheses
#output is a csv with two columns: frase, autor

import re
import csv
import os

#read the file
with open('../original/frases.clean.txt', 'r', encoding='utf-8') as f:
    frases = f.readlines()

#initialize the csv file
with open(os.path.relpath('../original/frases.clean.csv'), 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['frase', 'autor']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
    writer.writeheader()

    #parse the file
    for frase in frases:
        #use regular expressions to extract the frase and the autor
        match = re.match(r'(.*)\((.*)\)', frase)
        if match:
            frase = match.group(1).strip()
            autor = match.group(2).strip()
            #write to the csv file
            writer.writerow({'frase': frase, 'autor': autor.strip()})
        else:
            print(frase)


