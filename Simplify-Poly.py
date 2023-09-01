# 4 kyu Simplifying multilinear polynomials
# https://www.codewars.com/kata/55f89832ac9a66518f000118/train/python
import re

# https://regex101.com/r/W3tsKf/1
ITEM_REGEX = "(?P<sign>[+-])?(?P<multiplier>[\d]*)(?P<unknowns>[a-z]{1,})"


class Item:
    def __init__(self, match):
        groups = match.groupdict()
        self._sign = groups['sign'] or '+'
        self._multiplier = groups['multiplier'] if groups['multiplier'] else 1
        self.unknowns = set(groups['unknowns'])

    def number(self):
        return (1 if self._sign == '+' else -1) * int(self._multiplier)
    
    def _weigth(self): # for sorting
        return (''.join(sorted(self.unknowns)), self.number())

    def __add__ (self, other):
        if not other:
            return self
        summed_number = self.number() + other.number()
        if summed_number >= 0:
            self._sign = '+'
        else:
            self._sign = '-'
        self._multiplier = abs(summed_number)
        return self
    
    def __str__(self):
        if self._multiplier == 0: return ''
        return self._sign + (self._multiplier if self._multiplier != 1 else '') + ''.join(sorted(self.unknowns))
    
    def __lt__(self, other):
        return self._weigth() < other._weigth()
        



def simplify(poly):
    items = []
    for match in re.finditer(ITEM_REGEX, poly):
        items.append(Item(match))
    # grouping
    
    return ''.join(map(lambda i: str(i), sorted(reduced))).lstrip('+')


# print(simplify("dc+dcba"), "cd+abcd")
# print(simplify("2xy-yx"),"xy")
print(simplify("-a+5ab+3a-c-2a"),"-c+5ab")
print(simplify("-abc+3a+2ac"),"3a+2ac-abc")
# print(simplify("xyz-xz"),"-xz+xyz")
# print(simplify("a+ca-ab"),"a-ab+ac")
# print(simplify("xzy+zby"),"byz+xyz")
# print(simplify("-y+x"),"x-y")
# print(simplify("y-x"),"-x+y")