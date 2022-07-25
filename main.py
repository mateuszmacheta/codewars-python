import re

def str_to_hash(st):
    keyvalue = re.split(r', )|=', st)
    return {k: int(v) for k, v in zip(keyvalue[0::2], keyvalue[1::2])}

if __name__ == '__main__':
    print(str_to_hash("a=1, b=2, c=3, d=4"), {'a': 1, 'b': 2, 'c': 3, 'd': 4})