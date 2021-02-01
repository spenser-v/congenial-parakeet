from pathlib import Path
import re

file = open(Path.home() / 'madlib.txt')
text = file.read()
file.close()

regex = re.compile(r'adjective|noun|adverb|verb', re.I)
for i in regex.findall(text):
    if i != '':
        reg = re.compile(r'{}'.format(i))
        inp_text = input('Enter the substitute for %s: ' %i)
        text = reg.sub(inp_text, text, 1)

print(text)
file = open(Path.home() / 'madlib_ans.txt', 'w')
file.write(text)
file.close()
