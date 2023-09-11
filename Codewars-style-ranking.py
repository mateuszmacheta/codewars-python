# 4 kyu Codewars style ranking system
# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python

class User:
    ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        self.rank = User.ranks[0]
        self.progress = 0
        self._check_promotion(0)

    def __str__(self) -> str:
        return f"{self.rank} level and {self.progress}% progress."
    
    
    
    def _check_promotion(self, award: int):
        maximum_rank = User.ranks.index(self.rank) == len(User.ranks) - 1
        if not maximum_rank:
            up_levels, remainder = divmod(self.progress + award, 100)
            print(f'User can gain {up_levels} levels and end up with {remainder}% progress.')
            for _ in range(up_levels):
                if User.ranks.index(self.rank) < len(User.ranks) - 1: # there's room to level up
                    self.rank = User.ranks[User.ranks.index(self.rank) + 1]
                    print(f'Promoted to {self.rank}!')
                else:
                    print('Maximum rank!')
                    maximum_rank = True
                    break
          

        if maximum_rank or User.ranks.index(self.rank) == len(User.ranks) - 1:
            self.progress = 0
        else:
            self.progress = remainder

    def inc_progress(self, kata_lvl: int):
        print(f'Current rank:\t\t{self.rank}\nCurrent progress:\t{self.progress}')
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
        print(f'Award:\t\t{award}')
        self._check_promotion(award)



if __name__ == '__main__':
    # user = User()
    # user.rank = -2
    # user.progress = 80
    # print(user)
    # user.inc_progress(1)
    # print(user)
    # print("expected rank -1")

    # user = User()
    # user.inc_progress(-7)
    # print(user)
    # user.inc_progress(-5)
    # print(user)
    # print("expecting lvl -7 and progress 0")

    # user = User()
    # user.rank = 8
    # user.progress = 1
    # print(user)
    # user.inc_progress(8)
    # print(user)
    # print("expecting lvl 8 and progress 0")

    # Current rank:		7
    # Current progress:	91
    # completed kata lvl 8
    # diff: 1
    # Award:		10
    # User can gain 1 lelves and end up with 1% progress.
    # Promoted to 8!

    user = User()
    user.rank = 7
    user.progress = 91
    user.inc_progress(8)
    print(user)
    print("expecting level 8 with 0 progress")