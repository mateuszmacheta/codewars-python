# 5 kyu Merged String Checker
# https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python


def peek(l):
    if len(l) > 0: return l[0]
    return None

def is_merge(s, part1, part2):
    part1_lst = list(part1)
    part2_lst = list(part2)
    for c in s:
        if c == peek(part1_lst):
            part1_lst.pop(0)
        elif c == peek(part2_lst):
            part2_lst.pop(0)
        else:
            return False
    return not part1_lst and not part2_lst

print(is_merge('Bananas from Bahamas', 'Bahas', 'Bananas from am'))
# print(is_merge('codewars', 'code', 'wars'))
# print(is_merge('Making progress', 'Mak pross', 'inggre'))
# print(is_merge('codewars', 'cod', 'wars'))