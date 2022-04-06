# 5 kyu Calculating with Functions
# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

# what is DRY?
def zero(arg=None):
    if arg:
        return eval('0'+arg)
    return '0'
def one(arg=None):
    if arg:
        return eval('1'+arg)
    return '1'
def two(arg=None):
    if arg:
        return eval('2' + arg)
    return '2'
def three(arg=None):
    if arg:
        return eval('3' + arg)
    return '3'
def four(arg=None):
    if arg:
        return eval('4' + arg)
    return '4'
def five(arg=None):
    if arg:
        return eval('5' + arg)
    return '5'
def six(arg=None):
    if arg:
        return eval('6' + arg)
    return '6'
def seven(arg=None):
    if arg:
        return eval('7' + arg)
    return '7'
def eight(arg=None):
    if arg:
        return eval('8' + arg)
    return '8'
def nine(arg=None):
    if arg:
        return eval('9' + arg)
    return '9'

def plus(arg):
    return '+' + arg
def minus(arg):
    return '-' + arg
def times(arg):
    return '*' + arg
def divided_by(arg):
    return '//' + arg

print(seven(times(five())))
