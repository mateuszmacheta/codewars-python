# 4 kyu Matrix Determinant
# https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python

import numpy as np

def determinant(matrix):
    np_matrix = np.array(matrix)
    return np.linalg.det(np_matrix)
    


m4 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]
print(determinant(m2))