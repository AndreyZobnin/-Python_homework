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

#mas = list(map(chr, range(97, 123)))  
#print(mas)
#n=15
#b1=0
#b2=25
#a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
#a=a%1
#s=''
#for i in range (10):
#    a = a*(datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
#    a=(a*1000)%1
#    #sleep(1)
#    print(a)
#    stroka=mas[round(b1+(b2-b1)*a)]
#    s+=stroka
#print(s)


#import math
#from scipy.optimize import fsolve
#def func(x):
#    return x*math.cos(x-4)
#
#x0 = fsolve(func, 0.0)

#Сумма делителей двух чисел
""" a = int(input("Введите число:  "))
b = int(input("Введите число:  "))
#a, b = 7, 5
i = min(a, b)
while True:
    if i%a==0 and i%b==0:
        break
    i += 1
print(i) """


""" def gin(): # get valid int number
    try:
        user_input = int(input('Введите целое число '))
        return user_input
    except ValueError as v:
        print(v)         
        return gin()

n1 = gin()
n2 = gin()
a = True
b = 1
while a:
    if (n1*b) % n2 == 0:
        print(n1*b)
        a = False        
    b += 1
 """