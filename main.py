from math import factorial

am_i_wilson = lambda P: P - 1 > -1 and (factorial(P-1) + 1) / (P * P) % 1 == 0

print(am_i_wilson(5))