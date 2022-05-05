import re

def sp_eng(sentence):
    return re.search(r'English', sentence, re.IGNORECASE)

print(sp_eng("1234english ;k"))