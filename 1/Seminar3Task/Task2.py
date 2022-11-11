# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

Spisok = [2, 3, 4, 5, 6]

# if len(list)%2 == 0:
#     size = len(list) // 2
import math 
size = math.ceil(len(Spisok)/2)
print(size)
spisok2 = []
for i in range(size):
    spisok2.append(Spisok[i]*Spisok[-i - 1])
print(spisok2)