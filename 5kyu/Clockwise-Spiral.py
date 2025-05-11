# 5 kyu The Clockwise Spiral
# https://www.codewars.com/kata/536a155256eb459b8700077e/train/python
from collections import namedtuple
Move = namedtuple("Move", "x y")

moves = [Move(1, 0), Move(0, 1), Move(-1, 0), Move(0, -1)]

def create_spiral(n):
    if type(n) is not int or n < 1:
        return []
    result = [[0 for _ in range(n)] for _ in range(n)]
    move_index = 0
    y, x = 0, 0
    total = n * n
    current_move = moves[move_index]
    for i in range(1, total + 1):
        result[y][x] = i
        next_x_position = x + current_move.x
        next_y_position = y + current_move.y
        # if we try to go "outside of" our 2d array
        if n - 1 < next_x_position or next_x_position < 0 or n - 1 < next_y_position or next_y_position < 0 or \
        result[next_y_position][next_x_position] != 0: # or we encounter field that has already been populated
            move_index = (move_index + 1) % 4
            current_move= moves[move_index]
        x = x + current_move.x
        y = y + current_move.y

    return result


print(create_spiral(3))