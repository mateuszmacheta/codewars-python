# 4 kyu Simplifying multilinear polynomials
# https://www.codewars.com/kata/55f89832ac9a66518f000118/train/python
import re

# https://regex101.com/r/W3tsKf/1
ITEM_REGEX = "(?P<sign>[+-])?(?P<multiplier>[\d]*)(?P<unknowns>[a-z]{1,})"


class Item:
    def __init__(self, match):
        groups = match.groupdict()
        self._sign = groups['sign'] or '+'
        self._multiplier = groups['multiplier'] if groups['multiplier'] else '1'
        self.unknowns = set(groups['unknowns'])

    @property
    def number(self):
        return (1 if self._sign == '+' else -1) * int(self._multiplier)
    
    @property
    def unknowns_string(self):
        return ''.join(sorted(self.unknowns))
    
    def _weigth(self): # for sorting
        return (len(self.unknowns), self.unknowns_string)

    def __add__ (self, other):
        if not other:
            return self
        summed_number = self.number + other.number
        if summed_number >= 0:
            self._sign = '+'
        else:
            self._sign = '-'
        self._multiplier = str(abs(summed_number))
        return self
    
    def __str__(self):
        if self._multiplier == '0': return ''
        return self._sign + (self._multiplier if self._multiplier != '1' else '') + self.unknowns_string
    
    def __lt__(self, other):
        return self._weigth() < other._weigth()
        



def simplify(poly):
    items = []
    for match in re.finditer(ITEM_REGEX, poly):
        items.append(Item(match))
    # grouping
    reduced = dict()
    for item in items:
        if item.unknowns_string in reduced:
            reduced[item.unknowns_string] += item
        else:
            reduced[item.unknowns_string] = item
    return ''.join(map(lambda i: str(i), sorted(reduced.values()))).lstrip('+')


# print(simplify("dc+dcba"), "cd+abcd")
# print(simplify("2xy-yx"),"xy")
# print(simplify("-a+5ab+3a-c-2a"),"-c+5ab")
# print(simplify("-abc+3a+2ac"),"3a+2ac-abc")
# print(simplify("xyz-xz"),"-xz+xyz")
# print(simplify("a+ca-ab"),"a-ab+ac")
# print(simplify("xzy+zby"),"byz+xyz")
# print(simplify("-y+x"),"x-y")
# print(simplify("y-x"),"-x+y")
# print(simplify("3a+b+4ac+bc-ab+3a-cb-a-a"),"4a+b-ab+4ac")
print(simplify("dc+dcba"), "cd+abcd")
