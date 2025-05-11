# 5 kyu Can you get the loop ?
# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python

def loop_size(node):
    list = []
    list.append(id(node))
    current = node.next
    i = 0
    while id(current) not in list:
        list.append(id(current))
        current = current.next
        i += 1
    return i - list.index(id(current))