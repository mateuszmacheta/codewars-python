# 3 kyu Upside-Down Numbers - Challenge Edition
# https://www.codewars.com/kata/59f98052120be4abfa000304/train/python
upside = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
center = {'0', '1', '8'}

upside_count = len(upside)
center_count = len(center)

def generate_for_given_digit_count(digits: int, x: str, y: str) -> int:
    digits_min = len(x)
    digits_max = len(y)
    # if we have digits that are for beginning of range end of range then we do additional check
    check_edge_digits = digits == digits_min or digits == digits_max
    if not check_edge_digits:
        if digits % 2: # odd number of digits
            count = upside_count ** (digits // 2 - 1) * center_count
        else: # even number of digits
            count = upside_count ** (digits // 2)
    else:
        return 0
    return 0

def upsidedown(x: str, y: str) -> int:
    digits_min = len(x)
    digits_max = len(y)
    count = 0
    for digits in range(digits_min, digits_max + 1):
        count += generate_for_given_digit_count(digits, x, y)
    return count

if __name__ == '__main__':
    print(upsidedown('0','10'))
    print(upsidedown('10','100'))
    # print(upsidedown('100000','12345678900000000'))
          