# 6 kyu Operation Transformation
# https://www.codewars.com/kata/579ef9607cb1f38113000100/train/python

from math import log, floor

is_power_of_2 = lambda x: floor(log(x, 2)) == log(x, 2)

def operation(a,b):
    if is_power_of_2(a):
        return abs(log(a, 2) - log(b, 2))
    n = a
    count = 0
    while not is_power_of_2(n):
        if n % 2 == 1:
            n = (n - 1) // 2
        else:
            n //= 2
        count += 1
    return count + abs(log(n, 2) - log(b, 2))


print(operation(3, 8))