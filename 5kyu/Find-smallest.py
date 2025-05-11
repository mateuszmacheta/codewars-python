# 5 kyu Find the smallest
# https://www.codewars.com/kata/573992c724fc289553000e95


def smallest(n):
    s = str(n)
    results = []
    for i in range(len(s) - 1):
        next_smaller_digit = min(s[1 + i:])
        final = i
        initial = last_index(s, next_smaller_digit)
        initial = initial - 1 * (final > initial)
        results.append([int(misplace_letters(s, initial, final)), initial, final])
    return results[0]


def last_index(s, needle):
    return len(s) - 1 - s[::-1].index(needle)


def misplace_letters(s, initial, final):
    letters = list(s)
    taken = letters.pop(initial)
    letters.insert(final, taken)
    return ''.join(letters)


if __name__ == '__main__':
    #print(misplace_letters('261235', 2, 0))
    #print(smallest(261235))
    print(smallest(209917))