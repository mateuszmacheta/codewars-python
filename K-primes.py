# 5 kyu k-Primes
# https://www.codewars.com/kata/5726f813c8dcebf5ed000a6b/train/python
from gmpy2 import next_prime
from functools import lru_cache

@lru_cache
def check_kprime(n: int, k: int) -> bool: # assuming k >= 2 always
    if n < 2: return False
    prime = 2 # first prime that we're goint to start dividing
    number = n
    prime_factors = 0
    n_2 = n // 2
    while True:
        if prime > n_2: return prime_factors == k # stop looking if we cross sqrt(n) limit
        quotient, remainder = divmod(number, prime)
        if remainder == 0: # this prime is a factor as it divides without remainder
            if quotient == next_prime(quotient - 1): # finish when quotient is also prime
                prime_factors += 2
                return prime_factors == k
            if prime_factors >= k: return False # it has already more than k factors
            prime_factors += 1
            number = quotient
        else:
            prime = next_prime(prime)

def count_Kprimes(k: int, start: int, end: int) -> bool:
    result = []
    for n in range(start, end + 1, 1):
        if check_kprime(n, k): result.append(n)
    return result

print(count_Kprimes(5, 500, 600))

# test for k = 2
# for n in [4, 6, 9, 10, 14, 15, 21, 22]:
#     print(check_kprime(n, 2))

# test for k = 3
# for n in [8, 12, 18, 20, 27, 28, 30]:
#     print(check_kprime(n, 3))

# test for k = 5
# for n in [32, 48, 72, 80, 108, 112]:
#     print(check_kprime(n, 5))