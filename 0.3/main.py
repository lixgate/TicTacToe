board = []
player = "X"
game_continue = True
winner = None


def play_game():
    show_rules()
    create_board()  #создает доску
    show_board()    #показывает доску

    while game_continue:
        make_turn(player)     #делает ход
        check_if_game_over()  #можно ли еще играть
        flip_player()         #меняет игрока


def show_rules():
    print("Добро пожаловать в крестики-нолики REMASTERED")
    print("Перед началом игры Вам будет предложено выбрать размер игрового поля.")
    print("Первый, выстроивший в ряд своих фигуры по вертикали, горизонтали или диагонали, выигрывает.")
    print("Для поля 3х3 - 3 в ряд")
    print("Для поля 5х5 и меньше - 4 в ряд")
    print("Для поля 6х6 и больше - 5 в ряд")
    print()


# принимает количество строк и столбцов от пользователя
def create_board():
    print("Введите количество игровых строк и столбцов.")
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
    if winner is None:
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

    if rows_winner is True or columns_winner is True or diagonals_winner is True:
        game_continue = False
        winner = player
        print("Победил игрок {}".format(player))
        print("GGWP")


# проверяет победу по горизонтали. если три соседних знака равны и не равны "-" вовзращает True в check_for_winner.
def check_rows():
    # проверка 3 в ряд
    if len(board) <= 3 or len(board[0]) <= 3:
        for row in board:
            for i in range(len(board[0])):
                if 0 < i < (len(board[0])-1) and row[i] == row[i - 1] == row[i + 1] != "-":
                    return True
    # проверка 4 в ряд
    elif len(board) <= 5 or len(board[0]) <= 5:
        for row in board:
            for i in range(len(board[0])):
                if 0 < i < (len(board[0])-2) and row[i] == row[i - 1] == row[i + 1] == row[i + 2] != "-":
                    return True
    # проверка 5 в ряд
    else:
        for row in board:
            for i in range(len(board[0])):
                if 0 < i < (len(board[0])-3) and row[i] == row[i - 1] == row[i + 1] == row[i + 2] == row[i + 3] != "-":
                    return True



# транспонирует текущее игровое поле и делает проверку по вертикали.
# если три соседних знака равны и не равны "-" возвращает True в check_for_winner.
def check_columns():
    #транспонирует доску, чтобы свести задачу по поиску вертикальной победы к предыдущей
    board_vertical = [list(e) for e in zip(*board)]
    if len(board_vertical) <= 3 or len(board_vertical[0]) <= 3:
        for row in board_vertical:
            for i in range(len(board_vertical[0])):
                if 0 < i < (len(board_vertical[0])-1) and row[i] == row[i - 1] == row[i + 1] != "-":
                    return True
    elif len(board_vertical) <= 5 or len(board_vertical[0]) <= 5:
        for row in board_vertical:
            for i in range(len(board_vertical[0])):
                if 0 < i < (len(board_vertical[0])-2) and row[i] == row[i - 1] == row[i + 1] == row[i + 2] != "-":
                    return True
    else:
        for row in board_vertical:
            for i in range(len(board_vertical[0])):
                if 0 < i < (len(board_vertical[0])-3) and row[i] == row[i - 1] == row[i + 1] == row[i + 2] == row[i + 3] != "-":
                    return True

# проверяет, есть ли выигрыш по диагонали. если поле меньше 3х3, возвращает False, иначе True в check_for_winner.
def check_diagonals():
    #для полей со стороной меньше 3 диагональная проверка отсустсвует
    if len(board) < 3 or len(board[0]) < 3:
        return False

    #проверка поля 3х3. побеждает 3 в ряд
    elif len(board) == 3 and len(board[0]) == 3:
        for i in range(len(board)):
            for j in range(len(board)):
                if 0 < i < (len(board) - 1) and 0 < j < (len(board[0]) - 1) and board[i][j] == board[i - 1][j - 1] == board[i + 1][j + 1] != "-":
                    return True

        for i in range(len(board)):
            for j in range(len(board)):
                if 0 < i < (len(board) - 1) and 0 < j < (len(board[0]) - 1) and board[i - 1][j + 1] == board[i][j] == board[i + 1][j - 1] != "-":
                    return True

    #проверка полей до 5x5, побеждает 4 в ряд
    elif len(board) <= 5 or len(board[0]) <= 5:
        for i in range(len(board)):
            for j in range(len(board)):
                if 0 < i < (len(board) - 2) and 0 < j < (len(board[0]) - 2) and board[i][j] == board[i - 1][j - 1] == board[i + 1][j + 1] == board[i + 2][j + 2] != "-":
                    return True

        for i in range(len(board)):
            for j in range(len(board)):
                if 0 < i < (len(board) - 2) and 0 < j < (len(board[0]) - 1) and board[i - 1][j + 1] == board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] != "-":
                    return True

    #проверка полей больше 5х5, побеждает 5 в ряд
    else:
        for i in range(len(board)):
            for j in range(len(board)):
                if 0 < i < (len(board) - 3) and 0 < j < (len(board[0]) - 3) and board[i][j] == board[i - 1][j - 1] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] != "-":
                    return True

        for i in range(len(board)):
            for j in range(len(board)):
                if 0 < i < (len(board) - 3) and 0 < j < (len(board[0]) - 1) and board[i - 1][j + 1] == board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] == board[i + 3][j - 3] != "-":
                    return True

#запускаем игру
play_game()