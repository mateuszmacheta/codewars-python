# 6 kyu Longest alphabetical substring
# https://www.codewars.com/kata/5a7f58c00025e917f30000f1/train/python

def longest(s):
    if len(s) < 2:
        return s
    s = s + '`'
    longest_substring = []
    cached = []
    for i, current in enumerate(s[:-1]):
        cached.append(current)
        next = s[i+1]
        if current > next:
            if len(cached) > len(longest_substring):
                longest_substring = cached
            cached = []
    return ''.join(longest_substring)


if __name__ == '__main__':
    print(longest('asdfaaaabbbbcttavvfffffdf'), 'aaaabbbbctt')