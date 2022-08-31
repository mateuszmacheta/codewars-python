# 2 kyu Power tower modulo m
# https://www.codewars.com/kata/5a08b22b32b8b96f4700001c
from functools import lru_cache
from math import gcd, pow

# def tower(base, h, m):
# 	print(base, h, m)
# 	if m == 1:
# 		return 0
# 	if base == 1 or h == 0:
# 		return 1
# 	value = base % m
# 	for _ in range(h):
# 		value = pow(value, base, m)
# 	return value


@lru_cache(maxsize=1000)
def power_with_modulo(base, exponent, modulo):
	G = {i for i in range(1, modulo) if gcd(i, modulo) == 1}
	# b ** (q * totient(m) + r) % m == b ** r % m.
	totient = len(G)
	print(G)
	print(totient)
	if base in G:
		r = exponent % totient
	else:
		print('WTF')
	return pow(base, r % modulo)


if __name__ == '__main__':
	print(power_with_modulo(2, 8, 100000000))
	# print(tower(3, 3, 25), 25)