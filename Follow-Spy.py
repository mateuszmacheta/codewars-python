# 6 kyu Follow that Spy
# https://www.codewars.com/kata/5899a4b1a6648906fe000113/train/python

def find_routes(routes):
    working_set = set(routes)
    first_element = next(e for e in routes if e[0] not in map(lambda x: x[1], routes))
    result = [first_element[0]]
    working_set.remove(first_element)
    next_element = first_element
    while working_set:
        for e in working_set:
            if next_element[1] == e[0]:
                next_element = e
                break
        if not next_element: raise Exception("This shoudln't happen - invalid input.")
        print(next_element)
        result.append(next_element[0])
        working_set.remove(next_element)
    result.append(next_element[1])
    return ', '.join(result)

print(find_routes([('ITA','GER'), ('GER','BEL'), ('BEL','CAN')]), 'ITA, GER, BEL, CAN')