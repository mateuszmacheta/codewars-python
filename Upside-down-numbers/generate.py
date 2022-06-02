# 3 kyu Upside-Down Numbers - Challenge Edition
# https://www.codewars.com/kata/59f98052120be4abfa000304/train/python
# attempt at generating valid numbers

import itertools

upside = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
center = {'0', '1', '8'}

MAX_LEN = 4
valid = set(center)


def generate():
    for l in range(2, MAX_LEN, 2):
        print(l)
        half_size = l // 2
        pool = list(itertools.product(upside, repeat=half_size))
        for e in pool:
            half = ''.join(e)
            new = half + half[::-1].translate(str.maketrans(upside))
            # new_trimmed = new.lstrip('0')
            # if len(new_trimmed) != l: continue
            valid.add(new) # add element of length l
            for c in center: # add elements of length l + 1 (odd)
                if half_size == 1: print(new[:half_size] + c + new[half_size:])
                valid.add(new[:half_size//2] + c + new[half_size//2:])
    return True


def upsidedown(x: str, y: str):
    pass


if __name__ == '__main__':
    print(generate())
    print(valid)