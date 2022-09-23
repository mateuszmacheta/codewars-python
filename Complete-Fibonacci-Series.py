s = [0, 1]


def fibonacci(n):
    if n <= 0:
        return []
    while n > len(s):
        s.append(s[-1] + s[-2])
    return s[:n]


if __name__ == '__main__':
    print(fibonacci(5))