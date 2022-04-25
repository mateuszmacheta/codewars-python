# 4 kyu Don't give me five! Really!
# https://www.codewars.com/kata/621f89cc94d4e3001bb99ef4/train/python
import math

def dont_give_me_five(start, end):
    result = 0
    for i in range(min(start,end), max(start,end)+1):
        if str(i).find('5') == -1:
            result += 1
    return result


print(dont_give_me_five(50, 0))