# 3 kyu Upside-Down Numbers - Challenge Edition
# https://www.codewars.com/kata/59f98052120be4abfa000304/train/python
from math import log, floor

upside = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
center = {'0', '1', '8'}

upside_count = len(upside)
center_count = len(center)

def easy_case(digits: int) -> int:
    # easy case is when we have some number of digits that is not from "edge" cases, like we have start with 4 digits and end with 6 digits
    # then easy case will be 5 digits. In other words all numbers with 5 digits are possible
    # in general for edge cases there may be not all numbers possible, EXCEPT for when whe have edge case with 10, 100, 1000, powers of 10
    # then it's the same easy case
    if digits % 2: # odd number of digits
        count = upside_count ** (digits // 2) * center_count # general case disregarding leading zeroes
        count -= digits // 2 + 1 # we don't count case with 0, 00, 000, ... digits // 2 + 1 case with cente
    else: # even number of digits
        count = upside_count ** (digits // 2) # general case disregarding leading zeroes
        count -= digits // 2 # we don't count case with 0, 00, 000, ... digits // 2 + 1 case with cente
    return count

def hard_case(digits: int, minimum: int, maximum: int) -> int:
    raise NotImplementedError("hard_case function is not yet implemented")

def upsidedown(x: str, y: str) -> int:
    digits_min = len(x)
    digits_max = len(y)
    count = 0
    if digits_min == digits_max:
        raise NotImplementedError("Checking for range where therex limit to same  is not yet implemented")
    for digits in range(digits_min, digits_max + 1):
        logarithm = log(digits, 10)
        is_base_10 = logarithm == floor(logarithm)
        if digits in [digits_min, digits_max] and is_base_10:
            count += easy_case(digits)
        elif digits not in [digits_min, digits_max]:


    return count

if __name__ == '__main__':
    print(upsidedown('0','10'))
    print(upsidedown('10','100'))
    print(upsidedown('10','1000'))

    # print(upsidedown('100000','12345678900000000'))
          