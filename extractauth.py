import re

autores = []
regex = r"(?<=\().*(?=\))"

with open('frases.txt', 'r') as file:
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
for autor in autores:
    print(f'{cont}:{autor}')
    cont += 1
