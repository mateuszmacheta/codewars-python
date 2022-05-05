import itertools as it


def valid_word(seq, word):
    if not seq: return False
    indexes = range(-1, len(seq))
    maxlen = len(word)
    words = set()
    maxelements = len(word) // min([len(w) for w in seq])
    for combination in it.product(indexes, repeat=maxelements):
        combined_word = ''
        try:
            for index in combination:
                if index == -1: continue
                if not word.startswith(combined_word) or len(combined_word) > maxlen: raise Exception("Not valid")
                combined_word += seq[index]
            words.add(combined_word)
        except:
            pass
    return word in words


print(valid_word(['code', 'wars'], 'codewars'))
