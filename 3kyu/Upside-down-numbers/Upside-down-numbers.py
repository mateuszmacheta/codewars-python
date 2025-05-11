# 6 kyu Upside down numbers
# https://www.codewars.com/kata/59f7597716049833200001eb/train/python
upside = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}


def solve(a: int, b: int):
    count = 0
    for n in range(a, b):
        s = str(n)
        if any(d not in upside for d in s):
            continue
        if check(s):
            count += 1
    return count


def check(s: str):
    l = len(s)
    six_nine = {'6', '9'}
    if s in six_nine:
        return False
    for i in range(l // 2):
        if upside[s[i]] != s[-1 - i]:
            return False
    if l % 2:
        return s[l // 2] not in six_nine
    return True


if __name__ == '__main__':
    print(solve(0, 1000))
