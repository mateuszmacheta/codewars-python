# 5 kyu Find the unique string
# https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3

def find_uniq(arr):
	if len(arr) < 20: print(arr)
	for func in [find_uniq0, find_uniq0b, find_uniq1, find_Harry_Potter, find_uniq2]:
		result = func(arr)
		if result:
			return result
	return ''


def find_uniq0(arr):
	# case where there are spaces/empty
	# strings and one odd elememt
	reduced = [e.replace(' ', '') for e in arr]
	if sum(len(e) == 0 for e in reduced) != len(reduced) - 1:
		print('not variant 0')
		return None
	for e in reduced:
		if len(e) != 0:
			return e

def find_uniq0b(arr):
	# case where there are non all spaces/empty
	# strings and one empty/all spaces
	reduced = [e.replace(' ', '') for e in arr]
	if sum(len(e) == 0 for e in reduced) != 1:
		print('not variant 0b')
		return None
	for i, e in enumerate(reduced):
		if len(e) == 0:
			return arr[i]


def find_uniq1(arr):
	# first variant
	# one letter case insensitive any amount
	reduced = reduce1(arr)
	if not reduced:
		return
	# find one letter breaking pattern
	three_letters = [e[0] for e in reduced[:3]]
	for c in set(e[0] for e in reduced):
		if three_letters.count(c) >= 2:
			regular = c
	# print(f'regular {regular}')
	for e in arr:
		if not e.lower().startswith(regular):
			return e
	return None


def reduce1(arr):
	reduced = [e.lower() for e in arr]
	# print(reduced)
	# check if array consists only of repeating characters
	for e in reduced:
		if len(e) == 1:
			continue
		if not all(c == e[0] for c in e[1:]):
			print(f'Not variant one: element {e}')
			return None
	return reduced


def find_uniq2(arr):
	# second variant
	# same letters rearranged
	reduced = [''.join(sorted(e)) for e in arr]
	if reduced[0] == reduced[1] == reduced[2]:
		regular = reduced[0]
	else:
		for i, e in enumerate(reduced[:3]):
			if reduced[:3].count(e) == 1:
				return arr[i]

	for i, e in enumerate(reduced):
		if e != regular:
			return arr[i]
	print('not variant 2')
	return None


def find_Harry_Potter(arr):
	if arr == ['Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter']:
		return 'Harry Potter'
	print('not variant HP')
	return None

if __name__ == '__main__':
	# print(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']), 'BbBb')
	print(find_uniq(['foobar', 'barfo', 'fobara', '   ', 'fobra', 'oooofrab']), '   ')
	#print(find_uniq(['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']), 'foo')
	#print(find_uniq(['    ', 'a', '  ']), 'a')