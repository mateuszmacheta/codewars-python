# 5kyu Shortest Code: Collatz Array(Split or merge)
# https://www.codewars.com/kata/56fc7a29fca8b900eb001fac

def sc(a,n):
    if n==0:return a
    o=[];b=iter(a)
    for e in b:
        o+=[e*3+1+next(b,0)] if e&1 else[e//2]*2
    return sc(o,n-1)

if __name__ == "__main__":
    print(sc([3, 4, 5],  0), [3, 4, 5])
    print(sc([3, 4, 5],  1), [14, 16])
    print(sc([3, 4, 5],  2), [7, 7, 8, 8])
