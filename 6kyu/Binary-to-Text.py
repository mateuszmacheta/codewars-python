# 6 kyu Binary to Text (ASCII) Conversion
# https://www.codewars.com/kata/5583d268479559400d000064/train/python

def binary_to_string(binary):
    if binary:
        return ''.join(map(lambda x: chr(int(x, 2)), (binary[8*i:8*i+8] for i in range(len(binary)//8))))
    return ''


if __name__ == '__main__':
    print(binary_to_string('0100100001100101011011000110110001101111'), 'Hello')