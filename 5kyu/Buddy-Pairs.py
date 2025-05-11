# 5 kyu Buddy Pairs
# https://www.codewars.com/kata/59ccf051dcc4050f7800008f/train/python
import math

divisor_sums = dict()

def buddy(start, limit):
    for n in range(start, limit +1):
        if n in divisor_sums:
            divisor_sum_n = divisor_sums[n]
        else:
            divisor_sum_n = get_divisor_sum(n)
            divisor_sums[n] = divisor_sum_n

        m = divisor_sum_n - 1
        if m <= n:
            continue

        if m in divisor_sums:
            divisor_sum_m = divisor_sums[m]
        else:
            divisor_sum_m = get_divisor_sum(m)
            divisor_sums[m] = divisor_sum_m
        if divisor_sum_m - 1 == n:
            return [n, m]

    return "Nothing"


def get_divisor_sum(num):
    sum = 1
    sqrt = math.isqrt(num)
    for i in range(2, sqrt):
        if num % i == 0:
            print(i, num // i)
            sum += i + num // i
    if sqrt**2 == num: sum -= sqrt
    return sum


#print(buddy(10,50))
print(buddy(310,2755))