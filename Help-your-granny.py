# 5 kyu Help your granny
# https://www.codewars.com/kata/5536a85b6ed4ee5a78000035/train/python
from math import sqrt, floor


def tour(friends, friend_towns, home_to_town_distances):
	print(f'Friends: {friends}')
	print(f'Friend towns: {friend_towns}')
	print(f'Home to town distances: {home_to_town_distances}')
	# get names of friends translated to names of towns to be visited
	towns_to_be_visited = [e[1] for e in friend_towns if e[0] in friends]

	town_distances = [home_to_town_distances[e] for e in home_to_town_distances if e in towns_to_be_visited]
	distances = []
	for town1, town2 in zip(town_distances, town_distances[1:]):
		d = sqrt(town2*town2 - town1*town1)
		distances.append(d)
		print(d)

	return floor(sum(distances) + town_distances[0] + town_distances[-1])


if __name__ == '__main__':
	# friends1 = ["A1", "A2", "A3", "A4", "A5"]
	# fTowns1 = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]]
	# distTable1 = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}
	# print(tour(friends1, fTowns1, distTable1), 889)

	friends2 = ['B1', 'B2', 'B3']
	fTowns2 = [['B1', 'Y1'], ['B2', 'Y2'], ['B3', 'Y3'], ['B4', 'Y4'], ['B5', 'Y5']]
	distTable2 = {'Y1': 60.0, 'Y2': 80.0, 'Y3': 100.0, 'Y4': 110.0, 'Y5': 150.0}
	print(tour(friends2, fTowns2, distTable2), 272)
