# Напишем программу, которая считывает 10 чисел и определяет сколько из них больше 10.
#
# counter = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
# print('Было введено', counter, 'чисел, больших 10.')

# посчитаем еще и количество нулей среди введенных чисел.
#
# counter1 = 0
# counter2 = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter1 = counter1 + 1
#     if num == 0:
#         counter2 = counter2 + 1
# print('Было введено', counter1, 'чисел, больших 10.')
# print('Было введено', counter2, 'нулей.' )

# Напишем программу, которая считывает 10 чисел и определяет сумму тех из них, которые больше 10.
#
# total = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         total = total + num
# print('Сумма чисел больших 10 равна',  total)

# считает сумму натуральных чисел от 1 до 100:
#
# total = 0
# for i in range(1, 101):
#     total = total + i
# print('Сумма равна', total)

# натуральное число является простым:
# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#
# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

#  считывает 10 положительных чисел и находит среди них наибольшее число.
#
# largest = -1
# for i in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)

# находит среди них наибольшее:
#
# largest = int(input())  # принимаем первое число за максимальное
# for i in range(9):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)

# num1 = 4
# num2 = 6
# num1 += num2
# num1 *= num1
# print(num1)

# total = 0
# for i in range(1, 6):
#     total += i
# print(total)

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')

# подсчитывает количество чисел в диапазоне от a до b включительно,
# куб которых оканчивается на 4 или 9.
# a, b = int(input()), int(input())
# counter = 0
# for i in range(a, b + 1):
#     if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#         counter += 1
# print(counter)

# На вход программе подается натуральное число n,
# а затем n целых чисел, каждое на отдельной строке.
# Напишите программу, которая подсчитывает сумму введенных чисел.

# n = int(input())
# su = 0
# for i in range(n):
#     num = int(input())
#     su += num
# print(su)

# n = int(input())
# import math
# su = 0
# for i in range(1, n + 1):
#     su += 1 / i
# print(su - math.log(n))


# На вход программе подается натуральное число n.
# Напишите программу, которая подсчитывает сумму тех чисел от 1 до n
# (включительно) квадрат которых оканчивается на 2, 5 или 8.

# n = int(input())
# su = 0
# for i in range(n + 1):
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         su += i
#
# print(su)

# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет n!.

# n = int(input())
# mult = 1
# if n < 13:
#     for i in range (1, n + 1):
#         mult = mult * i
# print(mult)

# которая считывает 10 чисел и выводит произведение отличных от нуля чисел

# mult = 1
# for i in range(1, 11):
#     num = int(input())
#     if num != 0:
#         mult *= num
# print(mult)

# которая вычисляет сумму всех его делителей.

# n = int(input())
# su = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         su += i
# print(su)

#  Напишите программу вычисления знакочередующей суммы
# 1−2+3−4+5−6+

# n = int(input())
# su = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         su -= i
#     else:
#         su += i
# print(su)

# На вход программе подается натуральное число n, а затем n различных
# натуральных чисел, каждое на отдельной строке. Напишите программу,
# которая выводит наибольшее и второе наибольшее число последовательности.

# n = int(input())
# mm = 2
# nn = 1
# for i in range(n):
#     num = int(input())
#     if num > mm:
#         nn = mm
#         mm = num
#     elif num > nn:
#         nn = num
# print(mm)
# print(nn)


# Напишите программу, которая считывает последовательность
# из 10 целых чисел и определяет является ли каждое из них четным или нет.

# n = 0
# for i in range(10):
#     num = int(input())
#     n += num % 2
# if n == 0:
#     print('YES')
# else:
#     print('NO')

# Программа должна вывести члены последовательности Фибоначчи,
# отделенные символом пробела.

# n = int(input())
# a, b = 1, 1
#
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b