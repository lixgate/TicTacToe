from tic_tac_toe import TicTacToeEngine


def show_rules():
    print("Добро пожаловать в крестики-нолики REMASTERED")
    print("Перед началом игры Вам будет предложено выбрать размер игрового поля.")
    print("Первый, выстроивший в ряд своих фигуры по вертикали, горизонтали или диагонали, выигрывает.")
    print("Для поля 3х3 - 3 в ряд")
    print("Для поля 5х5 и меньше - 4 в ряд")
    print("Для поля 6х6 и больше - 5 в ряд")
    print()


def take_board_size(n_rows="", n_cols=""):
    while n_rows.isdigit() is False or n_cols.isdigit() is False or int(n_rows) < 1 or int(n_cols) < 1:
        n_cols = input("Введите количество столбцов ")
        n_rows = input("Введите количество строк ")
    return n_rows, n_cols


def take_turn_coordinates(x=0, y=0, n_rows=3, n_cols=3):
    turn_coordinates = [x, y]
    while (" " not in turn_coordinates or str(turn_coordinates_lst[0]).isdigit() is False or
           str(turn_coordinates_lst[1]).isdigit() is False or int(turn_coordinates_lst[0]) < 0 or
           int(turn_coordinates_lst[1]) < 0 or int(turn_coordinates_lst[0]) > int(n_cols) or
           int(turn_coordinates_lst[1]) > int(n_rows)):
        turn_coordinates = input(
            "Введите координаты хода в виде 1 2 (первое число - столбец, второе число - строка): ")
        turn_coordinates_lst = turn_coordinates.split(" ")
    x, y = int(turn_coordinates_lst[0]) - 1, int(turn_coordinates_lst[1]) - 1

    return x, y


def play_game():
    show_rules()
    board_size = take_board_size()
    game = TicTacToeEngine(board_size[0], board_size[1])
    game_continue = True
    current_player = 'X'
    print("Ход игрока X")

    while game_continue:

        turn_coordinates = take_turn_coordinates(n_rows=int(board_size[0]), n_cols=int(board_size[1]))
        is_turn_done = game.make_turn(current_player, int(turn_coordinates[0]), int(turn_coordinates[1]))
        if not is_turn_done:
            continue

        if game.is_rows_winner() or game.is_cols_winner() or game.is_dias_winner():
            print(game)
            print(f"Игрок {current_player} победил!")
            break

        if game.is_draw():
            print(game)
            print("Ничья")
            break

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

        print()
        print(game)
        print()
        print(f"Ход игрока {current_player}")


play_game()
