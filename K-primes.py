# 5 kyu k-Primes
# https://www.codewars.com/kata/5726f813c8dcebf5ed000a6b/train/python
import time
from math import sqrt, ceil

start_time = time.time()
LIMIT = 20000000
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

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print(len(prime_nums))
print(elapsed_time)
