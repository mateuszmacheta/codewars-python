# 6 kyu Word a10n (abbreviation)
# https://www.codewars.com/kata/5375f921003bf62192000746/train/python

import re

def abbreviate(s):
    words = re.split(r'[^a-zA-Z]', s)
    separators = re.sub(r'[a-zA-Z]', '', s)
    words = [shorten(w) for w in words]
    print(words)
    print(separators)
    separators = list(separators)
    output = ''
    for i, e in enumerate(words[:-1]):
        output = output + words[i] + separators[i]
    return output + words[-1]

def shorten(s):
    l = len(s)
    if l <= 4: return s
    return s[0] + str(l-2) + s[-1]


print(abbreviate("elephant-ride"))