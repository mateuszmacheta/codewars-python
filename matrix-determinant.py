# 4 kyu Matrix Determinant
# https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python

def determinant(matrix):
    size: int = len(matrix[0])
    if size > 3:
        det = 0
        for y in range(0, size):
            for x in range(0, size):
                #print(f"x: {x}, y: {y}")
                if matrix[y][x]:
                    det += int(-1**(x+y) * matrix[y][x] * determinant(minor_matrix(matrix, y, x)))
        return det

    elif size == 3:
        positive_factors = matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] +\
                            matrix[0][2] * matrix[1][0] * matrix[2][1]
        negative_factors = -matrix[0][2] * matrix[1][1] * matrix[2][0] - matrix[0][0] * matrix[1][2] * matrix[2][1] -\
                           matrix[0][1] * matrix[1][0] * matrix[2][2]
        return positive_factors + negative_factors
    elif size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        return matrix[0][0]

    return 0

def minor_matrix(matrix, y, x):
    minor = [row[:x] + row[x + 1:] for row in matrix[:y]+matrix[y+1:]]
    return minor

m4 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]
print(determinant(m2))