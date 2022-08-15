# 4 kyu Simple Fun #159: Middle Permutation
# https://www.codewars.com/kata/58ad317d1541651a740000c5/train/python

from itertools import permutations as p


def middle_permutation(s):
    print(list(''.join(e) for e in p(s)))
    return '\n\n\n'


def helper(t, t2):
    t = ''.join(sorted(t))
    return ''.join(map(str, (t.index(c) for c in t2)))

if __name__ == '__main__':
    print(helper('abc', 'bac'))
    print(helper('abcd', 'bdca'))
    print(helper('abcdx', 'cbxda'))
    print(helper('abcdxg', 'cxgdba'))
    print(helper('abcdxgz', 'dczxgba'))
    # print(middle_permutation("abc"), "bac")
    # print(middle_permutation("abcd"), "bdca")
    # print(middle_permutation("abcdx"), "cbxda")
    # print(middle_permutation("abcdxg"), "cxgdba")
    # print(middle_permutation("abcdxgz"), "dczxgba")
    #print(middle_permutation("abc"), "bac")
    #print(middle_permutation("abcd"), "bdca")
    #print(middle_permutation("abcdx"), "cbxda")
    #print(middle_permutation("abcdxg"), "cxgdba")
    #print(middle_permutation("abcdxgz"), "dczxgba")
    #print(middle_permutation("123"), "213")
    # print(middle_permutation("1234"), "2431")
    # print(middle_permutation("12345"), "32541")
    # print(middle_permutation("123456"), "365421")
    # print(middle_permutation("1234567"), "4376521")