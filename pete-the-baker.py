# 5 kyu Pete, the baker
# https://www.codewars.com/kata/525c65e51bf619685c000059

def cakes(recipe, available):
    for key in recipe:
        if key not in available:
            return 0
    return min([available[key] // recipe[key] for key in recipe])