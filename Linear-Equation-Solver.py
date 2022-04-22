# 4 kyu Linear Equation Solver
# https://www.codewars.com/kata/56d6d927c9ae3f115b0008dd/train/python
# https://www.mathsisfun.com/algebra/systems-linear-equations-matrices.html
import re


def solve(*equations):
    var_pattern = r"(\-?\d*[a-z]+)"
    free_pattern = r"(\d+)(?:[^a-z])"
    var_matrix = []
    free_matrix = []
    for eq in equations:
        left, right = eq.split('=')
        var_matches = re.match(var_pattern, left)
        free_matches = re.match(free_pattern, left)
        print('x')

    return 0

solve("2x+8y=4", "-x+4y=14")