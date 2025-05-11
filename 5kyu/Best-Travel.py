# 5 kyu Best travel
# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/solutions/python

from itertools import combinations

def choose_best_sum(t, k, ls):
    distances = []
    for towns in combinations(ls, k):
        distance = sum(towns)
        if distance == t: return distance
        if distance < t: distances.append(distance)
    return sorted(distances)[-1] if distances else None