# 6 kyu Who won the election?
# https://www.codewars.com/kata/554910d77a3582bbe300009c/train/python

from collections import Counter as c

def get_winner(ballots):
    c_ballots = c(ballots)
    max_votes = max(c_ballots.values())
    if max_votes <= len(ballots) / 2: return None
    c_ballots = {key: value for key, value in c_ballots.items() if value == max_votes}
    return next(iter(c_ballots)) if len(c_ballots) == 1 else None