LIMIT = 10 ** 2

infinite_string = ''
position = -1

natural_positions = dict()
early_birds = dict()

for i in range(1, LIMIT):
    s = str(i)
    position += len(s)
    infinite_string += str(i)
    natural_positions[i] = position
    earliest_position = infinite_string.find(s)
    if earliest_position != -1 and earliest_position < position:
        early_birds[i] = earliest_position

print(natural_positions)
print(early_birds)