#Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

dig = [6, 3, 6, 10, 12, 19, 1]
print(dig)
summ = 0
for i in range(1, len(dig), 2):
    if i % 2 == 1:
        summ += dig[i]       
print(f"{dig} -> сумма элементов на нечётных позициях: {summ}")