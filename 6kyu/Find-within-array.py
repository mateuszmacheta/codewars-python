# 6 kyu Find within array
# https://www.codewars.com/kata/51f082ba7297b8f07f000001/train/python

def find_in_array(seq, f):
    print(seq, f)
    for i, e in enumerate(seq):
        if f(e, i): return i
    return -1


if __name__ == '__main__':
    true_if_even = lambda v, i: v % 2 == 0
    never_true = lambda v, i: False
    true_if_value_equals_index = lambda v, i: v == i
    true_if_length_equals_index = lambda v, i: len(v) == i
    print(find_in_array([1,3,5,6,7], true_if_even) , 3)