m4 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

def minor_matrix(matrix, y, x):
    minor = [row[:x] + row[x + 1:] for row in matrix[:y]+matrix[y+1:]]
    return minor

print(minor_matrix(m4,2,1))