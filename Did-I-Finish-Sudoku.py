# 5 kyu Did I Finish my Sudoku?
# https://www.codewars.com/kata/53db96041f1a7d32dc0004d2/train/python

def done_or_not(board):
    reference = {1,2,3,4,5,6,7,8,9}
    # validate rows
    for row in board:
        if set(row) != reference:
            return 'Try again!'
    # validate columns
    for i in range(9):
        row = {board[j][i] for j in range(9)}
        if row != reference:
            return 'Try again!'
    # validate squares:
    for x in range(3):
        for y in range(3):
            #print(f'x: {x*3} y: {y*3}')
            if not validate_square(board, x*3, y*3): return 'Try again!'
    return 'Finished!' #'Try again!'

def validate_square(board, start_x, start_y):
    reference = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    square = set()
    for x in range(3):
        for y in range(3):
            #print(f"adding y {start_y+y} x {start_x+x} item {board[start_y+y][start_x+x]}")
            square.add(board[start_y+y][start_x+x])
    if square != reference:
        return False
    return True

done1 =                 [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]

not_done =              [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]

print(done_or_not(not_done))