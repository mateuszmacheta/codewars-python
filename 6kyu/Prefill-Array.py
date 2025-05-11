# 6 kyu Prefill an Array
# https://www.codewars.com/kata/54129112fb7c188740000162/train/python

def prefill(n, v=None):
    count = n if type(n) is int else str(n)
    if type(n) is not int and not all(d.isdigit() for d in str(n)): raise TypeError(f'{n} is invalid')
    return [v]*count