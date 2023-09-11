# 6 kyu Hidden "Cubic" numbers
# https://www.codewars.com/kata/55031bba8cba40ada90011c4/train/python
import re

PATTERN = '\d{1,3}'

check_cubic = lambda num: int(num) == sum(int(d)**3 for d in num)

def is_sum_of_cubes(s):
    input, numbers = s, []
    while number_match := re.search(PATTERN, input):
        number = number_match.group(0)
        print(f'found: {number}')
        if check_cubic(number):
            numbers.append(number)
        input = input.replace(number, '', 1)
        print(input)
    if numbers:
        return f"{' '.join(numbers)} {sum(int(number) for number in numbers)} Lucky"
    return "Unlucky"


print(is_sum_of_cubes("&z _upon 407298a --- ???ry, ww/100 I thought, 631str*ng and w===y -721&()"), "407 407 Lucky")
print(is_sum_of_cubes("No numbers!"), "Unlucky")