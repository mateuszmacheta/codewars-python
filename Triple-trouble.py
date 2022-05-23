# 6 kyu Triple trouble
# https://www.codewars.com/kata/55d5434f269c0c3f1b000058/train/python

import re

def triple_double(num1, num2):
    s1, s2 = str(num1), str(num2)
    for e in re.findall(r'(\d)\1{2}', s1):
        if re.findall(e + '{2}', s2): return 1
    return 0

print(triple_double(451999277, 41177722899))