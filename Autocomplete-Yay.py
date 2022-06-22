# 6 kyu Autocomplete! Yay!
# https://www.codewars.com/kata/5389864ec72ce03383000484


import re


def autocomplete(input_, dictionary):
    clean = re.sub(r'\W', '', input_)
    return [entry for entry in dictionary if re.match(r'^' + clean, entry, flags=re.IGNORECASE)]


if __name__ == '__main__':
    dictionary = ['abnormal',
                  'arm-wrestling',
                  'absolute',
                  'airplane',
                  'airport',
                  'amazing',
                  'apple',
                  'ball']
    print(autocomplete('ai@@#$', dictionary))