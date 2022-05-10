# 4 kyu Square into Squares
# https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python
import math as m


def decompose(n):
    result = dec_inner(n, n**2)
    if result: return result[:-1:]
    return None


def dec_inner(n, total):
    if total == 0:
        return [n]
    i = n -1
    while i > 0:
        if total - i**2 >= 0:
            result = dec_inner(i, total - i**2)
            i = m.isqrt(total - i ** 2)
            if result:
                result.append(n)
                return result
        i -= 1
    return None




print(decompose(5))