# 5 kyu John and Ann sign up for Codewars
# https://www.codewars.com/kata/57591ef494aba64d14000526/train/python
import time

MAX_SIZE = 500000
john_seq = [0]
ann_seq = [1]

tic = time.perf_counter()
for x in range(1, MAX_SIZE):
    john_seq.append(x - ann_seq[john_seq[x-1]])
    ann_seq.append(x - john_seq[ann_seq[x-1]])
toc = time.perf_counter()
print(f'Sequences generated {toc-tic:0.3f}')

def john(n):
    return john_seq[0:n]


def ann(n):
    return ann_seq[0:n]


def sum_john(n):
    return sum(john_seq[0:n])


def sum_ann(n):
    return sum(ann_seq[0:n])

if __name__ == '__main__':
    pass