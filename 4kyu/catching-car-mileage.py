# 4 kyu Catching Car Mileage Numbers
# https://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/python

import re
MIN_INTERESTING = 100


def is_interesting(number: int, awesome_phrases):
    awesome_phrases = set(awesome_phrases)
    if number in awesome_phrases:
        return 2
    if number + 1 in awesome_phrases or number + 2 in awesome_phrases:
        return 1
    if check_interesting(number):
        return 2
    if check_interesting(number + 1) or check_interesting(number + 2):
        return 1
    return 0


def check_interesting(number: int):
    if number < MIN_INTERESTING:
        return 0
    number = str(number)
    return followed_by_zeroes(number) or sequence(number) or palindrome(number)


def followed_by_zeroes(number: str):
    return re.match('^\d[0]{2,}$', number)


def sequence(number: str):
    return number in "1234567890" or number in "9876543210"


def palindrome(number: str):
    return number == number[::-1]
