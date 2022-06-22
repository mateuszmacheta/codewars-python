# 5 kyu Vector class
# https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4/train/python

class Vector:
    def __init__(self, coords):
        self.coords = coords

    def join(self, other, method):
        if type(other) is not Vector:
            raise 'Can only add another vector!'
        if len(self) != len(other):
            raise 'Can only add two vectors of the same size!'

        result = 0
        new = Vector([None]*len(self))

        for i, e in enumerate(self.coords):
            if method == 'add':
                new.coords[i] = self.coords[i] + other.coords[i]
            elif method == 'subtract':
                new.coords[i] = self.coords[i] - other.coords[i]
            elif method == 'dot':
                result += self.coords[i] * other.coords[i]

        if method == 'dot':
            return result
        return new

    def add(self, other):
        return self.join(other, 'add')

    def subtract(self, other):
        return self.join(other, 'subtract')

    def dot(self, other):
        return self.join(other, 'dot')

    def equals(self, other):
        return self.coords == other.coords

    def norm(self):
        return sum(e**2 for e in self.coords)**0.5

    def __str__(self):
        return '(' + ','.join(str(e) for e in self.coords) + ')'

    def __len__(self):
        return len(self.coords)


if __name__ == '__main__':
    a = Vector([1, 2])
    b = Vector([3, 4])

    print(a.add(b).equals(Vector([4, 6])))

    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])

    print(a.add(b).equals(Vector([4, 6, 8])))
    print(a.subtract(b).equals(Vector([-2, -2, -2])))
    print(a.dot(b), 26)
    print(a.norm(), 14 ** 0.5)