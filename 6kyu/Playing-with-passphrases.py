# 6 kyu Playing with passphrases
# https://www.codewars.com/kata/559536379512a64472000053/train/python


def play_pass(s, n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 1. shift
    s = [e if not e.isalpha() else alphabet[alphabet.index(e) + n] for e in s]
    # 2. digits
    s = [e if not e.isdigit() else str(9 - int(e)) for e in s]
    # 3. alternating case
    s = [e.upper() if i % 2 == 0 else e.lower() for i, e in enumerate(s)]
    return "".join(s[::-1])


if __name__ == '__main__':
    print(play_pass("I LOVE YOU!!!", 1))