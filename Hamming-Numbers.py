# 4 kyu Hamming Numbers
# https://www.codewars.com/kata/526d84b98f428f14a60008da/train/python
import time


MAX_VAL = 10e24


class HammingNumbers:
    numbers = dict().fromkeys([1, 2, 3, 5])

    @classmethod
    def generate(cls):
        while True:
            for n in list(cls.numbers.keys()):
                cls.numbers[n*2] = None
                cls.numbers[n*3] = None
                cls.numbers[n*5] = None
            if n*2 > MAX_VAL:
                cls.numbers = sorted(cls.numbers)
                print(len(cls.numbers))
                return True



tic = time.perf_counter()
HammingNumbers.generate()

def hamming(n):
    return HammingNumbers.numbers[n - 1]

if __name__ == '__main__':

    print(hamming(816))
    toc = time.perf_counter()
    print(f"Code executed in {toc - tic:0.4f} seconds")