# 4 kyu Vigenère Cipher Helper
# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python
from itertools import cycle


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        return self.inner(text)

    def decode(self, text):
        return self.inner(text, encode=False)

    def inner(self, text, encode=True):
        c = cycle(self.key)
        o = []
        for e in text:
            shift = self.alphabet.index(next(c))
            if not encode:
                shift *= -1
            if e not in self.alphabet:
                o.append(e)
            else:
                e2 = self.alphabet[(self.alphabet.index(e) + shift) % len(self.alphabet)]
                o.append(e2)
        return ''.join(o)


if __name__ == '__main__':
    abc = "abcdefghijklmnopqrstuvwxyz"
    key = "password"
    c = VigenereCipher(key, abc)

    print(c.encode('codewars'), 'rovwsoiv')
    print(c.decode('rovwsoiv'), 'codewars')

    print(c.encode('waffles'), 'laxxhsj')
    print(c.decode('laxxhsj'), 'waffles')

    print(c.encode('CODEWARS'), 'CODEWARS')
    print(c.decode('CODEWARS'), 'CODEWARS')