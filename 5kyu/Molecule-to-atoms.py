# 5 kyu Molecule to atoms
# https://www.codewars.com/kata/52f831fa9d332c6591000511
from collections import defaultdict
import re

elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F(?!e)', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P(?!d)', 'S', 'Cl', 'Ar', 'K',
            'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
            'Rb',
            'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
            'Cs',
            'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf',
            'Ta',
            'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
            'Pa',
            'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs',
            'Mt',
            'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']


def parse_molecule (formula):
    atoms = formula
    for i in range(3):
        opening = '([{'[i]
        closing = ')]}'[i]
        while in_brackets := re.search(fr'\{opening}(\w+)\{closing}(\d*)', atoms):
            group = in_brackets.group()
            print(f'Expanding {group}')
            start_inner, end_inner = in_brackets.span(1)
            start, end = in_brackets.span(0)
            multiplier = 1
            if in_brackets.group(2):
                multiplier = int(in_brackets.group(2))
            expanded = expand(atoms[start_inner:end_inner]) * multiplier
            atoms = atoms[:start] + expanded + atoms[end:]
    atoms = expand(atoms)

    return count(atoms)


def expand(formula):
    if not any(c.isdigit() for c in formula):
        return formula

    elements_re = '(' + '|'.join(elements) + r')(\d*)'
    recreated = []

    for group in re.findall(elements_re, formula):
        character = group[0]
        multiplier = group[1]
        if multiplier:
            recreated.append(character * int(multiplier))
        else:
            recreated.append(character)

    return ''.join(recreated)


def count(atoms):
    elements_re = '(' + '|'.join(elements) + ')'
    result = defaultdict(int)
    for match in re.findall(elements_re, atoms):
        result[match] += 1
    return dict(result)

if __name__ == '__main__':
    #print(parse_molecule("H2O"), {'H': 2, 'O': 1}, "Should parse water")
    #print(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O': 2, 'H': 2})
    print(parse_molecule("K4[ON(SO3)2]2"), {'K': 4, 'O': 14, 'N': 2, 'S': 4})
