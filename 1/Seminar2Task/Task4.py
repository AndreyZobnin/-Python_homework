#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число  N '))
list = []

for i in range(-n,n+1):
    list.append(i)
print(list)

res = 1
with open('file1.txt','w') as data:
    data.write('2 \n')
    data.write('1 \n')
    data.write('3 \n')
    data.write('0 \n')
    data.write('5 \n')
    # data.write('4 \n')

patch = 'file.txt'
data = open(patch, 'r')

for line in data:
    pos = int(line)
    res *= list[pos]
print(res)