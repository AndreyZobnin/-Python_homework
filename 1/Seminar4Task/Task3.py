#Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

nums = 111566773322
str = str(nums)
my_dictionary = {}

for i in str:
    if i not in my_dictionary:
        my_dictionary[i] = 0
    elif i in my_dictionary:
        my_dictionary[i] += 1

print(my_dictionary)
unique = []


for k, v in my_dictionary.items():
    if v == 0:
        unique.append(int(k))


print(unique)