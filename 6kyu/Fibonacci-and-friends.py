# 6 kyu Fibonacci, Tribonacci and friends
# https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/python

def Xbonacci(signature,n):
    if n < len(signature): return signature[:n]
    result = list(signature)
    for i in range(n - len(signature)):
        result.append(sum([result[-i-1] for i in range(len(signature))]))
    return result


print(Xbonacci([1,1], 5))