# 6 kyu Prime Factors
# https://www.codewars.com/kata/542f3d5fd002f86efc00081a/train/python

# SIEVE BEGINS
from math import sqrt, ceil

LIMIT = 200000
MAX_RANGE = ceil(sqrt(LIMIT))

prime_nums = []
numbers = [True] * (MAX_RANGE + 1)

# Commencing sieve
p = 2
while p * p <= MAX_RANGE:
    if numbers[p]:
        for i in range(p * p, MAX_RANGE + 1, p):
            numbers[i] = False
    p += 1

for num in range(2, MAX_RANGE + 1):
    if numbers[num]:
        prime_nums.append(num)

# SIEVE ENDS

def prime_factors (n):
    result = []
    if n == 1: return result
    if n in prime_nums: return [n]
    quotient = n
    i = 0
    while quotient > 1:
        current_prime = prime_nums[i]
        current_quotient, remainder = divmod(quotient, current_prime)
        if remainder == 0:
            result.append(current_prime)
            quotient = current_quotient
        else:
            i += 1  
    return result


print(prime_factors(12))