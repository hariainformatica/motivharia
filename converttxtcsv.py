#build a csv from frases.1.txt using regular expressions
#every line is a frase with autor in parentheses
#output is a csv with two columns: frase, autor

import re
import csv

#read the file
with open('original/frases.clean.txt', 'r') as f:
    frases = f.readlines()

#initialize the csv file
with open('data/frases.clean.csv', 'w') as csvfile:
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
            writer.writerow({'frase': frase, 'autor': autor})
        else:
            print(frase)


