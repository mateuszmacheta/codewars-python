# 5 kyu Last digit of a large number
# https://www.codewars.com/kata/5511b2f550906349a70004e1/python

def last_digit(n1, n2):
    n1 = n1 % 10
    if n2 == 0:
        return 1
    if n1 == 2:
        return [2, 4, 8, 6][(n2 % 4)-1]
    if n1 == 3:
        return [3, 9, 7, 1][(n2 % 4)-1]
    if n1 == 4:
        return [4, 6][(n2 % 2)-1]
    if n1 == 7:
        return [7, 9, 3, 1][(n2 % 4)-1]
    if n1 == 8:
        return [8, 4, 2, 6][(n2 % 4)-1]
    if n1 == 9:
        return [9, 1][(n2 % 2)-1]
    return n1



print(last_digit(123,504))