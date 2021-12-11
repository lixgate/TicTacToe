from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

from tic_tac_toe import TicTacToeEngine


Builder.load_file("./tic_tac_toe.kv")
Window.size = (450, 550)


class TictactoeWidget(Widget):
    pass


class TictactoeApp(App):
    def build(self):
        return TictactoeWidget()

    current_player = "X"
    game = TicTacToeEngine(3, 3)
    board = game.create_board(3, 3)
    x_wins = 0
    o_wins = 0

    def make_turn(self, btn):
        if self.current_player == "X":
            btn.text = "X"
            btn.disabled = True
            self.root.ids.game_message.text = "Ход игрока O"
            self.current_player = "O"

        else:
            btn.text = "O"
            btn.disabled = True
            self.root.ids.game_message.text = "Ход игрока X"
            self.current_player = "X"

        self.board_transformed()
        self.is_draw()
        self.is_winner()



    def game_winner(self, a, b, c):

        a.color = "red"
        b.color = "red"
        c.color = "red"

        self.disable_all_buttons()
        self.root.ids.game_message.text = f"Игрок {a.text} победил!"
        if a.text == "X":
            self.x_wins += 1
            self.root.ids.game_score.text = f"X: {self.x_wins} | O: {self.o_wins}"
        else:
            self.o_wins += 1
            self.root.ids.game_score.text = f"X: {self.x_wins} | O: {self.o_wins}"

    def is_winner(self):
        self.is_rows_winner()
        self.is_cols_winner()
        self.is_dias_winner()

    def board_transformed(self):

        self.board[0][0] = self.root.ids.btn1.text
        self.board[0][1] = self.root.ids.btn2.text
        self.board[0][2] = self.root.ids.btn3.text
        self.board[1][0] = self.root.ids.btn4.text
        self.board[1][1] = self.root.ids.btn5.text
        self.board[1][2] = self.root.ids.btn6.text
        self.board[2][0] = self.root.ids.btn7.text
        self.board[2][1] = self.root.ids.btn8.text
        self.board[2][2] = self.root.ids.btn9.text

    def is_rows_winner(self):
        row_number = 0
        for row in self.board:
            row_number += 1
            for i in range(3):
                if 0 < int(i) < 2 and row[i] == row[i - 1] == row[i + 1] != "":
                    if row_number == 1:
                        self.game_winner(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)
                    elif row_number == 2:
                        self.game_winner(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)
                    elif row_number == 3:
                        self.game_winner(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)

    def is_cols_winner(self):
        board_vertical = [list(e) for e in zip(*self.board)]
        row_number = 0
        for row in board_vertical:
            row_number += 1
            for i in range(3):
                if 0 < int(i) < 2 and row[i] == row[i - 1] == row[i + 1] != "":
                    if row_number == 1:
                        self.game_winner(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)
                    elif row_number == 2:
                        self.game_winner(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)
                    elif row_number == 3:
                        self.game_winner(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)

    def is_dias_winner(self):
        for i in range(3):
            for j in range(3):
                if (0 < int(i) < 2 and 0 < j < 2 and
                        self.board[i][j] == self.board[i - 1][j - 1] == self.board[i + 1][j + 1] != ""):
                    self.game_winner(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)

        for i in range(3):
            for j in range(3):
                if (0 < int(i) < 2 and 0 < j < 2 and
                        self.board[i - 1][j + 1] == self.board[i][j] == self.board[i + 1][j - 1] != ""):
                    self.game_winner(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)

    def is_draw(self):
        board_united = []

        for i in self.board:
            for j in i:
                board_united.append(j)
        if '' not in board_united:
            self.root.ids.game_message.text = "Ничья"

    def disable_all_buttons(self):
        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True

    def restart_game(self):

        self.current_player = "X"
        self.root.ids.game_message.text = "Игрок Х начинает"

        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = ""
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = ""
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""

        self.root.ids.btn1.color = "black"
        self.root.ids.btn2.color = "black"
        self.root.ids.btn3.color = "black"
        self.root.ids.btn4.color = "black"
        self.root.ids.btn5.color = "black"
        self.root.ids.btn6.color = "black"
        self.root.ids.btn7.color = "black"
        self.root.ids.btn8.color = "black"
        self.root.ids.btn9.color = "black"


if __name__ == "__main__":
    TictactoeApp().run()
