# 6 kyu Street Fighter 2 - Character Selection
# https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/python

def street_fighter_selection(fighters, initial_position, moves):
    result = []
    y = initial_position[0]
    x = initial_position[1]
    rows_max = len(fighters) - 1
    coords = {'down': (1, 0), 'right': (0, 1), 'up': (-1, 0), 'left': (0, -1)}
    for move in moves:
        move_coords = coords[move]
        y += move_coords[0]
        if y < 0:
            y = 0
        elif y > rows_max:
            y = rows_max
        x = (x + move_coords[1]) % len(fighters[y])
        result.append(fighters[y][x])
    return result


fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
    ]

# print(street_fighter_selection(fighters, (0,0), ["down","right","up","left"]*2))

fighters2 = []

print(street_fighter_selection(fighters, (0,0), ["left"]*8))