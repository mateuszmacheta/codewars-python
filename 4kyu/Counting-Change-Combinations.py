# 4 kyu Counting Change Combinations
# https://www.codewars.com/kata/541af676b589989aed0009e7
import itertools as it

def count_change(money, coins):
    smallest = min(coins)
    max_coins = money // smallest
    if max_coins * smallest == money:
        # case where max amount of coins  adds up to exact money amount
        total = 1
        max_coins -= 1
    else:
        total = 0

    for i in range(2, max_coins + 1):
        combinations = it.combinations_with_replacement(coins, i)
        total += sum(sum(e) == money for e in combinations)
    return total


def sum_with_limit(l: list, limit: int):
    # will return True with sum is equal to limit, otherwise False
    total = 0
    for e in l:
        total += e
        if total > limit: return False
    return total == limit

# def combine_with_limit(l: list, r: int, limit: int):
#     total = 0
#     n = len(l)
#     combination_count = int(scipy.special.binom(n + r - 1, r))
#     return total


if __name__ == '__main__':
    print(count_change(10, [5,2,3]))