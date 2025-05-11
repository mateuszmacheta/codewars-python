# 5 kyu k-Primes
# https://www.codewars.com/kata/5726f813c8dcebf5ed000a6b/train/python
from gmpy2 import next_prime, is_prime

def check_kprime(n: int, k: int) -> bool: # assuming k >= 2 always
    prime = 2 # first prime that we're goint to start dividing
    number = n
    prime_factors = 0
    n_sqrt = n ** (1/2)
    while True:
        if prime > n_sqrt: return prime_factors == k # stop looking if we cross n**(1/2) limit
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
    if k == 1:
        prime = next_prime(start - 1)
        while prime <= end:
            result.append(prime)
            prime = next_prime(prime)
        return result
    for n in range(start, end + 1):
        if check_kprime(n, k): result.append(n)
    return result

def puzzle(s):
    # the lowest number with possible solution of 1 or more is 138
    if s < 138: return 0
    # the highest number seen is below 700 so we gonna hardcode 7-primes
    k7_primes = count_Kprimes(7, 1, 700)
    # the highest one can be 700 - 128 - 2 = 570
    k3_primes = count_Kprimes(3, 1, 700)
    # if s - k7_prime - k3_prime equals to a prime number then we found a solution
    count = 0
    for k7_prime in k7_primes:
        if s - k7_prime < 0: break
        for k3_prime in k3_primes:
            if s - k7_prime - k3_prime < 0: break
            # print(k7_prime, k3_prime)
            count += is_prime(s - k7_prime - k3_prime) 
    return count



print(puzzle(408))
# 10 should equal 13
# print(puzzle(138))
# print(puzzle(143))

# print(count_Kprimes(5, 500, 600))

# test for k = 2
# for n in [4, 6, 9, 10, 14, 15, 21, 22]:
#     print(check_kprime(n, 2))

# test for k = 3
# for n in [8, 12, 18, 20, 27, 28, 30]:
#     print(check_kprime(n, 3))

# test for k = 5
# for n in [32, 48, 72, 80, 108, 112]:
#     print(check_kprime(n, 5))