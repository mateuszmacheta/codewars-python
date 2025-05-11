# 5 kyu Binary Contiguous Array
# https://www.codewars.com/kata/60aa29e3639df90049ddf73d/train/python
# see also 5 kyu Longest sequence with zero sum https://www.codewars.com/kata/52b4d1be990d6a2dac0002ab

def binarray(s) -> int:
    sum_index = dict()
    sum = 0
    max_len = 0
    for i in range(len(s)):
        e = 1 if s[i] else -1
        sum += e
        if sum == 0:
            max_len = max(max_len, i + 1)
        elif sum in sum_index:
            max_len = max(max_len, i - sum_index[sum])
        else:
            sum_index[sum] = i

    return max_len


if __name__ == '__main__':
    # print(binarray([0, 1]), 2)
    # print(binarray([0]), 0)
    print(binarray([1, 1, 0, 1, 1, 0, 1, 1]), 4)
    # print(binarray([0, 1, 1, 0, 1, 1, 1, 0, 0, 0]), 10)
    # print(binarray([0, 0, 1, 1, 1, 0, 0, 0, 0, 0]), 6)