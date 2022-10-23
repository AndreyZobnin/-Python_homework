#Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_positive(value):
    value = int(value)
    if value < 0:
        return False
    else:
        return True


def is_position(value):
    value = int(value)
    if 0 <= value <= (N - 1):
        return True
    else:
        return False


N = input('Введите натуральное число от 4 до 1000:')

while not is_int(N):
    print('Введённое значение не явлется целым числом')
    N = input('Введите натуральное число от 4 до 1000:')

while not is_positive(N):
    print('Введённое значение не явлется положительным числом')
    N = input('Введите натуральное число от 4 до 1000:')

while (4 > int(N)) or (int(N) > 1000):
    print('Введённое значение не явлется натуральным числом от 4 до 1000')
    N = input('Введите натуральное число от 4 до 1000:')

N = int(N)
f = open('Task2.txt', 'r')
s = f.readline()

sim = [2]
for line in f:
    strs = line.split(' ')
    for s in strs:
        if s != '':
            sim = sim + [int(s)]

f.close()

mults = []
for i in range(0, len(sim)):
    if N == sim[i]:
        print('N - простое число')
    elif N % sim[i] == 0:
        mults.append(sim[i])
print(mults)