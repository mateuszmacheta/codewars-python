# 5 kyu Square Matrix Multiplication
# https://www.codewars.com/kata/5263a84ffcadb968b6000513

def matrix_mult(a, b):
    col_a, row_a = len(a[0]), len(a)
    col_b, row_b = len(b[0]), len(b)
    if col_a != row_b:
        raise ValueError(f'Unable to perform multiplication:'
                         f' As column number is {col_a} is not the same as Bs row number {row_b}')
    # resulting array has col_b columns and row_a rows
    ab = []
    for row in range(row_a):
        ab_row = []
        for col in range(col_b):
            #print(f'row {row} col {col}')
            ab_row.append(sum(a[row][i] * b[i][col] for i in range(col_a)))
        ab.append(ab_row)
    return ab


if __name__ == '__main__':
    a1 = [ [1, 2],
    [3, 2] ]
    b1 = [ [3, 2],
    [1, 1] ]
    print(matrix_mult(a1, b1))
