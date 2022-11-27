from tkinter import *
import random

root = Tk()
root.title("Крестики-Нолики")
game_run = True  # глобальная переменная, к которой обращаемся из функции
field = []
cross_count = 0     # счетчик количества крестиков, чтобы после выставления пятого крестика фиксировать ничью, глобальная переменная, к которой обращаемся из функции


def new_game():   #  очистка игрового поля
    for row in range(3):
        for col in range(3):
            field[row][col]["text"] = " "
            field[row][col]["background"] = "lavender"
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):   # ход игрока
    if game_run and field[row][col]["text"] == " ":   # проверка пустого поля
        field[row][col]["text"] = "X"                 # заполняем поле крестиком
        global cross_count
        cross_count += 1
        check_win("X")                                 # проверка победителя после хода крестиков
        if game_run and cross_count < 5:
            computer_move()    # ход бота
            check_win("O")     # проверка победителя после хода ноликов


def check_win(smb):         # проверка победителя по победным линиям
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)


def check_line(a1,a2,a3,smb):  # проверка линии и изменение цвета полей, если победная линия содержит одинаковые символы
    if a1["text"] == smb and a2["text"] == smb and a3["text"] == smb:
        a1["background"] = a2["background"] = a3["background"] = "pink"
        global game_run
        game_run = False


def can_win(a1,a2,a3,smb):    # победный ход бота
    res = False
    if a1["text"] == smb and a2["text"] == smb and a3["text"] == " ":
        a3["text"] = "O"
        res = True
    if a1["text"] == smb and a2["text"] == " " and a3["text"] == smb:
        a2["text"] = "O"
        res = True
    if a1["text"] == " " and a2["text"] == smb and a3["text"] == smb:
        a1["text"] = "O"
        res = True
    return res


def computer_move():   #   ход бота 
    for n in range(3):  # если есть шанс победить, ход будет сделан в победную линию
        if can_win(field[n][0], field[n][1], field[n][2], "O"):
            return
        if can_win(field[0][n], field[1][n], field[2][n], "O"):
            return
    if can_win(field[0][0], field[1][1], field[2][2], "O"):
        return
    if can_win(field[2][0], field[1][1], field[0][2], "O"):
        return
    for n in range(3):  #  если есть вероятность проигрыша, бот делает ход в линию, которая почти выиграла
        if can_win(field[n][0], field[n][1], field[n][2], "X"):
            return
        if can_win(field[0][n], field[1][n], field[2][n], "X"):
            return
    if can_win(field[0][0], field[1][1], field[2][2], "X"):
        return
    if can_win(field[2][0], field[1][1], field[0][2], "X"):
        return
    while True:   # в остальных случаях ход делается в любую свободную клетку случайным образом
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]["text"] == " ":
            field[row][col]["text"] = "O"
            break


for row in range(3):   #  графический интерфейс
    line = []
    for col in range(3):
        button = Button(root, text=" ", width=4, height=2,     #  параметры кнопки
                        font=("Verdana", 28, "bold"),
                        background="lavender",
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky="nsew")   # размещение кнопки на сетке 
        line.append(button)   # добавляем кнопку в список line
    field.append(line)
new_button = Button(root, text="Новая игра", font=("Verdana", 12, "bold"), command=new_game)  #  кнопка запуска новой игры
new_button.grid(row=3, column=0, columnspan=3, sticky="nsew")
root.mainloop()