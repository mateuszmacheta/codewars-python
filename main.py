def f(n, m):
    print(n, m)
    if n < m:
        return n * (n + 1) // 2
    quotient, remainder = divmod(n, m)
    print(quotient, remainder)
    return quotient*(m * (m - 1) // 2) + remainder * (remainder + 1) // 2


# print(f(10, 5), 20)
# print(f(20, 20), 190)
print(f(15, 10), 60)