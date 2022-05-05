# 6 kyu Multi-tap Keypad Text Entry on an Old Mobile Phone
# https://www.codewars.com/kata/54a2e93b22d236498400134b/train/python

keyboard = ['1', 'ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9',
            '*', ' 0', '#']


def presses(phrase):
    return sum(get_number_of_presses(c) for c in phrase)


def get_number_of_presses(character: str):
    character = character.upper()
    for key in keyboard:
        position = key.find(character)
        if position > -1: return position + 1
    raise Exception("Character {} not found on keyboard".format(character))
