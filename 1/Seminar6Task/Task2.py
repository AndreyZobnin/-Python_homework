# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
	# Пример:
	# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
	
print('Введите целое число: ')
N = int(input())
	
list = [i for i in range(-N, N + 1)]
print(list)