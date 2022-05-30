import numpy as np

def transpose(m): return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]



if __name__ == '__main__':
    print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))