# 3 kyu Upside-Down Numbers - Challenge Edition
# https://www.codewars.com/kata/59f98052120be4abfa000304/train/python
# attempt at generating valid numbers
upside = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
center = {'0', '1', '8'}

def check_upside_down(s: str, i: int, j: int):
    if i == j: return s[i] in center # this is the case where we land in center
    return upside.get(s[i], -1) == s[j]

def upsidedown(a: int, b: int):
    count = 0
    for n in range(a, b + 1, 2):
        s = str(n)
        i = 0
        j = len(s) - 1
        while True:
            # print(i, j)
            # print(string[i], string[j])
            if check_upside_down(s, i, j):
                count += 1
                break
            i += 1
            j -= 1
            if j - i < 0: break
    return count


if __name__ == '__main__':
    print(upsidedown(10, 100))