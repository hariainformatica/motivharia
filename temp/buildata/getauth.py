import re
import csv
import os

autores = []
regex = r"(?<=\().*(?=\))"

with open(os.path.realpath('../original/frases.clean.txt'), 'r', encoding='utf-8') as file:
    test_str = file.read()

matches = re.finditer(regex, test_str, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    print ("Match {matchNum}: {match}".format(matchNum = matchNum, match = match.group()))
    #if author is not in the list, add it
    if match.group() not in autores:
        autores.append(match.group())

print("\n\n\nAutores:\n----------")

cont = 1
autores.sort()

with open(os.path.realpath('../../data/autores.csv'), 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='|')
    
    for autor in autores:
        writer.writerow([cont, autor])
        cont += 1
