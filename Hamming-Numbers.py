# 4 kyu Hamming Numbers
# https://www.codewars.com/kata/526d84b98f428f14a60008da/train/python

MAX_VAL = int(10e2)

class HammingNumbers:
    numbers_set = {1}
    numbers = [1]

    @classmethod
    def generate(cls):
        count = 1
        next_item = 1
        q2 = []
        q3 = []
        q5 = []

        while count < MAX_VAL:
            q2.append(2 * next_item)
            q3.append(3 * next_item)
            q5.append(5 * next_item)

            if q2[0] < q5[0]:
                if q2[0] < q3[0]:
                    next_item = q2.pop(0)
                else:
                    next_item = q3.pop(0)
            else:
                if q3[0] < q5[0]:
                    next_item = q3.pop(0)
                else:
                    next_item = q5.pop(0)

            if next_item not in cls.numbers_set:
                cls.numbers.append(next_item)
                cls.numbers_set.add(next_item)
                count += 1

HammingNumbers.generate()

def hamming(n):
    return HammingNumbers.numbers(n)

print(hamming(1))