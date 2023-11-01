def sxor(n):
    a = n
    for i in range(n):
        a = a ^ i
    return a


for i in range(20):
    print(f"{i}\t{sxor(i)}\t{i%4}")