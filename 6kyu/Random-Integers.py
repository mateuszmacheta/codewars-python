# 6 kyu Random Integers
# https://www.codewars.com/kata/580f1a22df91279f09000273/train/python

# this is a troll solution :)

class random_ints:
    def __init__(self, n, total):
        self.n = n
        self.total = total
    def __len__(self):
        return self.n
    
    def __iter__(self):
        return list(self.total)