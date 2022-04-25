# 4 kyu Don't give me five! Really!
# https://www.codewars.com/kata/621f89cc94d4e3001bb99ef4/train/python
import math


def dont_give_me_five(start: int, end: int):
    if math.copysign(1, start) != math.copysign(1, end):
        a = no_five(str(abs(start)))
        b = no_five(str(abs(end)))
        print(f"a {a} b {b}")
        return a + b - 1
    return no_five(str(max(abs(start), abs(end))))\
        - no_five(str(min(abs(start), abs(end)))) + 1


def no_five(n: str):
    digits = {'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    if len(n) <= 1:
        return digits[n]
    lower_part = str(int(n[0])-1) + '9'*(len(n)-1)
    # calculate top part
    if n[0] != '5':
        stripped = n[1:].lstrip('0')
        top_value = no_five(stripped) if len(stripped) > 0 else 0
    else:
        top_value = 0
    return top_value + math.prod(digits[d] for d in lower_part)



print(dont_give_me_five(-60, -53))