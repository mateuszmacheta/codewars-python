def myFun(a, b, c):
    if a > b > c:
        return a
    if b > a:
        return b
    return c


if __name__ == '__main__':
    print(myFun(10, 5, 2))