# 6 kyu Reverse polish notation calculator
# https://www.codewars.com/kata/52f78966747862fc9a0009ae/train/python

def calc(expr):
    stack = []; operators = {'*', '+', '-', '/'}
    if not len(expr): return 0
    if not any(operator in expr for operator in operators): return eval(expr)
    for e in expr.split():
        if e not in operators:
            stack.append(e)
        else:
            temp = stack.pop()
            stack.append(str(eval(stack.pop() + e + temp)))
    return eval(stack[0])

print(calc(''))
#print(calc('5 1 2 + 4 * + 3 -'))