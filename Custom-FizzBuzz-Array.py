# 6 kyu Custom FizzBuzz Array
# https://www.codewars.com/kata/5355a811a93a501adf000ab7/train/python
cache = {}
N_MIN = 1
N_MAX = 100


def fizz_buzz_custom(s1='Fizz', s2='Buzz', n1=3, n2=5):
    if s1 + s2 in cache:
        return cache[s1 + s2]
    cache[s1 + s2] = [n if (n % n1 and n % n2) else s1 * (not n % n1) + s2 * (not n % n2) for n in range(N_MIN, N_MAX + 1)]
    return cache[s1 + s2]


if __name__ == '__main__':
    print(list(fizz_buzz_custom()))