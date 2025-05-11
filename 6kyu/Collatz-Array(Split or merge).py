# 6kyu Coding 3min: Collatz Array(Split or merge)
# https://www.codewars.com/kata/56fe9d579b7bb6b027000001

def sc(arr, n):
    for _ in range(n):
        arr = step(arr)
    return arr

def step(arr):
    i = 0
    while i < len(arr):
        e = arr[i]
        if e % 2:
            e = e * 3 + 1
            if i < len(arr)-1:
                e += arr.pop(i+1)
            arr[i]=e
        else:
            arr[i]=e//2
            arr.insert(i, arr[i])
            i += 1
        i += 1
    return arr

if __name__ == "__main__":
    print(sc([3, 4, 5],  0), [3, 4, 5])
    print(sc([3, 4, 5],  1), [14, 16])
    print(sc([3, 4, 5],  2), [7, 7, 8, 8])
