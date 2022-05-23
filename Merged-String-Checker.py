# 5 kyu Merged String Checker
# https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python
import re


def is_merge(s, part1, part2):
    copy = str(s)
    try:
        for c in part1 + part2:
            indexes = re.finditer(c, copy)
            for i in (e.start() for e in indexes):
                copy = copy.replace(copy[i], '_', 1)
    except Exception:
        return False

    if copy != '_'*len(s):
        return False

    part1 = to_numbers(part1, s)
    part2 = to_numbers(part2, s)
    return all(a < b for a, b in zip(part1[:-1], part1[1:])) and all(a < b for a, b in zip(part2[:-1], part2[1:]))


def to_numbers(part, s):
    numbers = []
    for c in part:
        indexes = re.finditer(c, s)
        for i in indexes:
            numbers.append(i.start())
    return numbers

# print(is_merge('codewars', 'code', 'wars'))
print(is_merge('Making progress', 'Mak pross', 'inggre'))
# print(is_merge('codewars', 'cod', 'wars'))