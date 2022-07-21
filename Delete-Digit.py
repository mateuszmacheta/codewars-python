# 6 kyu Delete a Digit
# https://www.codewars.com/kata/5894318275f2c75695000146

def delete_digit(n):
    s = str(n)
    max_n = 0
    for i in range(len(s)):
        cur_n = int(s[:i] + s[i+1:])
        if cur_n > max_n: max_n = cur_n
    return max_n


if __name__ == '__main__':
    print(delete_digit(154))