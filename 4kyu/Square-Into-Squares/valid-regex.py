import re

filestream = open('valid-sequences.txt','r')
text = filestream.read()
filestream.close()

output = ''

text = re.findall(r'\[(.+)\]', text)
for match in text:
    output += match + "\n"


filestream = open('valid-sequences2.txt', 'w')
filestream.write(output)