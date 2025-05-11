# 5 kyu Snakes and Ladders
# https://www.codewars.com/kata/587136ba2eefcb92a9000027/train/python

class SnakesLadders():
    def __init__(self):
        self.board = [[] for i in range(0, 101)]
        self.board[0] = [0, 1]
        self.jumps = {  # snakes
            16: 6, 46: 25, 49: 11, 62: 19, 64: 60,
            74: 53, 89: 68, 92: 88, 95: 75, 99: 80,
            # ladders
            2: 38, 7: 14, 8: 31, 15: 26, 21: 42,
            28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94
        }
        self.player = 0  # 0 or 1
        self.win_message = ''

    def __str__(self):
        positions = [None, None]
        for i, e in enumerate(self.board):
            if e:
                for e_pos in e:
                    positions[e_pos] = i
            if positions[0] and positions[1]: break
        o = []
        for i in [0, 1]:
            o.append(f'Player {i + 1} is on square {positions[i]}')
        return '\n'.join(o)

    def play(self, die1, die2):
        print(f'Throw {die1} {die2}')
        if self.win_message:
            return 'Game over!'

        for i, e in enumerate(self.board):
            if self.player in e:
                print(f'Player {self.player + 1} position is {i}')
                currentPosition = i
        nextPosition = currentPosition + die1 + die2

        # rewrite board
        if nextPosition > 100:
            nextPosition = 100 - (nextPosition - 100)

        if nextPosition in self.jumps:
            nextPosition = self.jumps[nextPosition]


        self.board[currentPosition].remove(self.player)
        self.board[nextPosition].append(self.player)

        message = f'Player {self.player + 1} is on square {nextPosition}'

        # winning condition
        if self.board[-1]:
            self.win_message = f'Player {self.player + 1} Wins!'
            return self.win_message
        # switch player if die values are not the same
        if die1 != die2:
            self.player = (self.player + 1) % 2

        return message


if __name__ == '__main__':
    game = SnakesLadders()
    # print(game.play(1, 1), "Player 1 is on square 38")
    # print(game.play(1, 5), "Player 1 is on square 44")
    game.board[0] = []
    game.board[42] = [0]
    game.board[98] = [1]
    print(game)
    game.player = 1
    print(game.play(4, 6))