class TicTacToeEngine:
    def __init__(self, n_rows=3, n_cols=3):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.board = self.create_board(n_rows, n_cols)

    def create_board(self, n_rows, n_cols):
        board = []

        for row in range(int(n_rows)):
            row = []
            for column in range(int(n_cols)):
                row.append('-')
            board.append(row)

        return board

    def make_turn(self, player, x, y):
        if 0 <= x < int(self.n_cols) and 0 <= y < int(self.n_rows):
            if self.board[y][x] == "-":
                self.board[y][x] = player

                return True
            else:
                return False

    def is_draw(self):
        board_united = []

        for i in self.board:
            for j in i:
                board_united.append(j)

        if '-' not in board_united:
            return True
        else:
            return False

    def is_rows_winner(self):
        if int(self.n_rows) <= 3 or int(self.n_cols) <= 3:
            for row in self.board:
                for i in range(int(self.n_cols)):
                    if 0 < int(i) < (int(self.n_cols) - 1) and row[i] == row[i - 1] == row[i + 1] != "-":
                        return True

        elif int(self.n_rows) <= 5 or int(self.n_cols) <= 5:
            for row in self.board:
                for i in range(int(self.n_cols)):
                    if 0 < int(i) < (int(self.n_cols) - 2) and row[i] == row[i - 1] == row[i + 1] == row[i + 2] != "-":
                        return True

        else:
            for row in self.board:
                for i in range(int(self.n_cols)):
                    if (0 < int(i) < (int(self.n_cols) - 3) and
                            row[i] == row[i - 1] == row[i + 1] == row[i + 2] == row[i + 3] != "-"):
                        return True

    def is_cols_winner(self):
        board_vertical = [list(e) for e in zip(*self.board)]
        if int(self.n_cols) <= 3 or int(self.n_rows) <= 3:
            for row in board_vertical:
                for i in range(int(self.n_rows)):
                    print(i)
                    if 0 < int(i) < (int(self.n_rows) - 1) and row[i] == row[i - 1] == row[i + 1] != "-":
                        return True

        elif int(self.n_cols) <= 5 or int(self.n_rows) <= 5:
            for row in board_vertical:
                for i in range(int(self.n_cols)):
                    if 0 < int(i) < (int(self.n_rows) - 2) and row[i] == row[i - 1] == row[i + 1] == row[i + 2] != "-":
                        return True

        else:
            for row in board_vertical:
                for i in range(int(self.n_cols)):
                    if (0 < int(i) < (int(self.n_rows) - 3) and
                            row[i] == row[i - 1] == row[i + 1] == row[i + 2] == row[i + 3] != "-"):
                        return True

    def is_dias_winner(self):
        if int(self.n_cols) < 3 or int(self.n_rows) < 3:
            return False

        elif int(self.n_cols) == 3 and int(self.n_rows) == 3:
            for i in range(int(self.n_rows)):
                for j in range(int(self.n_rows)):
                    if (0 < int(i) < int(self.n_rows) - 1 and 0 < j < (int(self.n_cols) - 1) and
                            self.board[i][j] == self.board[i - 1][j - 1] == self.board[i + 1][j + 1] != "-"):
                        return True

            for i in range(int(self.n_rows)):
                for j in range(int(self.n_rows)):
                    if (0 < int(i) < int(self.n_rows) - 1 and 0 < j < (int(self.n_cols) - 1) and
                            self.board[i - 1][j + 1] == self.board[i][j] == self.board[i + 1][j - 1] != "-"):
                        return True

        elif int(self.n_cols) <= 5 or int(self.n_rows) <= 5:
            for i in range(int(self.n_rows)):
                for j in range(int(self.n_rows)):
                    if (0 < int(i) < int(self.n_rows) - 2 and 0 < j < (int(self.n_cols) - 2) and
                            self.board[i][j] == self.board[i - 1][j - 1] == self.board[i + 1][j + 1] ==
                            self.board[i + 2][j + 2] != "-"):
                        return True

            for i in range(int(self.n_rows)):
                for j in range(int(self.n_rows)):
                    if (0 < int(i) < int(self.n_rows) - 2 and 0 < j < (int(self.n_cols) - 1) and
                            self.board[i - 1][j + 1] == self.board[i][j] == self.board[i + 1][j - 1] ==
                            self.board[i + 2][j - 2] != "-"):
                        return True

        else:
            for i in range(int(self.n_rows)):
                for j in range(int(self.n_rows)):
                    if (0 < int(i) < int(self.n_rows) - 3 and 0 < j < (int(self.n_cols) - 3) and
                            self.board[i][j] == self.board[i - 1][j - 1] == self.board[i + 1][j + 1] ==
                            self.board[i + 2][j + 2] == self.board[i + 3][j + 3] != "-"):
                        return True

            for i in range(int(self.n_rows)):
                for j in range(int(self.n_rows)):
                    if (0 < int(i) < int(self.n_rows) - 3 and 0 < j < (int(self.n_cols) - 1) and
                            self.board[i - 1][j + 1] == self.board[i][j] == self.board[i + 1][j - 1] ==
                            self.board[i + 2][j - 2] == self.board[i + 3][j - 3] != "-"):
                        return True

    def __str__(self):
        row_lines = []
        for row in self.board:
            row_lines.append(" | ".join(row))

        string = "\n".join(row_lines)
        return string
