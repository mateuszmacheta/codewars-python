# 5 kyu Longest Common Subsequence
# https://www.codewars.com/kata/52756e5ad454534f220001ef

import numpy


def lcs(x, y):
    print(x, type(x), y, type(y))
    if len(x) == 0 or len(y) == 0: return ''
    if len(x) == len(y) == 1:
        return x if x == y else ''
    matrix = build_matrix(x, y)
    return get_sequence(x, y, matrix)

# Dynamic Programming | Set 4 (Longest Common Subsequence) | GeeksforGeeks - YouTube
# https://www.youtube.com/watch?v=HgUOWB0StNE


def build_matrix(x: str, y: str):
    n = len(x)
    m = len(y)
    matrix = numpy.zeros([n + 1, m + 1], int)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                matrix[i, j] = matrix[i - 1, j - 1] + 1
            else:
                matrix[i, j] = max(matrix[i - 1, j], matrix[i, j - 1])
    return matrix


def get_sequence(x: str, y: str, matrix: numpy.matrix):
    sequence = []
    n, m = matrix.shape
    i = n - 1
    j = m - 1
    current = matrix[i, j]
    while current > 0:
        if current != max(matrix[i - 1, j], matrix[i, j - 1]):  # pick character
            sequence.insert(0, x[i - 1])
            i = i - 1
            j = j - 1
        else:
            if matrix[i - 1, j] > matrix[i, j - 1]:  # upper cell has max value - move up
                i = i - 1
            else:  # left cell has max value - move left
                j = j - 1
        current = matrix[i, j]
    return ''.join(sequence)


if __name__ == '__main__':
    x = 'GXTXAYB'
    y = 'AGGTAB'
    m = build_matrix(x, y)
    print(get_sequence(x, y, m))