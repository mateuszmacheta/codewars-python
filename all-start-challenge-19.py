# 5 kyu All Star Code Challenge #19
# https://www.codewars.com/kata/5865a407b359c45982000036

def slogan_maker(arr):
    arr = make_unique(arr)
    if len(arr) <= 1:
        return list(arr)
    slogans = []
    for i in range(0,len(arr)):
        row = []
        row.append(arr[i])
        row += arr[:i] + arr[i+1:]
        slogans.append(" ".join(row))
        for j in range(1,len(arr)-1):
            row[j], row[j+1] = row[j+1], row[j]
            slogans.append(" ".join(row))
    return slogans


def make_unique(arr: list):
    result = []
    for e in arr:
        if e not in result:
            result.append(e)
    return result


# print(slogan_maker(["super", "hot", "guacamole"]))
print(slogan_maker(['break', 'impact', 'impact', 'exit', 'survival', 'higher']))