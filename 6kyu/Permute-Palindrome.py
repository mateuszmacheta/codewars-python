# 6 kyu Permute a Palindrome
# https://www.codewars.com/kata/58ae6ae22c3aaafc58000079/train/python
from collections import Counter

def permute_a_palindrome(input):
    # count letters
    letter_count = Counter(input)
    # transform to list of parity for all letters - 0 even and 1 is odd
    parity = list(map(lambda x: x % 2, letter_count.values()))
    # count how many letters occur even and odd times
    parity_count = Counter(parity)
    print(parity_count)
    return parity_count[1] <= 1
    


print(permute_a_palindrome("a"), True)
print(permute_a_palindrome("baabcd"), False)
print(permute_a_palindrome("abcdefghba"), False)
