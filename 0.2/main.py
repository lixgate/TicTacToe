board = []
player = "X"
game_continue = True
winner = None

def play_game():
    create_board()  #создает доску
    show_board()    #показывает доску

    while game_continue:
        make_turn(player)     #делает ход
        check_if_game_over()  #можно ли еще играть
        flip_player()         #меняет игрока


# принимает количество строк и столбцов от пользователя
def create_board():
    print("Доброе пожаловать в крестики-нолики. Введите количество игровых строк и столбцов.")
    rows = input("Введите количество строк ")
    while rows.isdigit() is False or int(rows) < 1:
        rows = input("Введите количество строк ")
    columns = input("Введите количество столбцов ")
    while columns.isdigit() is False or int(columns) < 1:
        columns = input("Введите количество столбцов ")
    for row in range(int(rows)):  # создаем игровое поле
        row = []
        for column in range(int(columns)):
            row.append('-')
        board.append(row)
    return board


# Показывает текущее состояние доски
def show_board():
    for row in board:
        print(*row, sep=" | ")


#делает ход. valid = True показывает, что проверки на корректность ввода и вохможность хода пройдены.
def make_turn(player):
    valid = False
    while not valid:
        print("Ход игрока {}".format(player))
        coordinates = (
            input("Введите координаты хода в виде 1 2 (первое число - столбец, второе число - строка): "))
        coor_lst = coordinates.split(" ")
        while " " not in coordinates:  #проверяем, есть ли пробел
            coordinates = (
                input("Введите координаты хода в виде 1 2 (первое число - столбец, второе число - строка): "))
        coor_lst = coordinates.split(" ")
        x = coor_lst[0]
        y = coor_lst[1]
        while (x.isdigit() is False or y.isdigit() is False or int(x) < 1 or int(y) < 1 or int(x) > len(board[0]) or int(y) > len(board)):
            x = input("Введите столбец: ")
            y = input("Введите строку: ")
        x = int(x) - 1
        y = int(y) - 1
        if board[y][x] == "-":
            valid = True
        else:
            print("Клетка уже занята")

    board[y][x] = player
    show_board()

# меняет игрока
def flip_player():
    global player
    if player == "X":
        player = "O"
        return player
    else:
        player = "X"
        return player


def check_if_game_over():
    check_for_winner()
    check_for_draw()


# Проверяет, есть ли еще ходы. Если ходы закончились и победитель не бы выявлен, игра заканчивается
def check_for_draw():
    if winner == None:
        board_united = []
        global game_continue
        for i in board:
            for j in i:
                board_united.append(j)
        if '-' not in board_united:
            game_continue = False
            print("Ничья")
            return game_continue


# Проверяет, сработало ли выигрышное условие. Если да, игра заканчивается, объявляется победитель
def check_for_winner():
    global game_continue, winner
    rows_winner = check_rows()
    columns_winner = check_columns()
    diagonals_winner = check_diagonals()

    if rows_winner == True or columns_winner == True or diagonals_winner == True:
        game_continue = False
        winner = player
        print("Победил игрок {}".format(player))
        print("GGWP")


# если три соседних знака равны и не равны "-" вовзращает True в check_for_winner.
def check_rows():
    for row in board:
            for i in range(len(board[0])):
                try:
                    if i > 0 and row[i] == row[i - 1] == row[i + 1] != "-":  # i>0 чтобы не складывались индексы 0,1,-1
                        return True
                except:
                    IndexError

# транспонирует текущее игровое поле и делает проверку по строкам.
# если три соседних знака равны и не равны "-" возвращает True в check_for_winner.
def check_columns():
    board_vertical = [list(e) for e in zip(*board)]
    for row in board_vertical:
            for i in range(len(board_vertical[0])):
                try:
                    if i > 0 and row[i] == row[i - 1] == row[i + 1] != "-":  # i>0 чтобы не складывались индексы 0,1,-1
                        return True
                except:
                    IndexError

# проверяет, есть ли выигрыш по диагонали. если поле меньше 3х3, возвращает False, иначе True в check_for_winner.
def check_diagonals():
    if len(board) < 3 or len(board[0]) < 3:
        return False
    else:
        for i in range(len(board)):
            for j in range(len(board)):
                try:
                    if i > 0  and j > 0 and board[i][j] == board[i - 1][j - 1] == board[i + 1][j + 1] != "-":
                        return True
                except:
                    IndexError

        for i in range(len(board)):
            for j in range(len(board)):
                try:
                    if i > 0 and j > 0 and board[i - 1][j + 1] == board[i][j] == board[i + 1][j - 1] != "-":
                        return True
                except:
                    IndexError

play_game()


