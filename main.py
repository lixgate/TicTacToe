def turn(): #функция ввода координат и знака
        coordinate = tuple(input("Введите координаты в виде 11x или 23o: "))
        if len(coordinate) != 3:
                return print("Неккоректный ввод")
        else:
                try:
                        x = int(coordinate[0])
                        y = int(coordinate[1])
                except ValueError:
                        return print("Некорректные координаты, попробуйте еще раз")

                if coordinate[2] == "x" or coordinate[2] == "o":
                        x = int(coordinate[0]) - 1
                        y = int(coordinate[1]) - 1
                        mark = coordinate[2]
                        return x, y, mark
                else:
                        print("Некорректный знак, попробуйте еще раз")


def turn_made(x, y, mark): #функция вносит ход игрока на доску
        try:
                board[y][x]
        except IndexError:
                return print("Координаты вне игрового поля")
        if board[y][x] == "_":
                board[y].pop(x)
                board[y].insert(x, mark)
                return board
        else:
                print("Поле уже занято, сделайте ход еще раз")

board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
board_united = board[0] + board[1] + board[2]
win = 0

while win < 1 and (board_united).count("_") > 0: #до получения условия победы или окончания количества ходов
        turn_tup = turn() #получаю значение функции
        if type(turn_tup) == tuple:
                x = turn_tup[0]
                y = turn_tup[1]
                mark = turn_tup[2]
                turn_made(x, y, mark)
                print(board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
                print(board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
                print(board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])

                board_united = board[0] + board[1] + board[2]

                #horizontal check сравниваю значения по горизонтали друг с другом. если совпадают, то win = 1
                counth1 = 0
                counth2 = 0
                counth3 = 0

                for i in board[0]:
                        if board[0][0] == i and i != "_":
                                counth1 += 1
                for i in board[1]:
                        if board[1][0] == i and i != "_":
                                counth2 += 1
                for i in board[2]:
                        if board[2][0] == i and i != "_":
                                counth3 += 1
                if counth1 == 3 or counth2 == 3 or counth3 == 3:
                        win = 1

                #vertical check сравниваю значения по вертикали друг с другом. циклами не смог
                if board[0][0] == board[1][0] and board[0][0] == board[2][0] and  board[0][0] != "_":
                        win = 1
                if board[0][1] == board[1][1] and board[0][1] == board[2][1] and  board[0][1] != "_":
                        win = 1
                if board[0][2] == board[1][2] and board[0][2] == board[2][2] and  board[0][2] != "_":
                        win = 1

                #diagonal check сравниваю значения по диагонали друг с другом.
                if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != "_":
                        win = 1
                if board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[1][1] != "_":
                        win = 1
        else:
                continue # если введеные координаты не tuple, то следующая итерация
else:
        if win >= 1 and board_united.count("_") >= 0:
                print("{} is the boss of the ♂gym♂ !".format(mark))
                print("Game over")
        else:
                print("No winner")