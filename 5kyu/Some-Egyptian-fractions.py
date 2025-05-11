# 5 kyu Some Egyptian fractions
# https://www.codewars.com/kata/54f8693ea58bce689100065f/train/python
from math import ceil, gcd


def from_decimal_representation(n: str):
	x_s = n.replace('.', '')
	x_s = x_s.lstrip('0')
	y = 10 ** (len(n) - n.index('.') - 1)
	return f'{x_s}/{y}'


def simplify(a: int, b: int):
	divisor = gcd(a, b)
	return a // divisor, b // divisor


def decompose(n: str):
	if n == '0':
		return []
	if '/' not in n:
		n = from_decimal_representation(n)
	else:
		a, b = map(int, n.split('/'))
		a, b = simplify(a, b)
		if a == 1:
			return ['{}/{}'.format(a, b)]
		fraction = a / b
		if fraction == ceil(fraction):
			return ['{}'.format(int(fraction))]
	expansion = [n]
	return decompose_inner(expansion)


def decompose_inner(expansion: list) -> list:
	if expansion[-1].startswith('1/'):  # final case when we have all fractions of 1/x format
		return expansion
	x, y = map(int, expansion[-1].split('/'))  # https://en.wikipedia.org/wiki/Greedy_algorithm_for_Egyptian_fractions
	expansion.pop(-1)
	if ceil(y / x) == 1:
		expansion.append('1')
	else:
		expansion.append(str('1/') + str(ceil(y / x)))
	second_term = simplify(-y % x, (y * ceil(y / x)))
	expansion.append('{}/{}'.format(*second_term))
	return decompose_inner(expansion)



if __name__ == '__main__':
	# print(from_decimal_representation('0.06'))
	# print(decompose('3/4'), ["1/2", "1/4"])
	# print(decompose('4/5'), ["1/2", "1/4", "1/20"])
	# print(decompose('7/15'))
	# print(decompose('0.66'), ["1/2", "1/7", "1/59", "1/5163", "1/53307975"])
	# print(decompose('1.25'), ["1", "1/4"])
	print(decompose('2/8'), ["1/4"])