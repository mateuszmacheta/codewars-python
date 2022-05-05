# 4 kyu Square into Squares
# https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python

def decompose(n):
    total = n**2
    x = n
    x -= 1
    result = []
    while x > 1:
        square = x**2
        total -= square
        if total == 0:
            result.insert(0, x)
            return result if len(result) >= 2 else None
        if total > 0:
            result.insert(0, x)
        x -= 1
    return None

print(decompose(5))