# 4 kyu parseInt() reloaded
# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/train/python
import re


def parse_int(s: str):
    numbers = [None, None, None]
    original = s.replace(' and', '')
    million_index = original.find('million')
    thousand_index = original.find('thousand')
    # million multiplier
    if million_index > 0:
        numbers[2] = original[:million_index]
    # thousand multiplier:
    if thousand_index > 0:
        numbers[1] = original[million_index + len('million') if million_index > 0 else 0:thousand_index]
        # the rest
    numbers[0] = original[max(million_index + len('million') if million_index > 0 else 0,
                           thousand_index + len('thousand') if thousand_index > 0 else 0, 0):]

    total = 0
    for i in range(0, len(numbers)):
        multiplier = 10 ** (i * 3)
        print(multiplier)
        if numbers[i] is not None:
            total += parse_sub_thousand(numbers[i]) * multiplier
    return total


def parse_sub_thousand(s: str):
    numbers = s.replace('and', '')
    numbers = numbers.split('hundred')
    total = 0
    if len(numbers) == 2:
        total = parse_sub_hundred(numbers[0]) * 100 + parse_sub_hundred(numbers[1])
    else:
        total = parse_sub_hundred(numbers[0])
    return total


def parse_sub_hundred(s: str):
    original = s
    total = 0
    digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
              'nine': 9}
    teens = {'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
             'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19}
    tenths = {'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
              'eighty': 80, 'ninety': 90}
    for key in tenths:
        if key in original:
            original = original.replace(key, '')
            total += tenths[key]
    for key in teens:
        if key in original:
            original = original.replace(key, '')
            total += teens[key]
    for key in digits:
        if key in original:
            original = original.replace(key, '')
            total += digits[key]
    return total


print(parse_int('two hundred forty-six'))
# print(parse_int('seven hundred eighty-three thousand nine hundred and nineteen'))
#print(parse_int('seven million seven hundred eighty-three thousand nine hundred and nineteen'))
