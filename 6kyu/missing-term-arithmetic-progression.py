# 6 kyu Find the missing term in an Arithmetic Progression
# https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python


def find_missing(seq):
    delta = [b - a for a, b in zip(seq[0:3], seq[1:4])] # sequence length at least 4
    unique_steps = set(delta) # check what is regular step value
    step = None
    if len(unique_steps) == 2:
        for u in unique_steps:
            if delta.count(u) > 1:
                step = u
                break
    else: step = delta[0]

    for i in range(1, len(seq)): # is step is not a regular one, just return missing value
        delta = seq[i] - seq[i-1]
        if delta != step:
            return seq[i-1] + step
    return None

print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]))