# 6 kyu Simple Encryption #1 - Alternating Split
# https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python
import math


def decrypt(s, n):
    print(f"decrypt: {s}, {n}")
    if n < 0 or (s is not None and len(s) < 2):
        return s
    result = s
    for i in range(0, n):
        left = result[:len(result) // 2]
        if len(result) % 2 == 1:
            left += '©'
        right = result[len(result) // 2:]
        result = ''
        for j in range(0, len(left)):
            #print(right[j],left[j])
            result += right[j] + left[j]
        result = result.replace('©', '')

    return result


def encrypt(s, n):
    print(f"encrypt: {s}, {n}")
    if n < 0 or len(s) < 2:
        return s
    for i in range(0, n % (len(s) // 2)):
        s = s[1::2] + s[0::2]
    return s

print(encrypt("", 0))

# print(decrypt("hsi  etTi sats!", 1))