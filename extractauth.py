import re

regex = r"(?<=\().*(?=\))"

#get the text from the file frases.txt and store it in the variable test_str
with open('frases.txt', 'r') as file:
    test_str = file.read()

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    print ("Match {matchNum}: {match}".format(matchNum = matchNum, match = match.group()))