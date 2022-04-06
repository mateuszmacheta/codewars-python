# 4 kyu Differentiate a polynomial
# https://www.codewars.com/kata/566584e3309db1b17d000027/train/python

import re

def differentiate(equation, point):
    equation = re.sub(r'\+x', '+1x', equation)
    equation = re.sub(r'\-x', '-1x', equation)
    equation = re.sub(r'^x', '1x', equation)
    elements = re.finditer(r'([+-]?\d*x(?:\^\d+)?)', equation)
    sum = 0
    for e in elements:
        text = e.group(0)
        text = text.replace('+', '')
        print(text)
        if text.__contains__('^'):
            old_power = int(text.split('^')[1])
            power = old_power - 1
            multiply = int(text.split('x')[0]) * old_power
            sum += multiply * point ** power
        else:
            multiply = int(text.split('x')[0])
            sum += multiply
    return sum


#print(differentiate("-5x^2+10x+4", 3))
print(differentiate("x^2-x", 3))