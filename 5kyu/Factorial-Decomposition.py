# 5 kyu Factorial decomposition
# https://www.codewars.com/kata/5a045fee46d843effa000070/train/python
import time

decomposed = dict()


def prime_decompose(e: int):
    n = e
    while n % 2 == 0:
        if e in decomposed:
            decomposed[e].append(2)
        else:
            decomposed[e] = [2]
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            if e in decomposed:
                decomposed[e].append(f)
            else:
                decomposed[e] = [f]
            n //= f
        else:
            f += 2
    if n != 1:
        if e in decomposed:
            decomposed[e].append(n)
        else:
            decomposed[e] = [n]
    return True

tic = time.perf_counter()
for e in range(2, 4001):
    prime_decompose(e)
toc = time.perf_counter()
print(f'Execution time {toc - tic:0.2f}')

def decomp(n):
    factorial = list(range(2, n + 1))
    result = dict()
    for e in factorial:
        for factor in decomposed[e]:
            if factor in result:
                result[factor] += 1
            else:
                result[factor] = 1
    return ' * '.join(f'{e}^{result[e]}' if result[e] > 1 else f'{e}' for e in result)


print(decomp(12))


