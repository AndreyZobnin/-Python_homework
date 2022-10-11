#n = int(input('Введите целое число: '))
#n = abs(n)
#for number in range(-n, n+1):
#     print(number)

# или

#N = int(input('Введите число N: '))
#N = abs(N)

#for i in range(-N, N+1):
#    print(i, end=', ')



#print(int(float(input("Введите число: "))*10)%10)

#a = float(input())
#b = int(a * 10 % 10)
#if b == 0:
#    print('no')
#print(b)


 #Напишите программу, которая принимает на вход число и проверяет, 
 #5кратно ли оно 5 и 10 или 15, но не 30.

#num = int(input('Введите число'))
#print(num)
#if (num%10 == 0 or num%15 == 0) and num%30 != 0:
#     print("Число удовлетворяет условию")
#else:
#     print("Число НЕ удовлетворяет условию") 

# или

#a =float (input())
#if ( a % 5 == 0 and a % 10 == 0 or a % 15 == 0 ) and a % 30!=0 :
#    print ("True")
#else: 
#    print ("False")


#while True:
#    x = int(input())
#    count = 0
#    y = 1
#
#    while count < x:
#        count += 1
#        y *= count
#
#    else:
#        print(y)

#a = int (input())
#b = 1
#for i in range (1,a+1):
#    b = b*i
#print(b)

#N = int(input('Введите число N: '))
#for i in range(N):
#     result = (-3)**i
#     print(result, end=" ")

#n = int(input('Введите натуральное число '))
#dict = {}
#for i in range (1,n+1):
#     dict[i] = 3*i + 1
#print(dict)

float_num = input('введите числа: ')
print(type(float_num))
sum = 0
for i in float_num:
     if i != '.':
         sum += int(i)
print(sum)