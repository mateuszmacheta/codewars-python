# 4 kyu Number of Proper Fractions with Denominator d
# https://www.codewars.com/kata/55b7bb74a0256d4467000070/train/python
from math import prod
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


def proper_fractions(n):
    if n == 1:
        return 0
    if n not in decomposed:
        prime_decompose(n)
    factors = set(decomposed[n])
    # Euler’s product formula
    return n * int(prod((1 - 1/e) for e in factors))


if __name__ == '__main__':
    print(proper_fractions(25))
    #     t = '''1
    # 2
    # 5
    # 15
    # 25
    # 9999999
    # 500000003
    # 1532420
    # 123456789
    # 9999999999
    # 59964944
    # 7527628342
    # 539066
    # 964334
    # 41
    # 9334706247
    # 61397363
    # 899736
    # 69610
    # 47
    # 245764765
    # 612564391
    # 8592
    # 74933
    # 9146969
    # 849452
    # 986083
    # 2161470052
    # 99101328
    # 10
    # 101223189
    # 20
    # 728727832
    # 1242
    # 8255
    # 100
    # 747
    # 224
    # 675001026
    # 657269541
    # 316
    # 65806404
    # 45652
    # 33
    # 5502749369
    # 533
    # 93537
    # 717255798
    # 8624870067
    # 23'''
    #     tic = time.perf_counter()
    #
    #     for d in [int(e) for e in t.strip().split('\n')]:
    #         print(proper_fractions(d))
    #     toc = time.perf_counter()
    #     print(f"Code executed in {toc - tic:0.4f} seconds")
    #     print(decomposed)