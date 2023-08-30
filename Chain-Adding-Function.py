# 5 kyu A Chain adding function
# https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python

class add:
    def __init__(self, value):
        self.value = value
        
    def __call__(self, argument):
        if isinstance(argument, int):
            self.value = self.value + argument
        else:
            self.value = self.value + argument.value
        return self

    def __eq__(self, other):
        return self.value == other
    
    def __add__(self, other):
        if isinstance(other, int):
            return add(self.value + other)
        else:
            return add(self.value + other.value)
        
a = add(6)
# assert a == 6
# assert not (a == 7)
b = a + 5
# assert not (b == 12)
# assert b == 11
c = a(a)
# assert c == 12
# assert not (c == 13)
d = add(1)
# assert not (d == 0)
# assert d == 1
e = d(9)
# assert not (e == 11)
# assert e == 10
f = c(e)
# assert f == 22
# assert not (f == 21)
g = f(e)
# assert g == 32
# assert not (g == 33)
h = g(0)