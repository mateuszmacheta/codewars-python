# 5 kyu Closest and Smallest
# https://www.codewars.com/kata/5868b2de442e3fb2bb000119/train/python
from itertools import combinations


get_weight = lambda number: sum(int(c) for c in number)
 

def candidates_win(first_candidate, second_candidate, top_pair):
    candidates_weight_difference = abs(first_candidate[0] - second_candidate[0])
    top_pair_weight_difference = abs(top_pair[0][0] - top_pair[1][0])
    # score is based on wegith difference, weight sume and indexes sum
    if candidates_weight_difference < top_pair_weight_difference:
        return True
    if candidates_weight_difference == top_pair_weight_difference:
        # lower weights
        candidates_weight = first_candidate[0] + second_candidate[0]
        top_weight = top_pair[0][0] + top_pair[1][0]
        if  candidates_weight < top_weight:
            return True
        if candidates_weight == top_weight:
            # lower indexes
            if first_candidate[1] + second_candidate[1] <  top_pair[0][1] + top_pair[1][1]:
                return True
    return False

def closest(strng):
    if not strng: return []
    arr = strng.split()
    top_pair = [[-10e10, 10e10, -1], [10e10, 10e10, -1]] # weight, index, actual value
    for pair in combinations(enumerate(arr), 2):
        first_candidate = [get_weight(pair[0][1]), pair[0][0], int(pair[0][1])]
        second_candidate = [get_weight(pair[1][1]), pair[1][0], int(pair[1][1])]
        if candidates_win(first_candidate, second_candidate, top_pair):
            top_pair = [first_candidate, second_candidate]
    return sorted(top_pair, key = lambda item: 1000 * item[0] + item[1])


# print(closest(""), [])
# print(closest("103 123 4444 99 2000 "), [[2, 4, 2000], [4, 0, 103]])
print(closest("456899 50 11992 176 272293 163 389128 96 290193 85 52"), [[13, 9, 85], [14, 3, 176]])
# print(closest("239382 162 254765 182 485944 134 468751 62 49780 108 54"), [[8, 5, 134], [8, 7, 62]])
# print(closest("241259 154 155206 194 180502 147 300751 200 406683 37 57"), [[10, 1, 154], [10, 9, 37]])
# print(closest("89998 187 126159 175 338292 89 39962 145 394230 167 1"), [[13, 3, 175], [14, 9, 167]])
