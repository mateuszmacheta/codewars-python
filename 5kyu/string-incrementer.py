# 5 kyu String Incrementer
# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

import re

def increment_string(strng: str):
    return strng + '1' if not re.match(r'^.+\d+$', strng) else increment(strng)

def increment(strng: str):
    length = len(strng)
    m = re.search('\d+$', strng)
    number_part = strng[m.start():]
    number = int(number_part)
    number += 1
    return strng[0:m.start()] + str(number).zfill(length-m.start())


print(increment_string("lentils001"))
