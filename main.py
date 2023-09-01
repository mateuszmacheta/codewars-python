def more_zeros(s):
    result = []
    for c in s:
        if c in result: continue
        b = bin(ord(c))[2:]
        if b.count('0') > b.count('1'):
            result.add(c)
    return result

print(bin(ord('h'))[2:])