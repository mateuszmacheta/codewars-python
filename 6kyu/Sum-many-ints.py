# 6 Sum of many ints
# https://www.codewars.com/kata/54c2fc0552791928c9000517

def debug(n, m):
    for i in range(1, n):
        print((i % m), end="")
        if (i % m) == 0:
            print()
    pass

def f(n, m):
    tot = m * (m - 1) / 2 * n // m
    return tot + sum(range(n % m))

if __name__ == '__main__':
    print(debug(15, 10))
    # print(f(15, 10), 60)
    # print(f(20, 20), 190)