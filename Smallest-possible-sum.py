# 4 kyu Smallest possible sum
# https://www.codewars.com/kata/52f677797c461daaf7000740/train/python

from math import gcd

def solution(a):
    if len(a) == 1:
        return a[0]
    o = gcd(a[0], a[1])
    for e in a[1:]:
        o = gcd(o, e)
    return o*len(a)