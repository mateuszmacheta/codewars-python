# 2 kyu The position of a digital string in a infinite digital string
# https://www.codewars.com/kata/582c1092306063791c000c00/train/python
#import numpy as np

def not_early_bird(number: int) -> int:
    i = 1
    while i * i < number:
        i = i + 1
    return i + 1

def find_position(s) -> int:
    number = int(s)
    return not_early_bird(number)

print(not_early_bird(9))
# print(find_position('10'))
# print(find_position('100'))
# print(find_position('1000'))



1940823735834114