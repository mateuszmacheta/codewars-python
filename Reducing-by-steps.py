# 6 kyu Reducing by steps
# https://www.codewars.com/kata/56efab15740d301ab40002ee/train/python
from math import gcd as gcdi
from math import lcm as lcmu
from operator import add as som

maxi = max
mini = min

def oper_array(fct, arr, init):
    o = []
    curr = init
    for e in arr:
        curr = fct(e, curr)
        o.append(curr)
    return o


if __name__ == '__main__':
    a = [18, 69, -90, -78, 65, 40]
    print(oper_array(som, a, a[0]), '\n', [18, 18, -90, -90, -90, -90 ])
    print(oper_array(gcdi, a, a[0]), '\n', [ 18, 3, 3, 3, 1, 1 ])
    print(oper_array(mini, a, a[0]))