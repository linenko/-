#Опишем функции которые будем использовать в игре

#Вывод полей в консоль
def print_pole1():
    print(pole1[0], end=" ")
    print(pole1[1], end=" ")
    print(pole1[2])

    print(pole1[3], end=" ")
    print(pole1[4], end=" ")
    print(pole1[5])

    print(pole1[6], end=" ")
    print(pole1[7], end=" ")
    print(pole1[8])


def print_pole2():
    print(pole2[0],'', end=" ")
    print(pole2[1],'', end=" ")
    print(pole2[2],'', end=" ")
    print(pole2[3])

    print(pole2[4],'', end=" ")
    print(pole2[5],'', end=" ")
    print(pole2[6],'', end=" ")
    print(pole2[7])

    print(pole2[8],'', end=" ")
    print(pole2[9], end=" ")
    print(pole2[10], end=" ")
    print(pole2[11])

    print(pole2[12], end=" ")
    print(pole2[13], end=" ")
    print(pole2[14], end=" ")
    print(pole2[15])


#Сделать ходы
def step_pole1(step, symbol):
    ind = pole1.index(step)
    pole1[ind] = symbol


def step_pole2(step, symbol):
    ind = pole2.index(step)
    pole2[ind] = symbol


#Получить актуальный результат игры
def get_result():
    win = ""

    for i in pobedy:
        if pole1[i[0]] == "X" and pole1[i[1]] == "X" and pole1[i[2]] == "X":
            win = "X"
        if pole1[i[0]] == "O" and pole1[i[1]] == "O" and pole1[i[2]] == "O":
            win = "O"

    return win


def get_result2():
    win = ""

    for i in pobedy2:
        if pole2[i[0]] == "X" and pole2[i[1]] == "X" and pole2[i[2]] == "X" and pole2[i[3]] == "X":
            win = "X"
        if pole2[i[0]] == "O" and pole2[i[1]] == "O" and pole2[i[2]] == "O" and pole2[i[3]] == "O":
            win = "O"

    return win

#Выберем режим игры
print('Выберите режим игры: \nВведите 2 - режим двух игроков \nВведите 1 - режим игры против компьтера')
rezim = int(input())
if rezim == 2:

    #создадим массивы с полями игры
    pole1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pole2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    #создадим массив с выигрышными комбинациями
    pobedy = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    pobedy2 = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [0, 4, 8, 12], [1, 5, 9, 13],
               [2, 6, 10, 14], [3, 7, 11, 15], [0, 5, 10, 15], [12, 9, 6, 3]]

    #выберем размер поля из 2 предложенных
    print("Выберите размер поля: 3x3 (Введите 1) или 4x4 (Введите 2)")
    razmer = int(input())

    #Основная программа
    game_over = False
    player1 = True

    while game_over == False:

        # 1. Показываем карту
        if razmer == 1:
            print_pole1()
        else:
            print_pole2()
        # 2. Спросим у играющего куда делать ход
        if player1 == True:
            symbol = "X"
            step = int(input("Человек 1, ваш ход: "))
        else:
            symbol = "O"
            step = int(input("Человек 2, ваш ход: "))
        if razmer == 1:
            step_pole1(step, symbol)
        else:
            step_pole2(step, symbol)  # делаем ход в указанную ячейку
        if razmer == 1:
            win = get_result()  # определим победителя
        else:
            win = get_result2()
        if win != "":
            game_over = True
        else:
            game_over = False

        player1 = not (player1)

    # Игра окончена. Покажем карту. Объявим победителя.
    if razmer == 1:
        print_pole1()
    else:
        print_pole2()
    print("Победил", win)
    import random
    pr = random.randint(1, 4)
    if pr == 1:
        print('/ᐠ - ˕ -マ')
    if pr == 2:
        print(' ฅ^•ﻌ•^ฅ')
    if pr == 3:
        print('ᨐฅ')
    if pr == 4:
        print('ʕ•ﻌ•`ʔ')

else:
    #Игра с компьютером
    #создадим массив отвечающий за поле игры
    pole1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #Создадим массив с выигрышными комбинациями
    pobedy = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    #Искусственный интеллект: поиск линии с нужным количеством X и O на победных линиях
    def check_line(sum_O, sum_X):
        step = ""
        for line in pobedy:
            o = 0
            x = 0

            for j in range(0, 3):
                if pole1[line[j]] == "O":
                    o = o + 1
                if pole1[line[j]] == "X":
                    x = x + 1

            if o == sum_O and x == sum_X:
                for j in range(0, 3):
                    if pole1[line[j]] != "O" and pole1[line[j]] != "X":
                        step = pole1[line[j]]

        return step

    # Искусственный интеллект: выбор хода
    def AI():
        step = ""

        # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
        step = check_line(2, 0)

        # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
        if step == "":
            step = check_line(0, 2)

            # 3) если 1 фигура своя и 0 чужих - ставим
        if step == "":
            step = check_line(1, 0)

            # 4) центр пуст, то занимаем центр
        if step == "":
            if pole1[4] != "X" and pole1[4] != "O":
                step = 5

                # 5) если центр занят, то занимаем первую ячейку
        if step == "":
            if pole1[0] != "X" and pole1[0] != "O":
                step = 1

        return step


    # Основная программа
    game_over = False
    human = True

    while game_over == False:

        # 1. Показываем карту
        print_pole1()

        # 2. Спросим у играющего куда делать ход
        if human == True:
            symbol = "X"
            step = int(input("Человек, ваш ход: "))
        else:
            print("Компьютер делает ход: ")
            symbol = "O"
            step = AI()

        # 3. Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
        if step != "":
            step_pole1(step, symbol)  # делаем ход в указанную ячейку
            win = get_result()  # определим победителя
            if win != "":
                game_over = True
            else:
                game_over = False
        else:
            print("Ничья!")
            game_over = True
            win = "дружба"

        human = not (human)

    # Игра окончена. Покажем карту. Объявим победителя.
    print_pole1()
    print("Победил", win)
    import random
    pr = random.randint(1, 4)
    if pr == 1:
        print('/ᐠ - ˕ -マ')
    if pr == 2:
        print(' ฅ^•ﻌ•^ฅ')
    if pr == 3:
        print('ᨐฅ')
    if pr == 4:
        print('ʕ•ﻌ•`ʔ')




