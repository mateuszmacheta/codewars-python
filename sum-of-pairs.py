# 5 kyu Sum of pairs
# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python

def sum_pairs(ints, s):
    # compose set containing numbers as keys and their indexes as values
    # only numbers that are half of sum will have two indexes
    set_ints = {}
    for e, i in zip(ints, range(0, len(ints))):
        if e not in set_ints:
            set_ints[e] = [i]
        elif 2*e == s and len(set_ints[e]) == 1:
            set_ints[e].append(i)
    # search for number - index pairs that have correct sum and the lowest indexes
    lowest = Number_Index_Pair([None, None], [10e10, 10e10])
    if s % 2 == 0 and s // 2 in set_ints and len(set_ints[s // 2]) == 2:
        lowest.update([s // 2, s // 2], set_ints[s // 2])
    for e in set_ints:
        if s - e in set_ints and s - e != e:
            temp = Number_Index_Pair([e, s - e], [set_ints[e][0], set_ints[s - e][0]])
            if temp < lowest:
                lowest.update([e, s - e], [set_ints[e][0], set_ints[s - e][0]])

    return lowest.numbers if lowest.numbers[0] is not None else None


class Number_Index_Pair:
    def __init__(self, numbers: list, indexes: list):
        self.numbers = None
        self.indexes = None
        self.update(numbers, indexes)
        if len(numbers) != 2 or len(indexes) != 2:
            raise Exception("Incorrect number of arguments: {} number(s), {} index(es)".format(len(numbers), len(indexes)))

    def update(self, numbers: list, indexes: list):
        # indexes always in ascending order
        if indexes[0] > indexes[1]:
            self.numbers = [numbers[1], numbers[0]]
            self.indexes = [indexes[1], indexes[0]]
        else:
            self.numbers = numbers
            self.indexes = indexes

    def __lt__(self, other):
        # one object is smaller if higher index is smaller than other higher index
        return self.indexes[1] < other.indexes[1]

# one = Number_Index_Pair([5, 5], [1, 5])
# two = Number_Index_Pair([3, 7], [3, 4])
#
# print(one < two)
# print(two < one)

l1= [1, 4, 8, 7, 3, 15]
l2= [1, 4, 8, 7, 4, 15]
l6= [4, -2, 3, 3, 4]

#print(sum_pairs(l1,8))
# print(sum_pairs(l6,8))
print(sum_pairs([20, -13, 40], -7))
