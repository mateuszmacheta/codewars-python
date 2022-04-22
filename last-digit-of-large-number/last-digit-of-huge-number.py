# 3 kyu Last digit of a huge number
# https://www.codewars.com/kata/5518a860a73e708c0a000027/train/python

def last_digit(lst):
    print(lst)

    if len(lst) == 0:
        return 1
    if len(lst) == 1:
        return lst[0] % 10
    my_list = lst.copy()
    for i in range(len(my_list)-1, 0, -1):
        my_list[i-1] = pow(my_list[i-1], my_list[i], 10)
    return my_list[0]

#print(last_digit([3, 4, 5]))
print(last_digit([7, 6, 21]))