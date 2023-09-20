# 6 kyu Frog jumping
# https://www.codewars.com/kata/536950ffc8a5ca9982001371/train/python

MAX_JUMPS = 1000

def solution(a):
    count, next = 1, a[0]
    while count < MAX_JUMPS:
        try:
            if next < 0:
                raise Exception
            else:
                next += a[next]
            count += 1
        except:
            return count
    return -1

# print(solution([1, 2, 2, -1]))
print(solution([-3, 0, 4, 8, 0, -3, 3, 7]))