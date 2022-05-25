# 5 kyu Factorial decomposition
# https://www.codewars.com/kata/5a045fee46d843effa000070/train/python

import math
import time

primes = set() # prepare set of primes

def check_prime(n):
    for i in range(math.isqrt(n), 1, -1):
        div = n / i
        if div == n // i: return False
    return True

for i in range(3, 4001):
    if check_prime(i): primes.add(i)


def decomp(n):
    factorial = list(range(2, n + 1))
    decomposed = dict()
    for div in range(2, n + 1):
        was_divided = True
        while was_divided:
            was_divided = False
            for i, e in enumerate(factorial):
                fraction = e / div
                if fraction == e // div:
                    was_divided = True
                    factorial[i] = fraction
                    if div in decomposed:
                        decomposed[div] = decomposed[div] + 1
                    else:
                        decomposed[div] = 1
            if 1.0 in factorial: factorial.remove(1.0)
    return ' * '.join(f'{e}^{decomposed[e]}' if decomposed[e] > 1 else f'{e}' for e in decomposed)

tic = time.perf_counter()
print(decomp(4000))
toc = time.perf_counter()

print(f'Execution time {toc - tic:0.2f}')