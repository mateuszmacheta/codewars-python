# 3 kyu The Millionth Fibonacci Kata
# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python

from decimal import Decimal, getcontext

# set decimal precision to following number of digits
getcontext().prec = 10000

root_5 = Decimal(5).sqrt()
Phi = (Decimal(1) + root_5) / Decimal(2)
phi = (Decimal(1) - root_5) / Decimal(2)


def fib(n):
	if n > 10000:
		return fib_huge(n)
	# Binets formula
	return round((Phi ** n - phi ** n) / root_5)


def fib_huge(n):
	# Lucas sequence identities
	a = q = 1
	b = p = 0
	while n > 0:
		if n % 2 == 0:
			qq = q * q
			q = 2 * p * q + qq
			p = p * p + qq
			n //= 2
		else:
			aq = a * q
			a = b * q + aq + a * p
			b = b * p + aq
			n -= 1
	return b
