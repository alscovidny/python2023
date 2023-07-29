from math import sqrt
a, b = input("Введите два числа: ").split() #Петя загадывает два числа
a, b = int(a), int(b)

if a<=1000 and b <=1000:

    k = a * b
    n = a + b
    #вариант 1
    sqrt_d = sqrt(n*n - 4*k) #корень из дискриминанта. по функции sqrt() из библиотеки math
    if sqrt_d < 0:
        print("комплексный корень") #на самом деле это условие для натуральных чисел не будет выполняться никогда
    else:
        num1, num2 = n/2 - sqrt_d/2, n/2 + sqrt_d/2
        print(f'По варианту 1: {int(num1)}, {int(num2)}')
    #вариант 2
    #сначала ищем одно из чисел через квадратное уравнение методом перебора от 1 до 1000 (если потребуется)
    a = 1
    while(a*a - a*n + k !=0):
        a += 1
    print(f'По варианту 2: {a}, {n-a}')

else:
    print("одно из чисел > 1000, попробуйте числа поменьше")
