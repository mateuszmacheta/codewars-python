# 4 kyu Don't give me five! Really!
# https://www.codewars.com/kata/621f89cc94d4e3001bb99ef4/train/python
import math

def dont_give_me_five(start, end):
    result = 0
    for i in range(start, end+1):
        if not check_five(i):
            result += 1
    return result


def check_five(i: int):

    return False


dont_give_me_five(-17,9)