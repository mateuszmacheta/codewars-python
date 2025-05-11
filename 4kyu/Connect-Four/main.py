# 4 kyu Connect Four
# https://www.codewars.com/kata/56882731514ec3ec3d000009

class Connect_Four:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.board = [[0 for x in range(columns)] for y in range(rows)]
        self.winning_message = {'R': "Red", 'Y': "Yellow"}
        self.max_moves = rows * columns
        self.moves = 0

    def check_winner(self):
        winner = ""
        winner = self.check_columns()
        if winner != "":
            return self.winning_message[winner]

        winner = self.check_rows()
        if winner != "":
            return self.winning_message[winner]

        winner = self.check_diagonals()
        if winner != "":
            return self.winning_message[winner]

        if self.moves == self.max_moves:
            return "Draw"
        return ""

    def check_columns(self):
        for i in range(self.columns):
            sum = 0
            player = self.board[0][i]
            for j in range(self.rows):
                current_player = self.board[j][i]
                if current_player == player and self.board[j][i] != 0:
                    sum += 1
                    if sum >= 4:
                        return player
                else:
                    player = self.board[j][i]
                    sum = 1
        return ""

    def check_rows(self):
        for i in range(self.rows):
            sum = 0
            player = self.board[i][0]
            for j in range(self.columns):
                #print(f"i: {i} j: {j}")
                current_player = self.board[i][j]
                if current_player == player and self.board[i][j] != 0:
                    sum += 1
                    if sum >= 4:
                        return player
                else:
                    player = self.board[i][j]
                    sum = 1
        return ""

    def check_diagonals(self):
        # NW - SE
        rowStart = 1
        while True:
            if rowStart > self.rows - 4:
                break
            sum = 0
            y = rowStart
            x = 0
            player = self.board[y][x]
            while True:
                if y >= self.rows or x >= self.columns:
                    break
                current_player = self.board[y][x]
                if current_player == player and self.board[y][x] != 0:
                    sum += 1
                    if sum >= 4:
                        return player
                else:
                    player = self.board[y][x]
                    sum = 1
                x += 1
                y += 1
            rowStart += 1

        colStart = x = y = 0
        while True:
            if colStart > self.columns - 4:
                break
            sum = 0
            x = colStart
            y = 0
            player = self.board[y][x]
            while True:
                if y >= self.rows or x >= self.columns:
                    break
                current_player = self.board[y][x]
                if current_player == player and self.board[y][x] != 0:
                    sum += 1
                    if sum >= 4:
                        return player
                else:
                    player = self.board[y][x]
                    sum = 1
                x += 1
                y += 1
            colStart += 1

        # NE - SW
        rowStart = 1
        while True:
            if rowStart > self.rows - 4:
                break
            sum = 0
            y = rowStart
            x = self.columns - 1
            player = self.board[y][x]
            while True:
                #print('#1:', player, 'x:', x, ' y:', y)
                if y >= self.rows or x < 0:
                    break
                current_player = self.board[y][x]
                if current_player == player and self.board[y][x] != 0:
                    sum += 1
                    if sum >= 4:
                        return player
                else:
                    player = self.board[y][x]
                    sum = 1
                x -= 1
                y += 1
            rowStart += 1

        colStart = self.columns - 1
        while True:
            if colStart < 3:
                break
            sum = 0
            x = colStart
            y = 0
            player = self.board[y][x]
            while True:
                #print('#2:', player, 'x:', x, ' y:', y)
                if y >= self.rows or x < 0:
                    break
                current_player = self.board[y][x]
                if current_player == player and self.board[y][x] != 0:
                    sum += 1
                    if sum >= 4:
                        return player
                else:
                    player = self.board[y][x]
                    sum = 1
                x -= 1
                y += 1
            colStart -= 1
        return ""

    def make_move(self, move: str):
        column = ord(move[0]) - 65
        player = move[2]
        added = False
        for i in range(self.rows - 1, -1, -1):
            if self.board[i][column] == 0:
                self.board[i][column] = player
                added = True
                break
        if not added:
            return "Invalid move"
        self.moves += 1
        print(self)
        return self.check_winner()

    def __str__(self):
        result = []
        for i in range(0, self.rows):
            row = []
            for j in range(0, self.columns):
                row.append(str(self.board[i][j]))
            result.append("\t".join(row))
        return "\n".join(result) + "\n"


def who_is_winner(pieces_position_list):
    c4 = Connect_Four()
    for move in pieces_position_list:
        winner = c4.make_move(move)
        if winner != "":
            return winner
    return "Draw"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # yell = [
    #         "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
    #         "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
    #         "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
    #         ]
    #yell = ["A_Red", "A_Red", "A_Red", "A_Yellow", "B_Red", "B_Red", "B_Yellow", "C_Red", "C_Yellow", "D_Yellow"]
    red1 = ['D_Red', 'F_Yellow', 'E_Red', 'E_Yellow', 'D_Red', 'C_Yellow', 'B_Red', 'E_Yellow', 'D_Red', 'A_Yellow', 'G_Red', 'B_Yellow', 'C_Red', 'D_Yellow', 'E_Red', 'D_Yellow', 'B_Red', 'B_Yellow', 'B_Red', 'E_Yellow', 'D_Red']
    red1 = red1[:-6:]
    print(who_is_winner(red1))
