# 6 kyu Shortest steps to a number
# https://www.codewars.com/kata/5cd4aec6abc7260028dcd942/train/python

def shortest_steps_to_num(num):
    n, steps = num, 0
    while n > 1:
        if n % 2:
            n -= 1
        else:
            n //= 2
        steps += 1
    return steps


if __name__ == '__main__':
    print(shortest_steps_to_num(71))