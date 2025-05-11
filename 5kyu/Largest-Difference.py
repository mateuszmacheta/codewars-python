# 5 kyu Largest Difference in Increasing Indexes
# https://www.codewars.com/kata/52503c77e5b972f21600000e/train/python
from itertools import combinations


def largest_difference(data):
    biggest = 0
    for pair in combinations(enumerate(data), 2):
        number_difference = pair[1][1] - pair[0][1]
        if number_difference < 0: continue
        index_difference = pair[1][0] - pair[0][0]
        if index_difference > biggest:
            biggest = index_difference
    return biggest


print(largest_difference([9, 4, 1, 10, 3, 4, 0, -1, -2]), 4)
print(largest_difference([3, 2, 1]), 0)
print(largest_difference([1, 2, 3]), 2)
print(largest_difference([9, 4, 1, 2, 3, 0, -1, -2]), 2)
print(largest_difference([9, 4, 1, 2, 3, 4, 0, -1, -2]), 4)
print(largest_difference([78, 88, 64, 94, 17, 91, 57, 69, 38, 62, 13, 17, 35, 15, 20]), 10)
print(largest_difference([4, 3, 3, 1, 5, 2]), 4)