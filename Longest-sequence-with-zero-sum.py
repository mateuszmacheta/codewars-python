# 5 kyu Longest sequence with zero sum
# https://www.codewars.com/kata/52b4d1be990d6a2dac0002ab/train/python

def max_zero_sequence(s):
    sum_index = dict()
    sum = 0
    max_arr = [0, 0, 0]
    for i in range(len(s)):
        sum += s[i]
        if sum == 0:
            if i + 1 > max_arr[0]:
                max_arr = i + 1, 0, i + 1
        elif sum in sum_index:
            if i - sum_index[sum] > max_arr[0]:
                max_arr = i - sum_index[sum], sum_index[sum] + 1, i + 1
        else:
            sum_index[sum] = i

    print(max_arr)
    return s[max_arr[1]: max_arr[2]]

if __name__ == '__main__':
    print(max_zero_sequence([1, 2, -3, 7, 8, -16]), [1, 2, -3])