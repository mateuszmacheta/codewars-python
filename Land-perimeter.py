# 5 kyu Land perimeter
# https://www.codewars.com/kata/5839c48f0cf94640a20001d3/train/python

def return_perimeter_for_x(arr: list, row: int, i: int):
    perimeter = 4
    total_rows = len(arr)
    row_width = len(arr[0])

    row_above = row - 1
    row_below = row + 1
    i_left = i - 1
    i_rigth = i + 1

    if row_above >= 0 and arr[row_above][i] == 'X': perimeter -= 1
    if row_below < total_rows and arr[row_below][i] == 'X': perimeter -= 1
    if i_left >= 0 and arr[row][i_left] == 'X': perimeter -= 1
    if i_rigth < row_width and arr[row][i_rigth] == 'X': perimeter -= 1

    return perimeter

def land_perimeter(arr):
    total_rows = len(arr)
    if total_rows == 0:
        return 0
    else:
        row_width = len(arr[0])

    perimeter = 0

    for row in range(total_rows):
        for i in range(row_width):
            print(f'row: {row} i: {i} character: {arr[row][i]}')
            if arr[row][i] == 'X':
                perimeter += return_perimeter_for_x(arr, row, i)
    return f'Total land perimeter: {perimeter}'

# print(land_perimeter([]), "Total land perimeter: 0")
print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]), "Total land perimeter: 60")
# print(land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]), "Total land perimeter: 52")
# print(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]), "Total land perimeter: 40")
# print(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]), "Total land perimeter: 54")
# print(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]), "Total land perimeter: 40")