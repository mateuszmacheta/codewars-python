# 6 kyu What's A Name In?
# https://www.codewars.com/kata/59daf400beec9780a9000045/train/python

def name_in_str(strng : str, name : str) -> bool:
    letters = list(strng.lower())
    name_letters = list(name.lower())
    while not(len(letters) == 0 or len(name_letters) == 0): # either one is empty then we exit loop
        letter = name_letters.pop(0)
        if letter not in letters: return False
        while True:
            removed = letters.pop(0)
            if removed == letter: break
    return not name_letters

print(name_in_str("Across the rivers", "chris"))
