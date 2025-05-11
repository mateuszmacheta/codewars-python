# 5 kyu Basic Nico variation
# https://www.codewars.com/kata/5968bb83c307f0bb86000015/train/python

def nico(key, message):
    encoded_key = get_key(key)
    if len(message) % len(key):
        print(len(message) + len(key) - (len(message) % len(key)))
        message_padded = message.ljust(len(message) + len(key) - (len(message) % len(key)), ' ')
    else:
        message_padded = message
    cipher = []
    for i in range(0, len(message_padded) // len(key)):
        cipher += ([(x+i*len(key)) for x in encoded_key])
    return "".join(message_padded[i] for i in cipher)


def get_key(key: str):
    result = []
    sorted_key = sorted(key)
    for c in sorted_key:
        result.append(key.index(c))
    return result

# print(nico("crazy", "secretinformation"))
# print(nico("abc", "abcd"))
print(nico("ba", "1234567890"))