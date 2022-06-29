# 5 kyu flatten
# https://www.codewars.com/kata/513fa1d75e4297ba38000003/train/python

def flatten(*args):
    result = []
    for arg in args:
        if type(arg) is list:
            result.extend(flatten(*arg))
        else:
            result.append(arg)
    return result


if __name__ == '__main__':
    print(flatten([1,2],[3,4,5],[6,[7],[[8]]]))