num = input('введите число: ')
print(type(num))
sum = 0
for i in num:
    if i != '.':
     sum += int(i)
print(sum)