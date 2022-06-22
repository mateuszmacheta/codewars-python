# 6 kyu Base Conversion
# https://www.codewars.com/kata/526a569ca578d7e6e300034e/train/python

bin      = '01'
oct      = '01234567'
dec      = '0123456789'
hex      = '0123456789abcdef'
allow    = 'abcdefghijklmnopqrstuvwxyz'
allup    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def convert(input, source, target):
    sourceBase = len(source)
    targetBase = len(target)
    # to decimal
    value = 0
    for i, e in enumerate(reversed(input)):
        value += source.index(e)*sourceBase**i
    print(f'decimal value: {value}')
    if target == dec:
        return str(value)
    # to target base
    number = int(value)
    result = ''
    if number == 0:
        return target[0]
    while number > 0:
        result += target[number % targetBase]
        number //= targetBase
    return result[::-1]


if __name__ == '__main__':
    # print(convert("15", dec, bin))
    print(convert("hello", allow, hex))