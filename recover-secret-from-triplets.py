# 4 kyu Recover a secret string from random triplets
# https://www.codewars.com/kata/53f40dff5f9d31b813000774

def recoverSecret(triplets):
    letters = []
    for triplet in triplets:
        for c in triplet:
            if c not in letters:
                letters.append(c)
    target = len(letters)
    secret = ''
    while len(secret) < target:
        secret += get_first(triplets, letters, secret)
    return secret

def get_first(triplets : list, letters : list, secret : str):
    positions = {}
    for letter in letters:
        if letter in secret:
            continue
        for triplet in triplets:
            triplet_stripped = []
            for t in triplet:
                if t not in secret:
                    triplet_stripped.append(t)
            if letter in triplet_stripped:
                positions[letter] = max(positions[letter] if letter in positions else -1, triplet_stripped.index(letter))

    for letter in positions:
        if positions[letter] == 0:
            return letter
    return ''

t = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(t))