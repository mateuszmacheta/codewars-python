# 6 kyu Bingo Card
# https://www.codewars.com/kata/566d5e2e57d8fae53c00000c/train/python
import random

def get_bingo_card():
    t = 'BINGO'
    return list(e + str(r) for i, e in enumerate(t) for r in random.sample(range(15*i, 15*i + 15), 4 if e == 'N' else 5))


if __name__ == '__main__':
    print(get_bingo_card())