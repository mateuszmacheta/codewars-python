# 4 kyu Codewars style ranking system
# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python

class User:
    ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        self.rank = User.ranks[0]
        self.progress = 0

    def inc_progress(self, kata_lvl: int):
        print(f'completed kata lvl {kata_lvl}')
        kata_difference = User.ranks.index(kata_lvl) - User.ranks.index(self.rank)
        print(f'diff: {kata_difference}')
        if kata_difference <= -2:
            return
        if kata_difference == -1:
            award = 1
        elif kata_difference == 0:
            award = 3
        else:
            award = 10 * kata_difference * kata_difference

        if self.progress + award >= 100:
            if User.ranks.index(self.rank) < len(User.ranks) - 1:
                self.rank = User.ranks[User.ranks.index(self.rank) + 1]
                print(f'Promoted to {self.rank}!')
                self.progress = (self.progress + award) % 100
            else:
                self.progress = 100
                print('Maximum rank!')
        else:
            self.progress += award




if __name__ == '__main__':
    u = User()
    u.inc_progress(-7)
    print(u.rank, u.progress)
    u.inc_progress(-5)
    print(u.rank, u.progress)