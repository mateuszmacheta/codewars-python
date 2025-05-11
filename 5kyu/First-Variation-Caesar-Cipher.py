# 5 kyu First Variation on Caesar Cipher
# https://www.codewars.com/kata/5508249a98b3234f420000fb/train/python
import math

alphabet = ''.join(map(chr, range(ord('a'), ord('z') + 1)))


def moving_shift(s: str, shift: int) -> list:
    l = len(s)
    s_lower = s.lower()
    encoded = []
    for i, e in enumerate(s_lower):
        if e in alphabet:
            shifted_index = shift + i
            encoded_char = alphabet[(alphabet.index(e) + shifted_index) % len(alphabet)]
            if s[i].isupper(): encoded_char = encoded_char.upper()
            encoded.append(encoded_char)
        else:
            encoded.append(e)
    return split_message(encoded)


def demoving_shift(s: list, shift: int) -> str:
    s_joined = ''.join(s)
    s_lower = s_joined.lower()
    decoded = []
    for i, e in enumerate(s_lower):
        if e in alphabet:
            shifted_index = shift + i
            decoded_char = alphabet[(alphabet.index(e) - shifted_index) % len(alphabet)]
            if s_joined[i].isupper(): decoded_char = decoded_char.upper()
            decoded.append(decoded_char)
        else:
            decoded.append(e)
    return ''.join(decoded)


def split_message(m: list) -> str:
    l = len(m)
    chunk_rounded = math.ceil(l / 5)
    even_chunks_count = l // chunk_rounded
    arr = [chunk_rounded] * even_chunks_count
    if l - chunk_rounded * even_chunks_count > 0:
        arr.append(l - chunk_rounded * even_chunks_count)
    for _ in range(max(0, 5 - len(arr))):
        arr.append(0)
    result = []
    for e in arr:
        result.append('')
        for _ in range(e):
            result[-1] += m.pop(0)

    return result


if __name__ == '__main__':
    print(split_message(list("I should have known that you w")))
    # print(moving_shift("I should have known that you would have a perfect answer for me!!!", 1),
    # ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"])
    # print(demoving_shift(['J vltasl rlhr ', 'zdfog odxr ypw', ' atasl rlhr p ', 'gwkzzyq zntyhv', ' lvz wp!!!'], 1))

