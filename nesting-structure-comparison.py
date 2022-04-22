# 4 kyu Nesting Structure Comparison
# https://www.codewars.com/kata/520446778469526ec0000001/train/python

def same_structure_as(original, other):
    return clear(original) == clear(other)


def clear(structure):
    if type(structure) is list:
        for i in range(0, len(structure)):
            if type(structure[i]) is list:
                clear(structure[i])
            else:
                structure[i] = None
    return structure

print(same_structure_as([1,[1,1]],[2,[2,2]]))
# print(same_structure_as([1,[1,1]],[[2,2],2]))
