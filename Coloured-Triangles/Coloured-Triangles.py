# 7 kyu Coloured Triangles
# https://www.codewars.com/kata/coloured-triangles

reduction = {'RR': 'R', 'GG': 'G', 'BB': 'B', 'BG': 'R', 'GB': 'R',
             'RG': 'B', 'GR': 'B', 'BR': 'G', 'RB': 'G'}


def triangle(row):
    line = list(row)
    l = len(line)
    while l > 1:
        for i in range(1, l):
            line[i-1] = reduction[line[i-1] + line[i]]
        l -= 1
        print(line[:l])
    return line[0]


if __name__ == '__main__':
    print(triangle('RRGBRGBB'))