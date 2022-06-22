# 6 kyu Number Zoo Patrol
# https://www.codewars.com/kata/5276c18121e20900c0000235/train/python

def find_missing_number(numbers):
    total = sum(numbers)
    l = len(numbers)
    theoretical_sum = (l + 1) * (l + 2) // 2
    return theoretical_sum - total


if __name__ == '__main__':
    print(find_missing_number([1, 2, 3]))