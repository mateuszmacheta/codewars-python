# 6 kyu Pascal's Triangle
# https://www.codewars.com/kata/5226eb40316b56c8d500030f/train/python
import scipy.special

def pascals_triangle(rows):
    triangle = []
    for n in range(rows):
        for k in range(n+1):
            print(f'n: {n} k: {k}')
            triangle.append(int(scipy.special.binom(n, k)))
    return triangle


print(pascals_triangle(1))