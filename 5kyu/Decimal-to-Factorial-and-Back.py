# 5 kyu Decimal to Factorial and Back
# https://www.codewars.com/kata/54e320dcebe1e583250008fd/train/python

digits = {str(i): i for i in range(10)}
offset = 55
for i in range(ord('A'), ord('Z') + 1):
	digits[chr(i)] = i - offset

digits_inversed = {digits[key]: key for key in digits.keys()}


def dec_2_fact_string(nb):
	'''
	Using method described in https://en.wikipedia.org/wiki/Factorial_number_system#Definition
	'''
	divider = 1
	number = nb
	result = []
	while number:
		number, remainder = divmod(number, divider)
		result.insert(0, digits_inversed[remainder])
		divider += 1

	return ''.join(result)


def fact_string_2_dec(string):
	result = 0
	multiplier = 1
	for i, e in enumerate(string[-2::-1], 1):
		#print(f'i {i} e {e}')
		multiplier *= i
		result += digits[e] * multiplier

	return result

if __name__ == '__main__':
	# print(dec_2_fact_string(463), "341010")
	print(fact_string_2_dec("341010"), 463)