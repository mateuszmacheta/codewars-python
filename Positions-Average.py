# 6 kyu Positions Average
# https://www.codewars.com/kata/59f4a0acbee84576800000af/train/python

from itertools import combinations

def pos_average(s):
    s_array = s.split(", ")
    word_length = len(s_array[0])
    total = 0 # total possible number of common posisitons
    common = 0
    for combination in combinations(s_array, 2):
        print(combination)
        total += word_length
        for i in range(word_length):
            common += combination[0][i] == combination[1][i]
    return 100 * common / total


print(pos_average("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"), 26.6666666667)
print("444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490", 29.2592592593)