# 3 kyu Make a spiral
# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6
from collections import namedtuple
from itertools import cycle
Move = namedtuple("Move", "x y")

moves_base = [Move(1, 0), Move(0, 1), Move(-1, 0), Move(0, -1)]
moves = cycle(moves_base)

def draw_board(board):
    output = ''
    for row in board:
        for item in row:
            output += str(item)
        output += '\n'
    return output

def spiralize(n):
    board = [[0]*n for i in range(n)]
    x, y = 0, 0
    current_move = next(moves)
    side_size = n - 1
    no_progress = 0
    while True:
        # if two fiels ahead we already have 1
        if board[max(0, min(y + 2 * current_move.y, n - 1))][max(0, min(x + 2 * current_move.x, n - 1))] == 1:
            no_progress += 1
            if no_progress >= 2:
                return board
            current_move = next(moves)
            continue
        no_progress = 0
        board[y][x] = 1
        x = max(0, min(x + current_move.x, n - 1))
        y = max(0, min(y + current_move.y, n - 1))
        print(board)

print(spiralize(5))