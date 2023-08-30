# 5 kyu Merged String Checker
# https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python


def peek(l, offset=0):
    if len(l) > offset: return l[offset]
    return None

def is_merge(s, part1, part2):
    part1_lst = list(part1)
    part2_lst = list(part2)
    consecutive = 0
    for c in s:
        if c == peek(part1_lst, consecutive) == peek(part2_lst, consecutive):
            consecutive += 1
        elif c == peek(part1_lst, consecutive):
            for _ in range(consecutive + 1): part1_lst.pop(0)
            consecutive = 0
        elif c == peek(part2_lst, consecutive):
            for _ in range(consecutive + 1): part2_lst.pop(0)
            consecutive = 0
        elif consecutive:
            if part1_lst:
                for _ in range(consecutive): part1_lst.pop(0)
            elif part2_lst:
                for _ in range(consecutive): part2_lst.pop(0)
            else:
                return False
        else:
            return False
    return not part1_lst and not part2_lst

# print(is_merge('Bananas from Bahamas', 'Bahas', 'Bananas from am'), True)
print(is_merge('DOpDD;7X_zB` J:', 'D;7X_` J:', 'DOpDzB'), True)

# print(is_merge('codewars', 'code', 'wars'))
# print(is_merge('Making progress', 'Mak pross', 'inggre'))
# print(is_merge('codewars', 'cod', 'wars'))