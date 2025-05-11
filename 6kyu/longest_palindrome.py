# 6 kyu longest_palindrome
# https://www.codewars.com/kata/54bb6f887e5a80180900046b/train/python


def longest_palindrome (s):
    maximum = 0
    length = len(s)
    for L in range(0, length+1):
        for R in range(L+1, length+1):
            if is_palindrome(s[L:R]):
                maximum = max(maximum, len(s[L:R]))
    return maximum


def is_palindrome(s):
    for i in range(0, len(s)//2):
        if s[i] != s[-1-i]: return False
    return True

if __name__ == '__main__':
    print(longest_palindrome("baablkj12345432133d"))
    #print(longest_palindrome("baa"))
    #print(is_palindrome("baablkj12345432133d"))
    #print(is_palindrome("1245"))