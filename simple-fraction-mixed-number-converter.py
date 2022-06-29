# 5 kyu Simple fraction to mixed number converter
# https://www.codewars.com/kata/556b85b433fb5e899200003f/train/python

from gmpy2 import bit_scan1 as ctz


def mixed_fraction(s):
    # special cases
    if s.endswith('/0'):
        raise ZeroDivisionError
    if s.startswith('0'):
        return '0'
    sign = '-'*(s.startswith('-') ^ ('/-' in s))
    dividend, divisor = s.split('/')
    dividend = abs(int(dividend))
    divisor = abs(int(divisor))
    integer = dividend // divisor
    # case with fraction simplified to integer
    if dividend / divisor == integer:
        return f'{sign}{integer}'
    # case with mixed number
    dividend = dividend % divisor
    greatest_common_divisor = gcd(dividend, divisor)
    divisor //= greatest_common_divisor
    dividend //= greatest_common_divisor
    return sign + f'{integer} '*(integer != 0) + f'{dividend}/{divisor}'


def gcd(u, v):
    if u == 0: return v
    if v == 0: return u
    #print(bin(u), bin(v))
    i = ctz(u)
    u >>= i
    j = ctz(v)
    v >>= j
    k = min(i, j)
    #print(f'k {k}')
    while True:
        if u > v:  # swap
            u, v = v, u
        v -= u
        if v == 0:
            return u << k
        v >>= ctz(v)
    return -1


if __name__ == '__main__':
    #print(mixed_fraction('-10/7'))
    print(mixed_fraction('5864730/-9235005'))