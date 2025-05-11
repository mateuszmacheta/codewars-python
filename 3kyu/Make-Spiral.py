# 3 kyu Make a spiral
# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6
from collections import namedtuple
from itertools import cycle
Move = namedtuple("Move", "x y")

moves_base = [Move(1, 0), Move(0, 1), Move(-1, 0), Move(0, -1)]
def draw_board(board):
    output = ''
    for row in board:
        output += ', '.join(map(str, row))
        output += '\n'
    return output

def spiralize(n):
    board = [[0]*n for i in range(n)]
    moves = cycle(moves_base)
    next_moves = cycle(moves_base)
    next_move = next(next_moves)
    x, y = 0, 0
    current_move = next(moves)
    side_size = n - 1
    no_progress = 0
    while True:
        # if one field ahead we already have 1
        one_fields_ahead = board[max(0, min(y + current_move.y, n - 1))][max(0, min(x + current_move.x, n - 1))] == 1
        # if two fiels ahead we already have 1
        two_fields_ahead = board[max(0, min(y + 2 * current_move.y, n - 1))][max(0, min(x + 2 * current_move.x, n - 1))] == 1
        # if field that is one step ahead and to the right we already have 1
        forward_and_to_the_right = board[max(0, min(y + current_move.y + next_move.y, n - 1))][max(0, min(x + current_move.x + next_move.x, n - 1))] == 1
        if one_fields_ahead or two_fields_ahead or forward_and_to_the_right:
            no_progress += 1
            if no_progress >= 2:
                # fix for odd n
                if n % 2 == 1:
                    board[y][x] = 1
                print(draw_board(board))
                return board
            current_move = next(moves)
            next_move = next(next_moves)
            continue
        no_progress = 0
        last_successful_move = current_move
        board[y][x] = 1
        x = max(0, min(x + current_move.x, n - 1))
        y = max(0, min(y + current_move.y, n - 1))
    return []

print(spiralize(7))

# from collections import namedtuple
# Move = namedtuple("Move", "x y")

# moves_base = [Move(1, 0), Move(0, 1), Move(-1, 0), Move(0, -1)]

# def draw_board(board):
#     output = ''
#     for row in board:
#         for item in row:
#             output += str(item)
#         output += '\n'
#     return output

# def spiralize(n):
#     board = [[0]*n for i in range(n)]
#     x, y = 0, 0
#     direction_index = 0
#     next_direciton_index = 1 
#     side_size = n - 1
#     no_progress = 0
#     while True:
#         # if two fiels ahead we already have 1
#         is_one_two_fields_ahead = board[max(0, min(y + 2 * current_move.y, n - 1))][max(0, min(x + 2 * current_move.x, n - 1))] == 1
#         if is_one_two_fields_ahead:
#             no_progress += 1
#             if no_progress >= 2:
#                 return board
#             current_move = next(moves)
#             continue
#         no_progress = 0
#         board[y][x] = 1
#         x = max(0, min(x + current_move.x, n - 1))
#         y = max(0, min(y + current_move.y, n - 1))
#         print(board)